from helpers import S, F, M

T = "func"
H = "5 · "

S("fn01", T, H + "Modular programming",
  """
  **Modular programming**: pecahkan program kepada **functions kecil**. Ini menjadikannya lebih mudah **ditulis, dibaca dan diselenggara** (write, read and maintain).

  Idealnya, **`main()` pendek** dan kebanyakannya **memanggil function lain**.
  """,
  "Apakah modular programming dan apakah faedahnya?",
  kw=["split|pecah|pecahkan|small|kecil|bahagi",
      "function|fungsi",
      "write|tulis|read|baca|maintain|selenggara|mudah|easier"],
  ans="Memecahkan program kepada functions kecil supaya lebih mudah ditulis, dibaca dan diselenggara.",
  hint="Tiga faedah: tulis, baca, …",
  fu=[F("""Idealnya `main()` pendek dan kebanyakannya memanggil function lain.""",
        "Bagaimanakah main() yang ideal dalam modular programming?",
        kw=["short|pendek|ringkas", "call|panggil|memanggil"],
        ans="Pendek, dan kebanyakannya memanggil function lain.",
        hint="Panjang atau pendek?")],
  mcq=M("Dalam modular programming yang baik, main()…",
        "Pendek dan banyak memanggil function lain", "Mengandungi semua kod", "Tidak wujud", "Mesti void"))

S("fn02", T, H + "Library functions · <cmath>",
  """
  **`<cmath>`**: `pow(x,y)`, `sqrt(x)`, `abs(x)`, `sin`, `cos`, `tan`, `log`. Function ini **menerima dan memulangkan double**.
  """,
  "Header apakah diperlukan untuk pow dan sqrt?",
  ans=["<cmath>", "cmath", "#include <cmath>"],
  hint="c + math.",
  fu=[F("""`cout << pow(2, 3) << " " << sqrt(25);`""",
        "Apakah output?",
        ans=["8 5"],
        hint="2³ dan √25."),
      F("""Function `<cmath>` menerima dan memulangkan **double**.""",
        "Jenis data apakah dipulangkan oleh sqrt?",
        ans=["double"],
        hint="Perpuluhan.")],
  mcq=M("Function manakah dalam <cmath>?",
        "sqrt", "strlen", "toupper", "rand"))

S("fn03", T, H + "Library functions · <cctype>",
  """
  **`<cctype>`**: `isalpha`, `isdigit`, `isalnum`, `islower`, `isupper`, `isspace`, `ispunct`, `isprint`, dan `toupper`, `tolower`.
  """,
  "Header apakah diperlukan untuk isdigit dan toupper?",
  ans=["<cctype>", "cctype", "#include <cctype>"],
  hint="c + c + type.",
  fu=[F("""`isdigit('7')` true, `isalpha('7')` false. `toupper('a')` → 'A'.""",
        "Function <cctype> apakah menukar huruf kepada huruf besar?",
        ans=["toupper", "toupper()"],
        hint="to + upper."),
      F("""`isspace` menguji ruang (whitespace), `ispunct` menguji tanda baca.""",
        "Function apakah menguji sama ada aksara ialah digit?",
        ans=["isdigit", "isdigit()"],
        hint="is + digit.")],
  mcq=M("`isupper` berada dalam header…",
        "<cctype>", "<cmath>", "<cstring>", "<cstdlib>"))

S("fn04", T, H + "Library functions · <cstring>",
  """
  **`<cstring>`**:
  - `strlen`: **panjang** (length)
  - `strcat`: **sambung** (join)
  - `strcpy`: **salin** (copy)
  - `strcmp`: **banding** (compare): **0 bermaksud sama**
  - `strstr`: **cari** (find)
  """,
  "Apakah fungsi strlen, strcat, strcpy, strcmp dan strstr?",
  kw=["strlen|length|panjang", "strcat|join|sambung|gabung",
      "strcpy|copy|salin", "strcmp|compare|banding", "strstr|find|cari"],
  ans="strlen = panjang, strcat = sambung, strcpy = salin, strcmp = banding (0 = sama), strstr = cari.",
  hint="length, join, copy, compare, find.",
  fu=[F("""`strlen("George")`.""",
        "Apakah nilai pulangan?",
        ans=["6"],
        hint="Kira huruf."),
      F("""`char s[20]; strcpy(s, "Hi"); strcat(s, "!!"); cout << s;`""",
        "Apakah output?",
        ans=["Hi!!"],
        hint="Salin, kemudian sambung.")],
  mcq=M("Function untuk mencari substring dalam C-string ialah…",
        "strstr", "strcat", "strlen", "strcpy"))

S("fn05", T, H + "Library functions · <cstdlib>",
  """
  **`<cstdlib>`**: `rand()`, `srand(x)`, `atoi`, `atol`, `atof` (**string → number**), `exit(0)`.
  """,
  "Header apakah mengandungi rand, atoi dan exit?",
  ans=["<cstdlib>", "cstdlib", "#include <cstdlib>"],
  hint="c + std + lib.",
  fu=[F("""atoi = string → int, atol = string → long, atof = string → double.""",
        "Function apakah menukar string kepada double?",
        ans=["atof", "atof()"],
        hint="a-to-f."),
      F("""`cout << atoi("42") + 1;`""",
        "Apakah output?",
        ans=["43"],
        hint="\"42\" → 42.")],
  mcq=M("`atoi`, `atol` dan `atof` menukar…",
        "String kepada nombor", "Nombor kepada string", "Huruf kecil kepada besar", "double kepada int"))

