from helpers import S, F, M

T = "func"

S("fn01", T, "5.1 What is a function",
  """
  **Function**: blok kod bernama yang melaksanakan satu tugas tertentu.

  Dua jenis:
  - **Predefined (library) functions**: disediakan C++, contoh `sqrt`, `pow`, `strlen`.
  - **User-defined functions**: ditulis oleh pengaturcara.

  Kelebihan: **modularity** (divide and conquer / decomposition), **reusability** (guna semula), mudah **debug** dan diselenggara.
  """,
  "Nyatakan dua jenis function dan dua kelebihan menggunakan function.",
  kw=["predefined|library|pustaka|terbina|built-in",
      "user-defined|user defined|pengguna|sendiri|programmer",
      "reuse|guna semula|reusability|modular|modularity|debug|divide|pecah|mudah"],
  ans="Predefined (library) dan user-defined. Kelebihan: reusability, modularity, mudah debug.",
  hint="Satu disediakan C++, satu anda tulis.",
  fu=[F("""`sqrt(16)` ialah predefined function daripada `<cmath>`.""",
        "`sqrt` ialah predefined atau user-defined function?",
        ans=["predefined", "library", "predefined function", "library function"],
        hint="Siapa yang tulis sqrt?")],
  mcq=M("Kelebihan utama memecahkan program kepada function ialah…",
        "Kod boleh diguna semula dan mudah di-debug", "Program sentiasa lebih laju",
        "Tidak perlu main()", "Tidak perlu isytihar pemboleh ubah"))

S("fn02", T, "5.2 Library header files (slide 6)",
  """
  Header untuk predefined functions:

  | Header | Contoh function |
  |---|---|
  | `<iostream>` | `cin`, `cout` |
  | `<cmath>` | `sqrt`, `pow`, `fabs`, `ceil`, `floor`, `acos` |
  | `<cstdlib>` | `rand`, `srand`, `atoi`, `atof`, `abs` |
  | `<cctype>` | `toupper`, `tolower`, `isdigit`, `isalpha` |
  | `<cstring>` | `strlen`, `strcpy`, `strcat`, `strcmp` |
  | `<ctime>` | `time` |

  Rujuk **cppreference.com**: bahagian "Defined in header", signature, Return value, Notes.
  """,
  "Header apakah diperlukan untuk sqrt dan pow?",
  ans=["<cmath>", "cmath", "#include <cmath>"],
  hint="c + math.",
  fu=[F("""`strcmp`, `strcpy`, `strlen` dalam header yang sama.""",
        "Header untuk strlen?",
        ans=["<cstring>", "cstring", "#include <cstring>"],
        hint="c + string (bukan <string>)."),
      F("""`rand`, `srand` dan `atoi` dalam general-purpose library.""",
        "Header untuk rand?",
        ans=["<cstdlib>", "cstdlib", "#include <cstdlib>"],
        hint="c + std + lib."),
      F("""`toupper`, `isdigit` ialah character functions.""",
        "Header untuk toupper?",
        ans=["<cctype>", "cctype", "#include <cctype>"],
        hint="c + c + type.")],
  mcq=M("Header untuk isdigit() ialah…",
        "<cctype>", "<cmath>", "<cstring>", "<iostream>"))

S("fn03", T, "5.3 Math functions in <cmath> (slides 8–13)", trap=True,
  text="""
  | Function | Maksud | Contoh |
  |---|---|---|
  | `sqrt(x)` | punca kuasa dua | `sqrt(16)` = 4 |
  | `pow(x, y)` | x kuasa y | `pow(2, 3)` = 8 |
  | `fabs(x)` | nilai mutlak (double) | `fabs(-3.5)` = 3.5 |
  | `ceil(x)` | bundar ke atas | `ceil(2.1)` = 3 |
  | `floor(x)` | bundar ke bawah | `floor(2.9)` = 2 |

  Semua memulangkan **double**.

  **TRAP**: `floor(-2.5)` = **-3** (ke bawah = lebih negatif), bukan -2.
  """,
  question="Apakah nilai floor(-2.5)?",
  ans=["-3", "-3.0"],
  hint="'Bawah' pada garis nombor.",
  fu=[F("""`cout << pow(2, 3) << " " << sqrt(16) << " " << ceil(2.1);`""",
        "Apakah output?",
        ans=["8 4 3"],
        hint="cout tidak cetak .0 untuk nombor bulat."),
      F("""Jarak antara (1, 2) dan (4, 6): `sqrt(pow(4 - 1, 2) + pow(6 - 2, 2))`.""",
        "Apakah jaraknya?",
        ans=["5"],
        hint="sqrt(9 + 16).")],
  mcq=M("`ceil(4.01)` memulangkan…",
        "5", "4", "4.01", "4.1"))

