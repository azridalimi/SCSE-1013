from helpers import S, F, M

T = "cpp"

S("cp01", T, "3.1 Parts of a C++ program",
  """
  Struktur asas program C++:

  ```
  #include <iostream>      // preprocessor directive
  using namespace std;     // guna nama dalam std
  int main()               // fungsi utama: pelaksanaan bermula di sini
  {
      cout << "Hello";     // statement berakhir dengan ;
      return 0;            // 0 = program tamat dengan jayanya
  }
  ```

  - `#include` dan `int main()` **tiada** `;` di hujung.
  - Badan function dalam `{ }`.
  """,
  "Di manakah pelaksanaan program C++ bermula, dan apakah maksud return 0?",
  kw=["main|int main|main()", "0|sifar|zero|success|berjaya|jayanya|normal|tamat"],
  ans="Pelaksanaan bermula di function main(). return 0 bermaksud program tamat dengan jayanya.",
  hint="Satu function wajib dalam setiap program.",
  fu=[F("""Susun semula (Lab 4 A3c): `int main()`, `}`, `return 0;`, `#include <iostream>`, `cout << "In 1492 Columbus sailed the ocean blue.";`, `{`, `using namespace std;`

        Susunan betul:
        ```
        #include <iostream>
        using namespace std;
        int main()
        {
            cout << "In 1492 Columbus sailed the ocean blue.";
            return 0;
        }
        ```""",
        "Apakah baris PERTAMA dalam program yang disusun dengan betul?",
        ans=["#include <iostream>", "#include<iostream>"],
        hint="Preprocessor directive."),
      F("""Cari kesilapan:
        ```
        int main();
        {
            return 0;
        }
        ```
        `int main();` dengan `;` menjadikannya prototype, bukan definition. Ralat: *expected initializer / expected unqualified-id before '{'*.""",
        "Apakah yang perlu dibuang daripada baris `int main();`?",
        ans=[";", "semicolon", "titik koma", "koma bertitik"],
        hint="Simbol di hujung baris.")],
  mcq=M("Baris manakah TIDAK berakhir dengan ; ?",
        "#include <iostream>", "using namespace std;", "return 0;", "cout << x;"))

S("cp02", T, "3.1 Comments", trap=True,
  text="""
  Komen (comments) diabaikan oleh compiler:

  - `// komen satu baris`
  - `/* komen berbilang baris */`

  **TRAP**: `/*` tanpa `*/` → ralat **unterminated comment**. Lab 4 A1: baris pertama `/ * Task ...` menghasilkan `error: unterminated comment` dan `expected unqualified-id before '/' token`.
  """,
  question="Apakah dua jenis komen dalam C++?",
  kw=["//|single|satu baris|single-line|one line", "/*|*/|multi|berbilang|multi-line|block|banyak baris"],
  ans="// untuk satu baris, /* ... */ untuk berbilang baris.",
  hint="Satu guna dua slash, satu guna slash-bintang.",
  fu=[F("""`/* Task: add two prices` tanpa penutup menyebabkan seluruh baki fail dianggap komen.""",
        "Apakah mesej ralat jika /* tidak ditutup?",
        ans=["unterminated comment", "error: unterminated comment"],
        hint="un……… comment.")],
  mcq=M("Yang manakah komen berbilang baris yang SAH?",
        "/* jumlah harga */", "// jumlah harga //", "<!-- jumlah harga -->", "# jumlah harga"))

S("cp03", T, "3.2 Program elements: keywords, identifiers, operators, punctuation",
  """
  Elemen dalam program C++:

  - **Keywords (reserved words)**: perkataan khas C++, contoh `int`, `double`, `return`, `if`. Tidak boleh dijadikan nama.
  - **Identifiers**: nama yang dicipta oleh pengaturcara (pemboleh ubah, function).
  - **Operators**: `+ - * / % = << >>`
  - **Punctuation**: `;` `,` `{ }` `( )`
  - **Literals**: nilai tetap dalam kod, contoh `2`, `"Hello"`.
  """,
  "Apakah beza keyword dan identifier?",
  kw=["keyword|reserved|kata kunci|simpanan|khas",
      "identifier|nama|name|pengecam",
      "programmer|pengaturcara|cipta|create|define|sendiri|user"],
  ans="Keyword ialah perkataan simpanan C++ (int, return); identifier ialah nama yang dicipta pengaturcara.",
  hint="Satu dimiliki C++, satu dicipta oleh anda.",
  fu=[F("""Dalam `int total = 5;`: `int` keyword, `total` identifier, `=` operator, `5` literal, `;` punctuation.""",
        "Dalam `int total = 5;`, apakah `total`?",
        ans=["identifier", "pengecam", "variable", "pemboleh ubah"],
        hint="Nama yang anda cipta.")],
  mcq=M("Dalam `double price = 4.5;`, `double` ialah…",
        "Keyword", "Identifier", "Literal", "Operator"))

