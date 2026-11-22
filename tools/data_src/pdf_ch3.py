from helpers import S, F, M

T = "cpp"
H = "3 · "

YES = ["yes", "ya", "boleh"]
NO = ["no", "tidak", "tak"]

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
  - `#include` is a **preprocessor directive** with **no `;`**.
  - The program **starts at `int main()`**.
  - `return 0;` tells the OS the program ended **"OK"**.
  """,
  "Where does a C++ program start, and what does `return 0;` mean?",
  kw=["main|int main|main()", "os|operating system|sistem operasi", "ok|berjaya|success|jayanya|selesai|successfully"],
  ans="The program starts at int main(); return 0 tells the OS the program ended OK.",
  hint="One required function; who does return 0 talk to?",
  fu=[F("""The sample program prints `"The sum is "` followed by sum (num1 = 5, num2 = 12).""",
        "What is the output of the sample program?",
        ans=["The sum is 17"],
        hint="5 + 12."),
      F("""`#include <iostream>` is a preprocessor directive and does **not** end with `;`.""",
        "True or false: `#include <iostream>;` needs a semicolon. (true / false)",
        ans=["false", "salah"],
        hint="(no ;)")],
  mcq=M("In a C++ program, `return 0;` in main…",
        "Tells the OS the program ended OK", "Prints 0", "Repeats the program", "Declares a variable"))

S("cp02", T, H + "Program elements · Keywords",
  """
  A program is made of: **keywords, identifiers, operators, punctuation**, following the **syntax**.

  **Keywords**: reserved words such as `int`, `return`.
  - **Always lowercase**.
  - You **can't use them as names**.
  """,
  "What is a keyword? Give two of its properties.",
  kw=["reserved|simpanan|khas|kata kunci",
      "lowercase|lower case|huruf kecil|kecil|small letters",
      "cannot|can't|cant|not as name|bukan nama|tidak boleh|tak boleh|name|names|nama"],
  ans="A reserved word such as int or return; always lowercase and can't be used as a name.",
  hint="Reserved, which case, usable as a name?",
  fu=[F("""Keywords are always lowercase, so `Int` and `RETURN` are not keywords.""",
        "Can `int` be used as a variable name? (yes / no)",
        ans=NO,
        hint="Reserved.")],
  mcq=M("Which is a C++ keyword?",
        "return", "num1", "Sum", "main1"))

S("cp03", T, H + "Program elements · Identifiers, operators, punctuation, syntax",
  """
  - **Identifiers**: names you choose, e.g. `num1`, `sum`.
  - **Operators**: `+ - * / =`
  - **Punctuation**: `;` `,`
  - **Syntax**: **the rules of the language**.
  """,
  "What do 'syntax' and 'identifier' mean?",
  kw=["syntax|sintaks", "rule|rules|peraturan|tatabahasa|grammar",
      "identifier|pengecam", "name|names|nama|choose|pilih|you|anda|programmer"],
  ans="Syntax is the rules of the language; an identifier is a name you choose (num1, sum).",
  hint="Rules vs names.",
  fu=[F("""Punctuation examples in the notes: `;` and `,`.""",
        "In `double num1 = 5, num2, sum;`, what category are `,` and `;`?",
        ans=["punctuation", "tanda baca"],
        hint="P…")],
  mcq=M("In `sum = num1 + num2;`, `num1` is an…",
        "Identifier", "Keyword", "Operator", "Punctuation"))

S("cp04", T, H + "REMEMBER: case-sensitive and braces",
  """
  ⚠ **REMEMBER**
  - C++ is **case-sensitive**: `Main` ≠ `main`.
  - Every `{` needs a `}`.
  """,
  "What does 'C++ is case-sensitive' mean? Give the example from the notes.",
  kw=["case|upper|lower|capital|uppercase|huruf besar|huruf kecil|besar",
      "different|berbeza|tidak sama|≠|not same|not the same|lain|distinct",
      "main"],
  ans="Upper and lower case letters are treated as different; e.g. Main ≠ main.",
  hint="The notes' example uses the name of the main function.",
  fu=[F("""A program with only `int Main()` (no `main`) cannot be linked into a program because `main` does not exist.""",
        "Are `Main` and `main` the same name? (yes / no)",
        ans=NO,
        hint="Case-sensitive."),
      F("""Every `{` needs a matching `}`.""",
        "How many `}` are needed if a program has 3 `{`?",
        ans=["3", "three", "tiga"],
        hint="One each.")],
  mcq=M("Which statement is TRUE?",
        "Main ≠ main in C++", "C++ ignores upper and lower case", "{ does not need }", "Keywords can be uppercase"))

S("cp05", T, H + "Special characters · comments and #",
  """
  | Char | Meaning |
  |---|---|
  | `//` `/* */` | **comments** |
  | `#` | **preprocessor directive** |
  """,
  "What does the `#` character mean in C++?",
  kw=["preprocessor|prapemproses|directive|arahan"],
  ans="It marks a preprocessor directive (e.g. #include).",
  hint="#include…",
  fu=[F("""`//` for a single-line comment, `/* */` for a multi-line comment.""",
        "Write the two comment symbols in C++.",
        kw=["//", "/*|*/"],
        ans="// and /* */",
        hint="Slashes.")],
  mcq=M("`/* */` is used for…",
        "Comments", "Preprocessor", "Strings", "A group of statements"))

S("cp06", T, H + "Special characters · < >, ( ), { }",
  """
  | Char | Meaning |
  |---|---|
  | `< >` | **file name in `#include`** |
  | `( )` | **function name** |
  | `{ }` | **group of statements** |
  """,
  "What are `{ }` for?",
  kw=["group|kumpulan|himpun|block|blok", "statement|statements|pernyataan|arahan"],
  ans="They group statements together.",
  hint="A block…",
  fu=[F("""`< >` in `#include <iostream>` holds the file name.""",
        "In `#include <iostream>`, what are the `< >` for?",
        kw=["file|fail", "name|nama|include"],
        ans="They hold the file name in #include.",
        hint="iostream is a…"),
      F("""`( )` follows a function name, e.g. `main()`.""",
        "Which symbols come after a function name?",
        ans=["( )", "()", "parentheses", "brackets", "kurungan"],
        hint="main…")],
  mcq=M("In `int main()`, the `( )` show…",
        "A function name", "A string", "A comment", "A single character"))

S("cp07", T, H + "Special characters · ;, \" \", ' '",
  """
  | Char | Meaning |
  |---|---|
  | `;` | **ends a statement** |
  | `" "` | **string** |
  | `' '` | **single character** |
  """,
  "What is the difference between `\" \"` and `' '`?",
  kw=["string|rentetan|text|teks", "single|one|satu|tunggal", "character|aksara|char"],
  ans="\" \" is for a string; ' ' is for a single character.",
  hint="How many characters?",
  fu=[F("""`;` marks **the end of a statement**.""",
        "What does `;` do?",
        kw=["end|ends|tamat|akhir|habis|tamatkan|menamatkan|terminate|terminates", "statement|pernyataan|arahan"],
        ans="It ends a statement.",
        hint="Like a full stop in a sentence.")],
  mcq=M("Which one is a single character?",
        "'C'", "\"C\"", "C", "{C}"))

S("cp08", T, H + "Variables",
  """
  A **variable** is a **named memory location**.
  - You must **declare it before using it**.
  - A new value **overwrites** the old one.
  """,
  "What is a variable? Give two rules about it.",
  kw=["named|bernama|nama|name", "memory|memori|location|lokasi",
      "declare|declared|isytihar|diisytihar|before|sebelum",
      "overwrite|overwrites|replace|replaces|ganti|tulis ganti|old|lama"],
  ans="A named memory location; it must be declared before use, and a new value overwrites the old one.",
  hint="Definition + declare + new value.",
  fu=[F("""
        ```
        int x = 3;
        x = 8;
        cout << x;
        ```""",
        "What is the output?",
        ans=["8"],
        hint="The new value replaces the old one.")],
  mcq=M("A variable is…",
        "A named memory location", "A fixed value in the code", "A keyword", "A comment"))

S("cp09", T, H + "Identifier rules",
  """
  **Identifier rules**: start with a **letter or `_`**, then **letters, digits or `_`**. **No keywords** and **no symbols**.
  """,
  "State the rules for naming an identifier.",
  kw=["letter|letters|huruf|abjad", "_|underscore|garis bawah",
      "digit|digits|number|nombor|angka", "keyword|keywords|kata kunci|reserved",
      "symbol|symbols|simbol"],
  ans="Start with a letter or _, then letters, digits or _; no keywords and no symbols.",
  hint="First character, following characters, two bans.",
  fu=[F("""First character: a letter or `_` only.""",
        "Can an identifier start with an underscore? (yes / no)",
        ans=YES,
        hint="Letter or _.")],
  mcq=M("An identifier can start with…",
        "A letter or _", "A digit", "$", "#"))

S("cp10", T, H + "Identifier table · valid and invalid",
  """
  | Identifier | Valid? | Reason |
  |---|---|---|
  | `totalSales` / `total_Sales` | ✅ | |
  | `total.Sales` | ❌ | `"."` not allowed |
  | `4thQtrSales` | ❌ | starts with a digit |
  | `totalSale$` | ❌ | `"$"` not allowed |
  """,
  "`4thQtrSales`: valid or invalid?",
  ans=["invalid", "tidak sah"],
  hint="Look at the first character.",
  fu=[F("""`total.Sales`: the dot is not allowed.""",
        "Why is `total.Sales` invalid?",
        kw=[".|dot|period|full stop|titik", "not allowed|tidak dibenarkan|tak boleh|tidak boleh|symbol|simbol|can't|cannot"],
        ans="The dot (.) is not allowed.",
        hint="The character in the middle."),
      F("""`totalSale$`: the `$` symbol is not allowed.""",
        "`totalSale$`: valid or invalid?",
        ans=["invalid", "tidak sah"],
        hint="The symbol at the end."),
      F("""`total_Sales` contains only letters and `_`.""",
        "`total_Sales`: valid or invalid?",
        ans=["valid", "sah"],
        hint="Underscores are allowed.")],
  mcq=M("Which identifier is VALID?",
        "total_Sales", "total.Sales", "4thQtrSales", "totalSale$"))

S("cp11", T, H + "Literals",
  """
  **Literal** = a value written directly in the code: `12`, `"hello"`, `'C'`.
  """,
  "What is a literal? Give an example.",
  kw=["value|nilai", "directly|terus|written|ditulis|code|kod", "12|hello|'c'|c"],
  ans="A value written directly in the code, e.g. 12, \"hello\", 'C'.",
  hint="Not a name, but a value.",
  fu=[F("""In `double num1 = 5, num2, sum; num2 = 12;`, the values written directly are literals.""",
        "Name the literal in `num2 = 12;`.",
        ans=["12"],
        hint="A number.")],
  mcq=M("Which is NOT a literal?",
        "sum", "12", "\"hello\"", "'C'"))

S("cp12", T, H + "Input & output · cout and cin",
  """
  - `cout <<` sends output to the screen: `cout << "Hi" << endl;`
  - `cin >>` reads from the keyboard: `cin >> height >> width;`
  - New line: **`endl`** or **`"\\n"`** (inside the string).
  - Separate input values with **spaces**. **Always show a prompt first.**
  """,
  "What do cout and cin do, and which operators do they use?",
  kw=["cout", "<<|output|screen|skrin|display|papar|print",
      "cin", ">>|input|keyboard|papan kekunci|read|reads|baca"],
  ans="cout << sends output to the screen; cin >> reads input from the keyboard.",
  hint="One goes out, one comes in.",
  fu=[F("""Two ways to start a new line: `endl` or `"\\n"`.""",
        "Apart from endl, what else starts a new line?",
        ans=["\"\\n\"", "\\n", "'\\n'"],
        hint="Backslash…"),
      F("""Before `cin`, always show a **prompt**, e.g. `cout << "Enter height and width: ";`""",
        "What must be shown before every cin?",
        ans=["prompt", "a prompt", "gesaan"],
        hint="P…")],
  mcq=M("Which line reads two values correctly?",
        "cin >> height >> width;", "cin << height << width;", "cout >> height;", "cin >> height, width;"))

S("cp13", T, H + "Memory trick: arrows point where the data goes",
  """
  💡 **MEMORY TRICK**: the arrows point **where the data goes**.

  - `cout <<` **pushes** data **out to the screen**.
  - `cin >>` **pulls** data **in to the variable**.
  """,
  "Explain the cout/cin arrows memory trick.",
  kw=["arrow|arrows|anak panah|panah|point|tunjuk",
      "data|go|goes|pergi|where|ke mana",
      "out|keluar|screen|skrin|push|pushes|tolak",
      "in|masuk|variable|pemboleh ubah|pull|pulls|tarik"],
  ans="The arrows point where the data goes: cout << pushes data out to the screen; cin >> pulls data in to the variable.",
  hint="Arrow direction = data direction.",
  fu=[F("""In `cin >> x`, the arrows point towards `x`.""",
        "In `cin >> x`, where does the data go?",
        ans=["x", "into x", "to x", "variable x", "the variable x"],
        hint="Follow the >>.")],
  mcq=M("According to the memory trick, `cout <<`…",
        "Pushes data out to the screen", "Pulls data in to the variable", "Clears the screen", "Reads a file"))

S("cp14", T, H + "Data types · char",
  """
  **char**: one character, **1 byte**. e.g. `'C'` (stored as **67**).
  """,
  "What is the size of a char and how is 'C' stored?",
  kw=["1 byte|1|one byte|satu byte", "67|ascii|number|nombor"],
  ans="1 byte; 'C' is stored as the number 67.",
  hint="One byte; the numeric code of 'C'.",
  fu=[F("""`'C'` is stored as 67. The next letter `'D'` = 68.""",
        "What is the output of `cout << int('C');`?",
        ans=["67"],
        hint="See the note."),
      F("""In arithmetic, `'A' + 1` becomes an int: 65 + 1.""",
        "What is the output of `cout << 'A' + 1;`?",
        ans=["66"],
        hint="char becomes int in arithmetic.")],
  mcq=M("`'C'` is stored in memory as…",
        "67", "3", "99", "'C' only, no number"))

S("cp15", T, H + "Data types · bool",
  """
  **bool**: `true` / `false`, **1 byte**. `true` = **1**, `false` = **0**.
  """,
  "What are the integer values of true and false?",
  kw=["true", "1|one|satu", "false", "0|zero|sifar"],
  ans="true = 1, false = 0.",
  hint="One and zero.",
  fu=[F("""bool is 1 byte.""",
        "What is the size of bool in bytes?",
        ans=["1", "1 byte", "one"],
        hint="Same as char.")],
  mcq=M("`cout << true;` prints…",
        "1", "true", "0", "T"))

S("cp16", T, H + "Data types · short / int / long",
  """
  **short / int / long**: whole numbers, sizes **2 / 4 / 4** bytes. e.g. `12`, `-6`.
  """,
  "What are the sizes of short, int and long in the notes?",
  ans=["2/4/4", "2 4 4", "2, 4, 4", "2 bytes 4 bytes 4 bytes"],
  hint="Format: short/int/long.",
  fu=[F("""int holds whole numbers such as `12` and `-6`, in 4 bytes.""",
        "What is the size of int in bytes?",
        ans=["4", "4 bytes", "4 byte"],
        hint="The middle value of 2/4/4.")],
  mcq=M("The type that holds whole numbers is…",
        "int", "float", "double", "bool"))

S("cp17", T, H + "Data types · float and double",
  """
  | Type | Holds | Size | Example |
  |---|---|---|---|
  | float | decimals (~7 digits) | 4 bytes | `3.14F` |
  | double | decimals (~15 digits) | 8 bytes | `3.14` (**default**) |

  A decimal literal without a suffix is a **double** by default; add **`F`** for a float.
  """,
  "What is the difference between float and double?",
  kw=["float", "7|seven|4 byte|4 bytes", "double", "15|fifteen|8 byte|8 bytes|default"],
  ans="float holds ~7 digits in 4 bytes (3.14F); double holds ~15 digits in 8 bytes and is the default for decimals (3.14).",
  hint="Compare digits of precision and size.",
  fu=[F("""`3.14` is a double (default). `3.14F` is a float.""",
        "What type is the literal `3.14F`?",
        ans=["float"],
        hint="The F suffix."),
      F("""double: ~15 digits of precision.""",
        "What is the size of double in bytes?",
        ans=["8", "8 bytes", "8 byte"],
        hint="Twice a float.")],
  mcq=M("The literal `3.14` (no suffix) has type…",
        "double", "float", "int", "long"))

S("cp18", T, H + "Data types · string",
  """
  **string**: text, needs **`#include <string>`**, size varies. e.g. `"George"`.
  """,
  "Which header is needed for the string type?",
  ans=["#include <string>", "<string>", "string"],
  hint="Same name as the type.",
  fu=[F("""Example string value in the notes: `"George"`.""",
        "Declare a string variable called name with the value George.",
        ans=["string name = \"George\";"],
        hint="string name = …;")],
  mcq=M("The size of a string is…",
        "It varies", "1 byte", "4 bytes", "8 bytes"))

S("cp19", T, H + "Data types · 'C' vs \"C\"",
  """
  - `'C'` = a **character**.
  - `"C"` = a **string**, stored as **C + `\\0`**.
  """,
  "What is the difference between 'C' and \"C\"?",
  kw=["character|char|aksara", "string|rentetan", "\\0|null|nul|terminator"],
  ans="'C' is a character; \"C\" is a string stored as C + \\0.",
  hint="One has an extra character at the end.",
  fu=[F("""`"C"` = `'C'` + `'\\0'`, so it takes 2 characters.""",
        "How many characters are stored for \"C\"?",
        ans=["2", "two"],
        hint="C and \\0."),
      F("""Find the mistake: `char grade = "A";`""",
        "Write the correct line.",
        ans=["char grade = 'A';"],
        hint="char needs single quotes.")],
  mcq=M("`\"C\"` is stored as…",
        "C + \\0", "C only", "67", "'C'"))

S("cp20", T, H + "Data types · C-string",
  """
  **C-string**: `char name[21];` holds **20 characters + `\\0`**.
  """,
  "How many characters can `char name[21];` hold?",
  ans=["20", "20 characters"],
  hint="One slot is for \\0.",
  fu=[F("""To hold a name of up to 30 characters, you need 30 + 1 for `\\0`.""",
        "Declare a C-string `name` for 30 characters.",
        ans=["char name[31];"],
        hint="char name[…];")],
  mcq=M("`char code[6];` can hold how many characters (besides \\0)?",
        "5", "6", "7", "4"))

S("cp21", T, H + "Data types · truncation",
  """
  A decimal value assigned to an **int** is **truncated, not rounded**:

  `int r = 3.88;` gives **3**.
  """,
  "What is r after `int r = 3.88;`?",
  ans=["3"],
  hint="Truncated, not rounded.",
  fu=[F("""Truncation cuts off the decimal part, whether it is .88 or .1.""",
        "Why is the result not 4?",
        kw=["truncate|truncated|truncation|potong|dipotong|cut|chop",
            "not round|not rounded|bukan bundar|tidak dibundarkan|round|rounded|bundar"],
        ans="Because the value is truncated, not rounded.",
        hint="Not rounding.")],
  mcq=M("`int x = 9.99;` stores…",
        "9", "10", "9.99", "An error"))

S("cp22", T, H + "Data types · number bases",
  """
  Number bases:
  - **decimal** (10)
  - **binary** (2)
  - **octal** (8): starts with **`0`**, e.g. `075`
  - **hex** (16): starts with **`0x`**, e.g. `0x75A`

  `1234L` = **long**.
  """,
  "How are octal and hex literals written in C++?",
  kw=["octal|oktal", "0|starts with 0|bermula 0|075|zero",
      "hex|hexadecimal|heksadesimal", "0x|0x75a"],
  ans="Octal starts with 0 (075); hex starts with 0x (0x75A).",
  hint="One prefix is 0, the other is 0x.",
  fu=[F("""`075` = 7×8 + 5 = 61 (octal).""",
        "What is the decimal value of `075`?",
        ans=["61"],
        hint="Base 8."),
      F("""The `L` suffix makes the literal a long.""",
        "What type is `1234L`?",
        ans=["long"],
        hint="L…")],
  mcq=M("The literal `0x75A` is in base…",
        "16 (hex)", "8 (octal)", "2 (binary)", "10 (decimal)"))

S("cp23", T, H + "Data types · sizeof",
  """
  **`sizeof(type)`** gives the size in **bytes**.

  e.g. `sizeof(char)` = 1, `sizeof(int)` = 4, `sizeof(double)` = 8.
  """,
  "What does sizeof do?",
  kw=["size|saiz", "byte|bytes|bait", "type|jenis|variable"],
  ans="It gives the size of a type (or variable) in bytes.",
  hint="Unit: bytes.",
  fu=[F("""`cout << sizeof(double);`""",
        "What is the output?",
        ans=["8"],
        hint="See the data types table."),
      F("""`cout << sizeof(char) << sizeof(int);`""",
        "What is the output?",
        ans=["14"],
        hint="1 then 4, no space.")],
  mcq=M("`sizeof(int)` usually returns…",
        "4", "2", "8", "1"))

S("cp24", T, H + "Constants",
  """
  ```
  const double PI = 3.14159;   // typed, preferred
  #define PI 3.14159           // no = and no ;
  ```
  - A constant's value **cannot change**.
  - By convention it is written in **UPPERCASE**.
  - `const` is **preferred** (it is **typed**). `#define` has **no `=` and no `;`**.
  """,
  "What are the two ways to write a constant, and which is preferred?",
  kw=["const", "#define|define",
      "preferred|prefer|recommended|better|disyorkan|typed|type|jenis"],
  ans="const double PI = 3.14159; (typed, preferred) and #define PI 3.14159 (no = and no ;).",
  hint="One has a data type, one is a preprocessor line.",
  fu=[F("""Find the mistake: `#define PI = 3.14159;`""",
        "Write the correct #define line.",
        ans=["#define PI 3.14159"],
        hint="No = and no ;"),
      F("""Convention: constant names are uppercase, e.g. `PI`, `TAX_RATE`.""",
        "By convention, constant names are written in which case?",
        ans=["uppercase", "upper case", "capital letters", "capitals", "huruf besar"],
        hint="UPPER…"),
      F("""`const double PI = 3.14159;` then `PI = 3;` → error, because a constant can't change.""",
        "Can PI be changed after `const double PI = 3.14159;`? (yes / no)",
        ans=NO,
        hint="It's a constant.")],
  mcq=M("Which is correct?",
        "#define PI 3.14159", "#define PI = 3.14159;", "const PI double = 3.14159;", "#define PI 3.14159;"))

