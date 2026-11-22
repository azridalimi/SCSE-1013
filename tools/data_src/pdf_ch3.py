from helpers import S, F, M

T = "cpp"
H = "3 · "

S("cp01", T, H + "Parts of a C++ program",
  """
  ```
  // sample program               ← comment
  #include <iostream>             ← preprocessor (no ;)
  using namespace std;
  int main()                      ← program starts here
  {
      double num1 = 5, num2, sum;
      num2 = 12;
      sum = num1 + num2;
      cout << "The sum is " << sum;
      return 0;                   ← tells the OS "OK"
  }
  ```
  - `#include` ialah **preprocessor directive**, **tiada `;`**.
  - Program **bermula di `int main()`**.
  - `return 0;` memberitahu OS bahawa program tamat **"OK"**.
  """,
  "Di manakah program C++ bermula, dan apakah maksud `return 0;`?",
  kw=["main|int main|main()", "os|operating system|sistem operasi", "ok|berjaya|success|jayanya|selesai"],
  ans="Program bermula di int main(); return 0 memberitahu OS bahawa program tamat OK.",
  hint="Satu function wajib; return 0 bercakap dengan siapa?",
  fu=[F("""Program contoh mencetak `"The sum is "` diikuti nilai sum (num1 = 5, num2 = 12).""",
        "Apakah output program sample?",
        ans=["The sum is 17"],
        hint="5 + 12."),
      F("""Baris `#include <iostream>` ialah preprocessor directive dan **tidak** berakhir dengan `;`.""",
        "Betul atau salah: `#include <iostream>;` perlu ada titik koma. (betul / salah)",
        ans=["salah", "false", "tidak"],
        hint="(no ;)")],
  mcq=M("Dalam program C++, `return 0;` dalam main…",
        "Memberitahu OS bahawa program tamat OK", "Mencetak 0", "Mengulang program", "Mengisytihar pemboleh ubah"))

S("cp02", T, H + "Program elements · Keywords",
  """
  Program dibina daripada: **keywords, identifiers, operators, punctuation**, mengikut **syntax**.

  **Keywords**: perkataan simpanan (reserved words) seperti `int`, `return`.
  - **Sentiasa huruf kecil** (always lowercase).
  - **Tidak boleh** digunakan sebagai nama.
  """,
  "Apakah keyword? Nyatakan dua ciri keyword.",
  kw=["reserved|simpanan|khas|kata kunci",
      "lowercase|huruf kecil|kecil",
      "cannot|tidak boleh|tak boleh|can't|not as name|bukan nama|nama"],
  ans="Perkataan simpanan (reserved words) seperti int, return; sentiasa huruf kecil dan tidak boleh dijadikan nama.",
  hint="Reserved, huruf apa, boleh jadi nama?",
  fu=[F("""Keyword sentiasa huruf kecil, jadi `Int` dan `RETURN` bukan keyword.""",
        "Adakah `int` boleh digunakan sebagai nama pemboleh ubah? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Reserved.")],
  mcq=M("Yang manakah keyword C++?",
        "return", "num1", "Sum", "main1"))

S("cp03", T, H + "Program elements · Identifiers, operators, punctuation, syntax",
  """
  - **Identifiers**: nama yang **anda pilih** (names you choose), contoh `num1`, `sum`.
  - **Operators**: `+ - * / =`
  - **Punctuation**: `;` `,`
  - **Syntax**: **peraturan bahasa** (the rules of the language).
  """,
  "Apakah maksud syntax dan identifier?",
  kw=["syntax|sintaks", "rule|peraturan|tatabahasa",
      "identifier|pengecam", "name|nama|choose|pilih|you|anda|programmer"],
  ans="Syntax ialah peraturan bahasa; identifier ialah nama yang dipilih oleh pengaturcara (num1, sum).",
  hint="Peraturan vs nama.",
  fu=[F("""Contoh punctuation dalam nota: `;` dan `,`.""",
        "Dalam `double num1 = 5, num2, sum;`, `,` dan `;` dikategorikan sebagai apa?",
        ans=["punctuation", "tanda baca"],
        hint="P…")],
  mcq=M("Dalam `sum = num1 + num2;`, `num1` ialah…",
        "Identifier", "Keyword", "Operator", "Punctuation"))

S("cp04", T, H + "REMEMBER: case-sensitive and braces",
  """
  ⚠ **REMEMBER**
  - C++ adalah **case-sensitive**: `Main` ≠ `main`.
  - Setiap `{` memerlukan `}`.
  """,
  "Apakah maksud C++ case-sensitive? Beri contoh daripada nota.",
  kw=["case|huruf besar|huruf kecil|besar|capital|uppercase",
      "different|berbeza|tidak sama|≠|not same|lain",
      "main"],
  ans="Huruf besar dan kecil dianggap berbeza; contohnya Main ≠ main.",
  hint="Contoh nota menggunakan nama function utama.",
  fu=[F("""Program dengan `int Main()` sahaja (tiada `main`) tidak boleh dipaut (link) menjadi program kerana `main` tidak wujud.""",
        "Adakah `Main` dan `main` dianggap nama yang sama? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Case-sensitive."),
      F("""Setiap `{` perlu `}` yang sepadan.""",
        "Berapakah `}` diperlukan jika program ada 3 `{`?",
        ans=["3", "tiga", "three"],
        hint="Setiap satu.")],
  mcq=M("Pernyataan manakah BETUL?",
        "Main ≠ main dalam C++", "C++ tidak membezakan huruf besar dan kecil", "{ tidak memerlukan }", "Keyword boleh huruf besar"))

