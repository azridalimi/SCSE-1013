"""Generate ../COVERAGE.md from data.js.  Run: python3 tools/build_coverage.py"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "data.js"), encoding="utf-8").read()
data = json.loads(src[src.index("{"): src.rstrip().rindex("}") + 1])
S = {s["id"]: s for s in data["statements"]}

SOURCES = {
 "cpp": ("Lab 4 · Ch3 Basic of programming (Topics covered)", [
   ("Parts of a program: keywords, identifiers, operators, punctuation, comments (slides 2–15, 22–25)", "cp01 cp02 cp03 cp04 cp05"),
   ("Variables and literals (slides 16–21, 26–31, 71–72)", "cp06"),
   ("Input and output with cin and cout, strings (slides 33–47)", "cp07 cp08"),
   ("Data types and number systems (slides 48–62, 70)", "cp09 cp10 cp11 cp12"),
   ("Named constants and the string class (slides 63–69)", "cp13 cp14"),
   ("Scope (slides 73–74)", "cp15"),
   ("Arithmetic operators, precedence, / and % (slides 75–86, 92)", "cp16 cp17 cp18 cp25"),
   ("Type conversion and casting (slides 87–91, 99–102)", "cp19 cp23"),
   ("Overflow, ++ and --, combined assignment (slides 94–98, 103–108)", "cp20 cp21 cp22"),
   ("Part A1 compile-error log", "cp24 cp01 cp02 cp05 cp07 cp15")]),
 "ctrl": ("Lab 5 · Ch4 Control structures (Topics covered)", [
   ("Relational and logical operators (slides 2–8, 11)", "cs01 cs02"),
   ("Complements of conditions (slides 9–10, 36)", "cs03"),
   ("if, if…else, nested and compound statements (slides 12–35)", "cs04 cs05 cs06 cs07 cs08 cs09"),
   ("n%2==1 with negatives (slide 37), leap year", "cs10 cs11"),
   ("Conditional expression ?: (slides 38–39)", "cs12"),
   ("switch and the selection patterns (slides 40–55)", "cs13 cs14 cs24"),
   ("Loop parts and while, for, do…while (slides 56–73)", "cs15 cs16 cs17 cs18 cs19 cs20"),
   ("break and continue (slides 74–80)", "cs21"),
   ("Loop patterns: counting, totals, sentinel (slides 84–91)", "cs22"),
   ("Nested loops (slides 92–94)", "cs23"),
   ("Debugger (Part A)", "cs25")]),
 "func": ("Lab 6 · Ch5 Functions: predefined functions (Topics covered) + user-defined functions", [
   ("Library functions and header files (slides 4–7)", "fn01 fn02"),
   ("Math functions in <cmath> (slides 8–13)", "fn03 fn04"),
   ("General-purpose library: rand (slide 14)", "fn05"),
   ("Character functions in <cctype> (slides 15–23)", "fn06"),
   ("C-string functions in <cstring> (slides 24–33)", "fn07"),
   ("String and number conversion: atoi, atol, atof (slides 34–36)", "fn08"),
   ("User-defined functions: prototype, parameters, return, void", "fn09 fn10 fn11 fn12"),
   ("Pass by value / reference, scope, static", "fn13 fn14 fn15 fn16"),
   ("Default arguments, overloading", "fn17 fn18"),
   ("Invalid headers and call errors", "fn19 fn20")]),
}

topics = {t["id"]: t for t in data["topics"]}
L = []
L.append("# COVERAGE: nota → statement\n")
L.append("> **Status: provisional.** `SCSE1013_Study_Notes.pdf` was not available when this data was built.")
L.append("> The statements are based on the SCSE1013 Lab 4, 5 and 6 documents (which follow the Ch3–Ch5 slide order)")
L.append("> and the standard SCSE1013 syllabus for Ch1, Ch2 and the cheat sheet. When the PDF is added, re-map each PDF")
L.append("> heading below and add statements for anything missing.\n")
L.append("Total: **%d statements**, **%d follow-up questions**, **%d TRAP statements** (used by Kuiz Trap).\n" % (
    len(S), sum(len(s["followUps"]) for s in S.values()), sum(s["trap"] for s in S.values())))
for t in data["topics"]:
    L.append("\n## Bab %s · %s\n" % (t["no"], t["title"]))
    if t["id"] in SOURCES:
        title, rows = SOURCES[t["id"]]
        L.append("**Source map: %s**\n" % title)
        L.append("| Source section | Statement IDs |\n|---|---|")
        for sec, ids in rows:
            for i in ids.split(): assert i in S, i
            L.append("| %s | %s |" % (sec.replace("|", "\\|"), ", ".join(ids.split())))
        L.append("")
    L.append("| Heading (tajuk kecil) | ID | TRAP | Follow-ups | Main question |\n|---|---|---|---|---|")
    for s in [x for x in data["statements"] if x["topic"] == t["id"]]:
        q = s["question"].replace("|", "\\|").replace("\n", " ")
        L.append("| %s | `%s` | %s | %d | %s |" % (s["section"], s["id"], "✓" if s["trap"] else "", len(s["followUps"]), q))
open(os.path.join(HERE, "..", "COVERAGE.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("COVERAGE.md written")