S("cp04", T, "3.2 Identifier rules (Ch3 slide 25)", trap=True,
  text="""
  Peraturan **identifier**:

  1. Aksara pertama: huruf (a–z, A–Z) atau underscore `_`.
  2. Aksara seterusnya: huruf, digit, atau `_`.
  3. **Tiada** ruang atau simbol lain (`.`, `$`, `-`, `#`).
  4. **Bukan** keyword.
  5. **Case-sensitive**: `total` ≠ `Total`.

  | Nama | Sah? | Sebab |
  |---|---|---|
  | totalSales | Valid | |
  | total_Sales | Valid | |
  | total.Sales | **Invalid** | `.` tidak dibenarkan |
  | 4thQtrSales | **Invalid** | mula dengan digit |
  | totalSale$ | **Invalid** | `$` bukan huruf/digit/_ |
  | int | **Invalid** | keyword |

  **TRAP**: g++ menerima `$` sebagai extension, jadi jangan uji dengan compiler. Ikut standard.
  """,
  question="Nyatakan peraturan menamakan identifier.",
  kw=["letter|huruf|alphabet|abjad", "underscore|_|garis bawah",
      "digit|nombor|number|angka", "keyword|reserved|kata kunci",
      "case|besar kecil|case-sensitive|huruf besar"],
  ans="Mula dengan huruf atau _, diikuti huruf/digit/_, tiada ruang/simbol, bukan keyword, case-sensitive.",
  hint="Ada 5 peraturan: aksara pertama, aksara seterusnya, simbol, keyword, case.",
  fu=[F("""`total.Sales` mengandungi titik. Titik digunakan untuk akses ahli (member), bukan sebahagian nama.""",
        "`total.Sales`: valid atau invalid?",
        ans=["invalid", "tidak sah", "tak sah"],
        hint="Lihat simbol di tengah."),
      F("""`totalSale$`: simbol `$` bukan huruf, digit atau underscore. Standard C++ tidak membenarkannya walaupun g++ terima.""",
        "`totalSale$`: valid atau invalid?",
        ans=["invalid", "tidak sah", "tak sah"],
        hint="Ikut standard, bukan compiler."),
      F("""`_count2` bermula dengan underscore dan diikuti huruf/digit sahaja.""",
        "`_count2`: valid atau invalid?",
        ans=["valid", "sah"],
        hint="Underscore dibenarkan di awal.")],
  mcq=M("Identifier manakah yang SAH?",
        "total_Sales", "4thQtrSales", "total.Sales", "int"))

S("cp05", T, "3.2 Case sensitivity", trap=True,
  text="""
  C++ adalah **case-sensitive**. `Total`, `total` dan `TOTAL` ialah tiga nama berbeza. `Cout` ≠ `cout`.

  Lab 4 A1: `cout << Total` sedangkan yang diisytihar ialah `total` →
  `error: 'Total' was not declared in this scope; did you mean 'total'?`
  """,
  question="Mengapa `cout << Total;` menghasilkan ralat jika pemboleh ubah diisytihar sebagai `int total;`?",
  kw=["case|besar|kecil|huruf besar|capital|uppercase|case-sensitive",
      "different|berbeza|lain|tidak sama|not same|not declared|tidak diisytihar"],
  ans="C++ case-sensitive: Total dan total ialah nama berbeza, jadi Total tidak diisytihar.",
  hint="Bandingkan huruf T.",
  fu=[F("""`Cout << "Hi";` → `Cout` tidak dikenali kerana objek sebenar ialah `cout` (huruf kecil).""",
        "Betulkan: `Cout << \"Hi\";`",
        ans=["cout << \"Hi\";"],
        hint="Huruf pertama.")],
  mcq=M("Yang manakah betul tentang `Sum` dan `sum` dalam C++?",
        "Dua identifier berbeza", "Identifier yang sama", "Kedua-duanya keyword", "Ralat sintaks"))

S("cp06", T, "3.3 Variables and literals (slide 31)",
  """
  - **Variable**: lokasi storan bernama dalam memori; nilainya boleh berubah.
  - **Literal**: nilai tetap yang ditulis terus dalam kod.

  ```
  int little;
  int big;
  little = 2;
  big = 2000;
  cout << "The little number is " << little << endl;
  cout << "The big number is " << big << endl;
  ```
  Variables: `little`, `big`. Literals: `2`, `2000`, `"The little number is "`, `"The big number is "`.
  """,
  "Apakah beza variable dan literal?",
  kw=["variable|pemboleh ubah|pembolehubah",
      "memory|memori|storage|storan|location|lokasi|named|bernama|berubah|change",
      "literal", "fixed|tetap|constant|nilai terus|ditulis terus"],
  ans="Variable ialah lokasi storan bernama yang nilainya boleh berubah; literal ialah nilai tetap yang ditulis terus dalam kod.",
  hint="Satu ada nama dan boleh berubah, satu ditulis terus.",
  fu=[F("""Program di atas mencetak dua baris.""",
        "Apakah baris output PERTAMA program little/big?",
        ans=["The little number is 2"],
        hint="Rentetan + nilai little.")],
  mcq=M("Dalam `big = 2000;`, `2000` ialah…",
        "Literal", "Variable", "Keyword", "Identifier"))