S("fn06", T, H + "C-STRINGS warning",
  """
  ⚠ **C-STRINGS**

  Anda **tidak boleh** banding dengan `==` atau assign dengan `=`. Gunakan **`strcmp`** dan **`strcpy`**.

  `strcmp` memulangkan **0 apabila string sama**.
  """,
  "Bagaimana membanding dan menyalin C-string?",
  kw=["strcmp", "strcpy", "== |==|=|cannot|tidak boleh|tak boleh"],
  ans="Guna strcmp untuk banding (0 = sama) dan strcpy untuk salin; tidak boleh guna == atau =.",
  hint="Dua function str…",
  fu=[F("""`strcmp("abc", "abc")`.""",
        "Apakah nilai pulangan?",
        ans=["0"],
        hint="Sama."),
      F("""Syarat untuk C-string a dan b yang sama.""",
        "Tulis syarat if yang benar apabila a dan b sama.",
        ans=["if (strcmp(a, b) == 0)", "strcmp(a, b) == 0", "strcmp(a,b)==0", "if (!strcmp(a, b))"],
        hint="strcmp(...) == 0")],
  mcq=M("Cara BETUL untuk memberi nilai \"Ali\" kepada `char name[10]` selepas pengisytiharan ialah…",
        "strcpy(name, \"Ali\");", "name = \"Ali\";", "name == \"Ali\";", "strcmp(name, \"Ali\");"))

S("fn07", T, H + "User-defined functions · structure",
  """
  ```
  returnType name(parameter list)   // header
  {
      local variables;
      statements;
      return value;                 // not needed if void
  }
  ```
  """,
  "Apakah tiga bahagian function header?",
  kw=["return type|returntype|jenis pulangan|return", "name|nama", "parameter|parameter list|senarai parameter"],
  ans="returnType, name, (parameter list).",
  hint="Jenis, nama, kurungan.",
  fu=[F("""`return value;` tidak diperlukan jika function ialah `void`.""",
        "Bilakah `return value;` tidak diperlukan?",
        ans=["void", "apabila void", "if void", "jika void"],
        hint="Jenis pulangan tiada."),
      F("""Header `double average(int a, int b)`.""",
        "Apakah return type dalam header ini?",
        ans=["double"],
        hint="Perkataan pertama.")],
  mcq=M("Dalam `int sum(int a, int b)`, `int a, int b` ialah…",
        "Parameter list", "Return type", "Nama function", "Badan function"))

S("fn08", T, H + "Prototype, definition, call",
  """
  | Prototype | Definition | Call |
  |---|---|---|
  | `int sum(int, int);` | `int sum(int a, int b) { return a + b; }` | `total = sum(x, y);` |
  | Diletak **sebelum main**, berakhir dengan **`;`** | | |
  """,
  "Di manakah prototype diletak dan bagaimana ia berakhir?",
  kw=["before|sebelum|atas|above", "main", ";|semicolon|titik koma|koma bertitik"],
  ans="Sebelum main, dan berakhir dengan ;.",
  hint="Lokasi + simbol.",
  fu=[F("""Prototype hanya perlu jenis parameter: `int sum(int, int);`""",
        "Tulis prototype untuk `double avg(double a, double b)`.",
        ans=["double avg(double, double);", "double avg(double a, double b);"],
        hint="Header + ;"),
      F("""`int x = 3, y = 4; total = sum(x, y);`""",
        "Apakah nilai total?",
        ans=["7"],
        hint="a + b.")],
  mcq=M("Yang manakah function CALL?",
        "total = sum(x, y);", "int sum(int, int);", "int sum(int a, int b)", "{ return a + b; }"))

S("fn09", T, H + "What the compiler must know before a call",
  """
  Compiler **mesti tahu** **nama** function, **return type**, dan **bilangan serta jenis parameter** **sebelum** ia dipanggil.

  Jadi gunakan **prototype**, atau **definisikan function di atas main**.
  """,
  "Apakah yang mesti diketahui compiler sebelum function dipanggil, dan bagaimana memastikannya?",
  kw=["name|nama", "return type|jenis pulangan|return",
      "number|bilangan|type|jenis|parameter",
      "prototype|above|atas|sebelum main|before main"],
  ans="Nama, return type, bilangan dan jenis parameter; gunakan prototype atau definisikan function di atas main.",
  hint="Tiga maklumat + dua cara.",
  fu=[F("""Tanpa prototype, dan definition di bawah main → `'f' was not declared in this scope`.""",
        "Selain prototype, apakah cara lain supaya compiler kenal function?",
        kw=["define|definisi|takrif|definition|letak|tulis", "above|atas|before|sebelum"],
        ans="Definisikan function di atas main.",
        hint="Kedudukan.")],
  mcq=M("Yang manakah TIDAK perlu diketahui compiler sebelum panggilan function?",
        "Isi badan function", "Nama function", "Return type", "Bilangan dan jenis parameter"))

S("fn10", T, H + "void functions",
  """
  **`void`** bermaksud function **tidak memulangkan apa-apa** (returns nothing).
  """,
  "Apakah maksud void?",
  kw=["nothing|tiada|tidak|no|tak", "return|pulang|memulangkan|nilai|value"],
  ans="Function tidak memulangkan apa-apa nilai.",
  hint="Kosong.",
  fu=[F("""`void printLine()` tidak memulangkan nilai, jadi `int x = printLine();` ialah ralat.""",
        "Bolehkah hasil void function disimpan dalam pemboleh ubah? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Tiada nilai.")],
  mcq=M("Function `void show(int n)`…",
        "Tidak memulangkan nilai", "Memulangkan int", "Memulangkan n", "Tidak boleh ada parameter"))

