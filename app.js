/* =========================================================
   SCSE1013 · Hafal — app logic (plain JS, works from file://)
   ========================================================= */
(function () {
  "use strict";

  // ---------------------------------------------------------------- storage
  var KEY_DATA = "scse1013.data.v1";
  var KEY_PROG = "scse1013.progress.v1";

  function lsGet(key) {
    try { var v = localStorage.getItem(key); return v ? JSON.parse(v) : null; } catch (e) { return null; }
  }
  function lsSet(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); return true; } catch (e) { return false; }
  }
  function lsDel(key) { try { localStorage.removeItem(key); } catch (e) { /* ignore */ } }

  function clone(o) { return JSON.parse(JSON.stringify(o)); }

  var DEFAULT = window.SCSE_DEFAULT_DATA || { topics: [], statements: [] };
  var DATA = lsGet(KEY_DATA) || clone(DEFAULT);
  if (!DATA.topics || !DATA.topics.length) DATA.topics = clone(DEFAULT.topics);

  function saveData() { lsSet(KEY_DATA, DATA); }
  function isCustomData() { return !!lsGet(KEY_DATA); }

  var PROG = lsGet(KEY_PROG) || {};
  PROG.stmts = PROG.stmts || {};
  PROG.sessions = PROG.sessions || 0;
  PROG.bestStreak = PROG.bestStreak || 0;
  function saveProg() { lsSet(KEY_PROG, PROG); }
  // statement IDs can change between data versions: drop per-statement progress from an older version
  var DATA_VERSION = DEFAULT.version || 1;
  if (PROG.dataVersion !== DATA_VERSION) {
    if (PROG.dataVersion !== undefined || Object.keys(PROG.stmts).length) PROG.stmts = {};
    PROG.dataVersion = DATA_VERSION; saveProg();
  }
  var customOutdated = isCustomData() && (DATA.version || 1) < DATA_VERSION;

  function topicById(id) { for (var i = 0; i < DATA.topics.length; i++) if (DATA.topics[i].id === id) return DATA.topics[i]; return null; }
  function stmtsOf(topicId) { return DATA.statements.filter(function (s) { return s.topic === topicId; }); }
  function stmtById(id) { for (var i = 0; i < DATA.statements.length; i++) if (DATA.statements[i].id === id) return DATA.statements[i]; return null; }

  function topicMastery(topicId) {
    var list = stmtsOf(topicId);
    if (!list.length) return 0;
    var sum = 0;
    list.forEach(function (s) { var p = PROG.stmts[s.id]; sum += p ? p.score : 0; });
    return Math.round(sum / list.length);
  }
  function overallMastery() {
    var list = DATA.statements;
    if (!list.length) return 0;
    var sum = 0;
    list.forEach(function (s) { var p = PROG.stmts[s.id]; sum += p ? p.score : 0; });
    return Math.round(sum / list.length);
  }
  function masteredCount(topicId) {
    return DATA.statements.filter(function (s) {
      var p = PROG.stmts[s.id];
      return (!topicId || s.topic === topicId) && p && p.mastered;
    }).length;
  }

  // ---------------------------------------------------------------- utils
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var app = document.getElementById("app");

  function esc(s) {
    return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }
  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  function toast(msg) {
    var t = document.getElementById("toast");
    t.textContent = msg; t.classList.add("on");
    clearTimeout(toast._t); toast._t = setTimeout(function () { t.classList.remove("on"); }, 2200);
  }

  // inline formatting: escape, then `code`, **bold**, *em* (bold may contain code)
  function inline(s) {
    var codes = [];
    var t = String(s).split(/(`[^`]+`)/g).map(function (p) {
      if (/^`[^`]+`$/.test(p)) { codes.push("<code>" + esc(p.slice(1, -1)) + "</code>"); return "\u0000" + (codes.length - 1) + "\u0000"; }
      return esc(p);
    }).join("");
    t = t.replace(/\*\*([^*]+?)\*\*/g, "<strong>$1</strong>");
    t = t.replace(/(^|[\s(])\*([^*\s][^*]*?)\*(?=[\s).,:;!?]|$)/g, "$1<em>$2</em>");
    return t.replace(/\u0000(\d+)\u0000/g, function (_, i) { return codes[+i]; });
  }

  // tiny markdown: ``` blocks, | tables |, - lists, 1. lists, paragraphs
  function md(src) {
    if (!src) return "";
    var out = [];
    var segs = String(src).split(/```/);
    segs.forEach(function (seg, i) {
      if (i % 2 === 1) {
        var code = seg.replace(/^[a-z+]*\n/, "").replace(/\n$/, "");
        out.push("<pre><code>" + esc(code) + "</code></pre>");
        return;
      }
      var lines = seg.split("\n");
      var buf = [], kind = null;
      function flush() {
        if (!buf.length) return;
        if (kind === "p") out.push("<p>" + buf.map(inline).join("<br>") + "</p>");
        else if (kind === "ul") out.push("<ul>" + buf.map(function (l) { return "<li>" + inline(l.replace(/^\s*-\s+/, "")) + "</li>"; }).join("") + "</ul>");
        else if (kind === "ol") out.push("<ol>" + buf.map(function (l) { return "<li>" + inline(l.replace(/^\s*\d+\.\s+/, "")) + "</li>"; }).join("") + "</ol>");
        else if (kind === "table") {
          var rows = buf.filter(function (l) { return !/^\s*\|[\s\-:|]+\|\s*$/.test(l); });
          var html = "<div class='table-wrap'><table>";
          rows.forEach(function (r, ri) {
            var cells = splitRow(r);
            var tag = ri === 0 ? "th" : "td";
            html += "<tr>" + cells.map(function (c) { return "<" + tag + ">" + inline(c) + "</" + tag + ">"; }).join("") + "</tr>";
          });
          out.push(html + "</table></div>");
        }
        buf = []; kind = null;
      }
      lines.forEach(function (l) {
        var k = null;
        if (!l.trim()) { flush(); return; }
        if (/^\s*\|.*\|\s*$/.test(l)) k = "table";
        else if (/^\s*-\s+/.test(l)) k = "ul";
        else if (/^\s*\d+\.\s+/.test(l)) k = "ol";
        else k = "p";
        if (k !== kind) flush();
        kind = k; buf.push(l.trim());
      });
      flush();
    });
    return out.join("");
  }
  // split a table row on | that are not inside `code`
  function splitRow(r) {
    r = r.trim().replace(/^\|/, "").replace(/\|$/, "");
    var cells = [], cur = "", inCode = false;
    for (var i = 0; i < r.length; i++) {
      var ch = r[i];
      if (ch === "`") inCode = !inCode;
      if (ch === "|" && !inCode) { cells.push(cur.trim()); cur = ""; } else cur += ch;
    }
    cells.push(cur.trim());
    return cells;
  }

  // ---------------------------------------------------------------- answer checking
  function levenshtein(a, b) {
    if (a === b) return 0;
    var m = a.length, n = b.length;
    if (!m) return n; if (!n) return m;
    var prev = new Array(n + 1), cur = new Array(n + 1);
    for (var j = 0; j <= n; j++) prev[j] = j;
    for (var i = 1; i <= m; i++) {
      cur[0] = i;
      for (j = 1; j <= n; j++) {
        var c = a.charCodeAt(i - 1) === b.charCodeAt(j - 1) ? 0 : 1;
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + c);
      }
      var t = prev; prev = cur; cur = t;
    }
    return prev[n];
  }
  function fixQuotes(s) { return String(s).replace(/[‘’‛′]/g, "'").replace(/[“”″]/g, '"').replace(/ /g, " "); }

  // normalise prose: lower case, remove punctuation (keep operator symbols)
  function normText(s) {
    return fixQuotes(s).toLowerCase()
      .replace(/([a-z])\/([a-z])/g, "$1 $2")
      .replace(/([a-z])-(?=[a-z])/g, "$1 ")
      .replace(/[.,;:?"'()\[\]{}`]/g, " ")
      .replace(/\s+/g, " ").trim();
  }
  function tokenEq(tok, kw) {
    if (tok === kw) return true;
    if (kw.length >= 6 && tok.length >= 6 && Math.abs(tok.length - kw.length) <= 2 && levenshtein(tok, kw) <= 2) return true;
    if (kw.length >= 4 && /^[a-z]/.test(kw) && tok.indexOf(kw) === 0 && tok.length - kw.length <= 3) return true;  // plural / suffix
    if (kw.length >= 5 && /^[a-z]+$/.test(kw) && tok.indexOf(kw) > 0) return true;  // word contains the keyword (e.g. recomputed ⊃ compute)
    return false;
  }
  function phraseIn(tokens, phrase, raw) {
    // keyword made only of symbols (e.g. ";" "==" "&&"): look for it in the raw answer
    if (!/[a-z0-9\u00C0-\u024F]/i.test(phrase)) return raw.indexOf(phrase) >= 0;
    var p = normText(phrase).split(" ").filter(Boolean);
    if (!p.length) return false;
    for (var i = 0; i + p.length <= tokens.length; i++) {
      var ok = true;
      for (var k = 0; k < p.length; k++) if (!tokenEq(tokens[i + k], p[k])) { ok = false; break; }
      if (ok) return true;
    }
    return false;
  }
  function splitSyn(group) {
    // split on | except an escaped \| (no regex lookbehind, for older Safari)
    var out = [], cur = "", g = String(group);
    for (var i = 0; i < g.length; i++) {
      if (g[i] === "\\" && g[i + 1] === "|") { cur += "|"; i++; }
      else if (g[i] === "|") { out.push(cur); cur = ""; }
      else cur += g[i];
    }
    out.push(cur);
    return out.map(function (x) { return x.trim(); }).filter(Boolean);
  }
  function checkExplain(input, keywords) {
    var tokens = normText(input).split(" ").filter(Boolean);
    var raw = fixQuotes(input);
    var found = [], missing = [];
    (keywords || []).forEach(function (g) {
      var syns = splitSyn(g);
      var hit = syns.some(function (s) { return phraseIn(tokens, s, raw); });
      (hit ? found : missing).push(syns[0]);
    });
    var total = (keywords || []).length || 1;
    var pct = Math.round(found.length / total * 100);
    return { pct: pct, found: found, missing: missing, verdict: pct >= 70 ? "ok" : pct >= 40 ? "near" : "bad" };
  }
  // code answers: symbols matter, whitespace and case-of-keywords do not get stripped of symbols
  var CODE_RX = /[;=<>(){}\[\]&|+*\/%#]/;
  function normExact(s, code) {
    s = fixQuotes(s).trim();
    if (code) return s.replace(/\s+/g, "");
    return s.toLowerCase().replace(/,/g, " ").replace(/\s+/g, " ").replace(/[.]$/, "").trim();
  }
  function checkExact(input, answers) {
    var ok = (answers || []).some(function (a) {
      var code = CODE_RX.test(a);
      return normExact(input, code) === normExact(a, code);
    });
    return { pct: ok ? 100 : 0, verdict: ok ? "ok" : "bad", found: [], missing: [] };
  }
  function evaluate(item, input) {
    if (!String(input).trim()) return { pct: 0, verdict: "bad", found: [], missing: (item.keywords || []).map(function (g) { return splitSyn(g)[0]; }), empty: true };
    return item.type === "exact" ? checkExact(input, item.answer) : checkExplain(input, item.keywords);
  }
  var ATTEMPT_SCORE = [100, 60, 30];

  // ---------------------------------------------------------------- sound
  var audioCtx = null;
  function beep(kind) {
    try {
      audioCtx = audioCtx || new (window.AudioContext || window.webkitAudioContext)();
      var notes = kind === "ok" ? [660, 880] : kind === "bad" ? [220, 165] : [440];
      notes.forEach(function (f, i) {
        var o = audioCtx.createOscillator(), g = audioCtx.createGain();
        o.type = kind === "bad" ? "square" : "sine"; o.frequency.value = f;
        var t0 = audioCtx.currentTime + i * 0.09;
        g.gain.setValueAtTime(0.0001, t0);
        g.gain.exponentialRampToValueAtTime(kind === "bad" ? 0.05 : 0.12, t0 + 0.01);
        g.gain.exponentialRampToValueAtTime(0.0001, t0 + 0.16);
        o.connect(g); g.connect(audioCtx.destination); o.start(t0); o.stop(t0 + 0.18);
      });
    } catch (e) { /* audio not available */ }
  }
  function burst(el) {
    if (reduceMotion || !el) return;
    var r = el.getBoundingClientRect();
    var colors = ["#2F5BFF", "#FFFFFF", "#34D399", "#38BDF8"];
    for (var i = 0; i < 14; i++) {
      (function (i) {
        var p = document.createElement("span");
        p.className = "burst";
        p.style.background = colors[i % colors.length];
        p.style.left = (r.left + r.width / 2) + "px"; p.style.top = (r.top + r.height / 2) + "px";
        document.body.appendChild(p);
        var a = Math.PI * 2 * i / 14, d = 60 + Math.random() * 50;
        var anim = p.animate([{ transform: "translate(0,0) rotate(0)", opacity: 1 },
          { transform: "translate(" + Math.cos(a) * d + "px," + Math.sin(a) * d + "px) rotate(" + (Math.random() * 360) + "deg)", opacity: 0 }],
          { duration: 650, easing: "cubic-bezier(.2,.7,.2,1)" });
        anim.onfinish = function () { p.remove(); };
      })(i);
    }
  }

  // ---------------------------------------------------------------- animations
  function revealAll() {
    var els = $all(".rv");
    if (reduceMotion || !("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("on"); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("on"); io.unobserve(en.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (e) { io.observe(e); });
  }
  function countUp(root) {
    $all("[data-count]", root).forEach(function (el) {
      var target = parseFloat(el.getAttribute("data-count")) || 0;
      var suffix = el.getAttribute("data-suffix") || "";
      if (reduceMotion) { el.innerHTML = target + suffix; return; }
      var t0 = null, dur = 1100;
      function step(ts) {
        if (!t0) t0 = ts;
        var k = Math.min(1, (ts - t0) / dur), e = 1 - Math.pow(1 - k, 3);
        el.innerHTML = Math.round(target * e) + suffix;
        if (k < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  }
  function fillBars(root) {
    requestAnimationFrame(function () {
      $all(".bar > span[data-w]", root).forEach(function (b) { b.style.width = b.getAttribute("data-w") + "%"; });
    });
  }
  var parallaxHandler = null;
  function setupParallax() {
    if (parallaxHandler) { window.removeEventListener("scroll", parallaxHandler); parallaxHandler = null; }
    if (reduceMotion) return;
    var items = $all("[data-parallax]");
    if (!items.length) return;
    parallaxHandler = function () {
      items.forEach(function (el) {
        var host = el.closest(".blue-block") || el;
        var r = host.getBoundingClientRect();
        var off = (r.top + r.height / 2 - window.innerHeight / 2);
        var f = parseFloat(el.getAttribute("data-parallax"));
        el.style.transform = "translate3d(0," + (off * f).toFixed(1) + "px,0) rotate(" + (off * f * 0.08).toFixed(2) + "deg)";
      });
    };
    window.addEventListener("scroll", parallaxHandler, { passive: true });
    parallaxHandler();
  }
  // blue wipe between note → answer
  function wipe(swap) {
    var w = document.getElementById("wipe");
    if (reduceMotion) { swap(); return; }
    w.className = "wipe in";
    setTimeout(function () {
      swap();
      w.className = "wipe out";
      setTimeout(function () { w.className = "wipe"; }, 450);
    }, 380);
  }

  function decoSVG() {
    return '' +
      '<div class="deco" aria-hidden="true">' +
      '<svg class="grain" xmlns="http://www.w3.org/2000/svg"><filter id="gn"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#gn)"/></svg>' +
      '<svg class="d1" data-parallax="-0.12" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">' +
      '<circle cx="200" cy="200" r="170" fill="none" stroke="#000" stroke-width="2" opacity=".55"/>' +
      '<circle cx="200" cy="200" r="120" fill="none" stroke="#fff" stroke-width="1.5" stroke-dasharray="4 8" opacity=".7"/>' +
      '<circle cx="200" cy="200" r="64" fill="#000"/>' +
      '<rect x="230" y="40" width="120" height="120" fill="#fff" opacity=".9" transform="rotate(18 290 100)"/>' +
      '<path d="M40 330 L160 330 L100 230 Z" fill="none" stroke="#000" stroke-width="3"/>' +
      '</svg>' +
      '<svg class="d2" data-parallax="0.18" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">' +
      '<g fill="#000">' + (function () { var s = ""; for (var y = 0; y < 8; y++) for (var x = 0; x < 8; x++) s += '<circle cx="' + (12 + x * 25) + '" cy="' + (12 + y * 25) + '" r="' + (2 + ((x + y) % 4)) + '"/>'; return s; })() + '</g>' +
      '</svg>' +
      '</div>';
  }

  // ---------------------------------------------------------------- router
  function setNav(name) {
    $all("[data-nav]").forEach(function (a) {
      if (a.getAttribute("data-nav") === name) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    });
  }
  var cleanup = null;
  function route() {
    if (cleanup) { cleanup(); cleanup = null; }
    var h = (location.hash || "#/").replace(/^#/, "");
    var parts = h.split("/").filter(Boolean);
    window.scrollTo(0, 0);
    if (!parts.length) { setNav("home"); renderHome(); }
    else if (parts[0] === "topic" && parts[1]) { setNav(""); renderTopic(parts[1]); }
    else if (parts[0] === "study" && parts[1]) { setNav(""); startStudy(parts[1], parts[2] === "weak"); }
    else if (parts[0] === "quiz" && parts[1]) { setNav(parts[1] === "trap" && !parts[2] ? "trap" : ""); startQuiz(parts[1], parts[2] === "trap"); }
    else if (parts[0] === "manage") { setNav("manage"); renderManage(parts[1]); }
    else if (parts[0] === "notes") { setNav("notes"); renderNotes(parts[1]); }
    else { setNav("home"); renderHome(); }
    revealAll(); countUp(app); fillBars(app); setupParallax();
    app.focus({ preventScroll: true });
  }
  window.addEventListener("hashchange", route);

  // ---------------------------------------------------------------- HOME
  function renderHome() {
    var total = DATA.statements.length;
    var html = '' +
      '<section class="hero"><div class="wrap">' +
      '<span class="eyebrow rv"><span class="dot"></span>SCSE1013 · FUNDAMENTAL PROGRAMMING CONCEPTS</span>' +
      '<h1 class="display rv rv-d1">Memorise SCSE1013. <span class="muted">One note at a time.</span></h1>' +
      '<p class="lead rv rv-d2">Read a note, hide it, then write what you remember. Every statement is checked against keywords, and follow-up questions drill code tracing and error-spotting, exactly like the exam.</p>' +
      (customOutdated ? '<div class="notice err rv" style="margin-top:24px">This browser is still using an older saved copy of the notes. <button class="btn btn-primary btn-sm" id="loadNew" style="margin-left:8px">Load the new English notes</button></div>' : '') +
      '<div class="row rv rv-d3"><a class="btn btn-primary" href="#topics">Start memorising <span class="arrow">→</span></a><a class="btn btn-ghost" href="#/quiz/trap">Exam Trap Quiz</a></div>' +
      '</div></section>' +
      '<section><div class="wrap"><div class="stats rv">' +
      stat(overallMastery(), "%", "Overall memorised") +
      stat(masteredCount(), '<small>/' + total + '</small>', "Statements mastered") +
      stat(PROG.bestStreak, "", "Best streak") +
      stat(PROG.sessions, "", "Sessions completed") +
      '</div></div></section>' +
      '<section class="section" id="topics"><div class="wrap">' +
      '<div class="section-head"><div><span class="eyebrow rv"><span class="dot"></span>TOPICS</span><h2 class="h2 rv rv-d1" style="margin-top:14px">Six chapters. One subject.</h2></div></div>' +
      '<div class="topics">' + DATA.topics.map(topicRow).join("") + '</div>' +
      '</div></section>' +
      '<section class="section" style="padding-top:0"><div class="wrap"><div class="blue-block rv">' + decoSVG() +
      '<div class="content"><span class="eyebrow"><span class="dot"></span>GAME MODE · 20 SECONDS PER QUESTION</span>' +
      '<h2 class="h2" style="margin:16px 0 14px">Exam Trap Quiz.</h2>' +
      '<p class="lead">Only questions from the TRAP, Common traps and Invalid headers sections: the mistakes that cost the most marks.</p>' +
      '<div class="row" style="margin-top:22px"><a class="btn btn-white" href="#/quiz/trap">Start trap quiz <span class="arrow">→</span></a></div></div>' +
      '</div></div></section>';
    app.innerHTML = html;
    var ln = $("#loadNew", app);
    if (ln) ln.addEventListener("click", function () {
      if (!confirm("Replace the saved notes in this browser with the new English notes? Use Manage Notes → Export JSON first if you want to keep your edits.")) return;
      lsDel(KEY_DATA); DATA = clone(DEFAULT); customOutdated = false; toast("New notes loaded"); route();
    });
    var a = $('a[href="#topics"]', app);
    if (a) a.addEventListener("click", function (e) { e.preventDefault(); document.getElementById("topics").scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth" }); });
  }
  function stat(n, suffix, label) {
    return '<div class="stat"><span class="num" data-count="' + n + '" data-suffix="' + esc(suffix) + '">' + n + suffix + '</span><span class="label eyebrow">' + esc(label) + '</span></div>';
  }
  function topicRow(t) {
    var n = stmtsOf(t.id).length, pct = topicMastery(t.id);
    return '<a class="topic rv" href="#/topic/' + t.id + '" style="--tc:' + t.color + '">' +
      '<span class="topic-no">' + esc(t.no) + '</span>' +
      '<div class="topic-body"><span class="tag">CH ' + esc(t.no) + '</span>' +
      '<h3 class="topic-title">' + esc(t.title) + '</h3>' +
      '<div class="topic-meta"><span class="topic-pct">' + pct + '%</span><span>memorised</span><span>·</span><span>' + n + ' statements</span><span>·</span><span>' + masteredCount(t.id) + ' mastered</span></div></div>' +
      '<span class="topic-go" aria-hidden="true">→</span>' +
      '<div class="bar"><span data-w="' + pct + '"></span></div></a>';
  }

  // ---------------------------------------------------------------- TOPIC
  function renderTopic(id) {
    var t = topicById(id);
    if (!t) { location.hash = "#/"; return; }
    var list = stmtsOf(id), pct = topicMastery(id);
    var fu = list.reduce(function (a, s) { return a + (s.followUps || []).length; }, 0);
    var traps = list.filter(function (s) { return s.trap; }).length;
    var weak = list.filter(function (s) { var p = PROG.stmts[s.id]; return !p || !p.mastered; }).length;
    app.innerHTML = '' +
      '<section class="hero" style="--tc:' + t.color + '"><div class="wrap">' +
      '<span class="eyebrow rv"><span class="tag" style="--tc:' + t.color + '">CH ' + esc(t.no) + '</span>' + esc(t.short) + '</span>' +
      '<h1 class="display rv rv-d1" style="max-width:16ch">' + esc(t.title) + '</h1>' +
      '</div></section>' +
      '<section><div class="wrap"><div class="stats rv">' +
      stat(pct, "%", "Topic memorised") + stat(list.length, "", "Statements") + stat(fu, "", "Follow-up questions") + stat(traps, "", "TRAP statements") +
      '</div></div></section>' +
      '<section class="section"><div class="wrap"><div class="grid-2">' +
      modeCard("#/notes/" + id, "READ", "Chapter notes", "Read this chapter's notes from the PDF, in order, before testing yourself.", "Read notes") +
      modeCard("#/study/" + id, "MEMORISE MODE", "Read → Hide → Write", "Note, answer and check for all " + list.length + " statements and their follow-ups. Anything you fail is repeated at the end of the session.", "Start full session") +
      modeCard("#/quiz/" + id, "QUIZ MODE", "20-second MCQ", "Every statement appears at least once as a multiple-choice question, in random order, with streaks.", "Start quiz") +
      (weak && weak < list.length ? modeCard("#/study/" + id + "/weak", "REVIEW WEAK SPOTS", weak + " statements not mastered yet", "Only statements you have not mastered yet or need to review.", "Review now") : "") +
      (traps ? modeCard("#/quiz/" + id + "/trap", "TRAP QUIZ", "This chapter's traps only", traps + " statements from the TRAP / Common traps / Invalid headers sections of this chapter.", "Start trap quiz") : "") +
      '</div>' +
      '<hr class="sep"><div class="eyebrow" style="margin-bottom:14px">CHAPTER CONTENTS</div>' +
      '<div class="list">' + list.map(function (s) {
        var p = PROG.stmts[s.id];
        return '<div class="list-item"><div><div class="meta"><span class="mono">' + esc(s.id) + '</span>' + (s.trap ? '<span class="tag trap">TRAP</span>' : '') + '<span>' + esc(s.section) + '</span></div></div>' +
          '<div class="meta">' + (p ? (p.mastered ? '<span style="color:var(--ok)">✓ ' + p.score + '%</span>' : '<span style="color:var(--bad)">↻ ' + p.score + '%</span>') : '<span>not yet</span>') + '</div></div>';
      }).join("") + '</div>' +
      '</div></section>';
  }
  function modeCard(href, eyebrow, title, desc, go) {
    return '<a class="card mode-card rv" href="' + href + '"><span class="eyebrow"><span class="dot"></span>' + esc(eyebrow) + '</span><h3 class="h3">' + esc(title) + '</h3><p>' + esc(desc) + '</p><span class="go">' + esc(go) + ' →</span></a>';
  }

  // ---------------------------------------------------------------- STUDY (memorise mode)
  var S = null; // current study session

  function itemsOf(st) {
    var items = [{ kind: "main", note: st.text, question: st.question, type: st.type, keywords: st.keywords, answer: st.answer, hint: st.hint }];
    (st.followUps || []).forEach(function (f, i) {
      items.push({ kind: "fu", fuIndex: i, fuTotal: st.followUps.length, note: f.note, question: f.question, type: f.type, keywords: f.keywords, answer: f.answer, hint: f.hint });
    });
    return items;
  }

  function startStudy(topicId, weakOnly) {
    var t = topicById(topicId);
    if (!t) { location.hash = "#/"; return; }
    var list = stmtsOf(topicId);
    if (weakOnly) list = list.filter(function (s) { var p = PROG.stmts[s.id]; return !p || !p.mastered; });
    if (!list.length) { app.innerHTML = emptyState("No statements in this topic.", "#/topic/" + topicId); return; }
    S = {
      topic: t, round: 1, queue: list.map(function (s) { return s.id; }), qi: 0, ii: 0,
      phase: "note", attempts: 0, input: "", last: null,
      results: {},   // id -> {scores: [], failed: bool}
      roundFailed: {},
      firstOrder: list.map(function (s) { return s.id; })
    };
    renderStudy();
    cleanup = function () { S = null; };
  }

  function curStmt() { return stmtById(S.queue[S.qi]); }
  function curItem() { return itemsOf(curStmt())[S.ii]; }

  function studyHeader() {
    var st = curStmt(), items = itemsOf(st);
    var doneUnits = S.qi / S.queue.length + (S.ii / items.length) / S.queue.length;
    var it = items[S.ii];
    var phaseNames = [["note", "A · Note"], ["answer", "B · Answer"], ["check", "C · Check"]];
    var ph = S.phase === "feedback" ? "check" : S.phase;
    return '<div class="study-top">' +
      '<span class="eyebrow"><span class="tag" style="--tc:' + S.topic.color + '">CH ' + esc(S.topic.no) + '</span>' + esc(S.topic.short) + (S.round > 1 ? ' · <span style="color:var(--near)">REVIEW ROUND ' + (S.round - 1) + '</span>' : '') + '</span>' +
      '<div class="row"><div class="phases">' + phaseNames.map(function (p) { return '<span class="phase-pill' + (p[0] === ph ? ' on' : '') + '">' + p[1] + '</span>'; }).join("") + '</div>' +
      '<button class="btn btn-ghost btn-sm" data-act="end">End session</button></div>' +
      '</div>' +
      '<div class="progress-line" aria-hidden="true"><span style="width:' + Math.round(doneUnits * 100) + '%"></span></div>' +
      '<div class="row" style="justify-content:space-between;margin-bottom:12px">' +
      '<span class="counter">Note ' + (S.qi + 1) + ' of ' + S.queue.length + (it.kind === "fu" ? ' · <span class="followup-tag">Follow-up ' + (it.fuIndex + 1) + '/' + it.fuTotal + '</span>' : '') + '</span>' +
      '<span class="counter">' + esc(st.id) + (st.trap ? ' · <span style="color:var(--bad)">TRAP</span>' : '') + (/^x/.test(st.id) ? ' · <span style="color:var(--text-2)">LAB EXTRA</span>' : '') + '</span></div>';
  }

  function renderStudy() {
    if (!S) return;
    var st = curStmt(), it = curItem();
    var body = "";
    if (S.phase === "note") {
      body = '<article class="card card-tc note-card" style="--tc:' + S.topic.color + '">' +
        '<span class="eyebrow">' + (it.kind === "fu" ? 'FOLLOW-UP NOTE · ' : '') + esc(st.section) + '</span>' +
        '<h2 class="h2">' + (it.kind === "fu" ? "Follow-up context" : esc(sectionTitle(st.section))) + '</h2>' +
        '<div class="rich">' + md(it.note) + '</div>' +
        '<div class="actions"><button class="btn btn-primary" data-act="tested">I&rsquo;ve read it, test me <span class="arrow">→</span></button></div>' +
        '</article>';
    } else {
      var isCode = it.type === "exact" && (it.answer || []).some(function (a) { return CODE_RX.test(a); });
      var locked = S.phase === "feedback" && (S.last.verdict === "ok" || S.attempts >= 3);
      body = '<article class="card card-tc" style="--tc:' + S.topic.color + '">' +
        '<div class="row" style="justify-content:space-between"><span class="eyebrow">' + (it.type === "exact" ? "EXACT ANSWER" : "EXPLAIN IN YOUR OWN WORDS") + '</span>' +
        '<span class="attempts" aria-label="Attempt ' + S.attempts + ' of 3">Attempts ' + [0, 1, 2].map(function (i) { return '<i class="' + (i < S.attempts ? 'used' : '') + '"></i>'; }).join("") + '</span></div>' +
        '<div class="question">' + inline(it.question) + '</div>' +
        '<label class="sr-only" for="ans">Your answer</label>' +
        '<textarea id="ans" class="answer-box' + (isCode ? ' code' : '') + '" placeholder="' + (it.type === "exact" ? "Type the exact answer…" : "Write what you remember and understand…") + '"' + (locked ? ' readonly' : '') + ' spellcheck="false" autocapitalize="off" autocomplete="off">' + esc(S.input) + '</textarea>' +
        '<div class="type-hint">' + (it.type === "exact" ? "Extra spaces and commas are ignored. For code, symbols such as == ; & ++ must be exact." : "Checked against keywords and their synonyms. ≥ 70% = CORRECT.") + ' · Ctrl/⌘ + Enter to submit.</div>' +
        (S.phase === "feedback" ? feedbackHTML(st, it) : '<div class="actions"><button class="btn btn-primary" data-act="check">Check answer</button></div>') +
        '</article>';
    }
    app.innerHTML = '<section class="study"><div class="wrap"><div class="stage">' + studyHeader() + body + '</div></div></section>';
    var ta = $("#ans", app);
    if (ta && !ta.readOnly) {
      ta.focus();
      ta.setSelectionRange(ta.value.length, ta.value.length);
      ta.addEventListener("input", function () { S.input = ta.value; });
      ta.addEventListener("keydown", function (e) { if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) { e.preventDefault(); doCheck(); } });
    }
    $all("[data-act]", app).forEach(function (b) { b.addEventListener("click", onStudyAction); });
    if (S.phase === "feedback") { var nb = $('[data-act="next"],[data-act="retry"]', app); if (nb) nb.focus({ preventScroll: true }); }
  }
  function sectionTitle(sec) { return String(sec || "").replace(/^[\d.]+\s*(·\s*)?/, "").replace(/^Cheat Sheet · /, ""); }

  function feedbackHTML(st, it) {
    var r = S.last, final = r.verdict === "ok" || S.attempts >= 3;
    var label = r.verdict === "ok" ? "CORRECT" : r.verdict === "near" ? "ALMOST" : "WRONG";
    var ico = r.verdict === "ok" ? "✓" : r.verdict === "near" ? "≈" : "✕";
    var h = '<div class="feedback ' + r.verdict + '" role="status" aria-live="polite">' +
      '<div class="verdict"><span class="ico" aria-hidden="true">' + ico + '</span>' + label +
      (it.type === "explain" ? '<span class="pct">' + r.pct + '% keywords</span>' : '') + '</div>';
    if (r.verdict === "ok") {
      h += '<p class="fb-text">Score for this item: <strong>' + ATTEMPT_SCORE[S.attempts - 1] + '%</strong> (attempt ' + S.attempts + ').</p>';
    } else if (!final) {
      h += '<p class="fb-text">' + (r.empty ? "Empty answer. " : "") + 'Attempt ' + S.attempts + ' of 3. Try again.</p>';
    } else {
      h += '<p class="fb-text">All 3 attempts used. This item is marked <strong>needs review</strong>.</p>';
    }
    if (it.type === "explain" && (r.found.length || r.missing.length)) {
      h += '<div class="chips">' + r.found.map(function (k) { return '<span class="chip hit">' + esc(k) + '</span>'; }).join("") +
        (final ? r.missing.map(function (k) { return '<span class="chip miss">' + esc(k) + '</span>'; }).join("")
               : (r.missing.length ? '<span class="chip miss">' + r.missing.length + ' keyword(s) missing</span>' : '')) + '</div>';
    }
    if (!final && it.hint) h += '<div class="hint"><b>Hint</b>' + inline(it.hint) + '</div>';
    if (final) {
      if (r.verdict !== "ok") {
        var ans = it.type === "exact" ? (it.answer || []).join("   or   ") : it.answer;
        if (ans) h += '<div class="reveal-box"><div class="eyebrow">REFERENCE ANSWER</div><div class="ref-answer">' + esc(ans) + '</div></div>';
      } else if (it.type === "explain" && it.answer) {
        h += '<div class="reveal-box"><div class="eyebrow">REFERENCE ANSWER</div><div class="ref-answer">' + esc(it.answer) + '</div></div>';
      }
      h += '<div class="reveal-box"><div class="eyebrow">ORIGINAL NOTE FOR COMPARISON</div><div class="rich">' + md(it.note) + '</div></div>';
    }
    h += '</div>';
    h += final
      ? '<div class="actions"><button class="btn btn-primary" data-act="next">Next <span class="arrow">→</span></button></div>'
      : '<div class="actions"><button class="btn btn-primary" data-act="retry">Try again</button></div>';
    return h;
  }

  function onStudyAction(e) {
    var act = e.currentTarget.getAttribute("data-act");
    if (act === "tested") { wipe(function () { S.phase = "answer"; S.attempts = 0; S.input = ""; renderStudy(); window.scrollTo(0, 0); }); }
    else if (act === "check") doCheck();
    else if (act === "retry") { S.phase = "answer"; renderStudy(); }
    else if (act === "next") nextItem();
    else if (act === "end") { if (confirm("End the session now? Unanswered items will not be counted.")) finishStudy(true); }
  }

  function doCheck() {
    if (!S || S.phase !== "answer") return;
    var it = curItem();
    var ta = $("#ans", app); S.input = ta ? ta.value : S.input;
    var r = evaluate(it, S.input);
    S.attempts++;
    S.last = r;
    var st = curStmt();
    var res = S.results[st.id] || (S.results[st.id] = { scores: [], failed: false, reviewed: false, reviewOk: true });
    if (r.verdict === "ok" || S.attempts >= 3) {
      var score = r.verdict === "ok" ? ATTEMPT_SCORE[S.attempts - 1] : 0;
      if (S.round === 1) { res.scores[S.ii] = score; if (score === 0) res.failed = true; }
      else { res.reviewed = true; if (score === 0) { res.reviewOk = false; S.roundFailed[st.id] = true; } }
      if (S.round === 1 && score === 0) S.roundFailed[st.id] = true;
      beep(r.verdict === "ok" ? "ok" : "bad");
    } else beep("near");
    S.phase = "feedback";
    renderStudy();
  }

  function nextItem() {
    var items = itemsOf(curStmt());
    if (S.ii + 1 < items.length) { S.ii++; }
    else if (S.qi + 1 < S.queue.length) { S.qi++; S.ii = 0; }
    else { endRound(); return; }
    S.phase = "note"; S.attempts = 0; S.input = ""; S.last = null;
    renderStudy(); window.scrollTo(0, 0);
  }

  function endRound() {
    var failed = S.queue.filter(function (id) { return S.roundFailed[id]; });
    if (failed.length) {
      var n = failed.length;
      app.innerHTML = '<section class="study"><div class="wrap"><div class="stage interstitial">' +
        '<span class="eyebrow"><span class="dot"></span>' + (S.round === 1 ? 'FIRST ROUND DONE' : 'REVIEW ROUND ' + (S.round - 1) + ' DONE') + '</span>' +
        '<h1 class="display">' + n + ' to review.</h1>' +
        '<p class="lead" style="margin:0 auto">These statements are repeated, starting again from the NOTE phase. The session score comes from the first round.</p>' +
        '<div class="row" style="justify-content:center;margin-top:28px"><button class="btn btn-primary" data-r="go">Review now <span class="arrow">→</span></button><button class="btn btn-ghost" data-r="end">See results</button></div>' +
        '</div></div></section>';
      $('[data-r="go"]', app).addEventListener("click", function () {
        S.round++; S.queue = failed; S.qi = 0; S.ii = 0; S.phase = "note"; S.attempts = 0; S.input = ""; S.roundFailed = {};
        renderStudy(); window.scrollTo(0, 0);
      });
      $('[data-r="end"]', app).addEventListener("click", function () { finishStudy(false); });
    } else finishStudy(false);
  }

  function finishStudy(early) {
    var t = S.topic, results = S.results;
    var mastered = [], redo = [], sum = 0, count = 0;
    S.firstOrder.forEach(function (id) {
      var r = results[id], st = stmtById(id);
      if (!r || !st) return;
      var n = itemsOf(st).length;
      var answered = r.scores.filter(function (x) { return typeof x === "number"; }).length;
      if (answered < n) return; // not finished in round 1 (session ended early)
      var sc = Math.round(r.scores.reduce(function (a, b) { return a + b; }, 0) / n);
      sum += sc; count++;
      var ok = !r.failed;
      (ok ? mastered : redo).push({ st: st, score: sc, reviewOk: r.reviewed && r.reviewOk });
      PROG.stmts[id] = { score: sc, mastered: ok, ts: Date.now() };
    });
    if (count) PROG.sessions++;
    saveProg();
    var pct = count ? Math.round(sum / count) : 0;
    renderResults({
      kind: "study", topic: t, pct: pct, early: early,
      stats: [[topicMastery(t.id) + "%", "Topic memorised"], [mastered.length, "Mastered"], [redo.length, "Needs review"]],
      groups: [
        { title: "Mastered", color: "var(--ok)", items: mastered.map(function (m) { return { id: m.st.id, q: m.st.question, sc: m.score + "%" }; }) },
        { title: "Needs review", color: "var(--bad)", items: redo.map(function (m) { return { id: m.st.id, q: m.st.question, sc: m.score + "%" + (m.reviewOk ? " · passed review" : "") }; }) }
      ],
      again: "#/study/" + t.id + (redo.length ? "/weak" : "")
    });
    S = null;
  }

  // ---------------------------------------------------------------- RESULTS
  function renderResults(o) {
    var t = o.topic;
    app.innerHTML = '<section class="result-hero"><div class="wrap">' +
      '<span class="eyebrow rv">' + (t ? '<span class="tag" style="--tc:' + t.color + '">CH ' + esc(t.no) + '</span>' + esc(t.short) : '<span class="tag trap">TRAP</span>ALL CHAPTERS') + ' · ' + (o.kind === "study" ? "MEMORISE SESSION RESULTS" : "QUIZ RESULTS") + '</span>' +
      '<div class="giant rv rv-d1"><span data-count="' + o.pct + '">' + o.pct + '</span><small>%</small></div>' +
      '<p class="lead rv rv-d2">' + (o.kind === "study" ? "Session score (1st try = 100%, 2nd = 60%, 3rd = 30%, failed = 0%)." : "Correct answers out of all questions.") + (o.early ? " Session ended early; only completed statements are counted." : "") + '</p>' +
      '<div class="result-stats rv">' + o.stats.map(function (s) { return '<div><span class="num"' + (typeof s[0] === "number" ? ' data-count="' + s[0] + '"' : '') + '>' + esc(s[0]) + '</span><div class="eyebrow">' + esc(s[1]) + '</div></div>'; }).join("") + '</div>' +
      o.groups.map(function (g, gi) {
        return '<details class="acc rv"' + (gi === 1 && g.items.length ? ' open' : '') + '><summary><span class="sw" style="background:' + g.color + '"></span>' + esc(g.title) + ' <span class="count">' + g.items.length + '</span><span class="plus" aria-hidden="true">+</span></summary>' +
          (g.items.length ? '<ul class="acc-list">' + g.items.map(function (i) { return '<li><span class="sid">' + esc(i.id) + '</span><span class="q">' + inline(i.q) + '</span><span class="sc">' + esc(i.sc) + '</span></li>'; }).join("") + '</ul>' : '<p style="color:var(--text-2);margin:0 0 22px">None.</p>') +
          '</details>';
      }).join("") +
      '<div class="row" style="margin-top:32px"><a class="btn btn-primary" href="' + o.again + '">Go again <span class="arrow">→</span></a>' +
      (t ? '<a class="btn btn-ghost" href="#/topic/' + t.id + '">Back to topic</a>' : '') + '<a class="btn btn-ghost" href="#/">Home</a></div>' +
      '</div></section>';
    revealAll(); countUp(app); window.scrollTo(0, 0);
  }

  // ---------------------------------------------------------------- QUIZ
  var Q = null;
  function startQuiz(scope, trapOnly) {
    var t = null, list;
    if (scope === "trap") { list = DATA.statements.filter(function (s) { return s.trap; }); trapOnly = true; }
    else {
      t = topicById(scope);
      if (!t) { location.hash = "#/"; return; }
      list = stmtsOf(scope);
      if (trapOnly) list = list.filter(function (s) { return s.trap; });
    }
    list = list.filter(function (s) { return s.mcq && s.mcq.options && s.mcq.options.length >= 2; });
    if (!list.length) { app.innerHTML = emptyState("No MCQ questions for this quiz.", t ? "#/topic/" + t.id : "#/"); return; }
    Q = { topic: t, trap: trapOnly, scope: scope, list: shuffle(list), i: 0, correct: 0, streak: 0, best: 0, wrong: [], right: [], timer: null, answered: false };
    renderQuizQ();
    cleanup = function () { if (Q && Q.timer) cancelAnimationFrame(Q.timer); Q = null; };
  }
  var QUIZ_SECONDS = 20;
  function renderQuizQ() {
    var s = Q.list[Q.i], tp = topicById(s.topic);
    var opts = s.mcq.options.map(function (o, idx) { return { text: o, correct: idx === (s.mcq.correct || 0) }; });
    Q.opts = shuffle(opts); Q.answered = false;
    app.innerHTML = '<section class="study"><div class="wrap"><div class="stage">' +
      '<div class="quiz-head"><span class="eyebrow">' + (Q.trap ? '<span class="tag trap">TRAP QUIZ</span>' : '') + '<span class="tag" style="--tc:' + tp.color + '">CH ' + esc(tp.no) + '</span>' + esc(tp.short) + '</span>' +
      '<span class="streak" id="streak"><span class="flame" aria-hidden="true">🔥</span><span>' + Q.streak + '</span><span class="sr-only">streak</span></span></div>' +
      '<div class="row" style="justify-content:space-between;margin-bottom:10px"><span class="counter">Question ' + (Q.i + 1) + ' of ' + Q.list.length + '</span><span class="counter" id="secs">' + QUIZ_SECONDS + 's</span></div>' +
      '<div class="timer" id="timer"><span></span></div>' +
      '<article class="card card-tc" style="--tc:' + tp.color + '">' +
      '<div class="question">' + inline(s.mcq.question) + '</div>' +
      '<div class="options" role="group" aria-label="Answer options">' + Q.opts.map(function (o, i) {
        return '<button class="opt" data-i="' + i + '"><span class="k">' + "ABCD"[i] + '</span><span>' + inline(o.text) + '</span></button>';
      }).join("") + '</div>' +
      '<div id="qfb"></div>' +
      '</article>' +
      '<div class="row" style="justify-content:flex-end;margin-top:16px"><button class="btn btn-ghost btn-sm" id="qend">End quiz</button></div>' +
      '</div></div></section>';
    $all(".opt", app).forEach(function (b) { b.addEventListener("click", function () { answerQuiz(parseInt(b.getAttribute("data-i"), 10)); }); });
    $("#qend", app).addEventListener("click", function () { if (confirm("End the quiz now?")) finishQuiz(); });
    startTimer();
  }
  function startTimer() {
    var bar = $("#timer > span", app), secs = $("#secs", app), wrap = $("#timer", app);
    var t0 = performance.now();
    function tick(now) {
      if (!Q || Q.answered) return;
      var el = (now - t0) / 1000, left = Math.max(0, QUIZ_SECONDS - el);
      bar.style.transform = "scaleX(" + (left / QUIZ_SECONDS) + ")";
      secs.textContent = Math.ceil(left) + "s";
      if (left <= 5) wrap.classList.add("low");
      if (left <= 0) { answerQuiz(-1); return; }
      Q.timer = requestAnimationFrame(tick);
    }
    Q.timer = requestAnimationFrame(tick);
  }
  function answerQuiz(i) {
    if (!Q || Q.answered) return;
    Q.answered = true;
    if (Q.timer) cancelAnimationFrame(Q.timer);
    var s = Q.list[Q.i];
    var btns = $all(".opt", app);
    btns.forEach(function (b, bi) { b.disabled = true; if (Q.opts[bi].correct) b.classList.add("correct"); });
    var ok = i >= 0 && Q.opts[i].correct;
    var fb = $("#qfb", app);
    var correctText = Q.opts.filter(function (o) { return o.correct; })[0].text;
    if (ok) {
      Q.correct++; Q.streak++; Q.best = Math.max(Q.best, Q.streak); Q.right.push(s);
      btns[i].classList.add("pop"); burst(btns[i]); beep("ok");
      var sk = $("#streak", app); sk.classList.remove("bump"); void sk.offsetWidth; sk.classList.add("bump");
      sk.querySelector("span:nth-child(2)").textContent = Q.streak;
    } else {
      Q.streak = 0; Q.wrong.push(s); beep("bad");
      if (i >= 0) btns[i].classList.add("wrong", "shake");
      $("#streak", app).querySelector("span:nth-child(2)").textContent = 0;
    }
    if (Q.best > PROG.bestStreak) { PROG.bestStreak = Q.best; saveProg(); }
    fb.innerHTML = '<div class="feedback ' + (ok ? "ok" : "bad") + '" role="status"><div class="verdict"><span class="ico" aria-hidden="true">' + (ok ? "✓" : "✕") + '</span>' + (ok ? "CORRECT" : (i < 0 ? "TIME'S UP" : "WRONG")) + '</div>' +
      (ok ? '' : '<p class="fb-text">Correct answer: <strong>' + inline(correctText) + '</strong></p>') +
      '<div class="reveal-box"><div class="eyebrow">NOTE · ' + esc(s.id) + ' · ' + esc(s.section) + '</div><div class="rich">' + md(s.text) + '</div></div></div>' +
      '<div class="actions"><button class="btn btn-primary" id="qnext">' + (Q.i + 1 < Q.list.length ? 'Next <span class="arrow">→</span>' : 'See results') + '</button></div>';
    var nb = $("#qnext", app);
    nb.addEventListener("click", function () { Q.i++; if (Q.i < Q.list.length) { renderQuizQ(); window.scrollTo(0, 0); } else finishQuiz(); });
    nb.focus({ preventScroll: true });
    fb.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "nearest" });
  }
  function finishQuiz() {
    if (Q.timer) cancelAnimationFrame(Q.timer);
    var asked = Q.right.length + Q.wrong.length;
    var pct = asked ? Math.round(Q.correct / asked * 100) : 0;
    if (asked) PROG.sessions++;
    saveProg();
    var o = Q;
    renderResults({
      kind: "quiz", topic: o.topic, pct: pct, early: asked < o.list.length,
      stats: [[o.correct + "/" + asked, "Correct"], [o.best, "Best streak"], [PROG.bestStreak, "Streak record"]],
      groups: [
        { title: "Correct", color: "var(--ok)", items: o.right.map(function (s) { return { id: s.id, q: s.mcq.question, sc: "✓" }; }) },
        { title: "Needs review", color: "var(--bad)", items: o.wrong.map(function (s) { return { id: s.id, q: s.mcq.question, sc: "✕" }; }) }
      ],
      again: "#/quiz/" + o.scope + (o.trap && o.scope !== "trap" ? "/trap" : "")
    });
    Q = null;
  }

  // ---------------------------------------------------------------- STUDY NOTES (read the PDF content)
  var PDF_PATH = "notes/SCSE1013_Study_Notes.pdf";
  function renderNotes(topicId) {
    var topics = topicId && topicById(topicId) ? [topicById(topicId)] : DATA.topics;
    var html = '<section class="hero" style="padding-bottom:20px"><div class="wrap">' +
      '<span class="eyebrow rv"><span class="dot"></span>STUDY NOTES · SCSE1013_Study_Notes.pdf</span>' +
      '<h1 class="display rv rv-d1" style="font-size:clamp(2.4rem,6vw,4.6rem)">' + (topics.length === 1 ? 'Chapter ' + esc(topics[0].no) + ' notes.' : 'Read the notes.') + '</h1>' +
      '<p class="lead rv rv-d2">Simple notes from Chapters 1–5 plus the one-page cheat sheet: what you need to understand and remember.</p>' +
      '<div class="row rv rv-d3" style="margin-top:24px"><a class="btn btn-primary" href="' + PDF_PATH + '" target="_blank" rel="noopener">Open the PDF <span class="arrow">↗</span></a>' +
      '<a class="btn btn-ghost" href="' + PDF_PATH + '" download>Download PDF</a>' +
      (topics.length === 1 ? '<a class="btn btn-ghost" href="#/notes">All chapters</a>' : '') + '</div>' +
      (topics.length > 1 ? '<div class="row" style="margin-top:22px;gap:8px">' + DATA.topics.map(function (t) {
        return '<a class="tag" style="--tc:' + t.color + ';text-decoration:none;padding:8px 12px" href="#/notes/' + t.id + '">CH ' + esc(t.no) + ' · ' + esc(t.short) + '</a>';
      }).join("") + '</div>' : '') +
      '</div></section>';
    topics.forEach(function (t) {
      var list = stmtsOf(t.id).filter(function (s) { return !/^x/.test(s.id); });
      html += '<section class="section" style="padding-top:28px"><div class="wrap"><div style="max-width:860px">' +
        '<div class="section-head"><div><span class="eyebrow"><span class="tag" style="--tc:' + t.color + '">CH ' + esc(t.no) + '</span>' + esc(t.short) + '</span>' +
        '<h2 class="h2" style="margin-top:12px">' + esc(t.title) + '</h2></div>' +
        '<a class="btn btn-ghost btn-sm" href="#/study/' + t.id + '">Test me on this chapter →</a></div>' +
        list.map(function (s) {
          return '<article class="card card-tc" style="--tc:' + t.color + ';margin-bottom:14px">' +
            '<div class="row" style="justify-content:space-between"><span class="eyebrow">' + esc(sectionTitle(s.section)) + '</span>' +
            (s.trap ? '<span class="tag trap">TRAP</span>' : '') + '</div>' +
            '<div class="rich" style="margin-top:12px">' + md(s.text) + '</div></article>';
        }).join("") +
        '</div></div></section>';
    });
    app.innerHTML = html;
  }

  function emptyState(msg, back) {
    return '<section class="hero"><div class="wrap"><h1 class="h2">' + esc(msg) + '</h1><div class="row" style="margin-top:24px"><a class="btn btn-ghost" href="' + back + '">Back</a></div></div></section>';
  }

  // ---------------------------------------------------------------- MANAGE (CRUD + import/export)
  var manageFilter = { topic: "", q: "" };
  function renderManage(editId) {
    if (editId) { renderEditor(editId === "new" ? null : decodeURIComponent(editId)); return; }
    var list = DATA.statements.filter(function (s) {
      if (manageFilter.topic && s.topic !== manageFilter.topic) return false;
      if (manageFilter.q) {
        var q = manageFilter.q.toLowerCase();
        return (s.id + " " + s.question + " " + s.section + " " + s.text).toLowerCase().indexOf(q) >= 0;
      }
      return true;
    });
    app.innerHTML = '<section class="hero" style="padding-bottom:20px"><div class="wrap">' +
      '<span class="eyebrow rv"><span class="dot"></span>MANAGE NOTES</span>' +
      '<h1 class="display rv rv-d1" style="font-size:clamp(2.4rem,6vw,4.6rem)">Add, edit, delete.</h1>' +
      '<p class="lead rv rv-d2">' + DATA.statements.length + ' statements. ' + (isCustomData() ? 'You are using edited data (saved in localStorage).' : 'You are using the original data from data.js.') + '</p>' +
      (customOutdated ? '<div class="notice err" style="margin-top:16px">The data saved in this browser is older than the current data.js. Export it first if you need it, then press <b>Reset to original data</b>.</div>' : '') +
      '<div class="toolbar"><a class="btn btn-primary" href="#/manage/new">+ Add statement</a>' +
      '<button class="btn btn-ghost" id="exp">Export JSON</button>' +
      '<label class="btn btn-ghost" for="imp" style="cursor:pointer">Import JSON</label><input type="file" id="imp" accept=".json,application/json" class="sr-only">' +
      '<button class="btn btn-danger" id="reset">Reset to original data</button>' +
      '<button class="btn btn-danger" id="resetp">Clear progress</button></div>' +
      '<div class="grid-2"><div class="field"><label for="ft">Topic</label><select id="ft" class="select"><option value="">All topics</option>' +
      DATA.topics.map(function (t) { return '<option value="' + t.id + '"' + (manageFilter.topic === t.id ? ' selected' : '') + '>' + esc(t.no + " · " + t.title) + '</option>'; }).join("") + '</select></div>' +
      '<div class="field"><label for="fq">Search</label><input id="fq" class="input" type="search" value="' + esc(manageFilter.q) + '" placeholder="ID, question or note text"></div></div>' +
      '</div></section>' +
      '<section style="padding-bottom:80px"><div class="wrap"><div class="list">' +
      list.map(function (s) {
        var t = topicById(s.topic) || { color: "#666", no: "?" };
        return '<div class="list-item"><div><div class="meta"><span class="tag" style="--tc:' + t.color + '">CH ' + esc(t.no) + '</span><span class="mono">' + esc(s.id) + '</span>' + (s.trap ? '<span class="tag trap">TRAP</span>' : '') + '<span>' + esc(s.type) + '</span><span>' + (s.followUps || []).length + ' follow-ups</span></div>' +
          '<div class="q">' + inline(s.question) + '</div></div>' +
          '<div class="row"><a class="btn btn-ghost btn-sm" href="#/manage/' + encodeURIComponent(s.id) + '">Edit</a><button class="btn btn-danger btn-sm" data-del="' + esc(s.id) + '">Delete</button></div></div>';
      }).join("") + (list.length ? '' : '<p style="color:var(--text-2);padding:20px 0">No matching statements.</p>') +
      '</div></div></section>';

    $("#ft", app).addEventListener("change", function (e) { manageFilter.topic = e.target.value; route(); });
    var fq = $("#fq", app), deb;
    fq.addEventListener("input", function (e) {
      clearTimeout(deb); deb = setTimeout(function () { manageFilter.q = e.target.value; route(); var f = $("#fq", app); if (f) { f.focus(); f.setSelectionRange(f.value.length, f.value.length); } }, 250);
    });
    $all("[data-del]", app).forEach(function (b) {
      b.addEventListener("click", function () {
        var id = b.getAttribute("data-del");
        if (!confirm("Delete statement " + id + "?")) return;
        DATA.statements = DATA.statements.filter(function (s) { return s.id !== id; });
        saveData(); toast("Statement " + id + " deleted"); route();
      });
    });
    $("#exp", app).addEventListener("click", exportJSON);
    $("#imp", app).addEventListener("change", importJSON);
    $("#reset", app).addEventListener("click", function () {
      if (!confirm("Discard all changes and go back to the original data.js?")) return;
      lsDel(KEY_DATA); DATA = clone(DEFAULT); customOutdated = false; toast("Original data restored"); route();
    });
    $("#resetp", app).addEventListener("click", function () {
      if (!confirm("Clear all memorisation progress, streaks and session count?")) return;
      PROG = { stmts: {}, sessions: 0, bestStreak: 0 }; saveProg(); toast("Progress cleared");
    });
  }
  function exportJSON() {
    var blob = new Blob([JSON.stringify(DATA, null, 2)], { type: "application/json" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "scse1013-notes-" + new Date().toISOString().slice(0, 10) + ".json";
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
    toast("JSON file downloaded");
  }
  function importJSON(e) {
    var f = e.target.files && e.target.files[0];
    if (!f) return;
    var rd = new FileReader();
    rd.onload = function () {
      try {
        var d = JSON.parse(rd.result);
        if (Array.isArray(d)) d = { topics: DATA.topics, statements: d };
        if (!d || !Array.isArray(d.statements)) throw new Error("No 'statements' list found.");
        d.statements.forEach(function (s, i) {
          var err = validateStmt(s, d.statements.slice(0, i).map(function (x) { return x.id; }));
          if (err) throw new Error((s && s.id ? s.id : "#" + (i + 1)) + ": " + err);
        });
        if (!Array.isArray(d.topics) || !d.topics.length) d.topics = DATA.topics;
        DATA = d; saveData(); toast("Imported " + d.statements.length + " statements"); route();
      } catch (err) { alert("Import failed. " + err.message); }
    };
    rd.readAsText(f);
  }
  function validateStmt(s, takenIds) {
    if (!s || typeof s !== "object") return "bukan objek";
    if (!s.id || !/^[A-Za-z0-9_-]+$/.test(s.id)) return "id must use only letters, digits, _ or -";
    if (takenIds.indexOf(s.id) >= 0) return "duplicate id";
    if (!topicById(s.topic) && !(DATA.topics || []).length) return "invalid topic";
    if (!s.text || !s.question) return "text and question are required";
    if (s.type !== "explain" && s.type !== "exact") return "type must be explain or exact";
    if (s.type === "explain" && !(s.keywords || []).length) return "explain needs at least one keyword";
    if (s.type === "exact" && !(Array.isArray(s.answer) && s.answer.length)) return "exact needs a list of answers";
    if (s.followUps && !Array.isArray(s.followUps)) return "followUps must be an array";
    if (s.mcq && !(Array.isArray(s.mcq.options) && s.mcq.options.length === 4)) return "mcq needs 4 options";
    return null;
  }

  function renderEditor(id) {
    var s = id ? stmtById(id) : null;
    if (id && !s) { location.hash = "#/manage"; return; }
    var isNew = !s;
    s = s ? clone(s) : { id: "", topic: manageFilter.topic || DATA.topics[0].id, section: "", trap: false, text: "", question: "", type: "explain", keywords: [], answer: "", hint: "", followUps: [], mcq: { question: "", options: ["", "", "", ""], correct: 0 } };
    var mcq = s.mcq || { question: "", options: ["", "", "", ""], correct: 0 };
    var correct = mcq.options[mcq.correct || 0] || "";
    var wrongs = mcq.options.filter(function (_, i) { return i !== (mcq.correct || 0); });
    while (wrongs.length < 3) wrongs.push("");
    var answerText = Array.isArray(s.answer) ? s.answer.join("\n") : (s.answer || "");
    app.innerHTML = '<section class="hero" style="padding-bottom:16px"><div class="wrap">' +
      '<span class="eyebrow"><span class="dot"></span>MANAGE NOTES · ' + (isNew ? "NEW STATEMENT" : "EDIT " + esc(s.id)) + '</span>' +
      '<h1 class="h2" style="margin-top:14px">' + (isNew ? "Add statement" : "Edit statement") + '</h1></div></section>' +
      '<section style="padding-bottom:80px"><div class="wrap"><form id="ed" class="card" novalidate>' +
      '<div class="grid-2">' +
      fld("ID", '<input class="input mono" name="id" required value="' + esc(s.id) + '" placeholder="cp99">', "Unique. Letters, digits, _ or -.") +
      fld("Topic", '<select class="select" name="topic">' + DATA.topics.map(function (t) { return '<option value="' + t.id + '"' + (t.id === s.topic ? ' selected' : '') + '>' + esc(t.no + " · " + t.title) + '</option>'; }).join("") + '</select>') +
      fld("Section (PDF sub-heading)", '<input class="input" name="section" value="' + esc(s.section) + '" placeholder="3.8 Arithmetic operators">') +
      fld("Question type", '<select class="select" name="type"><option value="explain"' + (s.type === "explain" ? ' selected' : '') + '>explain: own words (keywords)</option><option value="exact"' + (s.type === "exact" ? ' selected' : '') + '>exact: exact answer</option></select>') +
      '</div>' +
      '<div class="check"><input type="checkbox" id="trap" name="trap"' + (s.trap ? ' checked' : '') + '><label for="trap">TRAP / Common traps / Invalid headers section (included in Trap Quiz)</label></div>' +
      fld("Note (text)", '<textarea class="textarea" name="text" rows="9">' + esc(s.text) + '</textarea>', "Format: **bold**, `code`, lines starting with - for lists, | for tables, ``` for C++ code blocks.") +
      fld("Question", '<textarea class="textarea" name="question" rows="2">' + esc(s.question) + '</textarea>') +
      fld("Keywords (explain)", '<textarea class="textarea" name="keywords" rows="4" placeholder="decomposition|break into parts|split">' + esc((s.keywords || []).join("\n")) + '</textarea>', "One required keyword per line. Separate synonyms with |.") +
      fld("Answer", '<textarea class="textarea" name="answer" rows="3">' + esc(answerText) + '</textarea>', "explain: reference answer. exact: one accepted answer per line (e.g. 10 9 8 and 10, 9, 8).") +
      fld("Hint", '<input class="input" name="hint" value="' + esc(s.hint) + '">', "A clue that does not give the answer away.") +
      fld("Follow-up questions (JSON)", '<textarea class="textarea" name="followUps" rows="10">' + esc(JSON.stringify(s.followUps || [], null, 2)) + '</textarea>', 'Array of 1–3 objects: {"note","question","type":"exact"|"explain","answer":[…] or "…","keywords":[…],"hint"}.') +
      '<hr class="sep"><div class="eyebrow" style="margin-bottom:14px">MCQ (4 OPTIONS)</div>' +
      fld("MCQ question", '<input class="input" name="mq" value="' + esc(mcq.question) + '">') +
      fld("CORRECT option", '<input class="input" name="mc" value="' + esc(correct) + '">') +
      '<div class="grid-2">' + wrongs.slice(0, 3).map(function (w, i) { return fld("Wrong option " + (i + 1), '<input class="input" name="mw' + i + '" value="' + esc(w) + '">'); }).join("") + '</div>' +
      '<div id="edErr"></div>' +
      '<div class="actions"><button class="btn btn-primary" type="submit">Save</button><a class="btn btn-ghost" href="#/manage">Cancel</a></div>' +
      '</form></div></section>';
    $("#ed", app).addEventListener("submit", function (e) {
      e.preventDefault();
      var f = e.target, err = $("#edErr", app);
      var ns = {
        id: f.id.value.trim(), topic: f.topic.value, section: f.section.value.trim(), trap: f.trap.checked,
        text: f.text.value.replace(/\s+$/, ""), question: f.question.value.trim(), type: f.type.value,
        keywords: f.keywords.value.split("\n").map(function (x) { return x.trim(); }).filter(Boolean),
        hint: f.hint.value.trim()
      };
      var ansLines = f.answer.value.split("\n").map(function (x) { return x.trim(); }).filter(Boolean);
      ns.answer = ns.type === "exact" ? ansLines : f.answer.value.trim();
      if (ns.type === "exact") ns.keywords = [];
      try { ns.followUps = JSON.parse(f.followUps.value || "[]"); }
      catch (x) { err.innerHTML = '<div class="notice err">Follow-ups: invalid JSON (' + esc(x.message) + ').</div>'; return; }
      var opts = [f.mc.value.trim(), f.mw0.value.trim(), f.mw1.value.trim(), f.mw2.value.trim()];
      ns.mcq = { question: f.mq.value.trim(), options: opts, correct: 0 };
      var taken = DATA.statements.filter(function (x) { return !s || x.id !== (isNew ? "\u0000" : id); }).map(function (x) { return x.id; });
      var msg = validateStmt(ns, taken);
      if (!msg && ns.mcq.question && opts.some(function (o) { return !o; })) msg = "MCQ needs all 4 options filled in";
      if (!msg && !ns.mcq.question) msg = "MCQ is required (question and 4 options)";
      if (!msg) (ns.followUps || []).forEach(function (fu, i) {
        if (msg) return;
        if (!fu.note || !fu.question) msg = "Follow-up " + (i + 1) + ": note and question are required";
        else if (fu.type === "exact" && !(Array.isArray(fu.answer) && fu.answer.length)) msg = "Follow-up " + (i + 1) + ": exact needs a list of answers";
        else if (fu.type !== "exact" && !(fu.keywords || []).length) msg = "Follow-up " + (i + 1) + ": explain needs keywords";
      });
      if (msg) { err.innerHTML = '<div class="notice err">' + esc(msg) + '</div>'; err.scrollIntoView({ block: "center" }); return; }
      if (isNew) DATA.statements.push(ns);
      else {
        var idx = DATA.statements.findIndex(function (x) { return x.id === id; });
        DATA.statements[idx] = ns;
        if (id !== ns.id && PROG.stmts[id]) { PROG.stmts[ns.id] = PROG.stmts[id]; delete PROG.stmts[id]; saveProg(); }
      }
      saveData(); toast("Saved: " + ns.id); location.hash = "#/manage";
    });
  }
  function fld(label, control, help) {
    return '<label class="field"><span class="lbl">' + esc(label) + '</span>' + control + (help ? '<span class="help">' + esc(help) + '</span>' : '') + '</label>';
  }

  // expose engine for testing
  window.SCSE = { checkExplain: checkExplain, checkExact: checkExact, evaluate: evaluate, md: md, levenshtein: levenshtein };

  route();
})();