S("fn04", T, "5.3 Getting pi with acos(-1.0) (Lab 6 B2)",
  """
  `M_PI` **bukan** standard C++, ada compiler yang menolaknya. Cara mudah alih:

  ```
  const double PI = acos(-1.0);
  double area = PI * r * r;     // r = 3 → 28.2743
  ```
  """,
  "Mengapa kita guna acos(-1.0) dan bukan M_PI?",
  kw=["standard|piawai|not standard|bukan standard",
      "compiler|portable|mudah alih|reject|tolak|semua"],
  ans="M_PI bukan standard C++ dan sesetengah compiler menolaknya; acos(-1.0) standard dan memberi nilai pi.",
  hint="Isu standard dan compiler.",
  fu=[F("""Luas bulatan dengan r = 3 menggunakan PI = acos(-1.0).""",
        "Apakah output cout bagi luas?",
        ans=["28.2743"],
        hint="π × 9, 6 digit bererti.")],
  mcq=M("`acos(-1.0)` memulangkan nilai…",
        "π (3.14159…)", "-1", "0", "1"))

S("fn05", T, "5.4 Random numbers: rand and srand (slide 14)", trap=True,
  text="""
  - `rand()` memulangkan integer pseudo-random 0 hingga `RAND_MAX`.
  - `rand() % 6 + 1` → julat **1 hingga 6** (dadu).
  - `srand(seed)` menetapkan seed. Seed sama → jujukan sama (berguna untuk testing, contoh seed 42).
  - `srand(time(0))` → jujukan berbeza setiap kali (perlu `<ctime>`).

  **TRAP**: panggil `srand` **sekali sahaja** di awal program, bukan dalam loop.
  """,
  question="Apakah julat nilai `rand() % 6 + 1`?",
  ans=["1 hingga 6", "1 to 6", "1-6", "1 - 6", "1 sampai 6"],
  hint="% 6 memberi 0..5.",
  fu=[F("""`srand(42)` dua kali run → jujukan rand() sama.""",
        "Mengapa seed tetap (contoh 42) berguna?",
        kw=["same|sama|ulang|repeat|reproducible|tetap",
            "test|testing|uji|semak|debug"],
        ans="Jujukan nombor rawak sama setiap kali, jadi mudah untuk testing.",
        hint="Lab 6 B4 mode 1."),
      F("""Untuk julat 10 hingga 20: `rand() % 11 + 10`.""",
        "Tulis ungkapan untuk nombor rawak 1 hingga 100.",
        ans=["rand() % 100 + 1", "rand()%100+1", "1 + rand() % 100"],
        hint="% bilangan nilai, + nilai minimum.")],
  mcq=M("Di manakah srand(time(0)) patut dipanggil?",
        "Sekali di awal main()", "Dalam setiap ulangan loop", "Sebelum setiap rand()", "Selepas return 0"))

S("fn06", T, "5.5 Character functions in <cctype> (slides 15–23)", trap=True,
  text="""
  Ujian (memulangkan bukan-sifar jika benar, 0 jika palsu):
  `isdigit`, `isalpha`, `isalnum`, `isupper`, `islower`, `ispunct`, `isspace`

  Penukaran: `toupper(c)`, `tolower(c)`

  **TRAP**: `toupper` memulangkan **int**.
  ```
  cout << toupper('a');         // 65
  cout << char(toupper('a'));   // A
  ```
  """,
  question="Apakah output `cout << toupper('a');`?",
  ans=["65"],
  hint="Jenis pulangan toupper ialah int.",
  fu=[F("""Untuk cetak huruf, cast ke char.""",
        "Apakah output `cout << char(toupper('a'));`?",
        ans=["A"],
        hint="Cast."),
      F("""`isdigit('7')` bukan-sifar (true), `isalpha('7')` = 0.""",
        "Function apakah menguji sama ada aksara ialah tanda baca?",
        ans=["ispunct", "ispunct()"],
        hint="is + punct.")],
  mcq=M("`isupper('a')` memulangkan…",
        "0 (false)", "Bukan sifar (true)", "'A'", "65"))

S("fn07", T, "5.6 C-string functions in <cstring> (slides 24–33)", trap=True,
  text="""
  - `strlen(s)`: panjang, **tidak termasuk** `'\\0'`. `strlen("Hello")` = 5.
  - `strcpy(dest, src)`: salin src ke dest.
  - `strcat(dest, src)`: sambung src di hujung dest.
  - `strcmp(a, b)`: **0 jika sama**, < 0 jika a sebelum b, > 0 jika a selepas b.

  **TRAP**:
  - `if (strcmp(a, b))` bermaksud **TIDAK sama** (bukan-sifar = true).
  - Tidak boleh `dest = src;` atau `a == b` untuk C-string.
  """,
  question="Apakah nilai pulangan strcmp jika dua string sama?",
  ans=["0", "sifar", "zero"],
  hint="Bukan 1 / true.",
  fu=[F("""
        ```
        char s[20];
        strcpy(s, "Hi");
        strcat(s, " there");
        cout << s << " " << strlen(s);
        ```""",
        "Apakah output?",
        ans=["Hi there 8"],
        hint="Kira termasuk ruang."),
      F("""Palindrome (Lab 6 B5): salin dengan strcpy, toupper, terbalikkan, banding dengan strcmp.""",
        "Tulis syarat if yang benar apabila C-string a dan b SAMA.",
        ans=["strcmp(a, b) == 0", "strcmp(a,b)==0", "!strcmp(a, b)", "if (strcmp(a, b) == 0)"],
        hint="strcmp(...) == ?")],
  mcq=M("Cara yang BETUL untuk menyalin C-string src ke dest ialah…",
        "strcpy(dest, src);", "dest = src;", "strcpy(src, dest);", "dest == src;"))