S("cp05", T, H + "Special characters · comments and #",
  """
  | Char | Maksud |
  |---|---|
  | `//` `/* */` | **comments** |
  | `#` | **preprocessor directive** |
  """,
  "Apakah fungsi aksara `#` dalam C++?",
  kw=["preprocessor|prapemproses|directive|arahan"],
  ans="Menandakan preprocessor directive (contoh #include).",
  hint="#include…",
  fu=[F("""`//` untuk komen satu baris, `/* */` untuk komen berbilang baris.""",
        "Tulis dua bentuk simbol komen dalam C++.",
        kw=["//", "/*|*/"],
        ans="// dan /* */",
        hint="Slash.")],
  mcq=M("Simbol `/* */` digunakan untuk…",
        "Komen", "Preprocessor", "String", "Kumpulan statement"))

S("cp06", T, H + "Special characters · < >, ( ), { }",
  """
  | Char | Maksud |
  |---|---|
  | `< >` | **nama fail dalam `#include`** |
  | `( )` | **nama function** (function name) |
  | `{ }` | **kumpulan statement** (group of statements) |
  """,
  "Apakah fungsi `{ }`?",
  kw=["group|kumpulan|himpun|block|blok", "statement|pernyataan|arahan"],
  ans="Mengumpulkan beberapa statement (group of statements).",
  hint="Blok…",
  fu=[F("""`< >` dalam `#include <iostream>` mengandungi nama fail.""",
        "Dalam `#include <iostream>`, apakah fungsi `< >`?",
        kw=["file|fail", "name|nama|include"],
        ans="Mengandungi nama fail dalam #include.",
        hint="iostream ialah sebuah…"),
      F("""`( )` mengikuti nama function, contoh `main()`.""",
        "Simbol apakah digunakan selepas nama function?",
        ans=["( )", "()", "kurungan", "parentheses"],
        hint="main…")],
  mcq=M("Dalam `int main()`, `( )` menunjukkan…",
        "Nama function", "String", "Komen", "Satu aksara"))

S("cp07", T, H + "Special characters · ;, \" \", ' '",
  """
  | Char | Maksud |
  |---|---|
  | `;` | **tamatkan statement** (ends a statement) |
  | `" "` | **string** |
  | `' '` | **satu aksara** (single character) |
  """,
  "Apakah beza `\" \"` dan `' '`?",
  kw=["string|rentetan|teks", "single|satu|one|tunggal", "character|aksara|char"],
  ans="\" \" untuk string; ' ' untuk satu aksara.",
  hint="Berapa aksara?",
  fu=[F("""`;` menandakan **akhir sesuatu statement**.""",
        "Apakah fungsi `;`?",
        kw=["end|tamat|akhir|habis|tamatkan|menamatkan|penamat", "statement|pernyataan|arahan"],
        ans="Menamatkan statement.",
        hint="Titik dalam ayat.")],
  mcq=M("Yang manakah satu aksara (single character)?",
        "'C'", "\"C\"", "C", "{C}"))

S("cp08", T, H + "Variables",
  """
  **Variable**: lokasi memori bernama (a named memory location).
  - Mesti **diisytihar sebelum digunakan** (declare before using).
  - Nilai baru **menulis ganti** nilai lama (a new value overwrites the old one).
  """,
  "Apakah variable? Nyatakan dua peraturannya.",
  kw=["named|bernama|nama", "memory|memori|location|lokasi",
      "declare|isytihar|diisytihar|before|sebelum",
      "overwrite|ganti|tulis ganti|replace|old|lama"],
  ans="Lokasi memori bernama; mesti diisytihar sebelum digunakan; nilai baru menulis ganti nilai lama.",
  hint="Definisi + isytihar + nilai baru.",
  fu=[F("""
        ```
        int x = 3;
        x = 8;
        cout << x;
        ```""",
        "Apakah output?",
        ans=["8"],
        hint="Nilai baru menggantikan yang lama.")],
  mcq=M("Variable ialah…",
        "Lokasi memori bernama", "Nilai tetap dalam kod", "Keyword", "Komen"))

S("cp09", T, H + "Identifier rules",
  """
  **Peraturan identifier**: mula dengan **huruf atau `_`**, kemudian **huruf, digit atau `_`**. **Tiada keyword** dan **tiada simbol**.
  """,
  "Nyatakan peraturan menamakan identifier.",
  kw=["letter|huruf|abjad", "_|underscore|garis bawah",
      "digit|nombor|angka", "keyword|kata kunci|reserved",
      "symbol|simbol"],
  ans="Mula dengan huruf atau _, diikuti huruf, digit atau _; tiada keyword dan tiada simbol.",
  hint="Aksara pertama, aksara seterusnya, dua larangan.",
  fu=[F("""Aksara pertama: huruf atau `_` sahaja.""",
        "Bolehkah identifier bermula dengan underscore? (ya / tidak)",
        ans=["ya", "yes", "boleh"],
        hint="Letter or _.")],
  mcq=M("Identifier boleh bermula dengan…",
        "Huruf atau _", "Digit", "$", "#"))