S("fn11", T, H + "Arguments vs parameters",
  """
  - **Arguments (actual)** berada dalam **call**.
  - **Parameters (formal)** berada dalam **header**.
  - Dipadankan **mengikut turutan**, dan **bilangannya mesti sama**.
  """,
  "Apakah beza arguments dan parameters?",
  kw=["argument|actual|sebenar", "call|panggil|panggilan",
      "parameter|formal", "header|definition|definisi",
      "order|turutan|number|bilangan"],
  ans="Arguments (actual) dalam call; parameters (formal) dalam header; dipadankan ikut turutan dan bilangan mesti sama.",
  hint="Call vs header.",
  fu=[F("""`total = sum(x, y);` dengan header `int sum(int a, int b)`.""",
        "Parameter manakah menerima nilai y?",
        ans=["b"],
        hint="Kedudukan kedua."),
      F("""Bilangan argument mesti sama dengan parameter. `sum(1, 2, 3)` untuk `sum(int, int)` → ralat `too many arguments`.""",
        "Apakah yang berlaku jika bilangan argument tidak sama? (ralat / ok)",
        ans=["ralat", "error", "syntax error", "compile error"],
        hint="Mesti sama.")],
  mcq=M("Dalam `total = sum(x, y);`, x dan y ialah…",
        "Arguments (actual)", "Parameters (formal)", "Return values", "Prototypes"))

S("fn12", T, H + "Using a returned value",
  """
  Gunakan nilai pulangan dengan **menyimpannya** (assign), **mencetaknya** (print), atau **dalam ungkapan** (use it in an expression).

  ```
  total = sum(3, 4);            // assign
  cout << sum(3, 4);            // print
  int d = sum(3, 4) * 2;        // expression → 14
  ```
  """,
  "Apakah tiga cara menggunakan nilai yang dipulangkan oleh function?",
  kw=["assign|simpan|umpuk|=|pemboleh ubah", "print|cetak|cout|papar", "expression|ungkapan"],
  ans="Assign kepada pemboleh ubah, print (cout), atau guna dalam expression.",
  hint="Simpan, cetak, kira.",
  fu=[F("""`int d = sum(3, 4) * 2;`""",
        "Apakah nilai d?",
        ans=["14"],
        hint="7 × 2.")],
  mcq=M("Yang manakah BUKAN cara menggunakan nilai pulangan?",
        "sum(3, 4) = total;", "total = sum(3, 4);", "cout << sum(3, 4);", "d = sum(3, 4) * 2;"))

S("fn13", T, H + "Returning bool",
  """
  Function boleh memulangkan **bool**, contoh:

  ```
  bool isEven(int n) { return n % 2 == 0; }
  ```
  """,
  "Tulis header function isEven yang menerima int n dan memulangkan bool.",
  ans=["bool isEven(int n)"],
  hint="Return type bool.",
  fu=[F("""`cout << isEven(6) << isEven(7);`""",
        "Apakah output?",
        ans=["10"],
        hint="true = 1, false = 0.")],
  mcq=M("`bool isEven(int n)` memulangkan…",
        "true atau false", "Nombor genap", "n", "Tiada"))

S("fn14", T, H + "INVALID HEADERS · no return type", trap=True,
  text="""
  ⚠ **INVALID HEADERS**

  `one(int a, int b)`: **tiada return type** ❌
  """,
  question="Apakah kesilapan dalam header `one(int a, int b)`?",
  kw=["return type|jenis pulangan|return|type|jenis", "missing|tiada|no|tak ada|tertinggal"],
  ans="Tiada return type.",
  hint="Apa yang patut ada sebelum nama?",
  fu=[F("""Tambah return type, contoh `int`.""",
        "Tulis header yang betul jika function memulangkan int.",
        ans=["int one(int a, int b)"],
        hint="int + …")],
  mcq=M("Header `one(int a, int b)` tidak sah kerana…",
        "Tiada return type", "Parameter tiada jenis", "Tiada ( )", "Nama terlalu pendek"))

S("fn15", T, H + "INVALID HEADERS · each parameter needs a type", trap=True,
  text="""
  ⚠ **INVALID HEADERS**

  `char another(int a, b)`: **setiap parameter perlukan jenisnya sendiri** ❌
  """,
  question="Apakah kesilapan dalam header `char another(int a, b)`?",
  kw=["type|jenis|int", "each|setiap|b|parameter"],
  ans="Parameter b tiada jenis; setiap parameter perlukan jenisnya sendiri.",
  hint="Lihat b.",
  fu=[F("""Betul: `char another(int a, int b)`.""",
        "Tulis header yang betul.",
        ans=["char another(int a, int b)"],
        hint="Tambah int sebelum b.")],
  mcq=M("Header manakah SAH?",
        "char another(int a, int b)", "char another(int a, b)", "another(int a, int b)", "char another"))