S("cp07", T, "3.4 Output and input: cout and cin",
  """
  - `cout << x` → output, guna **insertion operator** `<<`.
  - `cin >> x` → input, guna **extraction operator** `>>`.
  - `endl` atau `"\\n"` untuk baris baru.
  - Satu `cin` boleh baca beberapa nilai dipisah ruang: `cin >> length >> width;`
  - Sentiasa paparkan **prompt** sebelum `cin`.

  ```
  cout << "Enter length and width: ";
  cin >> length >> width;
  cout << "Area = " << length * width << endl;
  ```
  Input `5 3` → `Area = 15`.
  """,
  "Apakah operator yang digunakan dengan cout dan cin?",
  kw=["<<|insertion|sisipan", ">>|extraction|ekstrak|pengekstrakan"],
  ans="cout guna << (insertion), cin guna >> (extraction).",
  hint="Anak panah menghala ke mana data pergi.",
  fu=[F("""Lab 4 A1: `Cout < "The total is RM " < Total` salah kerana guna `<` (less-than) dan bukan `<<`.""",
        "Betulkan operator: `cout < \"Hi\";`",
        ans=["cout << \"Hi\";"],
        hint="Insertion operator ada dua simbol."),
      F("""Input `5 3` ke `cin >> length >> width;` kemudian cetak perimeter `2 * (length + width)`.""",
        "Apakah perimeter yang dicetak?",
        ans=["16", "perimeter = 16"],
        hint="2 × (5 + 3).")],
  mcq=M("Yang manakah membaca dua nilai dengan betul?",
        "cin >> a >> b;", "cin << a << b;", "cout >> a >> b;", "cin >> a, b;"))

S("cp08", T, "3.4 cin with char arrays and getline", trap=True,
  text="""
  **TRAP**: `cin >>` berhenti membaca pada **whitespace** (ruang, tab, enter).

  ```
  char word[21];
  string name;
  cin >> word;          // taip: Hello World
  cin >> name;
  ```
  `word` = `Hello`, dan `World` kekal dalam buffer lalu terus masuk ke `name` tanpa menunggu pengguna (Lab 4 C2).

  Untuk baca satu baris penuh guna `cin.getline(word, 21)` (C-string) atau `getline(cin, name)` (string).
  """,
  question="Apa yang berlaku apabila pengguna menaip `Hello World` ke `cin >> word;`?",
  kw=["hello", "space|ruang|whitespace|berhenti|stop",
      "world|buffer|baki|tinggal|remain|seterusnya|next"],
  ans="Hanya 'Hello' dibaca kerana cin berhenti pada ruang; 'World' kekal dalam buffer untuk input seterusnya.",
  hint="Apa yang cin buat apabila jumpa ruang?",
  fu=[F("""`cin.getline(arr, size)` membaca sehingga Enter, termasuk ruang.""",
        "Function apakah membaca satu baris penuh ke dalam char array?",
        ans=["cin.getline", "cin.getline()", "getline"],
        hint="cin.get…"),
      F("""`char word[21]` boleh simpan 20 aksara + `'\\0'` (null terminator).""",
        "Berapakah aksara maksimum yang boleh disimpan dalam `char word[21]`?",
        ans=["20"],
        hint="Satu ruang untuk null terminator.")],
  mcq=M("Pengguna taip 'Ali Baba' untuk `cin >> name;` (string). Nilai name ialah…",
        "Ali", "Ali Baba", "Baba", "Ralat"))

S("cp09", T, "3.5 Data types and sizes (slide 62)",
  """
  Saiz biasa (`sizeof`, dalam byte):

  | Type | Bytes | Julat |
  |---|---|---|
  | char | 1 | -128 hingga 127 |
  | short | 2 | -32768 hingga 32767 |
  | int | 4 | -2147483648 hingga 2147483647 |
  | long | 4 (Windows) / 8 (Linux) | |
  | float | 4 | ~6–7 digit, ±3.40282e+38 |
  | double | 8 | ~15 digit, ±1.79769e+308 |
  | bool | 1 | true (1) / false (0) |

  `sizeof(type)` memulangkan saiz dalam byte.
  """,
  "Berapakah saiz int dan double dalam byte?",
  kw=["int", "4|empat|four", "double", "8|lapan|eight"],
  ans="int = 4 byte, double = 8 byte.",
  hint="double dua kali ganda float.",
  fu=[F("""`long` berbeza mengikut OS: Windows 4 byte, Linux 8 byte (Lab 4 B4).""",
        "Berapakah saiz long di Windows?",
        ans=["4", "4 bytes", "4 byte"],
        hint="Sama dengan int di Windows."),
      F("""`char` 1 byte, julat -128 hingga 127.""",
        "Apakah nilai MAKSIMUM bagi signed char?",
        ans=["127"],
        hint="2^7 − 1.")],
  mcq=M("Jenis data manakah paling sesuai untuk menyimpan 3.14159 dengan ketepatan tinggi?",
        "double", "int", "char", "bool"))

