from helpers import S, F, M

T = "ctrl"
H = "4 · "

S("cs01", T, H + "bool ↔ int",
  """
  - **bool → int**: `true` = **1**, `false` = **0**. Contoh: `2 + true` = **3**.
  - **int → bool**: `0` = **false**, **sebarang bukan-sifar = true** (termasuk **−10**).
  """,
  "Bagaimanakah int ditukar kepada bool?",
  kw=["0|sifar|zero", "false|palsu",
      "non-zero|bukan sifar|bukan-sifar|selain 0|lain|any other|nonzero", "true|benar"],
  ans="0 = false; sebarang nilai bukan sifar (termasuk negatif seperti −10) = true.",
  hint="Hanya satu nilai yang false.",
  fu=[F("""`cout << 2 + true;`""",
        "Apakah output?",
        ans=["3"],
        hint="true = 1."),
      F("""`if (-10) cout << "yes"; else cout << "no";`""",
        "Apakah output?",
        ans=["yes"],
        hint="−10 bukan sifar.")],
  mcq=M("Dalam C++, `-10` sebagai syarat bernilai…",
        "true", "false", "ralat", "-10"))

S("cs02", T, H + "if statement: 3 forms and compound statement",
  """
  ```
  if (cond)          if (cond) {          if (cond) {
      stmt;              stmt1;               ...
                         stmt2;           } else {
                     }                        ...
                                          }
  ```
  - Braces `{ }` adalah **pilihan apabila hanya satu statement**.
  - Sekumpulan statement dalam `{ }` dipanggil **compound statement**.
  """,
  "Apakah compound statement dan bilakah braces { } pilihan?",
  kw=["group|kumpulan|beberapa|multiple|lebih", "{ }|{}|braces|kurungan kerinting",
      "one|satu|single|hanya satu"],
  ans="Compound statement ialah sekumpulan statement dalam { }; braces pilihan apabila hanya ada satu statement.",
  hint="Dua bahagian: definisi dan bila boleh tinggal.",
  fu=[F("""
        ```
        int a = 8;
        if (a > 5) {
            cout << "big ";
            cout << "number";
        }
        ```""",
        "Apakah output?",
        ans=["big number"],
        hint="Kedua-dua dalam blok.")],
  mcq=M("Sekumpulan statement dalam { } dipanggil…",
        "Compound statement", "Null statement", "Preprocessor", "Literal"))

S("cs03", T, H + "if-else if chain (grade)",
  """
  ```
  if (score > 90)      grade = 'A';
  else if (score > 75) grade = 'B';
  else if (score > 60) grade = 'C';
  else if (score > 50) grade = 'D';
  else                 grade = 'F';
  ```
  Syarat diuji dari atas; **yang pertama benar** sahaja dijalankan.
  """,
  "Dengan kod di atas, apakah gred untuk score = 80?",
  ans=["B"],
  hint="80 > 90? 80 > 75?",
  fu=[F("""Sempadan: `score > 90` bermaksud lebih daripada 90, jadi 90 bukan A.""",
        "Apakah gred untuk score = 90?",
        ans=["B"],
        hint="90 > 90 false."),
      F("""score = 50: 50 > 50 false.""",
        "Apakah gred untuk score = 50?",
        ans=["F"],
        hint="Jatuh ke else.")],
  mcq=M("Dalam rantai if-else if, berapa cabang paling banyak dijalankan?",
        "Satu", "Semua yang benar", "Dua", "Tiada had"))