S("fn08", T, "5.7 atoi, atol, atof (slides 34–36)", trap=True,
  text="""
  Tukar string → nombor (`<cstdlib>`):
  - `atoi` → int, `atol` → long, `atof` → double.

  | Input | atoi | atof |
  |---|---|---|
  | "57" | 57 | 57 |
  | "12abc" | 12 | 12 |
  | "3.9" | **3** | 3.9 |
  | "-8" | -8 | -8 |
  | "abc" | **0** | 0 |

  **TRAP**: `atoi("abc")` dan `atoi("0")` sama-sama 0, jadi tidak boleh bezakan input tidak sah dengan sifar. Slide 35: hasil undefined untuk teks bukan digit.
  """,
  question="Apakah nilai atoi(\"12abc\")?",
  ans=["12"],
  hint="Berhenti pada aksara bukan digit.",
  fu=[F("""atoi hanya baca bahagian integer.""",
        "Apakah nilai atoi(\"3.9\")?",
        ans=["3"],
        hint="Berhenti pada titik."),
      F("""`atoi("abc")` = 0, `atoi("0")` = 0.""",
        "Mengapa atoi tidak boleh membezakan \"abc\" dan \"0\"?",
        kw=["0|sifar|zero", "same|sama|both|kedua-dua|keduanya"],
        ans="Kedua-duanya memulangkan 0, jadi tiada cara tahu input itu tidak sah.",
        hint="Bandingkan nilai pulangan.")],
  mcq=M("`atof(\"2.5kg\")` memulangkan…",
        "2.5", "2", "0", "Ralat"))

S("fn09", T, "5.8 User-defined function: definition, prototype, call",
  """
  ```
  #include <iostream>
  using namespace std;

  int square(int n);            // prototype (declaration), ada ;

  int main() {
      cout << square(3);        // function call → 9
      return 0;
  }

  int square(int n)             // header (tiada ;)
  {                             // body
      return n * n;
  }
  ```
  - **Function header**: return type + nama + parameter list.
  - **Prototype** diperlukan jika definition diletak **selepas** main. Nama parameter dalam prototype adalah pilihan: `int square(int);`
  """,
  "Bilakah function prototype diperlukan?",
  kw=["after|selepas|bawah|below|later", "main|dipanggil|call|digunakan|used|before|sebelum"],
  ans="Apabila definition function diletak selepas main (atau selepas tempat ia dipanggil).",
  hint="Compiler membaca dari atas ke bawah.",
  fu=[F("""Tanpa prototype dan definition selepas main → `'square' was not declared in this scope`.""",
        "Tulis prototype untuk function `double area(double r)`.",
        ans=["double area(double r);", "double area(double);"],
        hint="Header + ;"),
      F("""Bahagian function header: return type, nama, parameter list.""",
        "Dalam `int square(int n)`, apakah return type?",
        ans=["int"],
        hint="Perkataan pertama.")],
  mcq=M("Yang manakah prototype yang SAH?",
        "int max(int, int);", "int max(int a, b);", "max(int a, int b);", "int max(int a, int b)"))

S("fn10", T, "5.9 Parameters vs arguments",
  """
  - **Parameters (formal parameters)**: pemboleh ubah dalam header function, `int add(int a, int b)`.
  - **Arguments (actual parameters)**: nilai yang dihantar semasa panggilan, `add(2, 3)`.

  Bilangan, **turutan** dan **jenis** argument mesti sepadan dengan parameter.
  """,
  "Apakah beza parameter dan argument?",
  kw=["parameter|formal", "header|definition|definisi|function|takrif|declaration",
      "argument|actual|sebenar", "call|panggil|panggilan|hantar|pass|sent"],
  ans="Parameter (formal) ialah pemboleh ubah dalam header function; argument (actual) ialah nilai yang dihantar semasa panggilan.",
  hint="Satu di tempat takrif, satu di tempat panggil.",
  fu=[F("""`int add(int a, int b = 5);`, `add(2, 3)`.""",
        "Dalam `add(2, 3)`, 2 dan 3 dipanggil apa?",
        ans=["arguments", "argument", "actual parameters", "actual arguments", "argumen"],
        hint="Nilai sebenar.")],
  mcq=M("Dalam `double avg(int x, int y)`, x dan y ialah…",
        "Formal parameters", "Actual arguments", "Global variables", "Return values"))

