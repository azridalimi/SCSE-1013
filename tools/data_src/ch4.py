from helpers import S, F, M

T = "ctrl"

S("cs01", T, "4.1 Relational operators",
  """
  Relational operators membandingkan dua nilai dan menghasilkan `true` (1) atau `false` (0):

  `==` sama dengan, `!=` tidak sama, `<`, `>`, `<=`, `>=`

  ```
  int a = 4, b = 9;
  cout << (a < b) << " " << (a == b);   // 1 0
  ```
  """,
  "Apakah nilai yang dihasilkan oleh ungkapan relational dalam C++?",
  kw=["true|benar|1|satu", "false|palsu|0|sifar|salah"],
  ans="true (1) atau false (0).",
  hint="Dua nilai Boolean.",
  fu=[F("""`int a = 4, b = 9; cout << (a < b) << " " << (a == b);`""",
        "Apakah output?",
        ans=["1 0"],
        hint="cout mencetak bool sebagai nombor.")],
  mcq=M("Operator 'tidak sama dengan' dalam C++ ialah…",
        "!=", "<>", "=!", "=/="))

S("cs02", T, "4.1 Logical operators and short-circuit",
  """
  Logical operators:

  - `&&` AND: benar jika **kedua-dua** benar.
  - `||` OR: benar jika **salah satu** benar.
  - `!` NOT: songsangkan.

  Keutamaan: `!` > `&&` > `||`.

  **Short-circuit**: `&&` berhenti jika operand kiri false; `||` berhenti jika operand kiri true. Contoh `x == 7 || x / 0` tidak menilai `x / 0` apabila x = 7.
  """,
  "Apakah maksud short-circuit evaluation?",
  kw=["left|kiri|first|pertama", "stop|berhenti|skip|langkau|tidak dinilai|not evaluated|tak dinilai|tidak dikira",
      "&&|\\|\\||and|or|right|kanan"],
  ans="Jika operand kiri sudah menentukan jawapan (false untuk &&, true untuk ||), operand kanan tidak dinilai.",
  hint="Adakah C++ perlu tengok operand kanan jika kiri sudah false dalam &&?",
  fu=[F("""
        ```
        int x = 7;
        if (x > 5 && x < 10) cout << "in";
        else cout << "out";
        cout << " " << !(x > 5);
        ```""",
        "Apakah output?",
        ans=["in 0"],
        hint="7 dalam julat; !(true) = 0."),
      F("""Keutamaan: `!` dahulu, kemudian `&&`, akhirnya `||`.""",
        "Antara && dan ||, yang manakah dinilai dahulu?",
        ans=["&&", "and"],
        hint="AND lebih tinggi.")],
  mcq=M("`(5 > 3) || (2 > 8)` bernilai…",
        "true", "false", "ralat", "8"))

S("cs03", T, "4.2 Complements of conditions (De Morgan)", trap=True,
  text="""
  **Complement** (lawan) syarat:

  | Syarat | Complement |
  |---|---|
  | `x > 5` | `x <= 5` |
  | `x < 5` | `x >= 5` |
  | `x == 5` | `x != 5` |

  **De Morgan's law**:
  - `!(a && b)` = `!a || !b`
  - `!(a || b)` = `!a && !b`

  **TRAP**: lawan bagi `>` ialah `<=`, BUKAN `<`.
  """,
  question="Apakah complement bagi `x > 5`?",
  ans=["x <= 5", "x<=5", "!(x > 5)"],
  hint="Jangan lupa nilai 5 itu sendiri.",
  fu=[F("""De Morgan: `!(a && b)` → tukar `&&` kepada `||` dan songsangkan setiap bahagian.""",
        "Tulis semula `!(age >= 18 && member)` tanpa ! di luar kurungan.",
        ans=["age < 18 || !member", "(age < 18) || (!member)", "age<18||!member", "!member || age < 18"],
        hint="!(A && B) = !A || !B.")],
  mcq=M("`!(a || b)` bersamaan dengan…",
        "!a && !b", "!a || !b", "a && b", "!a || b"))