S("cp25", T, H + "Assignment",
  """
  - `size = 5;` ✅
  - `5 = size;` ❌ (**the variable must be on the left**)
  """,
  "Why is `5 = size;` wrong?",
  kw=["variable|pemboleh ubah|pembolehubah", "left|kiri|left side|left-hand"],
  ans="The variable must be on the left of the =.",
  hint="Who receives the value?",
  fu=[F("""g++ error for `5 = size;`: `lvalue required as left operand of assignment`.""",
        "Rewrite `5 = size;` correctly.",
        ans=["size = 5;"],
        hint="Swap the sides.")],
  mcq=M("Which assignment is VALID?",
        "total = a + b;", "a + b = total;", "5 = x;", "10 = 10;"))

S("cp26", T, H + "Initialisation",
  """
  **Initialise** (give a starting value) when declaring:

  `int width = 7, height = 5, area;`

  (`width` and `height` are initialised; `area` is not.)
  """,
  "In `int width = 7, height = 5, area;`, which variable is NOT initialised?",
  ans=["area"],
  hint="The one with no = value.",
  fu=[F("""Initialisation = giving a value at declaration.""",
        "Declare an int called count with starting value 0.",
        ans=["int count = 0;"],
        hint="int count = …;")],
  mcq=M("Which is an example of initialisation?",
        "int width = 7;", "width = 7;", "int width;", "cin >> width;"))