S("cs04", T, H + "Common traps · if (x = 0)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (x = 0)` | Ini **assignment**, bukan perbandingan. x menjadi 0, jadi syarat **sentiasa false**. | `if (x == 0)` |
  """,
  question="Mengapa `if (x = 0)` salah?",
  kw=["assignment|umpukan|assign|=",
      "not comparison|bukan perbandingan|bukan banding|compare|banding|==",
      "always false|sentiasa false|sentiasa palsu|false|0"],
  ans="Ia assignment, bukan perbandingan: x menjadi 0 dan syarat sentiasa false. Betul: if (x == 0).",
  hint="= vs ==.",
  fu=[F("""
        ```
        int x = 5;
        if (x = 0) cout << "T";
        else cout << "F";
        cout << " x=" << x;
        ```""",
        "Apakah output?",
        ans=["F x=0"],
        hint="x ditukar kepada 0, 0 = false."),
      F("""Betulkan syarat supaya ia membandingkan x dengan 0.""",
        "Tulis syarat yang betul.",
        ans=["if (x == 0)", "if(x==0)", "x == 0"],
        hint="Dua =.")],
  mcq=M("`if (x = 0)` akan…",
        "Menukar x kepada 0 dan sentiasa false", "Membandingkan x dengan 0", "Sentiasa true", "Ralat compile"))

S("cs05", T, H + "Common traps · if (2 < x < 9)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (2 < x < 9)` | `(2<x)` memberi **0 atau 1**, yang **sentiasa < 9**, jadi **sentiasa true** | `if (2<x && x<9)` |
  """,
  question="Mengapa `if (2 < x < 9)` sentiasa true?",
  kw=["0 or 1|0 atau 1|0|1|true|false", "always|sentiasa", "< 9|kurang daripada 9|less than 9|9"],
  ans="(2<x) dinilai dahulu dan memberi 0 atau 1; kedua-duanya < 9, jadi sentiasa true.",
  hint="Apakah nilai (2 < x)?",
  fu=[F("""x = 20: `(2 < 20)` = 1, kemudian `1 < 9` = true.""",
        "Dengan x = 20, apakah nilai `(2 < x < 9)`? (1 / 0)",
        ans=["1", "true"],
        hint="1 < 9."),
      F("""Tulis julat 2 < x < 9 dengan betul dalam C++.""",
        "Tulis syarat yang betul.",
        ans=["if (2<x && x<9)", "2<x && x<9", "if (2 < x && x < 9)", "x > 2 && x < 9", "(2 < x) && (x < 9)"],
        hint="Guna &&.")],
  mcq=M("Syarat betul untuk 'x antara 2 dan 9' ialah…",
        "2 < x && x < 9", "2 < x < 9", "2 < x || x < 9", "x < 2 && x > 9"))

S("cs06", T, H + "Common traps · if (0<x) && (x<10)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (0<x) && (x<10)` | **Syntax error**: seluruh syarat perlukan **kurungan luar** `( )` | `if ((0<x) && (x<10))` |
  """,
  question="Apakah kesilapan dalam `if (0<x) && (x<10)`?",
  kw=["syntax|sintaks", "outer|luar|whole|seluruh|keseluruhan", "( )|()|kurungan|parentheses|bracket"],
  ans="Syntax error: seluruh syarat perlu dalam kurungan luar. Betul: if ((0<x) && (x<10)).",
  hint="Kurungan if mesti meliputi semua.",
  fu=[F("""Syarat if mesti berada dalam **satu pasang kurungan luar**.""",
        "Tulis syarat yang betul.",
        ans=["if ((0<x) && (x<10))", "if((0<x)&&(x<10))", "if (0<x && x<10)", "if (0 < x && x < 10)"],
        hint="Tambah ( ) di luar.")],
  mcq=M("`if (0<x) && (x<10)` menghasilkan…",
        "Syntax error", "Sentiasa true", "Sentiasa false", "Berfungsi seperti biasa"))

S("cs07", T, H + "Common traps · if (!n > 9)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (!n > 9)` | `!` dinilai **dahulu**: `!5` = false = 0, dan `0 > 9` ialah false | `if (!(n > 9))` |
  """,
  question="Dengan n = 5, apakah nilai `!n > 9`? (1 / 0)",
  ans=["0", "false"],
  hint="!5 dahulu.",
  fu=[F("""Langkah: `!5` = 0, kemudian `0 > 9` = false.""",
        "Mengapa `!n > 9` tidak bermaksud 'n tidak lebih besar daripada 9'?",
        kw=["!|not", "first|dahulu|dulu|before|keutamaan|precedence|higher",
            "n|5|!n"],
        ans="Kerana ! dinilai dahulu pada n (!5 = 0), kemudian 0 > 9.",
        hint="Keutamaan operator."),
      F("""Bentuk betul: songsangkan seluruh perbandingan.""",
        "Tulis syarat yang betul.",
        ans=["if (!(n > 9))", "!(n > 9)", "if(!(n>9))", "n <= 9", "if (n <= 9)"],
        hint="!( … )")],
  mcq=M("`!n > 9` dinilai sebagai…",
        "(!n) > 9", "!(n > 9)", "n < 9", "n != 9"))

