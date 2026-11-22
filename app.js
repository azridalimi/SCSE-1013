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
    if (kw.length >= 5 && /^[a-z]+$/.test(kw) && tok.indexOf(kw) > 0) return true;  // Malay prefix: memecahkan ⊃ pecah
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
      '<h1 class="display rv rv-d1">Hafal SCSE1013. <span class="muted">Satu nota pada satu masa.</span></h1>' +
      '<p class="lead rv rv-d2">Baca nota, tutup, tulis semula apa yang anda ingat. Setiap statement disemak dengan kata kunci, dan soalan susulan menguji trace code dan cari kesilapan seperti dalam peperiksaan.</p>' +
      '<div class="row rv rv-d3"><a class="btn btn-primary" href="#topics">Mula hafal <span class="arrow">→</span></a><a class="btn btn-ghost" href="#/quiz/trap">Kuiz Trap Peperiksaan</a></div>' +
      '</div></section>' +
      '<section><div class="wrap"><div class="stats rv">' +
      stat(overallMastery(), "%", "Hafalan keseluruhan") +
      stat(masteredCount(), '<small>/' + total + '</small>', "Statement dikuasai") +
      stat(PROG.bestStreak, "", "Streak terbaik") +
      stat(PROG.sessions, "", "Sesi selesai") +
      '</div></div></section>' +
      '<section class="section" id="topics"><div class="wrap">' +
      '<div class="section-head"><div><span class="eyebrow rv"><span class="dot"></span>TOPIK</span><h2 class="h2 rv rv-d1" style="margin-top:14px">Enam bab. Satu subjek.</h2></div></div>' +
      '<div class="topics">' + DATA.topics.map(topicRow).join("") + '</div>' +
      '</div></section>' +
      '<section class="section" style="padding-top:0"><div class="wrap"><div class="blue-block rv">' + decoSVG() +
      '<div class="content"><span class="eyebrow"><span class="dot"></span>MOD GAME · 20 SAAT SETIAP SOALAN</span>' +
      '<h2 class="h2" style="margin:16px 0 14px">Kuiz Trap Peperiksaan.</h2>' +
      '<p class="lead">Hanya soalan daripada bahagian TRAP, Common traps dan Invalid headers. Soalan yang paling kerap menjatuhkan markah.</p>' +
      '<div class="row" style="margin-top:22px"><a class="btn btn-white" href="#/quiz/trap">Mula kuiz trap <span class="arrow">→</span></a></div></div>' +
      '</div></div></section>';
    app.innerHTML = html;
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
      '<div class="topic-body"><span class="tag">BAB ' + esc(t.no) + '</span>' +
      '<h3 class="topic-title">' + esc(t.title) + '</h3>' +
      '<div class="topic-meta"><span class="topic-pct">' + pct + '%</span><span>hafalan</span><span>·</span><span>' + n + ' statement</span><span>·</span><span>' + masteredCount(t.id) + ' dikuasai</span></div></div>' +
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
      '<span class="eyebrow rv"><span class="tag" style="--tc:' + t.color + '">BAB ' + esc(t.no) + '</span>' + esc(t.short) + '</span>' +
      '<h1 class="display rv rv-d1" style="max-width:16ch">' + esc(t.title) + '</h1>' +
      '</div></section>' +
      '<section><div class="wrap"><div class="stats rv">' +
      stat(pct, "%", "Hafalan topik") + stat(list.length, "", "Statement") + stat(fu, "", "Soalan susulan") + stat(traps, "", "Statement TRAP") +
      '</div></div></section>' +
      '<section class="section"><div class="wrap"><div class="grid-2">' +
      modeCard("#/study/" + id, "MOD HAFALAN", "Baca → Tutup → Tulis", "Kitaran nota, jawab dan semak untuk setiap " + list.length + " statement dan soalan susulannya. Yang gagal diulang di hujung sesi.", "Mula sesi penuh") +
      modeCard("#/quiz/" + id, "MOD KUIZ", "MCQ 20 saat", "Setiap statement keluar sekurang-kurangnya sekali sebagai soalan aneka pilihan, susunan rawak, dengan streak.", "Mula kuiz") +
      (weak && weak < list.length ? modeCard("#/study/" + id + "/weak", "ULANG YANG LEMAH", weak + " statement belum dikuasai", "Hanya statement yang belum pernah dikuasai atau perlu ulang.", "Ulang sekarang") : "") +
      (traps ? modeCard("#/quiz/" + id + "/trap", "KUIZ TRAP", "Trap bab ini sahaja", traps + " statement daripada bahagian TRAP / Common traps / Invalid headers dalam bab ini.", "Mula kuiz trap") : "") +
      '</div>' +
      '<hr class="sep"><div class="eyebrow" style="margin-bottom:14px">KANDUNGAN BAB</div>' +
      '<div class="list">' + list.map(function (s) {
        var p = PROG.stmts[s.id];
        return '<div class="list-item"><div><div class="meta"><span class="mono">' + esc(s.id) + '</span>' + (s.trap ? '<span class="tag trap">TRAP</span>' : '') + '<span>' + esc(s.section) + '</span></div></div>' +
          '<div class="meta">' + (p ? (p.mastered ? '<span style="color:var(--ok)">✓ ' + p.score + '%</span>' : '<span style="color:var(--bad)">↻ ' + p.score + '%</span>') : '<span>belum</span>') + '</div></div>';
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
    if (!list.length) { app.innerHTML = emptyState("Tiada statement dalam topik ini.", "#/topic/" + topicId); return; }
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
    var phaseNames = [["note", "A · Nota"], ["answer", "B · Jawab"], ["check", "C · Semak"]];
    var ph = S.phase === "feedback" ? "check" : S.phase;
    return '<div class="study-top">' +
      '<span class="eyebrow"><span class="tag" style="--tc:' + S.topic.color + '">BAB ' + esc(S.topic.no) + '</span>' + esc(S.topic.short) + (S.round > 1 ? ' · <span style="color:var(--near)">ULANGAN ' + (S.round - 1) + '</span>' : '') + '</span>' +
      '<div class="row"><div class="phases">' + phaseNames.map(function (p) { return '<span class="phase-pill' + (p[0] === ph ? ' on' : '') + '">' + p[1] + '</span>'; }).join("") + '</div>' +
      '<button class="btn btn-ghost btn-sm" data-act="end">Tamat sesi</button></div>' +
      '</div>' +
      '<div class="progress-line" aria-hidden="true"><span style="width:' + Math.round(doneUnits * 100) + '%"></span></div>' +
      '<div class="row" style="justify-content:space-between;margin-bottom:12px">' +
      '<span class="counter">Nota ' + (S.qi + 1) + ' daripada ' + S.queue.length + (it.kind === "fu" ? ' · <span class="followup-tag">Soalan susulan ' + (it.fuIndex + 1) + '/' + it.fuTotal + '</span>' : '') + '</span>' +
      '<span class="counter">' + esc(st.id) + (st.trap ? ' · <span style="color:var(--bad)">TRAP</span>' : '') + (/^x/.test(st.id) ? ' · <span style="color:var(--text-2)">TAMBAHAN LAB</span>' : '') + '</span></div>';
  }

  function renderStudy() {
    if (!S) return;
    var st = curStmt(), it = curItem();
    var body = "";
    if (S.phase === "note") {
      body = '<article class="card card-tc note-card" style="--tc:' + S.topic.color + '">' +
        '<span class="eyebrow">' + (it.kind === "fu" ? 'NOTA SUSULAN · ' : '') + esc(st.section) + '</span>' +
        '<h2 class="h2">' + (it.kind === "fu" ? "Konteks soalan susulan" : esc(sectionTitle(st.section))) + '</h2>' +
        '<div class="rich">' + md(it.note) + '</div>' +
        '<div class="actions"><button class="btn btn-primary" data-act="tested">Saya dah baca, uji saya <span class="arrow">→</span></button></div>' +
        '</article>';
    } else {
      var isCode = it.type === "exact" && (it.answer || []).some(function (a) { return CODE_RX.test(a); });
      var locked = S.phase === "feedback" && (S.last.verdict === "ok" || S.attempts >= 3);
      body = '<article class="card card-tc" style="--tc:' + S.topic.color + '">' +
        '<div class="row" style="justify-content:space-between"><span class="eyebrow">' + (it.type === "exact" ? "JAWAPAN TEPAT" : "TERANGKAN DENGAN AYAT SENDIRI") + '</span>' +
        '<span class="attempts" aria-label="Cubaan ' + S.attempts + ' daripada 3">Cubaan ' + [0, 1, 2].map(function (i) { return '<i class="' + (i < S.attempts ? 'used' : '') + '"></i>'; }).join("") + '</span></div>' +
        '<div class="question">' + inline(it.question) + '</div>' +
        '<label class="sr-only" for="ans">Jawapan anda</label>' +
        '<textarea id="ans" class="answer-box' + (isCode ? ' code' : '') + '" placeholder="' + (it.type === "exact" ? "Taip jawapan tepat…" : "Tulis apa yang anda ingat dan faham…") + '"' + (locked ? ' readonly' : '') + ' spellcheck="false" autocapitalize="off" autocomplete="off">' + esc(S.input) + '</textarea>' +
        '<div class="type-hint">' + (it.type === "exact" ? "Ruang berlebihan dan koma diabaikan. Untuk kod, simbol seperti == ; & ++ mesti tepat." : "Disemak dengan kata kunci (English atau Bahasa Melayu). ≥ 70% = BETUL.") + ' · Ctrl/⌘ + Enter untuk hantar.</div>' +
        (S.phase === "feedback" ? feedbackHTML(st, it) : '<div class="actions"><button class="btn btn-primary" data-act="check">Semak jawapan</button></div>') +
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
  function sectionTitle(sec) { return String(sec || "").replace(/^[\d.]+\s*/, ""); }

  function feedbackHTML(st, it) {
    var r = S.last, final = r.verdict === "ok" || S.attempts >= 3;
    var label = r.verdict === "ok" ? "BETUL" : r.verdict === "near" ? "HAMPIR" : "SALAH";
    var ico = r.verdict === "ok" ? "✓" : r.verdict === "near" ? "≈" : "✕";
    var h = '<div class="feedback ' + r.verdict + '" role="status" aria-live="polite">' +
      '<div class="verdict"><span class="ico" aria-hidden="true">' + ico + '</span>' + label +
      (it.type === "explain" ? '<span class="pct">' + r.pct + '% kata kunci</span>' : '') + '</div>';
    if (r.verdict === "ok") {
      h += '<p class="fb-text">Markah item ini: <strong>' + ATTEMPT_SCORE[S.attempts - 1] + '%</strong> (cubaan ke-' + S.attempts + ').</p>';
    } else if (!final) {
      h += '<p class="fb-text">' + (r.empty ? "Jawapan kosong. " : "") + 'Cubaan ' + S.attempts + ' daripada 3. Cuba lagi.</p>';
    } else {
      h += '<p class="fb-text">3 cubaan habis. Item ini ditanda <strong>perlu ulang</strong>.</p>';
    }
    if (it.type === "explain" && (r.found.length || r.missing.length)) {
      h += '<div class="chips">' + r.found.map(function (k) { return '<span class="chip hit">' + esc(k) + '</span>'; }).join("") +
        (final ? r.missing.map(function (k) { return '<span class="chip miss">' + esc(k) + '</span>'; }).join("")
               : (r.missing.length ? '<span class="chip miss">' + r.missing.length + ' kata kunci tertinggal</span>' : '')) + '</div>';
    }
    if (!final && it.hint) h += '<div class="hint"><b>Hint</b>' + inline(it.hint) + '</div>';
    if (final) {
      if (r.verdict !== "ok") {
        var ans = it.type === "exact" ? (it.answer || []).join("   atau   ") : it.answer;
        if (ans) h += '<div class="reveal-box"><div class="eyebrow">JAWAPAN RUJUKAN</div><div class="ref-answer">' + esc(ans) + '</div></div>';
      } else if (it.type === "explain" && it.answer) {
        h += '<div class="reveal-box"><div class="eyebrow">JAWAPAN RUJUKAN</div><div class="ref-answer">' + esc(it.answer) + '</div></div>';
      }
      h += '<div class="reveal-box"><div class="eyebrow">NOTA ASAL UNTUK PERBANDINGAN</div><div class="rich">' + md(it.note) + '</div></div>';
    }
    h += '</div>';
    h += final
      ? '<div class="actions"><button class="btn btn-primary" data-act="next">Seterusnya <span class="arrow">→</span></button></div>'
      : '<div class="actions"><button class="btn btn-primary" data-act="retry">Cuba lagi</button></div>';
    return h;
  }

  function onStudyAction(e) {
    var act = e.currentTarget.getAttribute("data-act");
    if (act === "tested") { wipe(function () { S.phase = "answer"; S.attempts = 0; S.input = ""; renderStudy(); window.scrollTo(0, 0); }); }
    else if (act === "check") doCheck();
    else if (act === "retry") { S.phase = "answer"; renderStudy(); }
    else if (act === "next") nextItem();
    else if (act === "end") { if (confirm("Tamatkan sesi sekarang? Item yang belum dijawab tidak dikira.")) finishStudy(true); }
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
        '<span class="eyebrow"><span class="dot"></span>' + (S.round === 1 ? 'PUSINGAN PERTAMA SELESAI' : 'ULANGAN ' + (S.round - 1) + ' SELESAI') + '</span>' +
        '<h1 class="display">' + n + ' perlu ulang.</h1>' +
        '<p class="lead" style="margin:0 auto">Statement ini akan diulang bermula dengan FASA NOTA. Markah sesi dikira daripada pusingan pertama.</p>' +
        '<div class="row" style="justify-content:center;margin-top:28px"><button class="btn btn-primary" data-r="go">Ulang sekarang <span class="arrow">→</span></button><button class="btn btn-ghost" data-r="end">Lihat keputusan</button></div>' +
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
      stats: [[topicMastery(t.id) + "%", "Hafalan topik"], [mastered.length, "Dikuasai"], [redo.length, "Perlu ulang"]],
      groups: [
        { title: "Dikuasai", color: "var(--ok)", items: mastered.map(function (m) { return { id: m.st.id, q: m.st.question, sc: m.score + "%" }; }) },
        { title: "Perlu ulang", color: "var(--bad)", items: redo.map(function (m) { return { id: m.st.id, q: m.st.question, sc: m.score + "%" + (m.reviewOk ? " · lulus ulangan" : "") }; }) }
      ],
      again: "#/study/" + t.id + (redo.length ? "/weak" : "")
    });
    S = null;
  }

  // ---------------------------------------------------------------- RESULTS
  function renderResults(o) {
    var t = o.topic;
    app.innerHTML = '<section class="result-hero"><div class="wrap">' +
      '<span class="eyebrow rv">' + (t ? '<span class="tag" style="--tc:' + t.color + '">BAB ' + esc(t.no) + '</span>' + esc(t.short) : '<span class="tag trap">TRAP</span>SEMUA BAB') + ' · ' + (o.kind === "study" ? "KEPUTUSAN SESI HAFALAN" : "KEPUTUSAN KUIZ") + '</span>' +
      '<div class="giant rv rv-d1"><span data-count="' + o.pct + '">' + o.pct + '</span><small>%</small></div>' +
      '<p class="lead rv rv-d2">' + (o.kind === "study" ? "Markah sesi (1st = 100%, 2nd = 60%, 3rd = 30%, gagal = 0%)." : "Jawapan betul daripada semua soalan.") + (o.early ? " Sesi ditamatkan awal; hanya statement yang lengkap dikira." : "") + '</p>' +
      '<div class="result-stats rv">' + o.stats.map(function (s) { return '<div><span class="num"' + (typeof s[0] === "number" ? ' data-count="' + s[0] + '"' : '') + '>' + esc(s[0]) + '</span><div class="eyebrow">' + esc(s[1]) + '</div></div>'; }).join("") + '</div>' +
      o.groups.map(function (g, gi) {
        return '<details class="acc rv"' + (gi === 1 && g.items.length ? ' open' : '') + '><summary><span class="sw" style="background:' + g.color + '"></span>' + esc(g.title) + ' <span class="count">' + g.items.length + '</span><span class="plus" aria-hidden="true">+</span></summary>' +
          (g.items.length ? '<ul class="acc-list">' + g.items.map(function (i) { return '<li><span class="sid">' + esc(i.id) + '</span><span class="q">' + inline(i.q) + '</span><span class="sc">' + esc(i.sc) + '</span></li>'; }).join("") + '</ul>' : '<p style="color:var(--text-2);margin:0 0 22px">Tiada.</p>') +
          '</details>';
      }).join("") +
      '<div class="row" style="margin-top:32px"><a class="btn btn-primary" href="' + o.again + '">Ulang lagi <span class="arrow">→</span></a>' +
      (t ? '<a class="btn btn-ghost" href="#/topic/' + t.id + '">Kembali ke topik</a>' : '') + '<a class="btn btn-ghost" href="#/">Halaman utama</a></div>' +
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
    if (!list.length) { app.innerHTML = emptyState("Tiada soalan MCQ untuk kuiz ini.", t ? "#/topic/" + t.id : "#/"); return; }
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
      '<div class="quiz-head"><span class="eyebrow">' + (Q.trap ? '<span class="tag trap">KUIZ TRAP</span>' : '') + '<span class="tag" style="--tc:' + tp.color + '">BAB ' + esc(tp.no) + '</span>' + esc(tp.short) + '</span>' +
      '<span class="streak" id="streak"><span class="flame" aria-hidden="true">🔥</span><span>' + Q.streak + '</span><span class="sr-only">streak</span></span></div>' +
      '<div class="row" style="justify-content:space-between;margin-bottom:10px"><span class="counter">Soalan ' + (Q.i + 1) + ' daripada ' + Q.list.length + '</span><span class="counter" id="secs">' + QUIZ_SECONDS + 's</span></div>' +
      '<div class="timer" id="timer"><span></span></div>' +
      '<article class="card card-tc" style="--tc:' + tp.color + '">' +
      '<div class="question">' + inline(s.mcq.question) + '</div>' +
      '<div class="options" role="group" aria-label="Pilihan jawapan">' + Q.opts.map(function (o, i) {
        return '<button class="opt" data-i="' + i + '"><span class="k">' + "ABCD"[i] + '</span><span>' + inline(o.text) + '</span></button>';
      }).join("") + '</div>' +
      '<div id="qfb"></div>' +
      '</article>' +
      '<div class="row" style="justify-content:flex-end;margin-top:16px"><button class="btn btn-ghost btn-sm" id="qend">Tamat kuiz</button></div>' +
      '</div></div></section>';
    $all(".opt", app).forEach(function (b) { b.addEventListener("click", function () { answerQuiz(parseInt(b.getAttribute("data-i"), 10)); }); });
    $("#qend", app).addEventListener("click", function () { if (confirm("Tamatkan kuiz sekarang?")) finishQuiz(); });
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
    fb.innerHTML = '<div class="feedback ' + (ok ? "ok" : "bad") + '" role="status"><div class="verdict"><span class="ico" aria-hidden="true">' + (ok ? "✓" : "✕") + '</span>' + (ok ? "BETUL" : (i < 0 ? "MASA TAMAT" : "SALAH")) + '</div>' +
      (ok ? '' : '<p class="fb-text">Jawapan betul: <strong>' + inline(correctText) + '</strong></p>') +
      '<div class="reveal-box"><div class="eyebrow">NOTA · ' + esc(s.id) + ' · ' + esc(s.section) + '</div><div class="rich">' + md(s.text) + '</div></div></div>' +
      '<div class="actions"><button class="btn btn-primary" id="qnext">' + (Q.i + 1 < Q.list.length ? 'Seterusnya <span class="arrow">→</span>' : 'Lihat keputusan') + '</button></div>';
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
      stats: [[o.correct + "/" + asked, "Betul"], [o.best, "Streak terbaik"], [PROG.bestStreak, "Rekod streak"]],
      groups: [
        { title: "Betul", color: "var(--ok)", items: o.right.map(function (s) { return { id: s.id, q: s.mcq.question, sc: "✓" }; }) },
        { title: "Perlu ulang", color: "var(--bad)", items: o.wrong.map(function (s) { return { id: s.id, q: s.mcq.question, sc: "✕" }; }) }
      ],
      again: "#/quiz/" + o.scope + (o.trap && o.scope !== "trap" ? "/trap" : "")
    });
    Q = null;
  }

  function emptyState(msg, back) {
    return '<section class="hero"><div class="wrap"><h1 class="h2">' + esc(msg) + '</h1><div class="row" style="margin-top:24px"><a class="btn btn-ghost" href="' + back + '">Kembali</a></div></div></section>';
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
      '<span class="eyebrow rv"><span class="dot"></span>URUS NOTA</span>' +
      '<h1 class="display rv rv-d1" style="font-size:clamp(2.4rem,6vw,4.6rem)">Tambah, edit, padam.</h1>' +
      '<p class="lead rv rv-d2">' + DATA.statements.length + ' statement. ' + (isCustomData() ? 'Anda sedang guna data yang telah diubah (disimpan dalam localStorage).' : 'Anda sedang guna data asal daripada data.js.') + '</p>' +
      (customOutdated ? '<div class="notice err" style="margin-top:16px">Data dalam pelayar ini lebih lama daripada data.js terkini (nota PDF penuh). Export dahulu jika perlu, kemudian tekan <b>Reset ke data asal</b>.</div>' : '') +
      '<div class="toolbar"><a class="btn btn-primary" href="#/manage/new">+ Tambah statement</a>' +
      '<button class="btn btn-ghost" id="exp">Export JSON</button>' +
      '<label class="btn btn-ghost" for="imp" style="cursor:pointer">Import JSON</label><input type="file" id="imp" accept=".json,application/json" class="sr-only">' +
      '<button class="btn btn-danger" id="reset">Reset ke data asal</button>' +
      '<button class="btn btn-danger" id="resetp">Padam kemajuan</button></div>' +
      '<div class="grid-2"><div class="field"><label for="ft">Topik</label><select id="ft" class="select"><option value="">Semua topik</option>' +
      DATA.topics.map(function (t) { return '<option value="' + t.id + '"' + (manageFilter.topic === t.id ? ' selected' : '') + '>' + esc(t.no + " · " + t.title) + '</option>'; }).join("") + '</select></div>' +
      '<div class="field"><label for="fq">Cari</label><input id="fq" class="input" type="search" value="' + esc(manageFilter.q) + '" placeholder="ID, soalan atau isi nota"></div></div>' +
      '</div></section>' +
      '<section style="padding-bottom:80px"><div class="wrap"><div class="list">' +
      list.map(function (s) {
        var t = topicById(s.topic) || { color: "#666", no: "?" };
        return '<div class="list-item"><div><div class="meta"><span class="tag" style="--tc:' + t.color + '">BAB ' + esc(t.no) + '</span><span class="mono">' + esc(s.id) + '</span>' + (s.trap ? '<span class="tag trap">TRAP</span>' : '') + '<span>' + esc(s.type) + '</span><span>' + (s.followUps || []).length + ' susulan</span></div>' +
          '<div class="q">' + inline(s.question) + '</div></div>' +
          '<div class="row"><a class="btn btn-ghost btn-sm" href="#/manage/' + encodeURIComponent(s.id) + '">Edit</a><button class="btn btn-danger btn-sm" data-del="' + esc(s.id) + '">Padam</button></div></div>';
      }).join("") + (list.length ? '' : '<p style="color:var(--text-2);padding:20px 0">Tiada statement sepadan.</p>') +
      '</div></div></section>';

    $("#ft", app).addEventListener("change", function (e) { manageFilter.topic = e.target.value; route(); });
    var fq = $("#fq", app), deb;
    fq.addEventListener("input", function (e) {
      clearTimeout(deb); deb = setTimeout(function () { manageFilter.q = e.target.value; route(); var f = $("#fq", app); if (f) { f.focus(); f.setSelectionRange(f.value.length, f.value.length); } }, 250);
    });
    $all("[data-del]", app).forEach(function (b) {
      b.addEventListener("click", function () {
        var id = b.getAttribute("data-del");
        if (!confirm("Padam statement " + id + "?")) return;
        DATA.statements = DATA.statements.filter(function (s) { return s.id !== id; });
        saveData(); toast("Statement " + id + " dipadam"); route();
      });
    });
    $("#exp", app).addEventListener("click", exportJSON);
    $("#imp", app).addEventListener("change", importJSON);
    $("#reset", app).addEventListener("click", function () {
      if (!confirm("Buang semua perubahan dan kembali ke data asal data.js?")) return;
      lsDel(KEY_DATA); DATA = clone(DEFAULT); toast("Data asal dipulihkan"); route();
    });
    $("#resetp", app).addEventListener("click", function () {
      if (!confirm("Padam semua kemajuan hafalan, streak dan bilangan sesi?")) return;
      PROG = { stmts: {}, sessions: 0, bestStreak: 0 }; saveProg(); toast("Kemajuan dipadam");
    });
  }
  function exportJSON() {
    var blob = new Blob([JSON.stringify(DATA, null, 2)], { type: "application/json" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "scse1013-notes-" + new Date().toISOString().slice(0, 10) + ".json";
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
    toast("Fail JSON dimuat turun");
  }
  function importJSON(e) {
    var f = e.target.files && e.target.files[0];
    if (!f) return;
    var rd = new FileReader();
    rd.onload = function () {
      try {
        var d = JSON.parse(rd.result);
        if (Array.isArray(d)) d = { topics: DATA.topics, statements: d };
        if (!d || !Array.isArray(d.statements)) throw new Error("Tiada senarai 'statements'.");
        d.statements.forEach(function (s, i) {
          var err = validateStmt(s, d.statements.slice(0, i).map(function (x) { return x.id; }));
          if (err) throw new Error((s && s.id ? s.id : "#" + (i + 1)) + ": " + err);
        });
        if (!Array.isArray(d.topics) || !d.topics.length) d.topics = DATA.topics;
        DATA = d; saveData(); toast("Import berjaya: " + d.statements.length + " statement"); route();
      } catch (err) { alert("Import gagal. " + err.message); }
    };
    rd.readAsText(f);
  }
  function validateStmt(s, takenIds) {
    if (!s || typeof s !== "object") return "bukan objek";
    if (!s.id || !/^[A-Za-z0-9_-]+$/.test(s.id)) return "id mesti huruf/nombor/_/- sahaja";
    if (takenIds.indexOf(s.id) >= 0) return "id berulang";
    if (!topicById(s.topic) && !(DATA.topics || []).length) return "topik tidak sah";
    if (!s.text || !s.question) return "text dan question wajib";
    if (s.type !== "explain" && s.type !== "exact") return "type mesti explain atau exact";
    if (s.type === "explain" && !(s.keywords || []).length) return "explain perlu sekurang-kurangnya satu keyword";
    if (s.type === "exact" && !(Array.isArray(s.answer) && s.answer.length)) return "exact perlu senarai answer";
    if (s.followUps && !Array.isArray(s.followUps)) return "followUps mesti array";
    if (s.mcq && !(Array.isArray(s.mcq.options) && s.mcq.options.length === 4)) return "mcq perlu 4 pilihan";
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
      '<span class="eyebrow"><span class="dot"></span>URUS NOTA · ' + (isNew ? "STATEMENT BARU" : "EDIT " + esc(s.id)) + '</span>' +
      '<h1 class="h2" style="margin-top:14px">' + (isNew ? "Tambah statement" : "Edit statement") + '</h1></div></section>' +
      '<section style="padding-bottom:80px"><div class="wrap"><form id="ed" class="card" novalidate>' +
      '<div class="grid-2">' +
      fld("ID", '<input class="input mono" name="id" required value="' + esc(s.id) + '" placeholder="cp99">', "Unik. Huruf, nombor, _ atau -.") +
      fld("Topik", '<select class="select" name="topic">' + DATA.topics.map(function (t) { return '<option value="' + t.id + '"' + (t.id === s.topic ? ' selected' : '') + '>' + esc(t.no + " · " + t.title) + '</option>'; }).join("") + '</select>') +
      fld("Bahagian (tajuk kecil PDF)", '<input class="input" name="section" value="' + esc(s.section) + '" placeholder="3.8 Arithmetic operators">') +
      fld("Jenis soalan", '<select class="select" name="type"><option value="explain"' + (s.type === "explain" ? ' selected' : '') + '>explain: ayat sendiri (kata kunci)</option><option value="exact"' + (s.type === "exact" ? ' selected' : '') + '>exact: jawapan tepat</option></select>') +
      '</div>' +
      '<div class="check"><input type="checkbox" id="trap" name="trap"' + (s.trap ? ' checked' : '') + '><label for="trap">Bahagian TRAP / Common traps / Invalid headers (masuk Kuiz Trap)</label></div>' +
      fld("Nota (text)", '<textarea class="textarea" name="text" rows="9">' + esc(s.text) + '</textarea>', "Format: **tebal**, `kod`, baris bermula - untuk senarai, | untuk jadual, ``` untuk blok kod C++.") +
      fld("Soalan", '<textarea class="textarea" name="question" rows="2">' + esc(s.question) + '</textarea>') +
      fld("Keywords (explain)", '<textarea class="textarea" name="keywords" rows="4" placeholder="decomposition|pecahkan|bahagi kepada bahagian kecil">' + esc((s.keywords || []).join("\n")) + '</textarea>', "Satu kata kunci wajib setiap baris. Sinonim dipisah dengan | (English dan Bahasa Melayu).") +
      fld("Jawapan", '<textarea class="textarea" name="answer" rows="3">' + esc(answerText) + '</textarea>', "explain: jawapan rujukan. exact: satu jawapan diterima setiap baris (contoh 10 9 8 dan 10, 9, 8).") +
      fld("Hint", '<input class="input" name="hint" value="' + esc(s.hint) + '">', "Petunjuk tanpa memberi jawapan.") +
      fld("Soalan susulan (JSON)", '<textarea class="textarea" name="followUps" rows="10">' + esc(JSON.stringify(s.followUps || [], null, 2)) + '</textarea>', 'Array 1–3 objek: {"note","question","type":"exact"|"explain","answer":[…] atau "…","keywords":[…],"hint"}.') +
      '<hr class="sep"><div class="eyebrow" style="margin-bottom:14px">MCQ (4 PILIHAN)</div>' +
      fld("Soalan MCQ", '<input class="input" name="mq" value="' + esc(mcq.question) + '">') +
      fld("Pilihan BETUL", '<input class="input" name="mc" value="' + esc(correct) + '">') +
      '<div class="grid-2">' + wrongs.slice(0, 3).map(function (w, i) { return fld("Pilihan salah " + (i + 1), '<input class="input" name="mw' + i + '" value="' + esc(w) + '">'); }).join("") + '</div>' +
      '<div id="edErr"></div>' +
      '<div class="actions"><button class="btn btn-primary" type="submit">Simpan</button><a class="btn btn-ghost" href="#/manage">Batal</a></div>' +
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
      catch (x) { err.innerHTML = '<div class="notice err">Soalan susulan: JSON tidak sah (' + esc(x.message) + ').</div>'; return; }
      var opts = [f.mc.value.trim(), f.mw0.value.trim(), f.mw1.value.trim(), f.mw2.value.trim()];
      ns.mcq = { question: f.mq.value.trim(), options: opts, correct: 0 };
      var taken = DATA.statements.filter(function (x) { return !s || x.id !== (isNew ? "\u0000" : id); }).map(function (x) { return x.id; });
      var msg = validateStmt(ns, taken);
      if (!msg && ns.mcq.question && opts.some(function (o) { return !o; })) msg = "MCQ perlu 4 pilihan yang diisi";
      if (!msg && !ns.mcq.question) msg = "MCQ wajib (soalan dan 4 pilihan)";
      if (!msg) (ns.followUps || []).forEach(function (fu, i) {
        if (msg) return;
        if (!fu.note || !fu.question) msg = "Soalan susulan " + (i + 1) + ": note dan question wajib";
        else if (fu.type === "exact" && !(Array.isArray(fu.answer) && fu.answer.length)) msg = "Soalan susulan " + (i + 1) + ": exact perlu senarai answer";
        else if (fu.type !== "exact" && !(fu.keywords || []).length) msg = "Soalan susulan " + (i + 1) + ": explain perlu keywords";
      });
      if (msg) { err.innerHTML = '<div class="notice err">' + esc(msg) + '</div>'; err.scrollIntoView({ block: "center" }); return; }
      if (isNew) DATA.statements.push(ns);
      else {
        var idx = DATA.statements.findIndex(function (x) { return x.id === id; });
        DATA.statements[idx] = ns;
        if (id !== ns.id && PROG.stmts[id]) { PROG.stmts[ns.id] = PROG.stmts[id]; delete PROG.stmts[id]; saveProg(); }
      }
      saveData(); toast("Disimpan: " + ns.id); location.hash = "#/manage";
    });
  }
  function fld(label, control, help) {
    return '<label class="field"><span class="lbl">' + esc(label) + '</span>' + control + (help ? '<span class="help">' + esc(help) + '</span>' : '') + '</label>';
  }

  // expose engine for testing
  window.SCSE = { checkExplain: checkExplain, checkExact: checkExact, evaluate: evaluate, md: md, levenshtein: levenshtein };

  route();
})();