S("fn16", T, H + "INVALID HEADERS · no ( )", trap=True,
  text="""
  ⚠ **INVALID HEADERS**

  `double yetanother`: **tiada `( )`** ❌
  """,
  question="Apakah kesilapan dalam header `double yetanother`?",
  kw=["( )|()|kurungan|parentheses|bracket", "missing|tiada|no|tertinggal"],
  ans="Tiada ( ) selepas nama function.",
  hint="Function mesti ada…",
  fu=[F("""Function tanpa parameter tetap perlukan `( )`: `double yetanother()`.""",
        "Tulis header yang betul (tanpa parameter).",
        ans=["double yetanother()"],
        hint="Tambah ( ).")],
  mcq=M("`double yetanother` tidak sah sebagai function header kerana…",
        "Tiada ( )", "Tiada return type", "double tidak dibenarkan", "Nama salah"))

S("fn17", T, H + "Pass by value",
  """
  **By value**: `void f(int n)`

  Function mendapat **salinan** (copy). Mengubahnya **tidak mengubah yang asal**.

  Contoh: `m = 612` → `f(m)` tambah 37 di dalam → **m masih 612**.
  """,
  "Apakah maksud pass by value?",
  kw=["copy|salinan|salin", "original|asal|not change|tidak berubah|unchanged|kekal|tak berubah|tidak mengubah"],
  ans="Function menerima salinan; perubahan di dalam tidak mengubah pemboleh ubah asal.",
  hint="Salinan.",
  fu=[F("""
        ```
        void f(int n) { n = n + 37; }
        int m = 612;
        f(m);
        cout << m;
        ```""",
        "Apakah output?",
        ans=["612"],
        hint="Salinan sahaja yang berubah.")],
  mcq=M("Dalam pass by value, function bekerja dengan…",
        "Salinan", "Yang asal", "Alamat", "Pemalar"))

S("fn18", T, H + "Pass by reference",
  """
  **By reference**: `void f(int &n)`

  Function bekerja pada **yang asal** (an alias), jadi **perubahan kekal**.
  - Guna untuk **"memulangkan" lebih daripada satu nilai**.
  - `&` diletak dalam **prototype dan header**.
  - Argument **mesti pemboleh ubah**, bukan `5` atau `a+b`.
  """,
  "Apakah maksud pass by reference dan bilakah ia digunakan?",
  kw=["original|asal|alias", "change|ubah|perubahan|kekal|stay",
      "more than one|lebih daripada satu|beberapa|multiple|banyak"],
  ans="Function bekerja pada yang asal (alias), jadi perubahan kekal; digunakan untuk 'memulangkan' lebih daripada satu nilai.",
  hint="Alias…",
  fu=[F("""
        ```
        void f(int &n) { n = n + 37; }
        int m = 612;
        f(m);
        cout << m;
        ```""",
        "Apakah output?",
        ans=["649"],
        hint="612 + 37."),
      F("""Argument untuk reference parameter mesti pemboleh ubah. `f(5)` dan `f(a+b)` ialah ralat.""",
        "Bolehkah `f(a+b)` dipanggil untuk `void f(int &n)`? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Mesti pemboleh ubah."),
      F("""`&` diletak dalam prototype DAN header.""",
        "Tulis prototype untuk `void f(int &n)`.",
        ans=["void f(int &n);", "void f(int&);", "void f(int &);", "void f(int& n);"],
        hint="Jangan lupa & dan ;")],
  mcq=M("Untuk `void f(int &n)`, panggilan manakah SAH?",
        "f(m);", "f(5);", "f(a + b);", "f(&5);"))

S("fn19", T, H + "Memory trick: photocopy vs original",
  """
  💡 **MEMORY TRICK**

  - **Value = photocopy**: conteng padanya dan yang asal selamat.
  - **Reference = kertas asal**: `&` = "and change the real one".
  """,
  "Terangkan memory trick photocopy untuk value dan reference.",
  kw=["value|nilai", "photocopy|fotostat|salinan|copy",
      "reference|rujukan|&", "original|asal|real|sebenar"],
  ans="Value = photocopy (asal selamat); reference = kertas asal (& = ubah yang sebenar).",
  hint="Fotostat vs …",
  fu=[F("""`&` = "and change the real one".""",
        "Dalam memory trick, `&` bermaksud apa?",
        kw=["change|ubah", "real|sebenar|asal|original"],
        ans="And change the real one (ubah yang asal).",
        hint="and change the …")],
  mcq=M("Menurut memory trick, pass by value ibarat…",
        "Photocopy", "Kertas asal", "Pen", "Pemadam"))

S("fn20", T, H + "Local variables",
  """
  **Local**: diisytihar **dalam function**. **Dicipta pada setiap panggilan dan dimusnahkan pada akhir**. **Tidak auto-initialised**.
  """,
  "Apakah ciri pemboleh ubah local?",
  kw=["inside|dalam|function", "created|dicipta|each call|setiap panggilan|destroyed|musnah|dimusnahkan",
      "not auto|tidak auto|tak auto|not initialised|tidak diinisialisasi|garbage|sampah|tiada nilai awal"],
  ans="Diisytihar dalam function; dicipta setiap panggilan dan dimusnahkan di akhir; tidak auto-initialised.",
  hint="Di mana, berapa lama, nilai awal.",
  fu=[F("""Local variable tidak diberi nilai awal secara automatik, jadi ia mengandungi nilai sampah jika tidak diinisialisasi.""",
        "Adakah local variable diberi nilai 0 secara automatik? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Not auto-initialised.")],
  mcq=M("Pemboleh ubah local…",
        "Dicipta setiap panggilan dan dimusnahkan di akhir", "Kekal sepanjang program", "Auto-initialised kepada 0", "Boleh diakses oleh semua function"))