S("cs08", T, H + "Common traps · if (x<3);", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (x<3);` | `;` ialah **null statement**, jadi baris seterusnya **sentiasa** dijalankan | Tiada `;` selepas `if (...)` |
  """,
  question="Apakah yang berlaku apabila ada ; selepas `if (x<3)`?",
  kw=["null|kosong|empty", "always|sentiasa", "next|seterusnya|line|baris|run|jalan"],
  ans="; menjadi null statement, jadi baris seterusnya sentiasa dijalankan.",
  hint="Badan if menjadi kosong.",
  fu=[F("""
        ```
        int x = 7;
        if (x < 3);
            cout << "small";
        ```""",
        "Apakah output?",
        ans=["small"],
        hint="cout tiada kaitan dengan if.")],
  mcq=M("`if (x<3); cout << \"A\";` dengan x = 10 mencetak…",
        "A", "Tiada", "Ralat", "10"))

S("cs09", T, H + "Common traps · 2 statements before else with no { }", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | 2 statements sebelum `else` tanpa `{ }` | **Syntax error: misplaced else** | Balut dengan `{ }` |

  ```
  if (x > 0)
      x = 1;
      x = 2;        // bukan milik if
  else              // error: 'else' without a previous 'if'
      x = 3;
  ```
  """,
  question="Apakah ralat jika dua statement diletak sebelum else tanpa { }?",
  kw=["syntax|sintaks|ralat|error", "misplaced|salah tempat|without|tanpa|else"],
  ans="Syntax error: misplaced else ('else' without a previous 'if'). Balut statement dengan { }.",
  hint="else tidak jumpa if-nya.",
  fu=[F("""Penyelesaian: balut kedua-dua statement dalam `{ }`.""",
        "Apakah yang perlu ditambah untuk membetulkannya?",
        ans=["{ }", "{}", "braces", "kurungan kerinting", "curly braces"],
        hint="Compound statement.")],
  mcq=M("Dua statement sebelum else tanpa braces menghasilkan…",
        "Syntax error: misplaced else", "else dijalankan dua kali", "Infinite loop", "Tiada masalah"))

S("cs10", T, H + "Common traps · nested if with no braces (dangling else)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | Nested if tanpa braces | `else` berpasangan dengan **if yang terdekat** (dangling else) | Guna `{ }` untuk tunjuk if yang mana |

  ```
  int a = 5, b = 1;
  if (a > 3)
      if (b > 3) cout << "X";
  else cout << "Y";
  ```
  """,
  question="Dengan a = 5, b = 1, apakah output kod di atas?",
  ans=["Y"],
  hint="else milik if (b > 3).",
  fu=[F("""else berpasangan dengan if **terdekat**, bukan ikut indentasi.""",
        "Dengan siapakah else berpasangan dalam nested if tanpa braces?",
        kw=["nearest|terdekat|dekat|closest|inner|dalam|last|terakhir"],
        ans="Dengan if yang terdekat.",
        hint="Dangling else.")],
  mcq=M("Dangling else bermaksud else berpasangan dengan…",
        "if yang terdekat", "if yang pertama", "if paling luar", "if yang diindent sama"))