S("fn11", T, "5.10 return and void functions",
  """
  - **Value-returning function**: ada return type (int, double…) dan mesti `return value;`.
  - **void function**: tidak memulangkan nilai; `return;` (pilihan) untuk keluar awal.
  - `return` **menamatkan** function serta-merta.

  ```
  int sq(int n) { return n * n; }
  cout << sq(3) + sq(2);     // 13
  ```
  **TRAP**: `cout << printLine();` jika `printLine` ialah void → ralat (tiada nilai untuk dicetak).
  """,
  "Apakah beza void function dan value-returning function?",
  kw=["void", "no value|tiada nilai|tidak pulangkan|tak pulangkan|does not return|tidak memulangkan|no return",
      "return|pulang|memulangkan|returns"],
  ans="void function tidak memulangkan nilai; value-returning function memulangkan satu nilai dengan return.",
  hint="Fokus pada nilai pulangan.",
  fu=[F("""`int sq(int n) { return n * n; }`""",
        "Apakah output `cout << sq(3) + sq(2);`?",
        ans=["13"],
        hint="9 + 4."),
      F("""
        ```
        int check(int x) {
            if (x > 0) return 1;
            return 0;
            cout << "end";
        }
        ```""",
        "Adakah \"end\" pernah dicetak? (ya / tidak)",
        ans=["tidak", "no", "tak", "tidak pernah"],
        hint="return menamatkan function.")],
  mcq=M("Berapa nilai maksimum yang boleh dipulangkan oleh satu return statement?",
        "Satu", "Dua", "Tiada had", "Sifar"))

S("fn12", T, "5.10 Trap: integer division inside a function", trap=True,
  text="""
  **TRAP**: return type double tidak menyelamatkan integer division yang sudah berlaku.

  ```
  double avg(int a, int b) {
      return (a + b) / 2;     // int / int = 3
  }
  cout << avg(3, 4);          // 3, bukan 3.5
  ```
  Betulkan: `return (a + b) / 2.0;`
  """,
  question="Apakah output `cout << avg(3, 4);`?",
  ans=["3"],
  hint="(3 + 4) / 2 dengan int.",
  fu=[F("""Tukar 2 kepada 2.0.""",
        "Tulis return statement yang betul.",
        ans=["return (a + b) / 2.0;", "return (a+b)/2.0;", "return static_cast<double>(a + b) / 2;"],
        hint="Salah satu operand mesti double.")],
  mcq=M("`double half(int n) { return n / 2; }` → half(5) ialah…",
        "2", "2.5", "3", "Ralat"))

S("fn13", T, "5.11 Pass by value",
  """
  **Pass by value**: function menerima **salinan** (copy). Perubahan dalam function **tidak** menjejaskan pemboleh ubah asal.

  ```
  void byVal(int x) { x = x + 10; }
  int a = 5;
  byVal(a);
  cout << a;     // 5
  ```
  """,
  "Apakah maksud pass by value?",
  kw=["copy|salinan|salin|copies",
      "original|asal|tidak berubah|not change|unchanged|kekal|tak berubah|tidak menjejaskan"],
  ans="Function menerima salinan nilai; pemboleh ubah asal tidak berubah.",
  hint="Fotostat dokumen.",
  fu=[F("""Kod byVal di atas.""",
        "Apakah output?",
        ans=["5"],
        hint="Hanya salinan ditambah."),
      F("""
        ```
        void swapV(int a, int b) { int t = a; a = b; b = t; }
        int a = 1, b = 2;
        swapV(a, b);
        cout << a << b;
        ```""",
        "Apakah output?",
        ans=["12"],
        hint="Pass by value tidak menukar yang asal.")],
  mcq=M("Dalam pass by value, function bekerja dengan…",
        "Salinan argument", "Alamat argument", "Pemboleh ubah global", "Pemalar sahaja"))