S("fn21", T, H + "Global variables",
  """
  **Global**: diisytihar **di luar semua function**. **Kelihatan dari baris itu hingga hujung fail**. **Auto-initialised kepada 0**.

  **Elakkan**; lebih baik guna **global constants**.
  """,
  "Apakah ciri pemboleh ubah global?",
  kw=["outside|luar", "visible|kelihatan|line|baris|end of file|hujung fail|file",
      "0|sifar|zero|auto",
      "avoid|elak|elakkan|constant|pemalar"],
  ans="Diisytihar di luar semua function; kelihatan dari baris itu hingga hujung fail; auto-initialised 0; elakkan, guna global constants.",
  hint="Di mana, skop, nilai awal, nasihat.",
  fu=[F("""`int gx;` di luar main, kemudian `cout << gx;` dalam main.""",
        "Apakah output?",
        ans=["0"],
        hint="Global auto-initialised.")],
  mcq=M("Pemboleh ubah global yang tidak diinisialisasi bernilai…",
        "0", "Nilai sampah", "1", "Ralat"))

S("fn22", T, H + "Static local variables",
  """
  **Static local**: `static int x;` dalam function. **Mengekalkan nilai antara panggilan**. **Diinisialisasi sekali sahaja** (default 0).

  ```
  void showVar() { static int var = 10; cout << var; var++; }
  // dipanggil 10×: 10 11 12 ... 19    (tanpa static: 10 10 10 ...)
  ```
  """,
  "Apakah ciri static local variable?",
  kw=["keep|kekal|mengekalkan|remember|ingat|retain",
      "between calls|antara panggilan|panggilan|calls",
      "once|sekali"],
  ans="Mengekalkan nilai antara panggilan dan diinisialisasi sekali sahaja (default 0).",
  hint="Ia 'ingat'.",
  fu=[F("""showVar() dipanggil 3 kali.""",
        "Apakah output (dengan ruang antara nilai)?",
        ans=["10 11 12"],
        hint="Bermula 10, bertambah."),
      F("""Tanpa `static`, var dicipta semula setiap panggilan.""",
        "Apakah output 3 panggilan tanpa static (dengan ruang)?",
        ans=["10 10 10"],
        hint="Sentiasa 10."),
      F("""Dipanggil 10 kali dengan static.""",
        "Apakah nilai TERAKHIR yang dicetak?",
        ans=["19"],
        hint="10 + 9.")],
  mcq=M("`static int x;` dalam function tanpa nilai awal bermula dengan…",
        "0", "Nilai sampah", "1", "Ralat"))

S("fn23", T, H + "Local wins over global",
  """
  Jika pemboleh ubah **local mempunyai nama yang sama** dengan global, **local menang** dalam function itu.

  ```
  int gy = 5;
  void shadow() { int gy = 99; cout << gy; }
  // shadow(); cout << " " << gy;  →  99 5
  ```
  """,
  "Jika local dan global mempunyai nama sama, yang mana digunakan dalam function?",
  ans=["local", "pemboleh ubah local", "tempatan"],
  hint="Local wins.",
  fu=[F("""Kod shadow di atas: `shadow(); cout << " " << gy;`""",
        "Apakah output?",
        ans=["99 5"],
        hint="Local dalam shadow, global dalam main.")],
  mcq=M("Dalam function yang ada local `x` dan global `x`, `cout << x;` mencetak…",
        "Nilai local", "Nilai global", "Ralat", "Hasil tambah kedua-duanya"))

S("fn24", T, H + "Default arguments",
  """
  ```
  int getSum(int, int = 0, int = 0);          // dalam prototype
  getSum(5); getSum(5, 2); getSum(5, 2, 1);   // semua OK
  ```
  - Nilai default mesti di **hujung kanan** senarai: `(int, int=0, int)` ❌
  - Jika anda tinggalkan satu argument, anda mesti **tinggalkan semua selepasnya**: `getSum(a, , c)` ❌
  """,
  "Nyatakan dua peraturan default arguments.",
  kw=["right|kanan|end|hujung",
      "leave out|tinggal|omit|skip|after|selepas|semua selepas|everything after"],
  ans="Default mesti di hujung kanan senarai; jika tinggalkan satu argument, tinggalkan semua selepasnya.",
  hint="Kanan… dan apa yang selepas.",
  fu=[F("""`getSum(int a, int b = 0, int c = 0)` memulangkan a + b + c.""",
        "Apakah nilai getSum(5, 2)?",
        ans=["7"],
        hint="5 + 2 + 0."),
      F("""Prototype `int f(int, int = 0, int);`""",
        "Adakah prototype ini sah? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Default di tengah."),
      F("""`getSum(a, , c)`""",
        "Adakah panggilan ini sah? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Tidak boleh langkau di tengah.")],
  mcq=M("Dengan `int getSum(int, int = 0, int = 0);`, panggilan manakah TIDAK sah?",
        "getSum(5, , 1);", "getSum(5);", "getSum(5, 2);", "getSum(5, 2, 1);"))