S("cs11", T, H + "Common traps · indentation only", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | Indentasi sahaja | **Indentasi tidak bermakna** kepada compiler | Guna `{ }` |

  ```
  int age = 15;
  if (age >= 18)
      cout << "Adult ";
      cout << "Can vote";
  ```
  """,
  question="Apakah output kod di atas?",
  ans=["Can vote"],
  hint="Hanya baris pertama milik if.",
  fu=[F("""Compiler mengabaikan ruang/indentasi. Hanya `{ }` menentukan blok.""",
        "Apakah yang menentukan statement mana milik if: indentasi atau braces?",
        ans=["braces", "{ }", "{}", "kurungan kerinting"],
        hint="Bukan ruang.")],
  mcq=M("Bagi compiler C++, indentasi…",
        "Tidak bermakna", "Menentukan blok", "Wajib", "Menggantikan ;"))

S("cs12", T, H + "Shortcuts · if (a), if (!a), if (n%2)",
  """
  | Long | Short |
  |---|---|
  | `if (a != 0)` | `if (a)` |
  | `if (a == 0)` | `if (!a)` |
  | `if (n%2 == 1)` (odd) | `if (n%2)` |
  """,
  "Tulis bentuk ringkas bagi `if (a != 0)`.",
  ans=["if (a)", "if(a)"],
  hint="Bukan sifar = true.",
  fu=[F("""`if (a == 0)` → `if (!a)`.""",
        "Tulis bentuk ringkas bagi `if (a == 0)`.",
        ans=["if (!a)", "if(!a)"],
        hint="NOT a."),
      F("""`n % 2` bukan sifar bermaksud ganjil (odd).""",
        "Tulis bentuk ringkas untuk menguji n ganjil.",
        ans=["if (n%2)", "if (n % 2)", "if(n%2)"],
        hint="Baki bukan sifar.")],
  mcq=M("`if (!a)` bersamaan dengan…",
        "if (a == 0)", "if (a != 0)", "if (a > 0)", "if (a = 0)"))

S("cs13", T, H + "Conditional (ternary) operator",
  """
  `cond ? value1 : value2`: **jika true, ambil value1; jika tidak, value2**.

  ```
  p = (p<5) ? q+1 : 5;
  ```
  """,
  "Terangkan conditional (ternary) operator.",
  kw=["?|ternary|conditional", "true|benar|value1|nilai pertama|first",
      "otherwise|jika tidak|false|value2|else|kedua|second"],
  ans="cond ? value1 : value2 — jika cond true ambil value1, jika tidak ambil value2.",
  hint="? dan :",
  fu=[F("""`int p = 3, q = 8; p = (p<5) ? q+1 : 5;`""",
        "Apakah nilai p?",
        ans=["9"],
        hint="3 < 5 true → q+1."),
      F("""`int p = 7, q = 8; p = (p<5) ? q+1 : 5;`""",
        "Apakah nilai p?",
        ans=["5"],
        hint="7 < 5 false.")],
  mcq=M("`x = (a > b) ? a : b;` menyimpan…",
        "Nilai yang lebih besar antara a dan b", "Nilai yang lebih kecil", "Sentiasa a", "Sentiasa b"))

S("cs14", T, H + "Complement a condition",
  """
  **Complement** syarat dengan meletakkan **`!( )`** di sekelilingnya:

  `!(n==0)` sama dengan `n != 0`.

  Gunakan apabila cabang **"Yes" flowchart berada di sebelah yang salah**.
  """,
  "Bagaimana membuat complement sesuatu syarat, dan bilakah ia berguna?",
  kw=["!( )|!()|!|not", "around|sekeliling|keliling|balut|wrap",
      "yes|flowchart|carta|wrong side|sebelah salah|salah"],
  ans="Letak !( ) di sekeliling syarat; berguna apabila cabang Yes flowchart berada di sebelah yang salah.",
  hint="Contoh !(n==0).",
  fu=[F("""`!(n==0)` = `n != 0`.""",
        "Tulis bentuk lain bagi `!(n==0)`.",
        ans=["n != 0", "n!=0"],
        hint="Tidak sama."),
      F("""Complement bagi `x > 5` boleh ditulis `!(x > 5)` atau `x <= 5`.""",
        "Tulis complement bagi `x > 5` tanpa menggunakan !.",
        ans=["x <= 5", "x<=5"],
        hint="Bukan x < 5.")],
  mcq=M("`!(n == 0)` sama dengan…",
        "n != 0", "n == 0", "n > 0", "n < 0"))

S("cs15", T, H + "switch · integral expression",
  """
  ```
  switch (grade) {
      case 'A': cout << "Excellent!"; break;
      case 'B': cout << "Very good!"; break;
      case 'C': cout << "Good";       break;
      default : cout << "Fail";
  }
  ```
  Expression mesti jenis **integral**: **`int`, `char`, `bool`**. **Bukan float dan bukan string.**
  """,
  "Apakah jenis yang dibenarkan untuk expression switch?",
  kw=["int|integer|integral", "char|character|aksara", "bool"],
  ans="Jenis integral: int, char, bool (bukan float, bukan string).",
  hint="Tiga jenis.",
  fu=[F("""Dengan `grade = 'B'` dalam kod di atas.""",
        "Apakah output?",
        ans=["Very good!"],
        hint="case 'B'."),
      F("""`double d = 1; switch (d) { ... }` → ralat `switch quantity not an integer`.""",
        "Bolehkah string digunakan sebagai expression switch? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Not float and not string.")],
  mcq=M("Jenis manakah TIDAK boleh digunakan dalam switch?",
        "float", "int", "char", "bool"))

S("cs16", T, H + "switch · case values must be constants",
  """
  Setiap nilai `case` mesti **constant**: **literal, `const` atau `#define`**, **bukan pemboleh ubah**.
  """,
  "Apakah yang boleh dijadikan nilai case?",
  kw=["constant|pemalar|tetap", "literal|const|#define|define"],
  ans="Constant sahaja: literal, const atau #define; bukan pemboleh ubah.",
  hint="Tiga jenis constant.",
  fu=[F("""`int c = 2; switch (x) { case c: ... }` → ralat: c bukan constant.""",
        "Bolehkah pemboleh ubah biasa dijadikan nilai case? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Mesti constant.")],
  mcq=M("Label case manakah SAH?",
        "case 'A':", "case x:", "case x > 5:", "case 2.5:"))

S("cs17", T, H + "switch · fall-through (missing break)",
  """
  Jika **`break` tertinggal**, ia **"falls through"** dan menjalankan **case seterusnya juga**.

  ```
  char grade = 'C';
  switch (grade) {
      case 'A': cout << "Excellent!";
      case 'B': cout << "Very good!";
      case 'C': cout << "Good";
      default : cout << "Fail";
  }
  ```
  """,
  "Apakah output kod di atas (tiada break)?",
  ans=["GoodFail"],
  hint="Mula di case 'C', terus ke default.",
  fu=[F("""Dengan grade = 'B' dalam kod tanpa break.""",
        "Apakah output?",
        ans=["Very good!GoodFail"],
        hint="Jatuh hingga hujung.")],
  mcq=M("Apa yang berlaku jika break tertinggal dalam case?",
        "Case seterusnya turut dijalankan (fall through)", "Ralat compile", "Program tamat", "Case dilangkau"))

S("cs18", T, H + "switch · default",
  """
  **`default`** dijalankan apabila **tiada case yang sepadan** (no case matches).
  """,
  "Bilakah default dijalankan dalam switch?",
  kw=["no case|tiada case|tiada yang|none|not match|tidak sepadan|tak sepadan|no match"],
  ans="Apabila tiada case yang sepadan.",
  hint="Pilihan terakhir.",
  fu=[F("""Kod switch gred (dengan break) dan `grade = 'Z'`.""",
        "Apakah output?",
        ans=["Fail"],
        hint="Tiada case 'Z'.")],
  mcq=M("Dalam switch, bahagian yang dijalankan apabila tiada case sepadan ialah…",
        "default", "break", "else", "continue"))

S("cs19", T, H + "Loops · 4 parts",
  """
  Setiap loop ada **4 bahagian**: **initialise**, **condition**, **body**, **update**.

  Jika anda **lupa update**, anda dapat **infinite loop**.
  """,
  "Apakah empat bahagian sesuatu loop?",
  kw=["initialise|initialize|initialization|inisialisasi|nilai awal|init",
      "condition|syarat|test",
      "body|badan",
      "update|kemas kini|increment|decrement"],
  ans="Initialise, condition, body, update.",
  hint="Mula, uji, kerja, ubah.",
  fu=[F("""Tanpa update, syarat tidak pernah berubah.""",
        "Apakah yang berlaku jika update dilupakan?",
        ans=["infinite loop", "loop tak terhingga", "infinite"],
        hint="Tidak pernah berhenti.")],
  mcq=M("Lupa bahagian update dalam loop biasanya menyebabkan…",
        "Infinite loop", "Syntax error", "Loop berjalan 0 kali", "Program lebih laju"))

S("cs20", T, H + "Loops · while, for, do-while print 10 to 1",
  """
  ```
  // while (pre-test)       // for (pre-test)             // do-while (post-test)
  n = 10;                   for (n = 10; n > 0; n--)      n = 10;
  while (n > 0) {           {                             do {
      cout << n << " ";         cout << n << " ";             cout << n << " ";
      n = n - 1;            }                                 n = n - 1;
  }                                                       } while (n > 0);   // ← ;
  ```
  Ketiga-tiganya mencetak **10 9 8 7 6 5 4 3 2 1**. Perhatikan **`;` selepas `while (n > 0)` dalam do-while**.
  """,
  "Apakah output ketiga-tiga loop di atas?",
  ans=["10 9 8 7 6 5 4 3 2 1"],
  hint="Dari 10 turun ke 1.",
  fu=[F("""do-while berakhir dengan `} while (n > 0);`""",
        "Simbol apakah yang mesti ada selepas `while (n > 0)` dalam do-while?",
        ans=[";", "semicolon", "titik koma", "koma bertitik"],
        hint="← ;"),
      F("""Jika `n = 0` pada mula: while tidak jalan (pre-test), do-while jalan sekali (post-test).""",
        "Dengan n = 0 pada mula, berapa kali badan do-while dijalankan?",
        ans=["1", "sekali", "once"],
        hint="Post-test.")],
  mcq=M("Loop manakah ialah post-test?",
        "do-while", "while", "for", "Ketiga-tiganya"))

S("cs21", T, H + "Loops · which loop to use",
  """
  | Loop | Use when… |
  |---|---|
  | `for` | tahu **berapa kali** (counter) |
  | `while` | mungkin berjalan **0 kali** (sentinel, bilangan tidak diketahui) |
  | `do-while` | mesti berjalan **sekurang-kurangnya sekali** (menu, input validation) |
  """,
  "Bilakah do-while paling sesuai?",
  kw=["at least once|sekurang-kurangnya sekali|sekali|once",
      "menu|validation|validasi|pengesahan|input"],
  ans="Apabila loop mesti berjalan sekurang-kurangnya sekali, contoh menu dan input validation.",
  hint="Menu…",
  fu=[F("""for = bilangan diketahui (counter).""",
        "Loop manakah sesuai untuk mencetak jadual 1 hingga 12?",
        ans=["for", "for loop"],
        hint="Bilangan diketahui."),
      F("""while = mungkin 0 kali (sentinel, bilangan tidak diketahui).""",
        "Loop manakah sesuai untuk membaca data sehingga sentinel -999?",
        ans=["while", "while loop"],
        hint="Bilangan tidak diketahui.")],
  mcq=M("Loop untuk menu yang mesti dipaparkan sekurang-kurangnya sekali ialah…",
        "do-while", "for", "while", "switch"))

S("cs22", T, H + "Jump statements · break",
  """
  **`break`** keluar dari loop (atau switch) **serta-merta**. Dalam **nested loops**, ia **hanya keluar dari loop dalam** (inner).

  Contoh nota: `for(n=10;n>0;n--){ if(n<8) break; cout<<n; }` memberi nilai **10 9 8** (tanpa ruang dalam cout, ia dicetak `1098`).
  ```
  for (n = 10; n > 0; n--) {
      if (n < 8) break;
      cout << n << " ";
  }
  ```
  Output: `10 9 8`
  """,
  "Apakah output loop break di atas (dengan ruang)?",
  ans=["10 9 8"],
  hint="Berhenti apabila n < 8.",
  fu=[F("""Dalam nested loop, break hanya keluar dari loop **dalam**.""",
        "Dalam nested loops, break keluar dari loop mana?",
        kw=["inner|dalam|innermost|terdalam"],
        ans="Hanya loop dalam (inner).",
        hint="Bukan kedua-duanya."),
      F("""
        ```
        int c = 0;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 5; j++) {
                if (j == 2) break;
                c++;
            }
        cout << c;
        ```""",
        "Apakah output?",
        ans=["6"],
        hint="Setiap i, j = 0 dan 1 sahaja.")],
  mcq=M("`break` dalam inner loop akan…",
        "Keluar dari inner loop sahaja", "Keluar dari semua loop", "Tamatkan program", "Langkau satu ulangan"))

S("cs23", T, H + "Jump statements · continue",
  """
  **`continue`** langkau baki pusingan ini (skips the rest of this round).
  - Dalam **for** loop: pergi ke **update**.
  - Dalam **while / do-while**: pergi ke **condition**.

  ```
  for (n = 10; n > 0; n--) {
      if (n % 2 == 1) continue;
      cout << n << " ";
  }
  ```
  Hanya nombor genap dicetak: **10 8 6 4 2**.
  """,
  "Apakah output loop continue di atas?",
  ans=["10 8 6 4 2"],
  hint="Nombor ganjil dilangkau.",
  fu=[F("""Dalam for, continue pergi ke update (`n--`). Dalam while/do-while, ia pergi ke condition.""",
        "Dalam for loop, continue melompat ke bahagian mana?",
        ans=["update", "the update", "kemas kini"],
        hint="n--."),
      F("""Dalam while, continue melompat terus ke condition.""",
        "Dalam while loop, continue melompat ke bahagian mana?",
        ans=["condition", "syarat", "the condition"],
        hint="Bukan update.")],
  mcq=M("`continue` dalam loop…",
        "Langkau baki pusingan dan teruskan pusingan seterusnya", "Keluar dari loop", "Tamatkan function", "Ulang pusingan semasa dari awal tanpa uji syarat"))

S("cs24", T, H + "Jump statements · return and goto",
  """
  - **`return`**: tamatkan **seluruh function**.
  - **`goto`**: lompat ke label. **Elakkan**, kerana ia menjadikan kod **tidak berstruktur** (unstructured).
  """,
  "Mengapa goto perlu dielakkan?",
  kw=["unstructured|tidak berstruktur|tak berstruktur|struktur|structure|messy|sukar"],
  ans="Kerana ia menjadikan kod tidak berstruktur.",
  hint="Lawan 'structured programming'.",
  fu=[F("""`return` menamatkan seluruh function, bukan hanya loop.""",
        "Jump statement manakah menamatkan seluruh function?",
        ans=["return"],
        hint="R…")],
  mcq=M("Jump statement yang melompat ke label dan perlu dielakkan ialah…",
        "goto", "break", "continue", "return"))

S("cs25", T, H + "TRAP: continue before the update in a while loop", trap=True,
  text="""
  ⚠ **TRAP**

  Dalam **while** loop, jika `continue` datang **sebelum update** (`n = n - 1`), update **tidak pernah dijalankan**. Loop mencetak **9 9 9 …** selama-lamanya.

  ```
  int n = 9;
  while (n > 0) {
      cout << n << " ";
      if (n % 2 == 1) continue;   // n ganjil: lompat ke condition
      n = n - 1;                  // tidak pernah sampai
  }
  ```
  """,
  question="Mengapa loop di atas mencetak 9 9 9 … selama-lamanya?",
  kw=["continue", "before|sebelum|skip|langkau",
      "update|n = n - 1|n-1|tolak|kurang|never|tidak pernah|tak pernah"],
  ans="Kerana continue datang sebelum update, jadi n = n - 1 tidak pernah dijalankan dan n kekal 9.",
  hint="Adakah n pernah berubah?",
  fu=[F("""Penyelesaian: letak update **sebelum** continue, atau guna for loop (continue dalam for pergi ke update).""",
        "Di manakah update patut diletak untuk mengelak trap ini?",
        kw=["before|sebelum|atas|above|first|dahulu"],
        ans="Sebelum continue.",
        hint="Susunan baris.")],
  mcq=M("Dalam while loop, continue sebelum update menyebabkan…",
        "Infinite loop", "Loop tamat awal", "Syntax error", "Update dijalankan dua kali"))

S("cs26", T, H + "Nested loops",
  """
  **Inner loop** menjalankan **semua pusingannya bagi setiap pusingan outer loop**.

  Jumlah inner runs = **outer × inner**. Contoh: loop 3 × 3 → badan dijalankan **9 kali**.
  """,
  "Berapa kali badan nested loop 3 × 3 dijalankan?",
  ans=["9", "sembilan", "9 kali"],
  hint="outer × inner.",
  fu=[F("""Outer 4 kali, inner 2 kali.""",
        "Berapa kali badan inner dijalankan?",
        ans=["8"],
        hint="4 × 2."),
      F("""
        ```
        for (int i = 1; i <= 2; i++)
            for (int j = 1; j <= 3; j++)
                cout << i << j << " ";
        ```""",
        "Apakah output?",
        ans=["11 12 13 21 22 23"],
        hint="j berjalan penuh bagi setiap i.")],
  mcq=M("Jumlah larian inner loop dalam nested loop ialah…",
        "outer × inner", "outer + inner", "inner sahaja", "outer sahaja"))