S("cs04", T, "4.3 if, if...else and compound statements",
  """
  ```
  if (condition)
      statement;            // satu statement sahaja

  if (condition) {          // compound statement / block
      statement1;
      statement2;
  } else {
      statement3;
  }
  ```
  Syarat mesti dalam `( )`. Gunakan `{ }` jika ada lebih daripada satu statement.
  """,
  "Bilakah kita MESTI menggunakan { } dalam if?",
  kw=["more than one|lebih daripada satu|lebih dari satu|banyak|multiple|beberapa|dua atau lebih|>1",
      "statement|pernyataan|arahan|baris"],
  ans="Apabila badan if (atau else) mengandungi lebih daripada satu statement.",
  hint="Tanpa { }, berapa statement milik if?",
  fu=[F("""
        ```
        int n = 4;
        if (n % 2 == 0)
            cout << "even ";
        else
            cout << "odd ";
        cout << "done";
        ```""",
        "Apakah output?",
        ans=["even done"],
        hint="4 % 2 = 0; baris terakhir di luar if.")],
  mcq=M("Struktur yang memilih antara dua laluan ialah…",
        "if...else", "while", "for", "do...while"))

S("cs05", T, "4.4 Common trap: = instead of ==", trap=True,
  text="""
  **TRAP**: `=` ialah assignment, `==` ialah perbandingan.

  ```
  int tickets = 5;
  if (tickets = 0)
      cout << "Sold out";
  else
      cout << "Left " << tickets;
  ```
  `tickets = 0` menukar tickets kepada 0, dan nilai ungkapan ialah 0 (false). Output: **`Left 0`**. g++ `-Wall` memberi warning *suggest parentheses around assignment used as truth value*.
  """,
  question="Apakah output program tickets di atas?",
  ans=["Left 0"],
  hint="Assignment berlaku dahulu, kemudian nilai 0 diuji.",
  fu=[F("""Betulkan syarat supaya ia membandingkan.""",
        "Tulis syarat if yang betul.",
        ans=["if (tickets == 0)", "tickets == 0", "if(tickets==0)", "(tickets == 0)"],
        hint="Dua simbol sama."),
      F("""`int x = 3; if (x = 7) cout << x;`""",
        "Apakah output?",
        ans=["7"],
        hint="x ditukar ke 7, dan 7 bukan sifar → true.")],
  mcq=M("`if (score = 100)` akan…",
        "Sentiasa benar dan menukar score kepada 100", "Membandingkan score dengan 100",
        "Ralat compile", "Sentiasa palsu"))

S("cs06", T, "4.4 Common trap: semicolon after if", trap=True,
  text="""
  **TRAP**: `;` selepas `if (...)` menjadi **empty statement**. Badan sebenar sentiasa dijalankan.

  ```
  int x = 2;
  if (x > 5);
      cout << "Big";
  ```
  Output: **`Big`**, walaupun x = 2.
  """,
  question="Apakah output program di atas?",
  ans=["Big"],
  hint="Apakah yang menjadi badan if?",
  fu=[F("""Badan if hanyalah `;` (kosong). `cout` tidak berkaitan dengan if.""",
        "Mengapa \"Big\" dicetak walaupun x = 2?",
        kw=[";|semicolon|titik koma|koma bertitik",
            "empty|kosong|null|tamat|end|habis|badan|body"],
        ans="Kerana ; selepas if menjadi empty statement; cout di luar if dan sentiasa dijalankan.",
        hint="Lihat hujung baris if.")],
  mcq=M("`if (a > b); cout << a;` bermaksud…",
        "cout << a sentiasa dijalankan", "cout hanya jika a > b", "Ralat compile", "Tiada output"))

S("cs07", T, "4.4 Common trap: missing braces", trap=True,
  text="""
  **TRAP**: tanpa `{ }`, hanya **satu** statement milik if. Indentasi tidak bermakna kepada compiler.

  ```
  int age = 15;
  if (age >= 18)
      cout << "Adult ";
      cout << "Can vote";
  ```
  Output: **`Can vote`**.
  """,
  question="Apakah output program di atas?",
  ans=["Can vote"],
  hint="Hanya baris pertama selepas if milik if.",
  fu=[F("""Betulkan dengan meletakkan kedua-dua statement dalam blok.""",
        "Simbol apakah perlu ditambah?",
        ans=["{ }", "{}", "braces", "kurungan kerinting", "curly braces", "{"],
        hint="Compound statement.")],
  mcq=M("Compiler C++ menentukan badan if berdasarkan…",
        "{ } atau satu statement selepasnya", "Indentasi", "Baris kosong", "Komen"))