S("cp27", T, H + "Scope",
  """
  **Scope**: you **can't use a variable before the line where it is declared**.
  """,
  "What is the scope rule in the notes?",
  kw=["before|sebelum|earlier", "declare|declared|declaration|isytihar|diisytihar|pengisytiharan",
      "cannot|can't|cant|tidak boleh|tak boleh|use|guna|not"],
  ans="You can't use a variable before the line where it is declared.",
  hint="Order of lines.",
  fu=[F("""
        ```
        cout << value;
        int value = 4;
        ```""",
        "Does this code compile? (yes / no)",
        ans=NO,
        hint="value is used before it is declared.")],
  mcq=M("`cout << n; int n = 2;` gives…",
        "Error: n was not declared in this scope", "2", "0", "A garbage value"))

S("cp28", T, H + "Arithmetic operators · + − *",
  """
  With 7 and 3:

  | Op | 7 ? 3 |
  |---|---|
  | `+` | 10 |
  | `−` | 4 |
  | `*` | 21 |
  """,
  "What is 7 * 3?",
  ans=["21"],
  hint="Multiply.",
  fu=[F("""`cout << 7 + 3 << " " << 7 - 3;`""",
        "What is the output?",
        ans=["10 4"],
        hint="Add and subtract.")],
  mcq=M("`7 - 3` is…",
        "4", "10", "21", "-4"))