S("cp10", T, "3.5 char vs string literal (slide 61)", trap=True,
  text="""
  - `'Z'` → **character literal** (single quotes), satu aksara, 1 byte.
  - `"Z"` → **string literal** (double quotes), aksara + `'\\0'` = 2 byte.

  **TRAP**:
  ```
  char letter = "Z";   // SALAH
  ```
  Ralat: `invalid conversion from 'const char*' to 'char'`. Betulkan: `char letter = 'Z';`
  """,
  question="Apakah beza 'Z' dan \"Z\"?",
  kw=["character|char|aksara", "single|tunggal|petik tunggal|'",
      "string|rentetan", "double|berganda|petik berganda|\"|null|\\0"],
  ans="'Z' ialah character literal (single quote, 1 aksara); \"Z\" ialah string literal (double quote, ada null terminator).",
  hint="Jenis petikan dan apa yang disimpan.",
  fu=[F("""Cari kesilapan: `char letter = "Z";`""",
        "Tulis baris yang betul.",
        ans=["char letter = 'Z';"],
        hint="Tukar jenis petikan."),
      F("""`"Z"` disimpan sebagai `'Z'` diikuti `'\\0'`.""",
        "Berapakah byte untuk string literal \"Z\"?",
        ans=["2", "2 bytes", "2 byte", "dua"],
        hint="Jangan lupa null terminator.")],
  mcq=M("Ralat `invalid conversion from 'const char*' to 'char'` berpunca daripada…",
        "char c = \"A\";", "char c = 'A';", "string s = \"A\";", "int c = 'A';"))

S("cp11", T, "3.5 ASCII codes",
  """
  Aksara disimpan sebagai **nombor ASCII**. `'A'` = 65, `'C'` = 67, `'a'` = 97, `'0'` = 48.

  ```
  char c = 'C';
  cout << int(c) << " " << char(c + 1);
  ```
  Output: `67 D`
  """,
  "Bagaimanakah char disimpan dalam komputer?",
  kw=["number|nombor|integer|integer|kod|code|numeric",
      "ascii"],
  ans="Sebagai nombor integer mengikut kod ASCII.",
  hint="'A' = 65.",
  fu=[F("""
        ```
        char c = 'C';
        cout << int(c) << " " << char(c + 1);
        ```""",
        "Apakah output?",
        ans=["67 D"],
        hint="'C' = 67, huruf selepas C."),
      F("""`'a'` = 97, iaitu 32 lebih daripada `'A'` (65).""",
        "Apakah kod ASCII 'a'?",
        ans=["97"],
        hint="65 + 32.")],
  mcq=M("`cout << int('A');` mencetak…",
        "65", "A", "97", "1"))

S("cp12", T, "3.5 Octal, hexadecimal and long literals", trap=True,
  text="""
  - Literal bermula dengan `0` → **octal** (asas 8): `075` = 7×8 + 5 = **61**.
  - Bermula dengan `0x` → **hexadecimal** (asas 16): `0x75A` = 7×256 + 5×16 + 10 = **1882**.
  - Akhiran `L` → **long**: `1234L` = 1234.

  **TRAP**: `075` BUKAN 75.
  """,
  question="Apakah nilai perpuluhan bagi literal `075`?",
  ans=["61"],
  hint="Bermula dengan 0 bermaksud octal (asas 8).",
  fu=[F("""`0x` = hexadecimal. A = 10.""",
        "Apakah nilai perpuluhan `0x75A`?",
        ans=["1882"],
        hint="7×256 + 5×16 + 10."),
      F("""Kod: `cout << 010 + 1;`""",
        "Apakah output?",
        ans=["9"],
        hint="010 dalam octal = 8.")],
  mcq=M("`cout << 012;` mencetak…",
        "10", "12", "0", "ralat"))

