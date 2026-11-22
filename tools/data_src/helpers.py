"""Helpers for authoring SCSE1013 statements.

Text fields support:
  ```  ...  ```  -> code block (<pre>)
  `inline`        -> inline code
  blank line      -> new paragraph
"""
import textwrap

ALL = []


def _clean(s):
    if s is None:
        return None
    return textwrap.dedent(s).strip("\n")


def F(note, question, *, kw=None, ans=None, hint="", type=None):
    """Follow-up question. kw -> explain, ans (list) -> exact."""
    t = type or ("exact" if ans is not None and kw is None else "explain")
    fu = {"note": _clean(note), "question": _clean(question), "type": t, "hint": hint}
    if t == "exact":
        fu["answer"] = list(ans)
        fu["keywords"] = []
    else:
        fu["keywords"] = list(kw or [])
        fu["answer"] = _clean(ans) if isinstance(ans, str) else ""
    return fu


def M(question, correct, *wrong):
    assert len(wrong) == 3, question
    return {"question": _clean(question), "options": [correct, *wrong], "correct": 0}


def S(id, topic, section, text, question, *, kw=None, ans=None, hint="",
      fu=(), mcq=None, trap=False):
    t = "exact" if kw is None else "explain"
    st = {
        "id": id,
        "topic": topic,
        "section": section,
        "trap": trap,
        "text": _clean(text),
        "question": _clean(question),
        "type": t,
        "keywords": list(kw or []),
        "answer": list(ans) if t == "exact" else _clean(ans or ""),
        "hint": hint,
        "followUps": list(fu),
        "mcq": mcq,
    }
    assert 1 <= len(st["followUps"]) <= 3, id
    assert mcq, id
    assert not any(s["id"] == id for s in ALL), id
    ALL.append(st)
    return st