S("fn14", T, "5.11 Pass by reference (&)",
  """
  **Pass by reference**: parameter dengan `&` ialah **alias** kepada pemboleh ubah asal. Perubahan dalam function **mengubah** yang asal.

  ```
  void byRef(int &x) { x = x + 10; }
  int a = 5;
  byRef(a);
  cout << a;     // 15
  ```
  Gunakan apabila function perlu ubah argument atau "pulangkan" lebih daripada satu nilai (contoh `swap`). Argument mesti pemboleh ubah, bukan literal (`byRef(5)` ralat).
  """,
  "Bilakah kita perlu menggunakan pass by reference?",
  kw=["change|ubah|modify|tukar|mengubah",
      "original|asal|caller|pemanggil|more than one|lebih daripada satu|banyak nilai|multiple"],
  ans="Apabila function perlu mengubah pemboleh ubah asal atau memulangkan lebih daripada satu nilai.",
  hint="Fikir swap.",
  fu=[F("""Kod byRef di atas.""",
        "Apakah output?",
        ans=["15"],
        hint="x ialah alias kepada a."),
      F("""
        ```
        void swapR(int &a, int &b) { int t = a; a = b; b = t; }
        int a = 1, b = 2;
        swapR(a, b);
        cout << a << b;
        ```""",
        "Apakah output?",
        ans=["21"],
        hint="Kali ini nilai asal ditukar."),
      F("""Cari kesilapan: `void byRef(int &x);` dipanggil sebagai `byRef(5);`""",
        "Mengapa ini ralat?",
        kw=["literal|constant|pemalar|nilai tetap|5",
            "variable|pemboleh ubah|lvalue|reference|rujukan|alias"],
        ans="Reference parameter memerlukan pemboleh ubah (lvalue); literal 5 tiada lokasi untuk dirujuk.",
        hint="Apa yang boleh diberi alias?")],
  mcq=M("Simbol yang menjadikan parameter sebagai reference ialah…",
        "&", "*", "#", "%"))

S("fn15", T, "5.12 Scope: local and global variables",
  """
  - **Local variable**: diisytihar dalam function/blok; hanya wujud di situ.
  - **Global variable**: diisytihar di luar semua function; boleh diakses di mana-mana.
  - Local dengan nama sama akan **menyembunyikan (shadow)** global.

  ```
  int x = 10;                     // global
  void show() { int x = 3; cout << x; }
  int main() { show(); cout << " " << x; }
  ```
  Output: `3 10`. Elakkan global variable kerana sukar dijejak.
  """,
  "Apakah beza local dan global variable?",
  kw=["local|tempatan", "inside|dalam|function|blok|block",
      "global|sejagat", "outside|luar|all|semua|mana-mana|anywhere|everywhere"],
  ans="Local diisytihar dalam function/blok dan hanya wujud di situ; global diisytihar di luar semua function dan boleh diakses di mana-mana.",
  hint="Di mana ia diisytihar?",
  fu=[F("""Kod show() di atas.""",
        "Apakah output?",
        ans=["3 10"],
        hint="Local x dalam show, global x dalam main."),
      F("""`for (int i = 0; i < 3; i++) {}  cout << i;`""",
        "Adakah ini compile? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Scope i hanya dalam for.")],
  mcq=M("Local variable yang sama nama dengan global akan…",
        "Menyembunyikan global dalam scope-nya", "Menukar nilai global", "Ralat compile", "Dikongsi dengan global"))

S("fn16", T, "5.13 static local variables",
  """
  `static` local variable **mengekalkan nilainya** antara panggilan function dan diinisialisasi **sekali sahaja**.

  ```
  void counter() {
      static int c = 0;
      c++;
      cout << c << " ";
  }
  counter(); counter(); counter();   // 1 2 3
  ```
  Tanpa `static`: `1 1 1`.
  """,
  "Apakah keistimewaan static local variable?",
  kw=["keep|kekal|retain|simpan|maintain|mengekalkan|ingat",
      "value|nilai", "between|antara|calls|panggilan|setiap kali"],
  ans="Ia mengekalkan nilai antara panggilan function dan hanya diinisialisasi sekali.",
  hint="Ia tidak 'lupa'.",
  fu=[F("""counter() dipanggil 3 kali.""",
        "Apakah output?",
        ans=["1 2 3"],
        hint="c tidak direset."),
      F("""Buang perkataan static.""",
        "Apakah output sekarang?",
        ans=["1 1 1"],
        hint="c dicipta semula setiap panggilan.")],
  mcq=M("Berapa kali `static int c = 0;` diinisialisasi jika function dipanggil 5 kali?",
        "Sekali", "5 kali", "Tidak pernah", "Bergantung pada compiler"))

S("fn17", T, "5.14 Default arguments",
  """
  **Default argument**: nilai lalai jika argument tidak diberi. Mesti dari **kanan ke kiri**.

  ```
  int add(int a, int b = 5) { return a + b; }
  add(2);      // 7
  add(2, 3);   // 5
  ```
  **Tidak sah**: `int f(int a = 1, int b);` (default di kiri tanpa di kanan).
  """,
  "Apakah output add(2) dan add(2, 3)? (tulis: x y)",
  ans=["7 5"],
  hint="b = 5 jika tidak diberi.",
  fu=[F("""Default mesti di sebelah kanan.""",
        "Adakah `int f(int a = 1, int b);` sah? (ya / tidak)",
        ans=["tidak", "no", "tak", "tidak sah"],
        hint="Kanan ke kiri.")],
  mcq=M("Prototype manakah SAH?",
        "void p(int a, int b = 2, int c = 3);", "void p(int a = 1, int b, int c);",
        "void p(int a = 1, int b, int c = 3);", "void p(int a, int b = 2, int c);"))