S("cp13", T, "3.6 Named constants: const vs #define (slides 63–66)", trap=True,
  text="""
  Dua cara buat pemalar:

  ```
  const double PI = 3.14159;   // ada jenis, mesti diberi nilai, ada ;
  #define PI 3.14159           // preprocessor, TIADA = dan TIADA ;
  ```

  - `PI = 3;` selepas `const` → ralat `assignment of read-only variable 'PI'`.
  - `PI = 3;` dengan `#define` → menjadi `3.14159 = 3;` → ralat `lvalue required as left operand of assignment`.
  - `#define PI 3.14159;` (ada `;`) → `;` ikut masuk ke setiap tempat PI digunakan → ralat sintaks.

  Pilihan disyorkan: **const**, kerana ada jenis data (type-checked) dan mengikut scope.
  """,
  question="Mengapakah `const` lebih disyorkan berbanding `#define`?",
  kw=["type|jenis|data type|type-checked|semak jenis",
      "scope|skop|compiler|safe|selamat|ralat|error|debug"],
  ans="const ada jenis data yang disemak compiler dan ikut scope; #define hanya penggantian teks oleh preprocessor.",
  hint="Siapa yang memproses #define? Adakah ia ada jenis?",
  fu=[F("""
        ```
        const double PI = 3.14159;
        PI = 3;
        ```""",
        "Apakah jenis ralat yang berlaku? (assignment of …)",
        ans=["assignment of read-only variable", "assignment of read-only variable 'PI'", "read-only", "read only"],
        hint="const = baca sahaja."),
      F("""Cari kesilapan: `#define PI 3.14159;`""",
        "Apakah simbol yang perlu dibuang?",
        ans=[";", "semicolon", "titik koma", "koma bertitik"],
        hint="#define bukan statement."),
      F("""Lab 4 B2: pemalar untuk formula cukai disimpan sebagai `const`.""",
        "Tulis pengisytiharan const untuk kadar cukai 0.25 bernama TAX_RATE (double).",
        ans=["const double TAX_RATE = 0.25;"],
        hint="const + jenis + nama = nilai;")],
  mcq=M("Yang manakah pengisytiharan pemalar yang BETUL?",
        "#define RATE 0.25", "#define RATE = 0.25;", "const RATE double = 0.25;", "const double RATE;"))

S("cp14", T, "3.6 The string class",
  """
  `string` ialah class C++ untuk teks. Perlu `#include <string>`.

  ```
  #include <string>
  string name = "Ali";
  cout << name;
  ```
  Berbeza dengan **C-string** (`char name[21]`) yang ditamatkan dengan `'\\0'`.
  """,
  "Apakah header yang diperlukan untuk menggunakan string class?",
  ans=["#include <string>", "<string>", "string"],
  hint="Nama header sama dengan nama jenis.",
  fu=[F("""`string` boleh diberi nilai dengan `=` dan dibanding dengan `==`. C-string tidak boleh (guna `strcpy`/`strcmp`, Bab 5).""",
        "Bolehkah dua C-string dibanding dengan `==`? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Bab 5: strcmp.")],
  mcq=M("Untuk `string name = \"Ali\";` header yang perlu ialah…",
        "<string>", "<cstring>", "<cmath>", "<cctype>"))

S("cp15", T, "3.7 Scope: declare before use (slide 74)", trap=True,
  text="""
  Pemboleh ubah mesti **diisytihar sebelum digunakan**. Scope bermula dari tempat pengisytiharan.

  ```
  int main()
  {
      cout << value;   // ralat
      int value;
      return 0;
  }
  ```
  Ralat: `'value' was not declared in this scope`. Program TIDAK compile.

  Lab 4 A1 juga: `average` digunakan sebelum `double average = total / 2.0;`.
  """,
  question="Adakah program di atas compile? Mengapa?",
  kw=["no|tidak|tak|not",
      "declare|diisytihar|declared|isytihar|pengisytiharan",
      "before|sebelum|after|selepas|scope|skop"],
  ans="Tidak. value digunakan sebelum diisytihar, jadi berada di luar scope.",
  hint="Lihat turutan dua baris dalam main.",
  fu=[F("""Betulkan dengan mengalihkan pengisytiharan ke atas dan beri nilai awal.""",
        "Apakah mesej ralat yang dipaparkan? ('value' was …)",
        ans=["'value' was not declared in this scope", "was not declared in this scope", "not declared in this scope", "not declared"],
        hint="… not declared in this scope.")],
  mcq=M("`cout << x; int x = 5;` menghasilkan…",
        "Ralat: x was not declared in this scope", "Output 5", "Output 0", "Output nilai sampah"))

S("cp16", T, "3.8 Arithmetic operators, / and %", trap=True,
  text="""
  Operator: `+  -  *  /  %`

  - **Integer division** buang bahagian perpuluhan (truncate): `13 / 5` = **2**, `46 / 9` = **5**.
  - **Modulus %** = baki (remainder): `13 % 5` = **3**. Hanya untuk integer.
  - Jika satu operand double: `10.0 / 4` = **2.5**.

  **TRAP**: `13 % 5` bukan 1 dan bukan 2.6. Ia baki: 13 = 5×2 + **3**.
  """,
  question="Apakah nilai 13 % 5?",
  ans=["3"],
  hint="13 = 5 × 2 + ?",
  fu=[F("""
        ```
        int a = 7, b = 2;
        cout << a / b << " " << a % b;
        ```""",
        "Apakah output?",
        ans=["3 1"],
        hint="Integer division dan baki."),
      F("""`cout << 10 / 4 << " " << 10.0 / 4;`""",
        "Apakah output?",
        ans=["2 2.5"],
        hint="Satu integer division, satu tidak.")],
  mcq=M("`cout << 17 / 5;` mencetak…",
        "3", "3.4", "2", "4"))