S("fn25", T, H + "Function overloading",
  """
  Function boleh berkongsi **nama yang sama** jika **senarai parameter berbeza** (bilangan atau jenis). Compiler memilih versi yang sepadan dengan argument.

  ```
  void getDimensions(int);           void getDimensions(int, int);
  void getDimensions(int, double);   void getDimensions(double, double);
  ```
  """,
  "Apakah function overloading?",
  kw=["same name|nama sama|sama nama|share|kongsi",
      "different|berbeza|lain", "parameter|parameter list|senarai",
      "number|bilangan|type|jenis"],
  ans="Function dengan nama sama tetapi senarai parameter berbeza (bilangan atau jenis); compiler pilih yang sepadan.",
  hint="Nama sama, apa yang berbeza?",
  fu=[F("""Panggilan `getDimensions(1, 2.5)`: argument int dan double.""",
        "Versi manakah dipilih? (tulis jenis parameter, contoh int, int)",
        ans=["int, double", "(int, double)", "int double", "getDimensions(int, double)"],
        hint="Padan jenis argument."),
      F("""Panggilan `getDimensions(1.5, 2.5)`.""",
        "Versi manakah dipilih?",
        ans=["double, double", "(double, double)", "double double", "getDimensions(double, double)"],
        hint="Dua double.")],
  mcq=M("Overloading memerlukan…",
        "Nama sama, senarai parameter berbeza", "Nama berbeza, parameter sama", "Return type berbeza sahaja", "Semua parameter double"))

S("fn26", T, H + "return vs exit()",
  """
  - **`return`** tamatkan function dan **kembali ke pemanggil** (caller). Kod selepasnya tidak dijalankan.
  - **`exit(0)`** tamatkan **seluruh program serta-merta**, dari mana-mana (`<cstdlib>`). Pemalar: `EXIT_SUCCESS` / `EXIT_FAILURE`.
  """,
  "Apakah beza return dan exit(0)?",
  kw=["return", "function|fungsi|caller|pemanggil",
      "exit", "program|whole|seluruh|immediately|serta-merta"],
  ans="return tamatkan function dan kembali ke pemanggil; exit(0) tamatkan seluruh program serta-merta.",
  hint="Function vs program.",
  fu=[F("""exit berada dalam `<cstdlib>`. Pemalar: `EXIT_SUCCESS` / `EXIT_FAILURE`.""",
        "Header apakah diperlukan untuk exit()?",
        ans=["<cstdlib>", "cstdlib", "#include <cstdlib>"],
        hint="Sama dengan rand."),
      F("""`return` dalam function biasa kembali ke pemanggil; kod selepas return dalam function itu tidak dijalankan.""",
        "Adakah kod selepas return dalam function yang sama dijalankan? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Code after it doesn't run.")],
  mcq=M("Untuk menamatkan SELURUH program dari dalam function, guna…",
        "exit(0)", "return", "break", "continue"))

# =================================================================== BAB 6 cheat sheet
T = "cheat"
H = "6 · Cheat Sheet · "

S("ch01", T, H + "Computational thinking",
  """
  **Computational thinking**: Decomposition · Pattern · Abstraction · Algorithm (**+ Modelling, Evaluation**)
  """,
  "Senaraikan empat skill computational thinking dan dua tambahan dalam versi extended.",
  kw=["decomposition|pecah", "pattern|corak", "abstraction|abstraksi", "algorithm|algoritma",
      "modelling|modeling|model", "evaluation|penilaian"],
  ans="Decomposition, Pattern, Abstraction, Algorithm + Modelling, Evaluation.",
  hint="D-P-A-A + M + E.",
  fu=[F("""Dua tambahan dalam versi extended: Modelling dan Evaluation.""",
        "Namakan satu stage tambahan dalam versi extended.",
        ans=["modelling", "modeling", "evaluation"],
        hint="M atau E.")],
  mcq=M("Yang manakah stage TAMBAHAN dalam versi extended?",
        "Modelling", "Decomposition", "Abstraction", "Pattern"))

S("ch02", T, H + "Problem solving",
  """
  **Problem solving**: IPO → Algorithm → Pseudocode / Flowchart → Trace table → Code
  """,
  "Tulis aliran problem solving dalam cheat sheet.",
  kw=["ipo|input", "algorithm|algoritma", "pseudocode|flowchart", "trace|trace table", "code|kod"],
  ans="IPO → Algorithm → Pseudocode / Flowchart → Trace table → Code.",
  hint="Bermula dengan IPO, berakhir dengan Code.",
  fu=[F("""Trace table datang sebelum Code dalam aliran cheat sheet.""",
        "Apakah langkah tepat sebelum Code?",
        ans=["trace table", "trace"],
        hint="Jadual.")],
  mcq=M("Dalam aliran problem solving, langkah pertama ialah…",
        "IPO", "Code", "Trace table", "Flowchart"))

S("ch03", T, H + "3 control structures and flowchart shapes",
  """
  - **3 control structures**: Sequence · Selection · Repetition
  - **Flowchart shapes**: **Oval** = start/end · **Rectangle** = process · **Parallelogram** = I/O · **Diamond** = decision
  """,
  "Padankan bentuk flowchart: Oval, Rectangle, Parallelogram, Diamond.",
  kw=["oval|bujur", "start|end|mula|tamat",
      "rectangle|segi empat tepat", "process|proses",
      "parallelogram|segi empat selari", "i/o|input|output",
      "diamond|berlian", "decision|keputusan"],
  ans="Oval = start/end, Rectangle = process, Parallelogram = I/O, Diamond = decision.",
  hint="4 pasangan.",
  fu=[F("""Diamond = decision.""",
        "Bentuk apakah untuk decision?",
        ans=["diamond", "berlian"],
        hint="Wajik.")],
  mcq=M("Parallelogram dalam flowchart ialah…",
        "Input/Output", "Process", "Decision", "Start/End"))

