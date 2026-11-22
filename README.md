# Hafal SCSE1013

Web app untuk **hafal dan faham** nota SCSE1013 Fundamental Programming Concepts.
HTML, CSS dan JavaScript biasa sahaja: tiada backend, tiada framework.

**Cara buka:** double-click `index.html`. Ia berfungsi terus daripada fail (`file://`), dan juga offline (font kembali ke font sistem).

## Struktur fail

| Fail | Kegunaan |
|---|---|
| `index.html` | Rangka halaman, memuatkan `data.js` kemudian `app.js` |
| `styles.css` | Tema gelap editorial (hitam + biru #2F5BFF), responsive, `prefers-reduced-motion` |
| `data.js` | Semua statement (`window.SCSE_DEFAULT_DATA`): 6 topik, 151 statement daripada PDF + 23 tambahan lab, 260 soalan susulan |
| `app.js` | Enjin: routing, mod hafalan (Nota → Jawab → Semak), kuiz MCQ, markah, Urus Nota |
| `COVERAGE.md` | Peta setiap tajuk / baris jadual / TIP / TRAP dalam `SCSE1013_Study_Notes.pdf` → ID statement |
| `tools/data_src/pdf_*.py` | Sumber nota daripada PDF, ikut susunan bab (mudah ditulis: blok kod, jadual) |
| `tools/data_src/lab_extras.json` | 23 statement tambahan daripada dokumen Lab 4–6 (ID bermula `x`) |
| `tools/build_data.py` | Jana `data.js` daripada `tools/data_src` |
| `tools/build_coverage.py` | Jana `COVERAGE.md` daripada `data.js` |
| `tools/verify/*.cpp` | Program C++ yang mengesahkan setiap contoh kod PDF dan output "trace code" |

## Cara tambah nota baru

**Cara 1: dalam app (paling mudah).** Buka **Urus Nota** → **+ Tambah statement**. Isi ID, topik, nota, soalan, jenis (`explain` atau `exact`), keywords atau jawapan, hint, soalan susulan (JSON) dan MCQ. Data disimpan dalam `localStorage` pelayar. Guna **Export JSON** untuk backup dan **Import JSON** untuk pindah ke peranti lain.

**Cara 2: kekal dalam fail.** Tambah `S(...)` baru dalam `tools/data_src/pdf_<bab>.py`, kemudian:

```
python3 tools/build_data.py
python3 tools/build_coverage.py
```

Format satu statement dalam `data.js`:

```js
{
  "id": "cp16", "topic": "cpp", "section": "3.8 Arithmetic operators, / and %", "trap": true,
  "text": "Nota penuh. **tebal**, `kod`, ``` blok kod ```, | jadual |",
  "question": "Apakah nilai 13 % 5?",
  "type": "exact",                       // atau "explain"
  "keywords": [],                        // explain: ["decomposition|pecahkan|bahagi kepada bahagian kecil", ...]
  "answer": ["3"],                       // exact: senarai jawapan diterima; explain: jawapan rujukan (teks)
  "hint": "13 = 5 × 2 + ?",
  "followUps": [{ "note": "...", "question": "...", "type": "exact", "answer": ["3 1"], "keywords": [], "hint": "..." }],
  "mcq": { "question": "...", "options": ["betul", "salah1", "salah2", "salah3"], "correct": 0 }
}
```

## Peraturan semakan

- **explain**: huruf kecil, tanda baca dibuang, kemudian kira % kumpulan keyword yang ada. Ejaan hampir diterima (Levenshtein ≤ 2 untuk perkataan ≥ 6 huruf). ≥ 70% BETUL, 40–69% HAMPIR, < 40% SALAH.
- **exact**: ruang berlebihan dan koma diabaikan. Jika jawapan ialah kod (ada `; = < > ( ) & + %` …), semua ruang diabaikan tetapi simbol dan huruf besar/kecil mesti tepat.
- Markah: cubaan 1 = 100%, 2 = 60%, 3 = 30%, gagal = 0%. Item yang gagal 3 kali ditanda *perlu ulang* dan diulang di hujung sesi, bermula dengan FASA NOTA.

## Sumber nota

Semua statement utama (ID tanpa awalan `x`) datang daripada **SCSE1013_Study_Notes.pdf** (Bab 1–6), mengikut susunan dan tajuk PDF. Statement `x…` ialah latihan tambahan daripada dokumen Lab 4–6, dilabel *Tambahan (Lab)* dan tidak dimasukkan dalam Kuiz Trap. **Kuiz Trap** hanya menggunakan bahagian ⚠ Common traps, ⚠ TRAP dan ⚠ INVALID HEADERS dalam PDF.