S("cp29", T, H + "Arithmetic operators · / integer division",
  """
  `7 / 3` = **2**: **int ÷ int = integer division** (the decimal part is dropped).

  If one side is a decimal: `13 / 5.0` = **2.6**.
  """,
  "What is 7 / 3 in C++?",
  ans=["2"],
  hint="int ÷ int.",
  fu=[F("""`13 / 5.0`: one operand is a double, so it is not integer division.""",
        "What is 13 / 5.0?",
        ans=["2.6"],
        hint="The decimal part is kept."),
      F("""`13 / 5` (both int).""",
        "What is 13 / 5?",
        ans=["2"],
        hint="Integer division.")],
  mcq=M("int ÷ int in C++ gives…",
        "Integer division (decimal part dropped)", "The full decimal value", "A rounded value", "An error"))

S("cp30", T, H + "Arithmetic operators · % remainder",
  """
  `7 % 3` = **1**: the **remainder**. `%` **works on integers only**.
  """,
  "What is 7 % 3?",
  ans=["1"],
  hint="7 = 3 × 2 + ?",
  fu=[F("""`%` works on integers only. `7.5 % 2` is a compile error.""",
        "Can % be used with a double? (yes / no)",
        ans=NO,
        hint="Integers only."),
      F("""`13 % 5`: 13 = 5 × 2 + 3.""",
        "What is 13 % 5?",
        ans=["3"],
        hint="The remainder.")],
  mcq=M("`%` in C++ gives the…",
        "Remainder", "Percentage", "Decimal quotient", "Power"))