S("cp17", T, "3.8 Operator precedence",
  """
  Keutamaan (tinggi → rendah):

  1. `( )`
  2. Unary `-`, `++`, `--`, `!`
  3. `*  /  %` (kiri ke kanan)
  4. `+  -` (kiri ke kanan)
  5. `=  +=  -=  *=  /=  %=` (kanan ke kiri)

  ```
  int y = -5;
  int z = 8 - 3 + 9 / 2 + 2 * -y;     // 8 - 3 + 4 + 10 = 19
  z = 8 - (3 + 9 / 2) + 2 * -y;       // 8 - 7 + 10 = 11
  ```
  """,
  "Antara * dan +, operator manakah dinilai dahulu?",
  kw=["*|darab|multiply|multiplication|pendaraban"],
  ans="* (pendaraban) dinilai sebelum +.",
  hint="Sama seperti matematik.",
  fu=[F("""
        ```
        int y = -5;
        int z = 8 - 3 + 9 / 2 + 2 * -y;
        ```
        Langkah: `9 / 2` = 4 (integer), `-y` = 5, `2 * 5` = 10.""",
        "Apakah nilai z?",
        ans=["19", "z = 19"],
        hint="8 − 3 + 4 + 10."),
      F("""`z = 8 - (3 + 9 / 2) + 2 * -y;` dengan `y = -5`.""",
        "Apakah nilai z?",
        ans=["11", "z = 11"],
        hint="Kurungan dahulu: 3 + 4 = 7."),
      F("""Lab 4 A2 4b/4c: `46 % 9 + 4 * 4 - 2` dan `45 + 43 % 5 * (23 * 3 % 2)`.""",
        "Apakah nilai `45 + 43 % 5 * (23 * 3 % 2)`?",
        ans=["48"],
        hint="23*3 = 69, 69 % 2 = 1, 43 % 5 = 3, 3 * 1 = 3.")],
  mcq=M("Nilai `46 % 9 + 4 * 4 - 2` ialah…",
        "15", "5", "18", "40"))

S("cp18", T, "3.9 Mixed types and evaluation order", trap=True,
  text="""
  **TRAP**: susunan operand mengubah jawapan apabila integer division terlibat.

  ```
  cout << 7 / 2 * 2.0;   // (7/2)=3 → 3*2.0 = 6
  cout << 2.0 * 7 / 2;   // 2.0*7=14.0 → 14.0/2 = 7
  ```
  Penilaian kiri ke kanan. Integer division berlaku jika KEDUA-DUA operand ketika itu integer.
  """,
  question="Apakah output `cout << 7 / 2 * 2.0;`?",
  ans=["6"],
  hint="7 / 2 dikira dahulu, kedua-duanya int.",
  fu=[F("""`cout << 2.0 * 7 / 2;`""",
        "Apakah output?",
        ans=["7"],
        hint="2.0 * 7 = 14.0 (double).")],
  mcq=M("Ungkapan manakah menghasilkan 3.5?",
        "7.0 / 2", "7 / 2", "7 / 2 * 1.0", "(double)(7 / 2)"))

S("cp19", T, "3.9 Type conversion and casting (slides 87–91, 99–102)", trap=True,
  text="""
  **Type casting** menukar jenis secara eksplisit:

  ```
  int sum = 241;
  cout << sum / 3;                       // 80
  cout << static_cast<double>(sum) / 3;  // 80.3333
  ```
  `sum / 3` ialah integer division. Cast ditukar SEBELUM bahagi supaya hasilnya double.

  **TRAP**: `(double)(10 / 4)` = **2**, kerana bahagi berlaku dulu (integer), baru ditukar.

  Implicit conversion: nilai double yang diberi kepada int akan dipotong (`int x = 3.9;` → 3).
  """,
  question="Mengapa sum / 3 mencetak 80 tetapi static_cast<double>(sum) / 3 mencetak 80.3333?",
  kw=["integer|int|integer division|pembahagian integer",
      "truncate|buang|potong|decimal|perpuluhan|fraction",
      "cast|static_cast|double|tukar|convert"],
  ans="sum / 3 ialah integer division yang membuang perpuluhan; static_cast<double> menukar sum kepada double sebelum bahagi jadi perpuluhan dikekalkan.",
  hint="Apakah jenis kedua-dua operand dalam setiap kes?",
  fu=[F("""`cout << (double)(10 / 4);`""",
        "Apakah output?",
        ans=["2"],
        hint="Kurungan dalam dikira dahulu."),
      F("""Average tiga nombor 70, 80, 91: sum = 241.""",
        "Tulis ungkapan C++ yang mengira purata dengan perpuluhan menggunakan static_cast.",
        ans=["static_cast<double>(sum) / 3", "static_cast<double>(sum)/3", "static_cast<double>(sum) / 3.0"],
        hint="static_cast<jenis>(nilai) / 3")],
  mcq=M("`int x = 9.8;` menyimpan nilai…",
        "9", "10", "9.8", "Ralat"))

