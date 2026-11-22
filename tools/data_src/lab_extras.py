"""Extra statements from the Lab 4–6 documents (not in the Study Notes PDF).
Kept as a JSON snapshot; ids are prefixed with 'x' and they are never trap=True."""
import json, os
from helpers import ALL
here = os.path.dirname(os.path.abspath(__file__))
for s in json.load(open(os.path.join(here, "lab_extras.json"), encoding="utf-8")):
    assert not any(x["id"] == s["id"] for x in ALL), s["id"]
    ALL.append(s)