S("fn18", T, "5.15 Function overloading",
  """
  **Overloading**: beberapa function dengan **nama sama** tetapi **parameter list berbeza** (bilangan atau jenis).

  ```
  int    twice(int n)    { return n * 2; }
  double twice(double n) { return n * 2.5; }
  twice(4);     // 8   (versi int)
  twice(4.0);   // 10  (versi double)
  ```
  **TRAP**: berbeza **return type sahaja** TIDAK cukup untuk overload.
  """,
  "Apakah syarat untuk function overloading?",
  kw=["same name|nama sama|sama nama", "parameter|argument|list|senarai",
      "different|berbeza|lain|number|jenis|type|bilangan"],
  ans="Nama sama tetapi parameter list berbeza (bilangan atau jenis); return type sahaja tidak cukup.",
  hint="Apa yang mesti sama dan apa yang mesti beza?",
  fu=[F("""Kod twice di atas.""",
        "Apakah output `cout << twice(4) << \" \" << twice(4.0);`?",
        ans=["8 10"],
        hint="Versi dipilih ikut jenis argument."),
      F("""`int f(int x);` dan `double f(int x);`""",
        "Adakah ini overloading yang sah? (ya / tidak)",
        ans=["tidak", "no", "tak", "tidak sah"],
        hint="Hanya return type berbeza.")],
  mcq=M("Yang manakah overload yang SAH bagi `int area(int s);`?",
        "int area(int l, int w);", "double area(int s);", "int area(int x);", "void area(int s);"))

S("fn19", T, "5.16 Invalid function headers", trap=True,
  text="""
  **Invalid headers** yang selalu keluar dalam soalan "cari kesilapan":

  | Header | Masalah |
  |---|---|
  | `int sum(int a, b)` | setiap parameter perlu jenis: `int a, int b` |
  | `void print(int x);` `{ ... }` | `;` selepas header definition |
  | `int f(int a, int a)` | nama parameter berulang |
  | `sum(int a, int b)` | tiada return type |
  | `void f(int a = 1, int b)` | default argument tidak di kanan |
  | `int f(int a) { }` | tiada return value (warning/undefined) |
  """,
  question="Apakah kesilapan dalam header `int sum(int a, b)`?",
  kw=["type|jenis|int", "b|setiap|each|every|parameter|kedua"],
  ans="Parameter b tiada jenis data; setiap parameter mesti ada jenis: int sum(int a, int b).",
  hint="Bandingkan a dan b.",
  fu=[F("""
        ```
        void print(int x);
        {
            cout << x;
        }
        ```""",
        "Apakah kesilapannya?",
        kw=[";|semicolon|titik koma|koma bertitik", "header|definition|selepas|after|hujung"],
        ans="Ada ; selepas header definition, jadi { } terpisah daripada function.",
        hint="Hujung baris pertama."),
      F("""`sum(int a, int b) { return a + b; }`""",
        "Apakah yang tertinggal?",
        ans=["return type", "int", "jenis pulangan", "return type int"],
        hint="Sebelum nama function.")],
  mcq=M("Header definition manakah yang SAH?",
        "double avg(int a, int b)", "double avg(int a, b)", "avg(int a, int b)", "double avg(int a, int a)"))

S("fn20", T, "5.17 Common function call errors",
  """
  Ralat biasa semasa memanggil function:

  - Function dipanggil sebelum diisytihar (tiada prototype) → `'f' was not declared in this scope`.
  - Bilangan argument salah → `too few/too many arguments to function`.
  - Panggil dengan jenis pulangan disertakan: `int sq(3);` ✗ → betul `sq(3);`
  - Hasil value-returning function tidak digunakan: `sq(3);` sah tetapi nilai dibuang.
  - Guna void function dalam ungkapan: `int x = printLine();` ✗
  """,
  "Apakah mesej ralat jika function dipanggil dengan bilangan argument yang kurang?",
  ans=["too few arguments to function", "too few arguments", "too few"],
  hint="too … arguments.",
  fu=[F("""`int sq(int n);` dan panggilan `cout << sq(2, 3);`""",
        "Apakah mesej ralat?",
        ans=["too many arguments to function", "too many arguments", "too many"],
        hint="Terlebih argument."),
      F("""Panggilan salah: `int sq(3);` dalam main.""",
        "Tulis panggilan yang betul untuk cetak sq(3).",
        ans=["cout << sq(3);", "cout<<sq(3);"],
        hint="Jangan tulis jenis semasa panggil.")],
  mcq=M("Panggilan manakah BETUL untuk `double area(double r);`?",
        "a = area(2.5);", "a = double area(2.5);", "a = area(double 2.5);", "area(double r);"))