S("ch04", T, H + "Integer maths",
  """
  **Integer maths**: `7/3` = 2 · `7%3` = 1 · `7/3.0` = 2.33 (cout mencetak `2.33333`) · `int x = 3.9` → 3
  """,
  "Apakah nilai 7/3 dan 7%3? (tulis: a b)",
  ans=["2 1"],
  hint="Integer division dan baki.",
  fu=[F("""`int x = 3.9;` → dipotong.""",
        "Apakah nilai x?",
        ans=["3"],
        hint="Truncated."),
      F("""`7/3.0`: satu operand double. cout mencetak 6 digit bererti.""",
        "Apakah output `cout << 7/3.0;`?",
        ans=["2.33333", "2.33"],
        hint="2.33…")],
  mcq=M("`7 % 3` bernilai…",
        "1", "2", "2.33", "0"))

S("ch05", T, H + "Precedence",
  """
  **Precedence** (tinggi → rendah):

  `( )` → `!` unary− → `* / %` → `+ −` → `< > <= >=` → `== !=` → `&&` → `||` → `=`
  """,
  "Antara && dan ||, yang manakah lebih tinggi keutamaannya?",
  ans=["&&", "and"],
  hint="AND sebelum OR.",
  fu=[F("""Relational (`< > <= >=`) lebih tinggi daripada equality (`== !=`), yang lebih tinggi daripada `&&`.""",
        "Apakah output `cout << (3 + 4 > 6 && 2 == 2);`?",
        ans=["1"],
        hint="7 > 6 true, 2 == 2 true."),
      F("""`=` mempunyai keutamaan paling rendah.""",
        "Operator manakah PALING rendah keutamaannya dalam senarai cheat sheet?",
        ans=["=", "assignment"],
        hint="Hujung senarai.")],
  mcq=M("Yang manakah dinilai DAHULU?",
        "!", "&&", "==", "||"))

S("ch06", T, H + "Truth",
  """
  **Truth**: `0` = false · **sebarang bukan-sifar = true**

  **AND**: semua mesti T · **OR**: satu T sudah cukup
  """,
  "Apakah nilai truth bagi 0 dan bagi nombor bukan sifar?",
  kw=["0|sifar|zero", "false|palsu", "non-zero|bukan sifar|bukan-sifar|lain", "true|benar"],
  ans="0 = false; sebarang bukan sifar = true.",
  hint="Hanya satu nilai false.",
  fu=[F("""AND: semua mesti T. OR: satu T cukup.""",
        "`true && false` bernilai? (true / false)",
        ans=["false", "0"],
        hint="AND ketat.")],
  mcq=M("`if (7)` dianggap…",
        "true", "false", "ralat", "7"))

S("ch07", T, H + "= vs ==",
  """
  **`=` assigns · `==` compares**

  `if (x = 5)` adalah **sentiasa true**! (x menjadi 5, dan 5 bukan sifar.)
  """,
  "Mengapa `if (x = 5)` sentiasa true?",
  kw=["assign|assignment|umpuk|=", "5|bukan sifar|non-zero|true"],
  ans="Kerana = memberi nilai 5 kepada x, dan 5 (bukan sifar) dianggap true.",
  hint="Nilai assignment ialah 5.",
  fu=[F("""`int x = 1; if (x = 5) cout << x;`""",
        "Apakah output?",
        ans=["5"],
        hint="x ditukar.")],
  mcq=M("Operator untuk MEMBANDINGKAN dua nilai ialah…",
        "==", "=", "!", "=>"))

S("ch08", T, H + "switch and loops",
  """
  - **switch**: int/char/bool sahaja · case constant · jangan lupa `break`
  - **Loops**: `for` = bilangan diketahui · `while` = 0+ kali · `do-while` = 1+ kali (**berakhir dengan `;`**)
  """,
  "Berapa kali minimum while dan do-while berjalan? (tulis: while do-while)",
  ans=["0 1", "0+ 1+"],
  hint="0+ dan 1+.",
  fu=[F("""switch: int/char/bool sahaja.""",
        "Senaraikan jenis yang dibenarkan dalam switch.",
        kw=["int", "char", "bool"],
        ans="int, char, bool.",
        hint="Tiga.")],
  mcq=M("Loop yang berakhir dengan ; ialah…",
        "do-while", "for", "while", "switch"))

S("ch09", T, H + "break / continue and function parts",
  """
  - **break** = keluar dari loop · **continue** = langkau ke pusingan seterusnya
  - **Function parts**: prototype `int f(int);` · header `int f(int a)` · call `y = f(x);`
  """,
  "Tulis contoh prototype, header dan call bagi function f dalam cheat sheet.",
  kw=["int f(int);|int f(int)", "int f(int a)", "y = f(x)|f(x)"],
  ans="Prototype: int f(int); Header: int f(int a). Call: y = f(x);",
  hint="Prototype ada ;, header ada nama parameter, call tiada jenis.",
  fu=[F("""break keluar; continue langkau ke pusingan seterusnya.""",
        "Jump statement manakah langkau ke pusingan seterusnya?",
        ans=["continue"],
        hint="Bukan break.")],
  mcq=M("Dalam cheat sheet, `y = f(x);` ialah…",
        "Call", "Prototype", "Header", "Definition"))

