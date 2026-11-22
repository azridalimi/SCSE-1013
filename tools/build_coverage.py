"""Generate ../COVERAGE.md: every item of SCSE1013_Study_Notes.pdf -> statement IDs.
Run: python3 tools/build_coverage.py   (fails if an ID does not exist or a PDF statement is unmapped)"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "data.js"), encoding="utf-8").read()
data = json.loads(src[src.index("{"): src.rstrip().rindex("}") + 1])
S = {s["id"]: s for s in data["statements"]}

# (PDF heading, [(item in the PDF, "ids")])
PDF = [
 ("1 · Computational Thinking", [
  ("Definition: solving a problem the way a computer would (break, patterns, steps)", "ct01"),
  ("4 key skills · Decomposition", "ct02"), ("4 key skills · Pattern recognition", "ct03"),
  ("4 key skills · Abstraction", "ct04"), ("4 key skills · Algorithm design", "ct05"),
  ("💡 MEMORY TRICK D-P-A-A", "ct06 ch01"),
  ("5 stages row 1 · Decomposition (divide and conquer)", "ct07"),
  ("5 stages row 2 · Generalisation & Pattern Recognition", "ct08"),
  ("5 stages row 3 · Modelling", "ct09"), ("5 stages row 4 · Abstraction", "ct10"),
  ("5 stages row 5 · Evaluation", "ct11"),
  ("Traffic example (5 rows)", "ct12 ct02 ct03 ct04 ct09 ct11"),
  ("Related ways of thinking · Logical thinking (Identify → Analyse → Formulate → Evaluate)", "ct13"),
  ("Related ways of thinking · Algorithmic thinking (Define → … → Evaluate)", "ct14"),
  ("Where it's used", "ct15")]),
 ("2 · Problem Solving: Algorithms, Pseudocode & Flowcharts", [
  ("The programming process", "al01"),
  ("IPO table · Rectangle area", "al02"), ("IPO table · Income tax", "al03"),
  ("💡 TIP nouns = inputs, formula = process, display = output", "al04"),
  ("Procedural vs Object-Oriented", "al05"),
  ("Algorithm definition", "al06"), ("Algorithm requirements (7)", "al07"),
  ("Three ways to design (pseudocode, flowchart, top-down/structure chart)", "al08"),
  ("Pseudocode + income tax example", "al09"),
  ("Flowchart symbol · Terminal (function ends with Return)", "al10"),
  ("Flowchart symbol · Process", "al11"), ("Flowchart symbol · Input/Output", "al12"),
  ("Flowchart symbol · Decision", "al13"), ("Flowchart symbol · Function/Subroutine", "al14"),
  ("Flowchart symbol · Connectors; flowline; comment symbol", "al15"),
  ("3 control structures", "al16 ch03"),
  ("Selection forms (3 rows)", "al17"),
  ("Operators · Relational table", "al18"), ("Operators · Logical table", "al19"),
  ("💡 MEMORY TRICK AND is strict / OR is generous + x=12,y=5,z=−4 example", "al20"),
  ("Repetition · Pre-test vs Post-test", "al21"),
  ("Counter-controlled loop 3 parts", "al22"),
  ("Pseudocode sum 1..10 → 55", "al23"),
  ("User-controlled loop (limit); Sentinel (-999, \"OK\")", "al24"),
  ("Trace table (Length/Width/Area/Perimeter rows)", "al25"),
  ("Modular flowcharts · call = what, definition = how", "al26"),
  ("Modular flowcharts · AVRG(R, a, b, c) … Return", "al27"),
  ("Modular flowcharts · actual vs formal, matched by order", "al28"),
  ("Modular flowcharts · only variables in the current chart", "al29"),
  ("From flowchart to code", "al30")]),
 ("3 · Basics of C++ Programming", [
  ("Parts of a C++ program (sample code, #include no ;, main, return 0 → OS \"OK\")", "cp01"),
  ("Keywords (reserved, lowercase, not names)", "cp02"),
  ("Identifiers, operators, punctuation, syntax", "cp03"),
  ("⚠ REMEMBER case-sensitive (Main ≠ main), every { needs }", "cp04"),
  ("Special characters · // /* */ and #", "cp05"),
  ("Special characters · < >, ( ), { }", "cp06"),
  ("Special characters · ;, \" \", ' '", "cp07"),
  ("Variables (named memory location, declare first, overwrite)", "cp08"),
  ("Identifier rules", "cp09"),
  ("Identifier table (totalSales/total_Sales ✅, total.Sales, 4thQtrSales, totalSale$ ❌)", "cp10"),
  ("Literal", "cp11"),
  ("Input & output (cout, cin, endl/\\n, spaces, prompt)", "cp12"),
  ("💡 MEMORY TRICK arrows point where the data goes", "cp13"),
  ("Data types row · char", "cp14"), ("Data types row · bool", "cp15"),
  ("Data types row · short/int/long", "cp16"), ("Data types rows · float, double", "cp17"),
  ("Data types row · string", "cp18"),
  ("'C' vs \"C\" (C + \\0)", "cp19"), ("C-string char name[21]", "cp20"),
  ("Truncation int r = 3.88 → 3", "cp21 ch04"), ("Number bases, 1234L", "cp22"), ("sizeof", "cp23"),
  ("Constants (const vs #define, cannot change, UPPERCASE)", "cp24"),
  ("Assignment size = 5 ✅ / 5 = size ❌", "cp25"), ("Initialisation", "cp26"), ("Scope", "cp27"),
  ("Arithmetic table · + − * (10, 4, 21)", "cp28"),
  ("Arithmetic table · / integer division, 13/5.0 = 2.6", "cp29"),
  ("Arithmetic table · % remainder, integers only", "cp30"),
  ("✔ ORDER OF OPERATIONS + 2+2*2-2 = 4, (2+2)*2-2 = 6", "cp31"),
  ("No ^ operator → pow(s, 2)", "cp32"),
  ("Type conversion · promotion order", "cp33"),
  ("char/short → int; = takes left-hand type", "cp34"),
  ("Manual cast (static_cast, (int)ch, int(ch))", "cp35"),
  ("Overflow/underflow wrap around", "cp36"),
  ("Prefix vs postfix", "cp37"), ("kira = 5 example → 35, kira 4", "cp38"),
  ("Combined assignment table (i += 3, i *= j+3)", "cp39"),
  ("x = y = z = 5 right to left", "cp40")]),
 ("4 · Control Structures in C++", [
  ("bool ↔ int (2 + true = 3, any non-zero = true, even −10)", "cs01 ch06"),
  ("if statement: 3 forms; braces optional; compound statement", "cs02"),
  ("if-else if grade chain", "cs03"),
  ("⚠ Common traps row 1 · if (x = 0)", "cs04"),
  ("⚠ Common traps row 2 · if (2 < x < 9)", "cs05"),
  ("⚠ Common traps row 3 · if (0<x) && (x<10)", "cs06"),
  ("⚠ Common traps row 4 · if (!n > 9)", "cs07"),
  ("⚠ Common traps row 5 · if (x<3);", "cs08"),
  ("⚠ Common traps row 6 · 2 statements before else with no { }", "cs09"),
  ("⚠ Common traps row 7 · nested if with no braces (dangling else)", "cs10"),
  ("⚠ Common traps row 8 · indentation only", "cs11"),
  ("Shortcuts table (if (a), if (!a), if (n%2))", "cs12"),
  ("Conditional (ternary) operator, p = (p<5) ? q+1 : 5", "cs13"),
  ("Complement a condition !( )", "cs14"),
  ("switch example + integral types (int, char, bool)", "cs15"),
  ("switch · case values must be constants", "cs16"),
  ("switch · fall through without break", "cs17"), ("switch · default", "cs18"),
  ("Loops · 4 parts, forgetting update → infinite loop", "cs19"),
  ("Loops · while / for / do-while print 10..1, do-while ends with ;", "cs20"),
  ("Loop 'use when' table (3 rows)", "cs21"),
  ("Jump · break (nested: inner only) + example 10 9 8", "cs22"),
  ("Jump · continue (for → update, while → condition) + example 10 8 6 4 2", "cs23"),
  ("Jump · return, goto", "cs24"),
  ("⚠ TRAP continue before update in while → 9 9 9 …", "cs25"),
  ("Nested loops (outer × inner, 3 × 3 = 9)", "cs26")]),
 ("5 · Functions", [
  ("Modular programming, main() short", "fn01"),
  ("Library table · <cmath>", "fn02"), ("Library table · <cctype>", "fn03"),
  ("Library table · <cstring>", "fn04"), ("Library table · <cstdlib>", "fn05"),
  ("⚠ C-STRINGS (no == or =, strcmp 0 = same)", "fn06"),
  ("User-defined function structure", "fn07"),
  ("Prototype / Definition / Call table", "fn08"),
  ("Compiler must know name, return type, number & types of parameters", "fn09"),
  ("void", "fn10"), ("Arguments (actual) vs parameters (formal), by order, same number", "fn11"),
  ("Using a returned value (assign, print, expression)", "fn12"),
  ("Returning bool (isEven)", "fn13"),
  ("⚠ INVALID HEADERS · one(int a, int b)", "fn14"),
  ("⚠ INVALID HEADERS · char another(int a, b)", "fn15"),
  ("⚠ INVALID HEADERS · double yetanother", "fn16"),
  ("Pass by value (m = 612 stays 612)", "fn17"),
  ("Pass by reference (alias, & in prototype & header, variable only)", "fn18"),
  ("💡 MEMORY TRICK photocopy vs original", "fn19"),
  ("Lifetime table · Local", "fn20"), ("Lifetime table · Global", "fn21"),
  ("Lifetime table · Static local + showVar example", "fn22"),
  ("Local wins over global", "fn23"),
  ("Default arguments (getSum, right end, leave out everything after)", "fn24"),
  ("Function overloading (getDimensions ×4)", "fn25"),
  ("return vs exit() (EXIT_SUCCESS / EXIT_FAILURE)", "fn26")]),
 ("6 · One-Page Cheat Sheet", [
  ("Computational thinking box", "ch01"), ("Problem solving box", "ch02"),
  ("3 control structures + Flowchart shapes boxes", "ch03"), ("Integer maths box", "ch04"),
  ("Precedence box", "ch05"), ("Truth box", "ch06"), ("= vs == box", "ch07"),
  ("switch + Loops boxes", "ch08"), ("break/continue + Function parts boxes", "ch09"),
  ("Value vs reference + Variable lifetime boxes", "ch10"),
  ("Default args + Overloading boxes", "ch11"),
  ("✔ EXAM-DAY CHECKLIST items 1–2", "ch12"), ("✔ EXAM-DAY CHECKLIST item 3", "ch13"),
  ("✔ EXAM-DAY CHECKLIST items 4–5", "ch14")]),
]

used = set()
for _, rows in PDF:
    for _, ids in rows:
        for i in ids.split():
            assert i in S, "unknown id " + i
            used.add(i)
pdf_ids = {i for i, s in S.items() if not i.startswith("x")}
unmapped = sorted(pdf_ids - used)
assert not unmapped, "PDF statements not in COVERAGE: %s" % unmapped

n_pdf = len(pdf_ids); n_x = len(S) - n_pdf
L = ["# COVERAGE: SCSE1013_Study_Notes.pdf → statement\n",
     "Every heading, table row, TIP, REMEMBER, TRAP, memory trick and example in the PDF is listed below with the statement ID(s) that test it. "
     "Generated by `tools/build_coverage.py`, which fails if a mapped ID is missing or a PDF statement is not mapped.\n",
     "- **%d** statements from the PDF + **%d** lab extras (`x…` IDs) = **%d** total" % (n_pdf, n_x, len(S)),
     "- **%d** follow-up questions, one MCQ per statement" % sum(len(s["followUps"]) for s in S.values()),
     "- **%d** TRAP statements (Common traps ×8, TRAP ×1, INVALID HEADERS ×3) used by **Kuiz Trap**\n" % sum(s["trap"] for s in S.values())]
for head, rows in PDF:
    L.append("\n## %s\n" % head)
    L.append("| PDF item | Statement IDs |\n|---|---|")
    for item, ids in rows:
        L.append("| %s | %s |" % (item.replace("|", "\\|"), ", ".join("`%s`" % i for i in ids.split())))
L.append("\n## Tambahan (Lab 4–6, not in the PDF)\n")
L.append("Extra practice from the lab documents. Labelled *Extra (Lab)* in the app and never used by Kuiz Trap.\n")
L.append("| ID | Topic | Section |\n|---|---|---|")
for s in data["statements"]:
    if s["id"].startswith("x"):
        L.append("| `%s` | %s | %s |" % (s["id"], s["topic"], s["section"].replace("|", "\\|")))
open(os.path.join(HERE, "..", "COVERAGE.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("COVERAGE.md written:", n_pdf, "PDF statements all mapped,", n_x, "extras")