S("cs08", T, "4.4 Common trap: dangling else", trap=True,
  text="""
  **TRAP**: `else` dipadankan dengan `if` **terdekat** yang belum ada else.

  ```
  int a = 5, b = 2;
  if (a > 3)
      if (b > 3)
          cout << "X";
  else
      cout << "Y";
  ```
  Walaupun `else` diindent di bawah if pertama, ia milik `if (b > 3)`. Output: **`Y`**.
  """,
  question="Apakah output program di atas?",
  ans=["Y"],
  hint="else milik if yang mana?",
  fu=[F("""Jika a = 1 (a > 3 false), if dalam tidak dinilai langsung, termasuk else-nya.""",
        "Dengan a = 1, b = 2, apakah output? (tulis 'tiada' jika tiada)",
        ans=["tiada", "none", "nothing", "tiada output", "-", "kosong"],
        hint="else milik if dalam.")],
  mcq=M("Dalam nested if tanpa braces, else dipadankan dengan…",
        "if terdekat yang belum ada else", "if pertama", "if paling luar", "Ralat compile"))

S("cs09", T, "4.5 Nested if / else-if chain (grade classifier)", trap=True,
  text="""
  Rantai `else if` diuji dari atas ke bawah; **syarat pertama yang benar** sahaja dijalankan.

  ```
  if (score > 90)      grade = 'A';
  else if (score > 75) grade = 'B';
  else if (score > 60) grade = 'C';
  else if (score > 50) grade = 'D';
  else                 grade = 'F';
  ```
  **TRAP**: "above 90" bermaksud `> 90`, jadi score **90 → B**, dan **50 → F**. Uji nilai sempadan (91, 90, 51, 50).
  """,
  question="Dengan kod di atas, apakah gred bagi score = 90?",
  ans=["B"],
  hint="90 > 90 ialah false.",
  fu=[F("""Nilai sempadan: 51 dan 50.""",
        "Apakah gred bagi score = 50?",
        ans=["F"],
        hint="50 > 50 false."),
      F("""Mengapa susunan penting? Jika `score > 50` diletak di atas, score 95 akan dapat D.""",
        "Jika `else if (score > 50)` diuji PERTAMA, apakah gred bagi 95?",
        ans=["D"],
        hint="Syarat pertama yang benar menang.")],
  mcq=M("Dalam rantai else-if, berapa cabang yang dijalankan paling banyak?",
        "Satu", "Semua yang benar", "Dua", "Bergantung pada braces"))

S("cs10", T, "4.6 Trap: n % 2 == 1 for negative numbers (slide 37)", trap=True,
  text="""
  **TRAP**: dalam C++, hasil `%` mengikut tanda operand kiri. `-3 % 2` = **-1**, bukan 1.

  Jadi `if (n % 2 == 1)` GAGAL mengesan nombor ganjil negatif.

  Betul: `if (n % 2 != 0)` → odd. Atau uji `n % 2 == 0` untuk even.
  """,
  question="Apakah nilai -3 % 2 dalam C++?",
  ans=["-1"],
  hint="Tanda ikut operand kiri.",
  fu=[F("""Syarat selamat untuk ganjil yang berfungsi untuk positif dan negatif.""",
        "Tulis syarat untuk n ganjil yang betul untuk nombor negatif.",
        ans=["n % 2 != 0", "n%2!=0", "(n % 2 != 0)", "n % 2 == -1 || n % 2 == 1"],
        hint="Bukan sama dengan sifar.")],
  mcq=M("Dengan n = -7, `n % 2 == 1` bernilai…",
        "false", "true", "ralat", "-1"))