S("ch10", T, H + "Value vs reference and variable lifetime",
  """
  - **Value vs reference**: `f(int a)` = salinan · `f(int &a)` = asal (mesti hantar pemboleh ubah)
  - **Variable lifetime**: local = setiap panggilan · static = ingat · global = seluruh fail (elakkan)
  """,
  "Padankan lifetime: local, static, global.",
  kw=["local|tempatan", "per call|setiap panggilan|panggilan",
      "static", "remember|ingat|kekal",
      "global", "whole file|seluruh fail|fail|file"],
  ans="local = setiap panggilan; static = ingat nilai; global = seluruh fail (elakkan).",
  hint="Per call, remembers, whole file.",
  fu=[F("""`f(int &a)` bekerja pada yang asal; argument mesti pemboleh ubah.""",
        "Header manakah mengubah pemboleh ubah asal: `f(int a)` atau `f(int &a)`?",
        ans=["f(int &a)", "int &a", "&a", "f(int& a)"],
        hint="Ada &.")],
  mcq=M("Pemboleh ubah yang 'mengingati' nilainya antara panggilan ialah…",
        "static", "local biasa", "parameter by value", "literal"))

S("ch11", T, H + "Default args and overloading",
  """
  - **Default args**: default dari **kanan ke kiri** · tinggalkan argument **dari kanan**
  - **Overloading**: **nama sama + senarai parameter berbeza** (bilangan/jenis)
  """,
  "Apakah syarat function overloading?",
  kw=["same name|nama sama|sama nama", "different|berbeza", "parameter|list|senarai"],
  ans="Nama sama dengan senarai parameter berbeza (bilangan atau jenis).",
  hint="Nama + parameter.",
  fu=[F("""Default args: kanan ke kiri; argument ditinggalkan dari kanan.""",
        "Dari arah manakah argument boleh ditinggalkan?",
        ans=["kanan", "right", "dari kanan", "from the right"],
        hint="Hujung senarai.")],
  mcq=M("Default arguments ditetapkan…",
        "Dari kanan ke kiri", "Dari kiri ke kanan", "Di tengah sahaja", "Dalam call sahaja"))

S("ch12", T, H + "EXAM-DAY CHECKLIST · trace table and traps",
  """
  ✔ **EXAM-DAY CHECKLIST WHEN TRACING CODE**
  1. Lukis **trace table** dengan **satu lajur bagi setiap pemboleh ubah**.
  2. Semak **`=` vs `==`**, **`;` tersasar selepas if/while**, dan **`break` yang hilang**.
  """,
  "Apakah tiga trap yang perlu disemak semasa trace code (checklist item 2)?",
  kw=["= vs ==|==|=", ";|semicolon|titik koma|stray", "break"],
  ans="= vs ==, ; tersasar selepas if/while, dan break yang hilang.",
  hint="Satu operator, satu tanda baca, satu keyword.",
  fu=[F("""Checklist item 1: trace table dengan satu lajur bagi setiap pemboleh ubah.""",
        "Berapakah lajur bagi setiap pemboleh ubah dalam trace table?",
        ans=["1", "satu", "one"],
        hint="One column per variable.")],
  mcq=M("Langkah pertama dalam exam-day checklist ialah…",
        "Lukis trace table, satu lajur setiap pemboleh ubah", "Tulis kod semula", "Compile", "Lukis flowchart"))

S("ch13", T, H + "EXAM-DAY CHECKLIST · arithmetic and ++",
  """
  ✔ **EXAM-DAY CHECKLIST**
  3. **Integer division? Truncation? Prefix atau postfix `++`?**
  """,
  "Apakah tiga soalan aritmetik dalam checklist item 3?",
  kw=["integer division|integer|pembahagian integer", "truncation|truncate|potong",
      "prefix|postfix|++"],
  ans="Integer division? Truncation? Prefix atau postfix ++?",
  hint="Bahagi, potong, tambah.",
  fu=[F("""
        ```
        int a = 7, b = 2;
        double c = a / b;
        cout << c;
        ```""",
        "Apakah output?",
        ans=["3"],
        hint="a / b ialah int ÷ int dahulu.")],
  mcq=M("`int k = 4; int m = k++ + 1;` → m =",
        "5", "6", "4", "Ralat"))

S("ch14", T, H + "EXAM-DAY CHECKLIST · value/reference and static",
  """
  ✔ **EXAM-DAY CHECKLIST**
  4. **Pass by value** (asal tidak berubah) atau **by reference** (asal berubah)?
  5. **Static variable** (kekalkan nilai) atau **local biasa** (reset setiap panggilan)?
  """,
  "Apakah dua soalan tentang functions dalam checklist item 4 dan 5?",
  kw=["value|nilai", "reference|rujukan|&", "static", "local|reset"],
  ans="Pass by value atau by reference? Static variable atau local biasa?",
  hint="Parameter dan lifetime.",
  fu=[F("""
        ```
        void addOne(int n) { n++; }
        int main() { int k = 9; addOne(k); cout << k; }
        ```""",
        "Apakah output?",
        ans=["9"],
        hint="Pass by value.")],
  mcq=M("Dalam soalan trace, local variable biasa (bukan static)…",
        "Reset setiap panggilan", "Mengekalkan nilai", "Auto 0 dan kekal", "Sama dengan global"))