S("cp10", T, H + "Identifier table · valid and invalid",
  """
  | Identifier | Valid? | Reason |
  |---|---|---|
  | `totalSales` / `total_Sales` | ✅ | |
  | `total.Sales` | ❌ | `"."` not allowed |
  | `4thQtrSales` | ❌ | starts with a digit |
  | `totalSale$` | ❌ | `"$"` not allowed |
  """,
  "`4thQtrSales`: valid atau invalid?",
  ans=["invalid", "tidak sah", "tak sah"],
  hint="Lihat aksara pertama.",
  fu=[F("""`total.Sales`: titik tidak dibenarkan.""",
        "Mengapa `total.Sales` invalid?",
        kw=[".|titik|dot|period", "not allowed|tidak dibenarkan|tak boleh|tidak boleh|simbol|symbol"],
        ans="Titik (.) tidak dibenarkan.",
        hint="Aksara di tengah."),
      F("""`totalSale$`: simbol `$` tidak dibenarkan.""",
        "`totalSale$`: valid atau invalid?",
        ans=["invalid", "tidak sah", "tak sah"],
        hint="Simbol di hujung."),
      F("""`total_Sales` hanya mengandungi huruf dan `_`.""",
        "`total_Sales`: valid atau invalid?",
        ans=["valid", "sah"],
        hint="Underscore dibenarkan.")],
  mcq=M("Identifier manakah VALID?",
        "total_Sales", "total.Sales", "4thQtrSales", "totalSale$"))

S("cp11", T, H + "Literals",
  """
  **Literal** = nilai yang ditulis terus dalam kod (a value written directly in the code): `12`, `"hello"`, `'C'`.
  """,
  "Apakah literal? Berikan contoh.",
  kw=["value|nilai", "directly|terus|written|ditulis|code|kod", "12|hello|'c'|c"],
  ans="Nilai yang ditulis terus dalam kod, contoh 12, \"hello\", 'C'.",
  hint="Bukan nama, tetapi nilai.",
  fu=[F("""Dalam `double num1 = 5, num2, sum; num2 = 12;`, nilai yang ditulis terus ialah literal.""",
        "Senaraikan literal dalam `num2 = 12;`.",
        ans=["12"],
        hint="Nombor.")],
  mcq=M("Yang manakah BUKAN literal?",
        "sum", "12", "\"hello\"", "'C'"))

S("cp12", T, H + "Input & output · cout and cin",
  """
  - `cout <<` menghantar output ke skrin: `cout << "Hi" << endl;`
  - `cin >>` membaca daripada papan kekunci: `cin >> height >> width;`
  - Baris baru: **`endl`** atau **`"\\n"`** (dalam string).
  - Pisahkan nilai input dengan **ruang** (spaces). **Sentiasa paparkan prompt dahulu.**
  """,
  "Apakah fungsi cout dan cin, dan operator yang digunakan?",
  kw=["cout", "<<|output|skrin|screen|papar",
      "cin", ">>|input|keyboard|papan kekunci|baca|read"],
  ans="cout << menghantar output ke skrin; cin >> membaca input dari papan kekunci.",
  hint="Satu keluar, satu masuk.",
  fu=[F("""Dua cara baris baru: `endl` atau `"\\n"`.""",
        "Selain endl, apakah cara lain untuk baris baru?",
        ans=["\"\\n\"", "\\n", "'\\n'"],
        hint="Backslash…"),
      F("""Sebelum `cin`, sentiasa paparkan **prompt**, contoh `cout << "Enter height and width: ";`""",
        "Apakah yang mesti dipaparkan sebelum setiap cin?",
        ans=["prompt", "gesaan", "a prompt", "mesej prompt"],
        hint="P…")],
  mcq=M("Yang manakah membaca dua nilai dengan betul?",
        "cin >> height >> width;", "cin << height << width;", "cout >> height;", "cin >> height, width;"))

S("cp13", T, H + "Memory trick: arrows point where the data goes",
  """
  💡 **MEMORY TRICK**: anak panah menunjuk **ke mana data pergi**.

  - `cout <<` **menolak** (pushes) data **keluar ke skrin**.
  - `cin >>` **menarik** (pulls) data **masuk ke pemboleh ubah**.
  """,
  "Terangkan memory trick anak panah cout dan cin.",
  kw=["arrow|anak panah|panah|point|tunjuk",
      "data|go|pergi|where|ke mana",
      "out|keluar|screen|skrin|push|tolak",
      "in|masuk|variable|pemboleh ubah|pull|tarik"],
  ans="Anak panah menunjuk ke mana data pergi: cout << tolak data keluar ke skrin; cin >> tarik data masuk ke pemboleh ubah.",
  hint="Arah anak panah = arah data.",
  fu=[F("""Dalam `cin >> x`, anak panah menghala ke `x`.""",
        "Dalam `cin >> x`, data mengalir ke mana?",
        ans=["x", "pemboleh ubah x", "variable x", "ke x"],
        hint="Ikut arah >>.")],
  mcq=M("Menurut memory trick, `cout <<`…",
        "Menolak data keluar ke skrin", "Menarik data masuk ke pemboleh ubah", "Memadam skrin", "Membaca fail"))