# ---------------------------------------------------------------- BAB 6 Cheat sheet
T = "cheat"

S("ch01", T, "6.1 Exam-day checklist: read the question (IPO)",
  """
  **Checklist #1**: sebelum menulis apa-apa, kenal pasti **Input, Process, Output** daripada soalan. Gariskan perkataan seperti "read", "calculate", "display". Kemudian baru lukis flowchart / tulis kod.
  """,
  "Apakah langkah pertama dalam checklist peperiksaan apabila membaca soalan program?",
  kw=["input", "process|proses", "output", "identify|kenal pasti|kenalpasti|cari"],
  ans="Kenal pasti Input, Process dan Output (IPO).",
  hint="Tiga huruf.",
  fu=[F("""Soalan: 'Read the radius and display the area.'""",
        "Apakah input bagi soalan ini?",
        ans=["radius", "jejari", "the radius"],
        hint="Perkataan selepas 'read'.")],
  mcq=M("'Calculate the average of three marks' ialah bahagian…",
        "Process", "Input", "Output", "Terminal"))

S("ch02", T, "6.2 Exam-day checklist: tracing code",
  """
  **Checklist #2**: untuk soalan trace code:

  1. Lukis **trace table**: satu lajur setiap pemboleh ubah + lajur output.
  2. Tandakan **integer division** (`int / int`) dan **%**.
  3. Teliti **prefix vs postfix** (`++x` vs `x++`).
  4. Tulis output **tepat**: ruang, baris baru (`endl`), 6 digit bererti.
  """,
  "Senaraikan dua perkara yang mesti diperhatikan semasa trace code.",
  kw=["integer division|int / int|pembahagian integer|/|%|modulus",
      "prefix|postfix|++|--|increment",
      "space|ruang|endl|baris|output tepat|format|table|jadual"],
  ans="Integer division / %, prefix vs postfix, format output tepat (ruang/endl), guna trace table.",
  hint="Apa yang selalu menipu dalam Bab 3?",
  fu=[F("""
        ```
        int a = 5, b = 2;
        double c = a / b;
        cout << c;
        ```""",
        "Apakah output?",
        ans=["2"],
        hint="a / b dikira sebagai int dahulu.")],
  mcq=M("`int a = 9; cout << a / 2 << a % 2;` mencetak…",
        "41", "4.51", "4 1", "4.5"))