S("cp20", T, "3.10 Overflow (slides 94–98)", trap=True,
  text="""
  **Overflow**: nilai melebihi julat jenis data lalu "berpusing" (wrap around).

  - `unsigned char` 255 + 1 → **0**; 0 − 1 → **255**.
  - `short` 32767 + 1 → **-32768**.
  - Overflow `int` biasa (signed) ialah **undefined behaviour**: compiler boleh buat apa sahaja. Sebab itu Lab 4 guna `unsigned char`/`short` untuk demo.
  """,
  question="Apakah yang berlaku apabila unsigned char bernilai 255 ditambah 1?",
  kw=["0|sifar|zero", "wrap|pusing|overflow|limpahan|balik|kembali"],
  ans="Overflow: nilai berpusing (wrap around) menjadi 0.",
  hint="Julat unsigned char ialah 0 hingga 255.",
  fu=[F("""`short s = 32767; s++;`""",
        "Apakah nilai s?",
        ans=["-32768"],
        hint="Pusing ke nilai paling kecil."),
      F("""Overflow pada signed int tidak boleh dijangka.""",
        "Apakah istilah untuk overflow signed int dalam standard C++?",
        ans=["undefined behaviour", "undefined behavior", "ub", "undefined"],
        hint="un……… behaviour.")],
  mcq=M("`unsigned char u = 0; u--;` menjadikan u bernilai…",
        "255", "-1", "0", "Ralat compile"))

S("cp21", T, "3.11 Increment ++ and decrement -- (slides 103–108)", trap=True,
  text="""
  - **Prefix** `++x`: tambah dulu, kemudian guna nilai baru.
  - **Postfix** `x++`: guna nilai lama dulu, kemudian tambah.

  ```
  int count = 5, first = 10, second;
  second = 5 * count-- + first;   // 5*5+10 = 35, count jadi 4
  second = 5 * --count + first;   // count jadi 3, 5*3+10 = 25
  ```
  **TRAP**: dalam baris kedua count sudah 4 (bukan 5).
  """,
  question="Apakah beza ++x dan x++?",
  kw=["prefix|++x|sebelum|before|dulu|dahulu",
      "postfix|x++|selepas|after|kemudian",
      "value|nilai|guna|use|digunakan"],
  ans="++x (prefix) tambah dahulu kemudian guna nilai baru; x++ (postfix) guna nilai lama dahulu kemudian tambah.",
  hint="Fikir bila nilai itu DIGUNAKAN berbanding bila ia DITAMBAH.",
  fu=[F("""
        ```
        int count = 5, first = 10, second;
        second = 5 * count-- + first;
        ```""",
        "Apakah nilai second dan count? (tulis: second count)",
        ans=["35 4", "second = 35 count = 4", "35 dan 4"],
        hint="Postfix guna 5 dahulu."),
      F("""Sambungan: `second = 5 * --count + first;` (count sekarang 4).""",
        "Apakah nilai second dan count? (tulis: second count)",
        ans=["25 3", "second = 25 count = 3", "25 dan 3"],
        hint="Prefix: count jadi 3 dahulu."),
      F("""
        ```
        int x = 5;
        cout << x++ << " ";
        cout << x << " ";
        cout << ++x;
        ```""",
        "Apakah output?",
        ans=["5 6 7"],
        hint="Postfix, kemudian nilai semasa, kemudian prefix.")],
  mcq=M("`int a = 3; int b = a++ * 2;` Nilai a dan b ialah…",
        "a = 4, b = 6", "a = 4, b = 8", "a = 3, b = 6", "a = 3, b = 8"))

S("cp22", T, "3.11 Combined and multiple assignment",
  """
  Combined assignment: `x op= expr` bermaksud `x = x op (expr)`. Seluruh sebelah kanan dikira DAHULU.

  ```
  int i = 10, j = 2;
  i *= j + 3;              // i = 10 * (2 + 3) = 50

  int a = 1; double d = 1.0;
  d += 1.5 * 3 + (++a);    // d = 1.0 + (4.5 + 2) = 7.5, a = 2
  a = 1; d = 1.0;
  d -= 1.5 * 3 + a++;      // d = 1.0 - (4.5 + 1) = -4.5, a = 2

  a = 1;
  a %= 3 / a + 3;          // a = 1 % 6 = 1

  int x, p, q;
  x = p = q = 5;           // kanan ke kiri, x+p+q = 15
  ```
  """,
  "Apakah maksud `i *= j + 3;`?",
  kw=["i = i *|i=i*|i = i*|darab|multiply", "(j + 3)|(j+3)|kurungan|j + 3 dahulu|dulu|dahulu|keseluruhan|whole"],
  ans="i = i * (j + 3): sebelah kanan dikira dahulu, kemudian didarab dengan i.",
  hint="Kembangkan op= menjadi bentuk penuh.",
  fu=[F("""`int i = 10, j = 2; i *= j + 3;`""",
        "Apakah nilai i?",
        ans=["50"],
        hint="10 × 5."),
      F("""`int a = 1; double d = 1.0; d += 1.5 * 3 + (++a);`""",
        "Apakah nilai d dan a? (tulis: d a)",
        ans=["7.5 2", "d = 7.5 a = 2"],
        hint="++a = 2, 4.5 + 2 = 6.5, 1.0 + 6.5."),
      F("""`int a = 1; a %= 3 / a + 3;`""",
        "Apakah nilai a?",
        ans=["1"],
        hint="3/1 + 3 = 6, 1 % 6.")],
  mcq=M("`int x = 4; x -= 2 * 3;` Nilai x ialah…",
        "-2", "6", "2", "-6"))