S("cp14", T, H + "Data types · char",
  """
  **char**: satu aksara (one character), **1 byte**. Contoh `'C'` (disimpan sebagai **67**).
  """,
  "Apakah saiz char dan bagaimana 'C' disimpan?",
  kw=["1 byte|1|satu byte|one byte", "67|ascii|nombor|number"],
  ans="1 byte; 'C' disimpan sebagai nombor 67.",
  hint="Satu byte; kod nombor 'C'.",
  fu=[F("""`'C'` disimpan sebagai 67. Huruf seterusnya `'D'` = 68.""",
        "Apakah output `cout << int('C');`?",
        ans=["67"],
        hint="Nota."),
      F("""`'A' + 1` dalam ungkapan aritmetik menjadi int: 65 + 1.""",
        "Apakah output `cout << 'A' + 1;`?",
        ans=["66"],
        hint="char menjadi int dalam aritmetik.")],
  mcq=M("`'C'` disimpan dalam memori sebagai…",
        "67", "3", "99", "'C' sahaja tanpa nombor"))

S("cp15", T, H + "Data types · bool",
  """
  **bool**: `true` / `false`, **1 byte**. `true` = **1**, `false` = **0**.
  """,
  "Apakah nilai integer bagi true dan false?",
  kw=["true", "1|satu|one", "false", "0|sifar|zero"],
  ans="true = 1, false = 0.",
  hint="Satu dan sifar.",
  fu=[F("""bool bersaiz 1 byte.""",
        "Berapakah saiz bool dalam byte?",
        ans=["1", "1 byte", "satu"],
        hint="Sama dengan char.")],
  mcq=M("`cout << true;` mencetak…",
        "1", "true", "0", "T"))

S("cp16", T, H + "Data types · short / int / long",
  """
  **short / int / long**: nombor bulat (whole numbers), saiz **2 / 4 / 4** byte. Contoh `12`, `-6`.
  """,
  "Apakah saiz short, int dan long dalam nota?",
  ans=["2/4/4", "2 4 4", "2, 4, 4", "2 byte 4 byte 4 byte"],
  hint="Format: short/int/long.",
  fu=[F("""int menyimpan nombor bulat seperti `12` dan `-6`, 4 byte.""",
        "Berapakah saiz int dalam byte?",
        ans=["4", "4 bytes", "4 byte"],
        hint="Nilai tengah 2/4/4.")],
  mcq=M("Jenis yang menyimpan nombor bulat (whole numbers) ialah…",
        "int", "float", "double", "bool"))

S("cp17", T, H + "Data types · float and double",
  """
  | Type | Holds | Size | Example |
  |---|---|---|---|
  | float | perpuluhan (~7 digit) | 4 byte | `3.14F` |
  | double | perpuluhan (~15 digit) | 8 byte | `3.14` (**default**) |

  Literal perpuluhan tanpa akhiran ialah **double** secara lalai; tambah **`F`** untuk float.
  """,
  "Apakah beza float dan double?",
  kw=["float", "7|tujuh|4 byte|4 bytes", "double", "15|lima belas|8 byte|8 bytes|default|lalai"],
  ans="float ~7 digit, 4 byte (3.14F); double ~15 digit, 8 byte, jenis lalai untuk perpuluhan (3.14).",
  hint="Bandingkan ketepatan digit dan saiz.",
  fu=[F("""`3.14` ialah double (default). `3.14F` ialah float.""",
        "Literal `3.14F` berjenis apa?",
        ans=["float"],
        hint="Akhiran F."),
      F("""double: ~15 digit ketepatan.""",
        "Berapakah saiz double dalam byte?",
        ans=["8", "8 bytes", "8 byte"],
        hint="Dua kali float.")],
  mcq=M("Literal `3.14` (tanpa akhiran) berjenis…",
        "double", "float", "int", "long"))

S("cp18", T, H + "Data types · string",
  """
  **string**: teks, perlu **`#include <string>`**, saiz berubah-ubah (varies). Contoh `"George"`.
  """,
  "Apakah header yang diperlukan untuk jenis string?",
  ans=["#include <string>", "<string>", "string"],
  hint="Nama sama dengan jenis.",
  fu=[F("""Contoh nilai string dalam nota: `"George"`.""",
        "Tulis pengisytiharan pemboleh ubah string bernama name dengan nilai George.",
        ans=["string name = \"George\";"],
        hint="string name = …;")],
  mcq=M("Saiz jenis string ialah…",
        "Berubah-ubah (varies)", "1 byte", "4 byte", "8 byte"))

S("cp19", T, H + "Data types · 'C' vs \"C\"",
  """
  - `'C'` = satu **character**.
  - `"C"` = satu **string**, disimpan sebagai **C + `\\0`**.
  """,
  "Apakah beza 'C' dan \"C\"?",
  kw=["character|char|aksara", "string|rentetan", "\\0|null|nul|terminator"],
  ans="'C' ialah character; \"C\" ialah string yang disimpan sebagai C + \\0.",
  hint="Satu ada aksara tambahan di hujung.",
  fu=[F("""`"C"` = `'C'` + `'\\0'`, jadi ia mengambil 2 aksara.""",
        "Berapakah aksara yang disimpan untuk \"C\"?",
        ans=["2", "dua", "two"],
        hint="C dan \\0."),
      F("""Cari kesilapan: `char grade = "A";`""",
        "Tulis baris yang betul.",
        ans=["char grade = 'A';"],
        hint="char perlu single quote.")],
  mcq=M("`\"C\"` disimpan sebagai…",
        "C + \\0", "C sahaja", "67", "'C'"))