S("cp31", T, H + "Order of operations",
  """
  ✔ **ORDER OF OPERATIONS**

  `( )` → **unary −** (right to left) → `* / %` (left to right) → `+ −` (left to right)

  - `2 + 2 * 2 - 2` = **4**
  - `(2 + 2) * 2 - 2` = **6**
  """,
  "Write the order of precedence for arithmetic operators.",
  kw=["( )|()|parentheses|brackets|bracket|kurungan",
      "unary|unari|negative|negatif",
      "* / %|*|multiply|multiplication|divide|darab|bahagi",
      "+ −|+ -|+|add|addition|subtract|tambah|tolak"],
  ans="( ) → unary − → * / % → + −",
  hint="Brackets first, add/subtract last.",
  fu=[F("""`2 + 2 * 2 - 2`: 2 * 2 first = 4, then 2 + 4 − 2.""",
        "What is `2 + 2 * 2 - 2`?",
        ans=["4"],
        hint="Multiply first."),
      F("""`(2 + 2) * 2 - 2`: brackets first.""",
        "What is `(2 + 2) * 2 - 2`?",
        ans=["6"],
        hint="4 × 2 − 2."),
      F("""Unary − is evaluated right to left; `* / %` and `+ −` left to right.""",
        "In which direction are `* / %` evaluated?",
        ans=["left to right", "kiri ke kanan"],
        hint="Like reading.")],
  mcq=M("The value of `10 - 4 / 2 * 3` is…",
        "4", "9", "1", "6"))