S("cp23", T, "3.12 Default cout precision",
  """
  Secara lalai `cout` memaparkan **6 digit bererti** (significant digits).

  `0.25 * (4250.50 * 11 - 3 * 450)` = 11351.375 tetapi dicetak `11351.4`.

  `80.33333…` dicetak `80.3333`. Format lain (setprecision) diajar kemudian (Week 10).
  """,
  "Berapakah digit bererti yang dipaparkan cout secara lalai?",
  ans=["6", "enam", "six", "6 digits"],
  hint="80.3333 ada berapa digit?",
  fu=[F("""Nilai sebenar 11351.375.""",
        "Apakah yang dicetak oleh cout?",
        ans=["11351.4"],
        hint="Bundarkan kepada 6 digit bererti.")],
  mcq=M("`cout << 2.0 / 3;` mencetak…",
        "0.666667", "0.6666666667", "0.67", "0"))

S("cp24", T, "3.13 Reading compiler errors (Lab 4 A1)", trap=True,
  text="""
  Format mesej g++: `file.cpp:LINE:COLUMN: error: message`.

  Strategi:
  1. Betulkan **ralat PERTAMA sahaja**, kemudian compile semula. Satu kesilapan boleh menyembunyikan/menyebabkan ralat lain.
  2. **TRAP**: baris yang dilaporkan kadang-kadang **selepas** kesilapan sebenar. Contoh `using namespace std` tanpa `;` dilaporkan sebagai `expected ';' before 'int'` pada baris seterusnya.
  3. Compile dengan `-Wall -Wextra` dan anggap warning sebagai kesilapan.
  """,
  question="Mengapa kita patut betulkan ralat pertama sahaja dahulu, kemudian compile semula?",
  kw=["first|pertama", "hide|sembunyi|cause|sebab|menyebabkan|lain|other|cascade|berantai|palsu|false"],
  ans="Kerana satu kesilapan boleh menyebabkan atau menyembunyikan ralat lain; selepas betulkan yang pertama, ralat lain mungkin hilang.",
  hint="Satu kesilapan boleh menghasilkan banyak mesej.",
  fu=[F("""
        ```
        using namespace std
        int main()
        ```
        Compiler lapor `expected ';' before 'int'` pada baris `int main()`.""",
        "Di baris manakah kesilapan sebenar? (baris using / baris int main)",
        ans=["using", "baris using", "using namespace std", "baris sebelum", "sebelumnya"],
        hint="Mesej kata ';' sepatutnya ada SEBELUM int."),
      F("""Lab 4 A1: `#include iostream` → `#include expects "FILENAME" or <FILENAME>`.""",
        "Tulis baris #include yang betul untuk iostream.",
        ans=["#include <iostream>", "#include<iostream>"],
        hint="Nama fail dalam < >.")],
  mcq=M("Mesej `expected ';' before 'cout'` pada baris 10 biasanya bermaksud…",
        "Baris 9 tiada ;", "Baris 10 tiada ;", "cout salah eja", "Perlu #include <cmath>"))

S("cp25", T, "3.14 Using / and % for unit conversion (Lab 4 B3)",
  """
  Tukar saat → jam, minit, saat guna `/` dan `%` sahaja:

  ```
  int s = 3725;
  cout << s / 3600 << " h "
       << (s % 3600) / 60 << " min "
       << s % 60 << " s";
  ```
  Output: `1 h 2 min 5 s`
  """,
  "Bagaimana mendapatkan bilangan minit (selepas jam) daripada jumlah saat s?",
  ans=["(s % 3600) / 60", "s % 3600 / 60", "(s%3600)/60"],
  hint="Buang jam penuh dahulu dengan %, kemudian bahagi 60.",
  fu=[F("""s = 7384. 7384 / 3600 = 2, 7384 % 3600 = 184, 184 / 60 = 3, 7384 % 60 = 4.""",
        "Apakah output untuk s = 7384? (format: X h Y min Z s)",
        ans=["2 h 3 min 4 s"],
        hint="Guna pengiraan dalam nota.")],
  mcq=M("`int s = 3725; cout << s % 60;` mencetak…",
        "5", "62", "2", "1"))