S("cp20", T, H + "Data types · C-string",
  """
  **C-string**: `char name[21];` boleh menyimpan **20 aksara + `\\0`**.
  """,
  "Berapakah aksara yang boleh disimpan oleh `char name[21];`?",
  ans=["20", "20 aksara", "20 characters"],
  hint="Satu ruang untuk \\0.",
  fu=[F("""Untuk menyimpan nama sehingga 30 aksara, perlukan 30 + 1 untuk `\\0`.""",
        "Tulis pengisytiharan C-string `name` untuk 30 aksara.",
        ans=["char name[31];"],
        hint="char name[…];")],
  mcq=M("`char code[6];` boleh menyimpan berapa aksara (selain \\0)?",
        "5", "6", "7", "4"))

S("cp21", T, H + "Data types · truncation",
  """
  Nilai perpuluhan yang diberi kepada **int** akan **dipotong (truncated), bukan dibundarkan**:

  `int r = 3.88;` memberi **3**.
  """,
  "Apakah nilai r selepas `int r = 3.88;`?",
  ans=["3"],
  hint="Truncated, not rounded.",
  fu=[F("""Truncation membuang bahagian perpuluhan, tidak kira .88 atau .1.""",
        "Mengapa hasilnya bukan 4?",
        kw=["truncate|truncated|potong|dipotong|buang|cut",
            "not round|bukan bundar|tidak dibundarkan|tak bundar|bundar|round"],
        ans="Kerana nilai dipotong (truncated), bukan dibundarkan.",
        hint="Bukan rounding.")],
  mcq=M("`int x = 9.99;` menyimpan…",
        "9", "10", "9.99", "Ralat"))

S("cp22", T, H + "Data types · number bases",
  """
  Asas nombor (number bases):
  - **decimal** (10)
  - **binary** (2)
  - **octal** (8): bermula dengan **`0`**, contoh `075`
  - **hex** (16): bermula dengan **`0x`**, contoh `0x75A`

  `1234L` = **long**.
  """,
  "Bagaimanakah literal octal dan hex ditulis dalam C++?",
  kw=["octal|oktal", "0|starts with 0|bermula 0|075",
      "hex|hexadecimal|heksadesimal", "0x|0x75a"],
  ans="Octal bermula dengan 0 (075); hex bermula dengan 0x (0x75A).",
  hint="Satu awalan 0, satu awalan 0x.",
  fu=[F("""`075` = 7×8 + 5 = 61 (octal).""",
        "Apakah nilai perpuluhan `075`?",
        ans=["61"],
        hint="Asas 8."),
      F("""Akhiran `L` menjadikan literal itu long.""",
        "`1234L` berjenis apa?",
        ans=["long"],
        hint="L…")],
  mcq=M("Literal `0x75A` ialah dalam asas…",
        "16 (hex)", "8 (octal)", "2 (binary)", "10 (decimal)"))

S("cp23", T, H + "Data types · sizeof",
  """
  **`sizeof(type)`** memberi saiz jenis dalam **byte**.

  Contoh: `sizeof(char)` = 1, `sizeof(int)` = 4, `sizeof(double)` = 8.
  """,
  "Apakah fungsi sizeof?",
  kw=["size|saiz", "byte|bytes|bait", "type|jenis"],
  ans="Memberi saiz sesuatu jenis (atau pemboleh ubah) dalam byte.",
  hint="Unit: byte.",
  fu=[F("""`cout << sizeof(double);`""",
        "Apakah output?",
        ans=["8"],
        hint="Jadual data types."),
      F("""`cout << sizeof(char) << sizeof(int);`""",
        "Apakah output?",
        ans=["14"],
        hint="1 kemudian 4, tanpa ruang.")],
  mcq=M("`sizeof(int)` biasanya memulangkan…",
        "4", "2", "8", "1"))

S("cp24", T, H + "Constants",
  """
  ```
  const double PI = 3.14159;   // typed, preferred
  #define PI 3.14159           // no = and no ;
  ```
  - Nilai constant **tidak boleh berubah**.
  - Mengikut konvensyen, ditulis dalam **HURUF BESAR** (UPPERCASE).
  - `const` lebih disyorkan (**typed**). `#define` **tiada `=` dan tiada `;`**.
  """,
  "Apakah dua cara menulis constant, dan yang mana disyorkan?",
  kw=["const", "#define|define",
      "preferred|disyorkan|lebih baik|recommended|typed|jenis"],
  ans="const double PI = 3.14159; (typed, disyorkan) dan #define PI 3.14159 (tiada = dan tiada ;).",
  hint="Satu ada jenis data, satu preprocessor.",
  fu=[F("""Cari kesilapan: `#define PI = 3.14159;`""",
        "Tulis baris #define yang betul.",
        ans=["#define PI 3.14159"],
        hint="No = and no ;"),
      F("""Konvensyen: nama constant ditulis dalam huruf besar, contoh `PI`, `TAX_RATE`.""",
        "Mengikut konvensyen, nama constant ditulis dalam huruf apa?",
        ans=["uppercase", "huruf besar", "besar", "capital"],
        hint="UPPER…"),
      F("""`const double PI = 3.14159;` kemudian `PI = 3;` → ralat kerana constant tidak boleh berubah.""",
        "Bolehkah nilai PI ditukar selepas `const double PI = 3.14159;`? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Constant.")],
  mcq=M("Yang manakah betul?",
        "#define PI 3.14159", "#define PI = 3.14159;", "const PI double = 3.14159;", "#define PI 3.14159;"))