S("cp32", T, H + "No ^ operator: use pow",
  """
  C++ has **no `^` operator** for powers. Use **`pow(s, 2)`** (needs `<cmath>`).
  """,
  "How do you write s squared in C++?",
  ans=["pow(s, 2)", "pow(s,2)", "s * s", "s*s"],
  hint="There is no ^.",
  fu=[F("""`pow(x, y)` = x to the power y.""",
        "What is the output of `cout << pow(2, 3);`?",
        ans=["8"],
        hint="2 × 2 × 2.")],
  mcq=M("To compute x² in C++, use…",
        "pow(x, 2)", "x ^ 2", "x ** 2", "x²"))

S("cp33", T, H + "Type conversion · promotion",
  """
  **Promotion**: the **lower type is converted up to the higher type**.

  Order: `int < unsigned int < long < unsigned long < float < double < long double`
  """,
  "What is promotion in type conversion?",
  kw=["lower|rendah|smaller|kecil", "higher|tinggi|bigger|besar|up|naik", "convert|converted|tukar|ditukar|promote|promoted"],
  ans="In an expression, the lower type is converted up to the higher type.",
  hint="Low → high.",
  fu=[F("""In `5 / 2.0`, the int 5 is promoted to double.""",
        "In `int + double`, what is the type of the result?",
        ans=["double"],
        hint="The higher one."),
      F("""Order: int < unsigned int < long < unsigned long < float < double < long double.""",
        "Which is the HIGHEST type in the promotion order?",
        ans=["long double"],
        hint="Higher than double.")],
  mcq=M("In the promotion order, which is higher than float?",
        "double", "long", "int", "unsigned long"))