S("ch03", T, "6.3 Exam-day checklist: semicolons", trap=True,
  text="""
  **Checklist #3: semicolon**

  Ada `;`: setiap statement, prototype, `do { } while (...);`, `using namespace std;`

  **TIADA** `;`: `#include`, `#define`, `if (...)`, `for (...)`, `while (...)` (sebelum badan), function header definition, selepas `}` function.
  """,
  question="Namakan TIGA tempat di mana ; TIDAK boleh diletakkan.",
  kw=["#include|include|#define|define|preprocessor",
      "if|for|while|loop",
      "header|function|definition|main"],
  ans="Selepas #include/#define, selepas if(...)/for(...)/while(...) sebelum badan, dan selepas function header definition.",
  hint="Preprocessor, struktur kawalan, function.",
  fu=[F("""do...while ialah pengecualian: ia mesti ada `;` di hujung.""",
        "Adakah `do { x++; } while (x < 5)` tanpa ; betul? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="do...while berakhir dengan ;")],
  mcq=M("Baris manakah PERLU ada ;?",
        "int sq(int n);   (prototype)", "#include <cmath>", "for (int i = 0; i < 3; i++)", "int sq(int n)   (definition header)"))

S("ch04", T, "6.4 Exam-day checklist: control structure traps", trap=True,
  text="""
  **Checklist #4**: semak setiap if dan switch:

  - `=` vs `==` dalam syarat.
  - `break` dalam setiap case (elak fall-through).
  - `{ }` jika lebih daripada satu statement.
  - else milik if terdekat.
  - Loop: nilai mula, `<` vs `<=`, update ada dan ke arah betul.
  """,
  question="Senaraikan tiga trap yang perlu disemak dalam if/switch/loop.",
  kw=["=|==|assignment|comparison|perbandingan",
   "break|fall-through|fall through|switch",
   "brace|braces|{}|{ }|kurungan|<=|off-by-one|update|infinite|else"],
  ans="= vs ==, break dalam switch, braces { }, dangling else, off-by-one dan update loop.",
  hint="Bab 4 Common traps.",
  fu=[F("""
        ```
        int n = 3;
        switch (n) {
            case 3: cout << "three ";
            case 4: cout << "four ";
            default: cout << "other";
        }
        ```""",
        "Apakah output?",
        ans=["three four other"],
        hint="Tiada break langsung.")],
  mcq=M("`if (x == 5); x++;` dengan x = 1. Nilai x selepas itu ialah…",
        "2", "1", "6", "5"))

S("ch05", T, "6.5 Exam-day checklist: functions",
  """
  **Checklist #5: functions**

  - Prototype sebelum `main` jika definition di bawah.
  - Jenis, bilangan dan turutan argument sepadan dengan parameter.
  - Value-returning function **mesti** ada `return` di setiap laluan.
  - Guna `&` jika function perlu ubah pemboleh ubah asal.
  - Header yang betul untuk library function (`<cmath>`, `<cstring>`, …).
  """,
  "Bilakah kita letak & pada parameter?",
  kw=["change|ubah|modify|tukar", "original|asal|caller|reference|rujukan"],
  ans="Apabila function perlu mengubah pemboleh ubah asal (pass by reference).",
  hint="Pass by …",
  fu=[F("""
        ```
        void addOne(int n) { n++; }
        int main() { int k = 9; addOne(k); cout << k; }
        ```""",
        "Apakah output?",
        ans=["9"],
        hint="Pass by value.")],
  mcq=M("Function yang perlu mengembalikan DUA hasil (min dan max) paling sesuai guna…",
        "Dua reference parameter", "Dua return statement berturut-turut", "Satu return value", "Global variable sahaja"))

S("ch06", T, "6.6 Exam-day checklist: flowchart symbols recap",
  """
  **Checklist #6: simbol flowchart**

  | Simbol | Bentuk |
  |---|---|
  | Start/End | Oval |
  | Input/Output | Parallelogram |
  | Process | Rectangle |
  | Decision | Diamond (Yes/No) |
  | Predefined process (function) | Rectangle dengan garis tepi berganda |
  | Connector | Bulatan kecil |
  """,
  "Padankan: Decision dan Input/Output masing-masing berbentuk apa?",
  kw=["diamond|berlian|wajik", "parallelogram|segi empat selari"],
  ans="Decision = diamond; Input/Output = parallelogram.",
  hint="Satu ada 2 keluaran, satu 'senget'.",
  fu=[F("""Process = rectangle, Start/End = oval.""",
        "Apakah bentuk simbol Start/End?",
        ans=["oval", "bujur"],
        hint="Kapsul.")],
  mcq=M("Simbol untuk memanggil function dalam flowchart ialah…",
        "Rectangle dengan garis tepi berganda", "Diamond", "Oval", "Parallelogram"))

S("ch07", T, "6.7 Exam-day checklist: output format",
  """
  **Checklist #7: format output**

  - Salin rentetan **tepat**, termasuk ruang di hujung `"Total = "`.
  - `endl` / `"\\n"` = baris baru; tanpanya output bersambung.
  - `cout` double: 6 digit bererti (80.3333, 11351.4); nombor bulat double dicetak tanpa `.0` (`2.0 * 7 / 2` → `7`).
  - `bool` dicetak sebagai 1/0.
  """,
  "Bagaimana cout mencetak nilai double 7.0?",
  ans=["7"],
  hint="Tiada .0",
  fu=[F("""`cout << "A" << "B" << endl << "C";`""",
        "Berapakah baris output?",
        ans=["2", "dua", "two"],
        hint="endl selepas AB."),
      F("""`cout << (3 > 2);`""",
        "Apakah output?",
        ans=["1"],
        hint="bool dicetak sebagai nombor.")],
  mcq=M("`cout << 10.0 / 3;` mencetak…",
        "3.33333", "3.3333333333", "3", "3.33"))

S("ch08", T, "6.8 Exam-day checklist: compile and test habits",
  """
  **Checklist #8: tabiat compile & test**

  - Compile dengan `g++ -std=c++17 -Wall -Wextra -pedantic`. Warning = kesilapan.
  - Betulkan ralat **pertama** dahulu.
  - Uji **nilai sempadan** (0, negatif, 90/91, 50/51) dan input tidak sah.
  - Setiap `cin` ada prompt.
  - Untuk nombor rawak, uji dengan seed tetap atau julat (bukan satu jujukan tertentu).
  """,
  "Mengapa kita perlu menguji nilai sempadan seperti 90 dan 91?",
  kw=["boundary|sempadan|edge|had|limit",
      "> |>=|<|<=|condition|syarat|off-by-one|salah|error|bug|kesilapan"],
  ans="Kerana kesilapan > vs >= (off-by-one) hanya kelihatan pada nilai sempadan.",
  hint="Lab 5 B1.",
  fu=[F("""Flag `-Wall -Wextra` memaparkan warning seperti assignment dalam syarat.""",
        "Apakah flag g++ untuk memaparkan semua warning asas?",
        ans=["-Wall", "-wall", "-Wall -Wextra"],
        hint="W + all.")],
  mcq=M("Nilai ujian terbaik untuk `if (score > 50)` ialah…",
        "50 dan 51", "0 dan 100", "75", "Hanya 51"))