S("cs11", T, "4.6 Compound condition: leap year",
  """
  Tahun lompat: boleh dibahagi 4, kecuali abad (100), melainkan boleh dibahagi 400.

  ```
  if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0)
      cout << y << " is a leap year";
  ```
  1900 → bukan, 2000 → ya, 2024 → ya, 2100 → bukan.
  """,
  "Tulis syarat C++ untuk tahun lompat y.",
  ans=["(y % 4 == 0 && y % 100 != 0) || y % 400 == 0",
       "y % 4 == 0 && y % 100 != 0 || y % 400 == 0",
       "y % 400 == 0 || (y % 4 == 0 && y % 100 != 0)"],
  hint="(div 4 DAN bukan div 100) ATAU div 400.",
  fu=[F("""1900: 1900 % 4 == 0 betul, tetapi 1900 % 100 == 0, dan 1900 % 400 = 300.""",
        "Adakah 1900 tahun lompat? (ya / tidak)",
        ans=["tidak", "no", "bukan", "tak"],
        hint="Abad, tidak boleh dibahagi 400."),
      F("""2000 % 400 == 0.""",
        "Adakah 2000 tahun lompat? (ya / tidak)",
        ans=["ya", "yes", "betul"],
        hint="Bahagian || selepas.")],
  mcq=M("Tahun manakah BUKAN tahun lompat?",
        "2100", "2000", "2024", "2400"))

S("cs12", T, "4.7 Conditional operator ?: (slides 38–39)",
  """
  **Conditional (ternary) operator**: `condition ? value_if_true : value_if_false`

  ```
  int a = 4, b = 9;
  cout << (a > b ? a : b);   // 9
  ```
  Ringkasan if...else yang menghasilkan nilai.
  """,
  "Apakah sintaks conditional operator?",
  ans=["condition ? value_if_true : value_if_false", "condition ? a : b", "cond ? x : y", "? :", "?:"],
  hint="Dua simbol: ? dan :",
  fu=[F("""`int a = 4, b = 9; cout << (a > b ? a : b);`""",
        "Apakah output?",
        ans=["9"],
        hint="4 > 9 false → ambil b."),
      F("""`int m = 45; cout << (m >= 50 ? "Pass" : "Fail");`""",
        "Apakah output?",
        ans=["Fail"],
        hint="45 >= 50?")],
  mcq=M("`x = (n > 0) ? 1 : -1;` dengan n = 0 memberi x =",
        "-1", "1", "0", "ralat"))

S("cs13", T, "4.8 switch statement rules",
  """
  ```
  switch (expression) {
      case 1:  statements; break;
      case 2:  statements; break;
      default: statements;
  }
  ```
  Peraturan:
  - Expression mestilah jenis **integral**: `int` atau `char` (bukan `double`, bukan `string`).
  - Label `case` mesti **pemalar** (constant), tidak boleh julat (`case > 90` tidak sah).
  - `break` keluar dari switch. `default` dijalankan jika tiada case sepadan (pilihan).
  """,
  "Apakah jenis data yang dibenarkan untuk expression dalam switch?",
  kw=["int|integer|integral", "char|character|aksara"],
  ans="Jenis integral sahaja: int atau char (bukan double/string).",
  hint="Nombor bulat dan aksara.",
  fu=[F("""
        ```
        char op = '+';
        int a = 6, b = 3;
        switch (op) {
            case '+': cout << a + b; break;
            case '-': cout << a - b; break;
            default:  cout << "?";
        }
        ```""",
        "Apakah output?",
        ans=["9"],
        hint="op ialah '+'."),
      F("""Cari kesilapan: `switch (price) { case 4.5: ... }` dengan `double price`.""",
        "Mengapa ini ralat?",
        kw=["double|float|perpuluhan|decimal",
            "integral|int|integer|char|tidak dibenarkan|not allowed|tak boleh|cannot|tidak boleh"],
        ans="switch tidak menerima double; hanya int/char.",
        hint="Jenis price.")],
  mcq=M("Yang manakah label case yang SAH?",
        "case 'A':", "case > 90:", "case 1.5:", "case \"yes\":"))

S("cs14", T, "4.8 Trap: switch fall-through (missing break)", trap=True,
  text="""
  **TRAP**: tanpa `break`, pelaksanaan **jatuh ke case seterusnya** (fall-through) sehingga jumpa break atau hujung switch.

  ```
  int x = 2;
  switch (x) {
      case 1: cout << "A";
      case 2: cout << "B";
      case 3: cout << "C"; break;
      default: cout << "D";
  }
  ```
  Output: **`BC`**.
  """,
  question="Apakah output program di atas?",
  ans=["BC"],
  hint="Mula di case 2, teruskan sehingga break.",
  fu=[F("""Dengan x = 1, mula di case 1 dan jatuh hingga break di case 3.""",
        "Apakah output jika x = 1?",
        ans=["ABC"],
        hint="A, kemudian terus…"),
      F("""Dengan x = 7, tiada case sepadan.""",
        "Apakah output jika x = 7?",
        ans=["D"],
        hint="default.")],
  mcq=M("Apa yang berlaku jika break tertinggal dalam case?",
        "Case seterusnya juga dijalankan", "Ralat compile", "Program berhenti", "Case itu dilangkau"))