S("cp34", T, H + "Type conversion · char/short in arithmetic, and =",
  """
  - `char` and `short` **become `int`** in arithmetic.
  - With `=`, the result **takes the type of the left-hand variable**.

  e.g. `int x = 7 / 2.0;` → the right side is 3.5 (double) but x is an int → **3**.
  """,
  "With =, which type does the final result take?",
  kw=["left|kiri|left-hand", "variable|pemboleh ubah|type|jenis"],
  ans="The type of the variable on the left-hand side.",
  hint="Who receives the value?",
  fu=[F("""`int x = 7 / 2.0;`""",
        "What is x?",
        ans=["3"],
        hint="3.5 stored in an int."),
      F("""`char c = 'A'; cout << c + 1;` → char becomes int in arithmetic.""",
        "What is the output?",
        ans=["66"],
        hint="'A' = 65.")],
  mcq=M("In arithmetic, char and short are converted to…",
        "int", "double", "bool", "string"))

S("cp35", T, H + "Type conversion · manual cast",
  """
  **Manual cast**:
  - `static_cast<double>(a) / b` (**preferred**)
  - `(int)ch`
  - `int(ch)`
  """,
  "Write the preferred cast that converts a to double before dividing by b.",
  ans=["static_cast<double>(a) / b", "static_cast<double>(a)/b"],
  hint="static_cast<…>(…)",
  fu=[F("""`int a = 7, b = 2; cout << static_cast<double>(a) / b;`""",
        "What is the output?",
        ans=["3.5"],
        hint="7.0 / 2."),
      F("""`char ch = 'C'; cout << (int)ch;`""",
        "What is the output?",
        ans=["67"],
        hint="The code of 'C'.")],
  mcq=M("The cast preferred in the notes is…",
        "static_cast<double>(a)", "(double)a", "double(a)", "a.toDouble()"))