S("cp25", T, H + "Assignment",
  """
  - `size = 5;` ✅
  - `5 = size;` ❌ (**pemboleh ubah mesti di sebelah kiri**)
  """,
  "Mengapa `5 = size;` salah?",
  kw=["variable|pemboleh ubah|pembolehubah", "left|kiri|sebelah kiri"],
  ans="Pemboleh ubah mesti berada di sebelah kiri tanda =.",
  hint="Siapa yang menerima nilai?",
  fu=[F("""Ralat g++ untuk `5 = size;`: `lvalue required as left operand of assignment`.""",
        "Tulis semula `5 = size;` dengan betul.",
        ans=["size = 5;"],
        hint="Tukar sisi.")],
  mcq=M("Assignment manakah SAH?",
        "total = a + b;", "a + b = total;", "5 = x;", "10 = 10;"))

S("cp26", T, H + "Initialisation",
  """
  **Initialise** (beri nilai awal) semasa mengisytihar:

  `int width = 7, height = 5, area;`

  (`width` dan `height` diinisialisasi; `area` tidak.)
  """,
  "Dalam `int width = 7, height = 5, area;`, pemboleh ubah manakah TIDAK diinisialisasi?",
  ans=["area"],
  hint="Yang tiada = nilai.",
  fu=[F("""Inisialisasi = memberi nilai semasa pengisytiharan.""",
        "Tulis pengisytiharan int count dengan nilai awal 0.",
        ans=["int count = 0;"],
        hint="int count = …;")],
  mcq=M("Yang manakah contoh initialisation?",
        "int width = 7;", "width = 7;", "int width;", "cin >> width;"))