S("cs15", T, "4.9 Loop parts and the while loop",
  """
  Setiap loop ada **tiga bahagian**:
  1. **Initialization**: beri nilai awal pada loop control variable.
  2. **Condition (test)**: diuji sebelum setiap ulangan.
  3. **Update**: ubah variable supaya loop akhirnya berhenti.

  `while` ialah **pre-test loop** (syarat diuji dahulu; mungkin 0 kali).
  ```
  int i = 1, total = 0;      // initialization
  while (i <= 5) {           // condition
      total += i;
      i++;                   // update
  }
  cout << total;             // 15
  ```
  """,
  "Apakah tiga bahagian sesuatu loop?",
  kw=["initialization|initialisation|inisialisasi|nilai awal|initialize|init|mula",
      "condition|syarat|test|ujian",
      "update|kemas kini|increment|decrement|ubah|tambah"],
  ans="Initialization, condition (test), update.",
  hint="Mula, uji, ubah.",
  fu=[F("""Kod total 1 hingga 5 di atas.""",
        "Apakah output?",
        ans=["15"],
        hint="1+2+3+4+5."),
      F("""`int n = 3; while (n > 0) { cout << n << "... "; n--; } cout << "Go!";`""",
        "Apakah output?",
        ans=["3... 2... 1... Go!"],
        hint="n berkurang 3, 2, 1.")],
  mcq=M("while loop dikenali sebagai…",
        "Pre-test loop", "Post-test loop", "Counter-only loop", "Selection structure"))

S("cs16", T, "4.9 The for loop",
  """
  ```
  for (initialization; condition; update)
      statement;
  ```
  Ketiga-tiga bahagian dalam satu baris. Sesuai apabila **bilangan ulangan diketahui**.

  ```
  for (int i = 10; i > 0; i -= 2)
      cout << i << " ";
  ```
  Output: `10 8 6 4 2`
  """,
  "Bilakah for loop paling sesuai digunakan?",
  kw=["known|diketahui|tahu|tetap|fixed|tentu|count|bilangan|berapa kali"],
  ans="Apabila bilangan ulangan diketahui (counter-controlled).",
  hint="Contoh: cetak jadual 1 hingga 10.",
  fu=[F("""`for (int i = 10; i > 0; i -= 2) cout << i << " ";`""",
        "Apakah output?",
        ans=["10 8 6 4 2"],
        hint="Turun 2 setiap kali, berhenti sebelum 0."),
      F("""Jadual darab: `for (int i = 1; i <= 10; i++) cout << 3 << " x " << i << " = " << 3 * i << endl;`""",
        "Apakah baris KELIMA output?",
        ans=["3 x 5 = 15"],
        hint="i = 5.")],
  mcq=M("Berapa kali `for (int i = 0; i < 10; i += 3)` berulang?",
        "4", "3", "10", "5"))

S("cs17", T, "4.9 The do...while loop",
  """
  `do...while` ialah **post-test loop**: badan dijalankan **sekurang-kurangnya sekali**, syarat diuji di hujung. Ada `;` selepas `while (...)`.

  ```
  int n = 10;
  do {
      cout << n;
      n++;
  } while (n < 5);
  ```
  Output: **`10`** (sekali, walaupun 10 < 5 false). Sesuai untuk **menu** dan validasi input.
  """,
  "Apakah beza utama do...while dan while?",
  kw=["at least once|sekurang-kurangnya sekali|sekali|once|minimum satu",
      "post-test|post test|hujung|akhir|end|selepas|after|bawah"],
  ans="do...while menjalankan badan sekurang-kurangnya sekali kerana syarat diuji di hujung (post-test); while uji dahulu.",
  hint="Bila syarat diuji?",
  fu=[F("""Kod n = 10 di atas.""",
        "Apakah output?",
        ans=["10"],
        hint="Badan jalan sekali dahulu."),
      F("""Lab 5 B4: menu kafe diulang dengan do...while sehingga pilihan 5; inner do...while ulang prompt sehingga pilihan 1–5.""",
        "Mengapa do...while sesuai untuk menu?",
        kw=["once|sekali|sekurang-kurangnya|at least|dulu|dahulu|first",
            "menu|display|papar|tunjuk|show"],
        ans="Menu mesti dipaparkan sekurang-kurangnya sekali sebelum pilihan diuji.",
        hint="Pengguna perlu nampak menu dahulu.")],
  mcq=M("Yang manakah sintaks do...while yang betul?",
        "do { ... } while (x < 5);", "do { ... } while (x < 5)", "do (x < 5) { ... }", "while { ... } do (x < 5);"))

