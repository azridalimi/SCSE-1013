# Memorise SCSE1013

A web app for **memorising and understanding** the SCSE1013 Fundamental Programming Concepts notes.
Plain HTML, CSS and JavaScript only: no backend, no framework.

**To open:** double-click `index.html`. It runs straight from the file (`file://`) and also works offline (fonts fall back to system fonts).

## Files

| File | Purpose |
|---|---|
| `index.html` | Page shell; loads `data.js` then `app.js` |
| `styles.css` | Dark editorial theme (black + blue #2F5BFF), responsive, respects `prefers-reduced-motion` |
| `data.js` | All statements (`window.SCSE_DEFAULT_DATA`): 6 topics, 151 statements from the PDF + 23 lab extras, 260 follow-up questions |
| `app.js` | Engine: routing, memorise mode (Note → Answer → Check), MCQ quiz, scoring, Manage Notes |
| `COVERAGE.md` | Maps every heading / table row / TIP / TRAP in `SCSE1013_Study_Notes.pdf` → statement IDs |
| `tools/data_src/pdf_*.py` | Source of the notes from the PDF, in chapter order (easy to write: code blocks, tables) |
| `tools/data_src/lab_extras.json` | 23 extra statements from the Lab 4–6 documents (IDs start with `x`) |
| `tools/build_data.py` | Generates `data.js` from `tools/data_src` |
| `tools/build_coverage.py` | Generates `COVERAGE.md` and fails if any PDF statement is unmapped |
| `tools/verify/*.cpp` | C++ programs that confirm every code example and "trace code" output |

## Adding a new note

**Option 1: in the app (easiest).** Open **Manage Notes** → **+ Add statement**. Fill in the ID, topic, note, question, type (`explain` or `exact`), keywords or answers, hint, follow-ups (JSON) and MCQ. Data is saved in the browser's `localStorage`. Use **Export JSON** for backups and **Import JSON** to move to another device.

**Option 2: permanently in the files.** Add a new `S(...)` in `tools/data_src/pdf_<chapter>.py`, then run:

```
python3 tools/build_data.py
python3 tools/build_coverage.py
```

Format of one statement in `data.js`:

```js
{
  "id": "cp30", "topic": "cpp", "section": "3 · Arithmetic operators · % remainder", "trap": false,
  "text": "Full note. **bold**, `code`, ``` code block ```, | table |",
  "question": "What is 7 % 3?",
  "type": "exact",                       // or "explain"
  "keywords": [],                        // explain: ["decomposition|break into parts|split", ...]
  "answer": ["1"],                       // exact: list of accepted answers; explain: reference answer (text)
  "hint": "7 = 3 × 2 + ?",
  "followUps": [{ "note": "...", "question": "...", "type": "exact", "answer": ["3"], "keywords": [], "hint": "..." }],
  "mcq": { "question": "...", "options": ["correct", "wrong1", "wrong2", "wrong3"], "correct": 0 }
}
```

## Checking rules

- **explain**: lower-cased, punctuation removed, then the % of keyword groups present is counted. Near-miss spellings are accepted (Levenshtein ≤ 2 for words of ≥ 6 letters). ≥ 70% CORRECT, 40–69% ALMOST, < 40% WRONG.
- **exact**: extra spaces and commas are ignored. If the answer is code (contains `; = < > ( ) & + %` …), all spaces are ignored but symbols and letter case must match exactly.
- Scoring: attempt 1 = 100%, 2 = 60%, 3 = 30%, failed = 0%. An item failed 3 times is marked *needs review* and repeated at the end of the session, starting again from the NOTE phase.

## Note sources

Every main statement (IDs without an `x` prefix) comes from **SCSE1013_Study_Notes.pdf** (Chapters 1–6), in the PDF's order and headings. `x…` statements are extra practice from the Lab 4–6 documents, labelled *Extra (Lab)* and never included in the Trap Quiz. The **Trap Quiz** only uses the PDF's ⚠ Common traps, ⚠ TRAP and ⚠ INVALID HEADERS sections.