S("cp27", T, H + "Scope",
  """
  **Scope**: anda **tidak boleh guna pemboleh ubah sebelum baris di mana ia diisytihar** (you can't use a variable before the line where it is declared).
  """,
  "Apakah peraturan scope dalam nota?",
  kw=["before|sebelum", "declare|isytihar|diisytihar|declared|pengisytiharan",
      "cannot|tidak boleh|tak boleh|can't|use|guna"],
  ans="Pemboleh ubah tidak boleh digunakan sebelum baris ia diisytihar.",
  hint="Turutan baris.",
  fu=[F("""
        ```
        cout << value;
        int value = 4;
        ```""",
        "Adakah kod ini compile? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="value digunakan sebelum diisytihar.")],
  mcq=M("`cout << n; int n = 2;` menghasilkan…",
        "Ralat: n was not declared in this scope", "2", "0", "Nilai sampah"))

S("cp28", T, H + "Arithmetic operators · + − *",
  """
  Dengan 7 dan 3:

  | Op | 7 ? 3 |
  |---|---|
  | `+` | 10 |
  | `−` | 4 |
  | `*` | 21 |
  """,
  "Apakah hasil 7 * 3?",
  ans=["21"],
  hint="Darab.",
  fu=[F("""`cout << 7 + 3 << " " << 7 - 3;`""",
        "Apakah output?",
        ans=["10 4"],
        hint="Tambah dan tolak.")],
  mcq=M("`7 - 3` bernilai…",
        "4", "10", "21", "-4"))

S("cp29", T, H + "Arithmetic operators · / integer division",
  """
  `7 / 3` = **2**: **int ÷ int = integer division** (perpuluhan dibuang).

  Jika salah satu ialah perpuluhan: `13 / 5.0` = **2.6**.
  """,
  "Apakah nilai 7 / 3 dalam C++?",
  ans=["2"],
  hint="int ÷ int.",
  fu=[F("""`13 / 5.0`: satu operand double, jadi bukan integer division.""",
        "Apakah nilai 13 / 5.0?",
        ans=["2.6"],
        hint="Perpuluhan dikekalkan."),
      F("""`13 / 5` (kedua-dua int).""",
        "Apakah nilai 13 / 5?",
        ans=["2"],
        hint="Integer division.")],
  mcq=M("int ÷ int dalam C++ menghasilkan…",
        "Integer division (perpuluhan dibuang)", "Nilai perpuluhan penuh", "Nilai dibundarkan", "Ralat"))

S("cp30", T, H + "Arithmetic operators · % remainder",
  """
  `7 % 3` = **1**: **baki** (remainder). `%` **hanya untuk integer** (works on integers only).
  """,
  "Apakah nilai 7 % 3?",
  ans=["1"],
  hint="7 = 3 × 2 + ?",
  fu=[F("""`%` hanya untuk integer. `7.5 % 2` ialah ralat compile.""",
        "Bolehkah % digunakan dengan double? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Integers only."),
      F("""`13 % 5`: 13 = 5 × 2 + 3.""",
        "Apakah nilai 13 % 5?",
        ans=["3"],
        hint="Baki.")],
  mcq=M("`%` dalam C++ memberi…",
        "Baki (remainder)", "Peratus", "Hasil bahagi perpuluhan", "Kuasa"))

S("cp31", T, H + "Order of operations",
  """
  ✔ **ORDER OF OPERATIONS**

  `( )` → **unary −** (right to left) → `* / %` (left to right) → `+ −` (left to right)

  - `2 + 2 * 2 - 2` = **4**
  - `(2 + 2) * 2 - 2` = **6**
  """,
  "Tulis turutan keutamaan operator aritmetik.",
  kw=["( )|()|kurungan|parentheses|bracket",
      "unary|unari|negative|negatif",
      "* / %|*|darab|bahagi|multiply",
      "+ −|+ -|+|tambah|tolak|add"],
  ans="( ) → unary − → * / % → + −",
  hint="Kurungan dahulu, tambah/tolak terakhir.",
  fu=[F("""`2 + 2 * 2 - 2`: 2 * 2 dahulu = 4, kemudian 2 + 4 − 2.""",
        "Apakah nilai `2 + 2 * 2 - 2`?",
        ans=["4"],
        hint="Darab dahulu."),
      F("""`(2 + 2) * 2 - 2`: kurungan dahulu.""",
        "Apakah nilai `(2 + 2) * 2 - 2`?",
        ans=["6"],
        hint="4 × 2 − 2."),
      F("""Unary − dinilai dari kanan ke kiri; `* / %` dan `+ −` dari kiri ke kanan.""",
        "Arah penilaian bagi `* / %`?",
        ans=["left to right", "kiri ke kanan"],
        hint="Seperti membaca.")],
  mcq=M("Nilai `10 - 4 / 2 * 3` ialah…",
        "4", "9", "1", "6"))

S("cp32", T, H + "No ^ operator: use pow",
  """
  C++ **tiada operator `^`** untuk kuasa. Gunakan **`pow(s, 2)`** (perlu `<cmath>`).
  """,
  "Bagaimana menulis s kuasa dua dalam C++?",
  ans=["pow(s, 2)", "pow(s,2)", "s * s", "s*s"],
  hint="Tiada ^.",
  fu=[F("""`pow(x, y)` = x kuasa y.""",
        "Apakah output `cout << pow(2, 3);`?",
        ans=["8"],
        hint="2 × 2 × 2.")],
  mcq=M("Untuk mengira x² dalam C++ guna…",
        "pow(x, 2)", "x ^ 2", "x ** 2", "x²"))

S("cp33", T, H + "Type conversion · promotion",
  """
  **Promotion**: jenis yang **lebih rendah ditukar ke jenis yang lebih tinggi**.

  Turutan: `int < unsigned int < long < unsigned long < float < double < long double`
  """,
  "Apakah promotion dalam type conversion?",
  kw=["lower|rendah|kecil", "higher|tinggi|besar|up|naik", "convert|tukar|ditukar|converted"],
  ans="Jenis yang lebih rendah ditukar ke jenis yang lebih tinggi dalam ungkapan.",
  hint="Rendah → tinggi.",
  fu=[F("""Dalam `5 / 2.0`, int 5 dinaikkan (promoted) kepada double.""",
        "Dalam `int + double`, hasilnya berjenis apa?",
        ans=["double"],
        hint="Lebih tinggi."),
      F("""Turutan: int < unsigned int < long < unsigned long < float < double < long double.""",
        "Apakah jenis PALING tinggi dalam turutan promotion?",
        ans=["long double"],
        hint="Lebih tinggi daripada double.")],
  mcq=M("Dalam turutan promotion, yang manakah lebih tinggi daripada float?",
        "double", "long", "int", "unsigned long"))

S("cp34", T, H + "Type conversion · char/short in arithmetic, and =",
  """
  - `char` dan `short` **menjadi `int`** dalam aritmetik.
  - Dengan `=`, hasil **mengambil jenis pemboleh ubah di sebelah kiri**.

  Contoh: `int x = 7 / 2.0;` → sebelah kanan 3.5 (double) tetapi x ialah int → **3**.
  """,
  "Apabila menggunakan =, hasil akhir mengambil jenis apa?",
  kw=["left|kiri", "variable|pemboleh ubah|type|jenis"],
  ans="Jenis pemboleh ubah di sebelah kiri.",
  hint="Siapa yang menerima nilai?",
  fu=[F("""`int x = 7 / 2.0;`""",
        "Apakah nilai x?",
        ans=["3"],
        hint="3.5 disimpan dalam int."),
      F("""`char c = 'A'; cout << c + 1;` → char menjadi int dalam aritmetik.""",
        "Apakah output?",
        ans=["66"],
        hint="'A' = 65.")],
  mcq=M("Dalam aritmetik, char dan short ditukar kepada…",
        "int", "double", "bool", "string"))

S("cp35", T, H + "Type conversion · manual cast",
  """
  **Manual cast**:
  - `static_cast<double>(a) / b` (**disyorkan**, preferred)
  - `(int)ch`
  - `int(ch)`
  """,
  "Tulis cast yang disyorkan untuk menukar a kepada double sebelum dibahagi dengan b.",
  ans=["static_cast<double>(a) / b", "static_cast<double>(a)/b"],
  hint="static_cast<…>(…)",
  fu=[F("""`int a = 7, b = 2; cout << static_cast<double>(a) / b;`""",
        "Apakah output?",
        ans=["3.5"],
        hint="7.0 / 2."),
      F("""`char ch = 'C'; cout << (int)ch;`""",
        "Apakah output?",
        ans=["67"],
        hint="Kod 'C'.")],
  mcq=M("Cara cast yang disyorkan dalam nota ialah…",
        "static_cast<double>(a)", "(double)a", "double(a)", "a.toDouble()"))

S("cp36", T, H + "Type conversion · overflow/underflow",
  """
  **Overflow/underflow**: nilai yang **terlalu besar atau terlalu kecil** untuk sesuatu jenis akan **"wrap around"** (berpusing).

  Contoh: `short s = 32767; s++;` → **-32768**.
  """,
  "Apakah yang berlaku apabila berlaku overflow?",
  kw=["too big|terlalu besar|besar|too small|terlalu kecil|kecil|exceed|melebihi|julat|range",
      "wrap|wrap around|pusing|berpusing|balik"],
  ans="Nilai terlalu besar/kecil untuk jenis itu akan wrap around (berpusing).",
  hint="Seperti odometer.",
  fu=[F("""`short s = 32767; s++;` (julat short: −32768 hingga 32767).""",
        "Apakah nilai s?",
        ans=["-32768"],
        hint="Pusing ke nilai terkecil.")],
  mcq=M("Overflow bermaksud nilai…",
        "Terlalu besar untuk jenis itu dan 'wrap around'", "Dibundarkan", "Menjadi 0 sentiasa", "Ditukar ke double"))

S("cp37", T, H + "Increment · prefix vs postfix",
  """
  - **Prefix `++x`**: **ubah dahulu, kemudian guna** (change first, then use).
  - **Postfix `x++`**: **guna dahulu, kemudian ubah** (use first, then change).
  """,
  "Apakah beza ++x dan x++?",
  kw=["prefix|++x", "change first|ubah dahulu|tambah dahulu|dahulu|dulu|first|before",
      "postfix|x++", "use first|guna dahulu|then change|kemudian|selepas|after|lepas"],
  ans="++x (prefix) ubah dahulu kemudian guna; x++ (postfix) guna dahulu kemudian ubah.",
  hint="Change-then-use vs use-then-change.",
  fu=[F("""
        ```
        int x = 5;
        cout << x++ << " ";
        cout << x;
        ```""",
        "Apakah output?",
        ans=["5 6"],
        hint="Postfix guna 5 dahulu."),
      F("""
        ```
        int x = 5;
        cout << ++x;
        ```""",
        "Apakah output?",
        ans=["6"],
        hint="Prefix.")],
  mcq=M("`int a = 3; int b = ++a;` → b =",
        "4", "3", "5", "Ralat"))

S("cp38", T, H + "Increment · kira example",
  """
  `kira = 5`:

  `5 * kira-- + 10` = **35**, dan **kira menjadi 4**.

  (Postfix: guna 5 dahulu → 5 × 5 + 10 = 35, kemudian kira − 1.)
  """,
  "Dengan kira = 5, apakah nilai `5 * kira-- + 10`?",
  ans=["35"],
  hint="Postfix: guna 5 dahulu.",
  fu=[F("""Selepas ungkapan `5 * kira-- + 10` dengan kira = 5.""",
        "Apakah nilai kira selepas itu?",
        ans=["4"],
        hint="Dikurangkan satu."),
      F("""Jika ditukar kepada prefix: `5 * --kira + 10` dengan kira = 5.""",
        "Apakah nilainya?",
        ans=["30"],
        hint="kira jadi 4 dahulu.")],
  mcq=M("kira = 5. `5 * kira-- + 10` memberi…",
        "35, kira = 4", "30, kira = 4", "35, kira = 5", "30, kira = 5"))

S("cp39", T, H + "Combined assignment",
  """
  | Short | Means |
  |---|---|
  | `i += 3` | `i = i + 3` |
  | `i *= j+3` | `i = i * (j+3)` |
  """,
  "Apakah maksud penuh `i *= j+3`?",
  ans=["i = i * (j+3)", "i = i * (j + 3)"],
  hint="Seluruh sebelah kanan dalam kurungan.",
  fu=[F("""`int i = 10, j = 2; i *= j + 3;`""",
        "Apakah nilai i?",
        ans=["50"],
        hint="10 × 5."),
      F("""`int i = 4; i += 3;`""",
        "Apakah nilai i?",
        ans=["7"],
        hint="i = i + 3.")],
  mcq=M("`i -= 2` bermaksud…",
        "i = i - 2", "i = 2 - i", "i = -2", "i == i - 2"))

S("cp40", T, H + "Chained assignment",
  """
  `x = y = z = 5` **memberi nilai dari kanan ke kiri** (assigns right to left): z = 5, kemudian y = z, kemudian x = y.
  """,
  "Dalam arah manakah `x = y = z = 5` dinilai?",
  ans=["right to left", "kanan ke kiri"],
  hint="Bermula dengan z.",
  fu=[F("""`int x, y, z; x = y = z = 5; cout << x + y + z;`""",
        "Apakah output?",
        ans=["15"],
        hint="Semua 5.")],
  mcq=M("Selepas `x = y = z = 5;`, nilai x ialah…",
        "5", "0", "Tidak ditentukan", "15"))