S("cs18", T, "4.10 Common trap: semicolon after for/while", trap=True,
  text="""
  **TRAP**: `;` selepas `for (...)` menjadikan loop berbadan kosong.

  ```
  int i;
  for (i = 0; i < 3; i++);
      cout << i;
  ```
  Loop berjalan 3 kali tanpa buat apa-apa, kemudian `cout` sekali. Output: **`3`**.

  Untuk `while (cond);` dengan syarat benar → **infinite loop**.
  """,
  question="Apakah output program di atas?",
  ans=["3"],
  hint="cout di luar loop; i selepas loop tamat.",
  fu=[F("""`int k = 0; while (k < 3); { k++; }`""",
        "Apakah yang berlaku?",
        kw=["infinite|tak berhenti|tidak berhenti|selama-lamanya|forever|tak terhingga|hang|never"],
        ans="Infinite loop: badan while ialah ; sahaja, k tidak pernah bertambah.",
        hint="k tidak pernah berubah.")],
  mcq=M("`for (int i = 0; i < 5; i++); cout << \"*\";` mencetak berapa bintang?",
        "1", "5", "0", "6"))

S("cs19", T, "4.10 Common trap: off-by-one (< vs <=)", trap=True,
  text="""
  **TRAP off-by-one**: salah pilih `<` atau `<=`, atau nilai mula 0 atau 1.

  ```
  for (int i = 0; i < 5; i++)    // 5 kali (0..4)
  for (int i = 0; i <= 5; i++)   // 6 kali (0..5)
  for (int i = 1; i <= 5; i++)   // 5 kali (1..5)
  ```
  Semak ulangan **pertama** dan **terakhir** secara manual.
  """,
  question="Berapa kali `for (int i = 0; i <= 5; i++)` berulang?",
  ans=["6", "enam", "6 kali"],
  hint="Kira 0, 1, 2, 3, 4, 5.",
  fu=[F("""`int c = 0; for (int i = 0; i < 5; i++) c++; cout << c;`""",
        "Apakah output?",
        ans=["5"],
        hint="0 hingga 4.")],
  mcq=M("Untuk cetak 1 hingga 10, syarat yang betul dengan `int i = 1` ialah…",
        "i <= 10", "i < 10", "i <= 11", "i > 10"))

S("cs20", T, "4.10 Common trap: infinite loop (missing/wrong update)", trap=True,
  text="""
  **TRAP infinite loop**: syarat tidak pernah menjadi false.

  ```
  int i = 1;
  while (i <= 5)
      cout << i;        // tiada i++ → infinite
  ```
  ```
  for (int i = 10; i > 0; i++)   // update ke arah salah → infinite
  ```
  Lab 5 A2 menggunakan "guard" untuk hentikan loop selepas 12 pusingan semasa debug.
  """,
  question="Namakan dua punca infinite loop.",
  kw=["update|kemas kini|i++|increment|tiada update|lupa",
      "wrong|salah|arah|direction|condition|syarat|never false|tak pernah false|tidak pernah",
      ";|semicolon"],
  ans="Tiada update (lupa i++), update ke arah salah, syarat tidak pernah false, atau ; selepas while.",
  hint="Apa yang membuat syarat menjadi false?",
  fu=[F("""`for (int i = 10; i > 0; i++)`""",
        "Apakah kesilapan dalam loop ini?",
        kw=["i++|increment|tambah|naik", "i--|decrement|kurang|turun|arah|direction|salah|wrong"],
        ans="Update i++ menjadikan i makin besar; sepatutnya i-- supaya i > 0 akhirnya false.",
        hint="i bermula 10 dan diuji > 0.")],
  mcq=M("`int i = 0; while (i < 3) { cout << i; }` akan…",
        "Infinite loop mencetak 0", "Cetak 012", "Cetak 0 sekali", "Ralat compile"))