S("cp36", T, H + "Type conversion · overflow/underflow",
  """
  **Overflow/underflow**: a value **too big or too small** for the type **"wraps around"**.

  e.g. `short s = 32767; s++;` → **-32768**.
  """,
  "What happens on overflow?",
  kw=["too big|too large|too small|terlalu besar|terlalu kecil|big|small|exceed|exceeds|range|julat",
      "wrap|wraps|wrap around|wraps around|pusing|berpusing"],
  ans="A value too big or too small for the type wraps around.",
  hint="Like a car's odometer.",
  fu=[F("""`short s = 32767; s++;` (short range: −32768 to 32767).""",
        "What is s?",
        ans=["-32768"],
        hint="Wraps to the smallest value.")],
  mcq=M("Overflow means the value…",
        "Is too big for the type and wraps around", "Is rounded", "Always becomes 0", "Is converted to double"))

S("cp37", T, H + "Increment · prefix vs postfix",
  """
  - **Prefix `++x`**: **change first, then use**.
  - **Postfix `x++`**: **use first, then change**.
  """,
  "What is the difference between ++x and x++?",
  kw=["prefix|++x", "change first|change|ubah dahulu|tambah dahulu|dahulu|first|before",
      "postfix|x++", "use first|use|guna dahulu|then change|after|later|kemudian|selepas"],
  ans="++x (prefix) changes first, then uses the value; x++ (postfix) uses the value first, then changes it.",
  hint="Change-then-use vs use-then-change.",
  fu=[F("""
        ```
        int x = 5;
        cout << x++ << " ";
        cout << x;
        ```""",
        "What is the output?",
        ans=["5 6"],
        hint="Postfix uses 5 first."),
      F("""
        ```
        int x = 5;
        cout << ++x;
        ```""",
        "What is the output?",
        ans=["6"],
        hint="Prefix.")],
  mcq=M("`int a = 3; int b = ++a;` → b =",
        "4", "3", "5", "An error"))

S("cp38", T, H + "Increment · kira example",
  """
  `kira = 5`:

  `5 * kira-- + 10` = **35**, and **kira becomes 4**.

  (Postfix: use 5 first → 5 × 5 + 10 = 35, then kira − 1.)
  """,
  "With kira = 5, what is `5 * kira-- + 10`?",
  ans=["35"],
  hint="Postfix: use 5 first.",
  fu=[F("""After the expression `5 * kira-- + 10` with kira = 5.""",
        "What is kira afterwards?",
        ans=["4"],
        hint="Decreased by one."),
      F("""Switch to prefix: `5 * --kira + 10` with kira = 5.""",
        "What is the value?",
        ans=["30"],
        hint="kira becomes 4 first.")],
  mcq=M("kira = 5. `5 * kira-- + 10` gives…",
        "35, kira = 4", "30, kira = 4", "35, kira = 5", "30, kira = 5"))

S("cp39", T, H + "Combined assignment",
  """
  | Short | Means |
  |---|---|
  | `i += 3` | `i = i + 3` |
  | `i *= j+3` | `i = i * (j+3)` |
  """,
  "What is the long form of `i *= j+3`?",
  ans=["i = i * (j+3)", "i = i * (j + 3)"],
  hint="The whole right-hand side goes in brackets.",
  fu=[F("""`int i = 10, j = 2; i *= j + 3;`""",
        "What is i?",
        ans=["50"],
        hint="10 × 5."),
      F("""`int i = 4; i += 3;`""",
        "What is i?",
        ans=["7"],
        hint="i = i + 3.")],
  mcq=M("`i -= 2` means…",
        "i = i - 2", "i = 2 - i", "i = -2", "i == i - 2"))

S("cp40", T, H + "Chained assignment",
  """
  `x = y = z = 5` **assigns right to left**: z = 5, then y = z, then x = y.
  """,
  "In which direction is `x = y = z = 5` evaluated?",
  ans=["right to left", "kanan ke kiri"],
  hint="It starts with z.",
  fu=[F("""`int x, y, z; x = y = z = 5; cout << x + y + z;`""",
        "What is the output?",
        ans=["15"],
        hint="All are 5.")],
  mcq=M("After `x = y = z = 5;`, x is…",
        "5", "0", "Undefined", "15"))