S("cs21", T, "4.11 break and continue (slides 74–80)", trap=True,
  text="""
  - `break`: keluar dari loop (atau switch) serta-merta.
  - `continue`: langkau baki badan dan terus ke ulangan seterusnya.

  ```
  for (int i = 1; i <= 6; i++) {
      if (i == 3) continue;
      if (i == 5) break;
      cout << i << " ";
  }
  ```
  Output: `1 2 4`

  **TRAP (slide 80)**: dalam `while`, `continue` boleh melangkau **update** → infinite loop. Letak update sebelum continue.
  """,
  question="Apakah beza break dan continue?",
  kw=["break", "exit|keluar|stop|berhenti|tamat|terminate",
      "continue", "skip|langkau|seterusnya|next|ulangan seterusnya"],
  ans="break keluar dari loop sepenuhnya; continue langkau baki ulangan semasa dan teruskan ulangan seterusnya.",
  hint="Satu keluar terus, satu langkau.",
  fu=[F("""Kod for i = 1..6 di atas.""",
        "Apakah output?",
        ans=["1 2 4"],
        hint="3 dilangkau, berhenti di 5."),
      F("""
        ```
        int i = 0;
        while (i < 5) {
            i++;
            if (i % 2 == 0) continue;
            cout << i << " ";
        }
        ```""",
        "Apakah output?",
        ans=["1 3 5"],
        hint="Nombor genap dilangkau; i++ sebelum continue."),
      F("""
        ```
        int i = 0;
        while (i < 5) {
            if (i == 2) continue;
            cout << i;
            i++;
        }
        ```""",
        "Apa yang berlaku apabila i = 2?",
        kw=["infinite|tak berhenti|tidak berhenti|forever|selama-lamanya|hang",
            "update|i++|langkau|skip|tidak bertambah|kekal"],
        ans="Infinite loop kerana continue melangkau i++, jadi i kekal 2.",
        hint="Adakah i++ dijalankan?")],
  mcq=M("Dalam loop, `continue` akan…",
        "Langkau ke ulangan seterusnya", "Keluar dari loop", "Keluar dari program", "Ulang ulangan semasa"))

S("cs22", T, "4.12 Loop patterns: counting, totals, sentinel (slides 84–91)",
  """
  Corak loop:
  - **Counter-controlled**: ulang N kali.
  - **Running total (accumulator)**: `sum += n`.
  - **Sentinel-controlled**: baca sehingga nilai khas (contoh `-1`).

  Lab 5 B6: input `12 -5 0 20 7 4 -1`, langkau nombor < 1 dengan continue:
  ```
  while (true) {
      cin >> n;            // baca di ATAS badan loop
      if (n == -1) break;
      if (n < 1) { cout << n << " is not positive, skipped."; continue; }
      sum += n; count++;
  }
  ```
  `Count = 4`, `Sum = 43`, `Average = 10.75`.
  """,
  "Apakah sentinel-controlled loop?",
  kw=["sentinel|nilai khas|special value|-1",
      "stop|berhenti|tamat|end|hentikan|until|sehingga",
      "input|baca|read|unknown|tidak diketahui"],
  ans="Loop yang terus membaca input sehingga pengguna memasukkan nilai khas (sentinel) seperti -1.",
  hint="Bilangan input tidak diketahui.",
  fu=[F("""Input: 12, -5, 0, 20, 7, 4, -1 (nombor < 1 dilangkau).""",
        "Apakah Count dan Sum? (tulis: count sum)",
        ans=["4 43", "count = 4 sum = 43"],
        hint="12 + 20 + 7 + 4."),
      F("""Purata dikira sebagai `static_cast<double>(sum) / count`.""",
        "Apakah Average yang dicetak?",
        ans=["10.75"],
        hint="43 / 4.")],
  mcq=M("Loop yang sesuai untuk membaca markah sehingga pengguna taip -1 ialah…",
        "Sentinel-controlled loop", "Counter-controlled for loop 10 kali", "switch", "Nested if"))

S("cs23", T, "4.13 Nested loops (slides 92–94)",
  """
  Dalam **nested loop**, inner loop berjalan **sepenuhnya** untuk setiap satu ulangan outer loop.

  ```
  for (int i = 1; i <= 3; i++) {
      for (int j = 1; j <= i; j++)
          cout << "*";
      cout << endl;
  }
  ```
  Output:
  ```
  *
  **
  ***
  ```
  Outer: 3 kali. Inner (jumlah): 1 + 2 + 3 = **6** kali.
  """,
  "Berapa kali inner loop berjalan secara keseluruhan dalam contoh segi tiga 3 baris?",
  ans=["6", "enam", "6 kali"],
  hint="1 + 2 + 3.",
  fu=[F("""
        ```
        for (int i = 1; i <= 3; i++)
            for (int j = 1; j <= 2; j++)
                cout << i * j << " ";
        ```""",
        "Apakah output?",
        ans=["1 2 2 4 3 6"],
        hint="i=1: 1 2; i=2: 2 4; i=3: …"),
      F("""Outer 4 kali, inner tetap 5 kali setiap outer.""",
        "Berapa kali statement dalam inner loop dijalankan?",
        ans=["20"],
        hint="4 × 5.")],
  mcq=M("`for(i=0;i<2;i++) for(j=0;j<3;j++) cout<<\"#\";` mencetak berapa #?",
        "6", "5", "3", "2"))

S("cs24", T, "4.14 Choosing the right control structure",
  """
  | Situasi | Pilihan |
  |---|---|
  | Pilih berdasarkan julat (score > 90) | `if / else if` |
  | Pilih nilai diskret (menu 1–5, char op) | `switch` |
  | Bilangan ulangan diketahui | `for` |
  | Bilangan tidak diketahui / sentinel | `while` |
  | Mesti jalan sekurang-kurangnya sekali (menu, validasi) | `do...while` |
  """,
  "Bilakah switch lebih sesuai berbanding if/else if?",
  kw=["discrete|diskret|specific|tertentu|exact|tepat|constant|pemalar|menu|pilihan|single value|nilai",
      "int|char|integer|integral|equal|sama|=="],
  ans="Apabila memilih berdasarkan nilai diskret/tepat jenis int atau char (contoh pilihan menu), bukan julat.",
  hint="switch tidak boleh uji julat.",
  fu=[F("""Gred berdasarkan julat markah (> 90, > 75…) tidak boleh terus guna switch.""",
        "Struktur apakah untuk menentukan gred daripada julat markah?",
        ans=["if else if", "if/else if", "else if", "if-else-if", "nested if", "if...else if", "if"],
        hint="Rantai…")],
  mcq=M("Struktur terbaik untuk 'ulang tanya kata laluan sehingga betul' ialah…",
        "do...while", "switch", "for dengan 10 ulangan", "if"))

S("cs25", T, "4.15 Debugging with breakpoints (Lab 5)",
  """
  Debugger membantu melihat nilai pemboleh ubah semasa program berjalan:

  - Compile dengan `-g`: `g++ -g -std=c++17 -Wall -Wextra -pedantic A1.cpp -o A1`
  - **F9** breakpoint, **F5** start/continue, **F10** Step Over, **F11** Step Into.
  - Tambah variable ke **Watch**.
  - GDB: `break 11`, `run`, `next`, `print tickets`, `continue`, `quit`.

  Contoh: Step Over `if (tickets = 0)` menunjukkan tickets berubah dari 5 ke 0.
  """,
  "Apakah fungsi breakpoint?",
  kw=["stop|berhenti|pause|hentikan|jeda", "line|baris|tempat|point|titik",
      "inspect|lihat|watch|nilai|variable|periksa|check"],
  ans="Menghentikan program pada baris tertentu supaya kita boleh periksa nilai pemboleh ubah dan step baris demi baris.",
  hint="Program berhenti sementara…",
  fu=[F("""Kekunci lalai VS Code: F9, F5, F10, F11.""",
        "Kekunci apakah untuk Step Over?",
        ans=["F10", "f10"],
        hint="Bukan F11 (Step Into).")],
  mcq=M("Flag compile yang diperlukan untuk maklumat debug ialah…",
        "-g", "-o", "-Wall", "-std=c++17"))
