from helpers import S, F, M

T = "func"
H = "5 · "

NO = ["no", "tidak", "tak"]

S("fn01", T, H + "Modular programming",
  """
  **Modular programming** means splitting a program into **small functions**. This makes it easier to **write, read and maintain**.

  Ideally, **`main()` is short** and mostly **calls other functions**.
  """,
  "What is modular programming and what are its benefits?",
  kw=["split|splitting|break|small|divide|pecah|pecahkan|kecil|bahagi",
      "function|functions|fungsi",
      "write|read|maintain|easier|tulis|baca|selenggara|mudah"],
  ans="Splitting a program into small functions so it is easier to write, read and maintain.",
  hint="Three benefits: write, read, …",
  fu=[F("""Ideally `main()` is short and mostly calls other functions.""",
        "What does an ideal main() look like in modular programming?",
        kw=["short|small|pendek|ringkas", "call|calls|panggil|memanggil"],
        ans="Short, and mostly calls other functions.",
        hint="Long or short?")],
  mcq=M("In good modular programming, main()…",
        "Is short and mostly calls other functions", "Contains all the code", "Does not exist", "Must be void"))

S("fn02", T, H + "Library functions · <cmath>",
  """
  **`<cmath>`**: `pow(x,y)`, `sqrt(x)`, `abs(x)`, `sin`, `cos`, `tan`, `log`. These **take and return double**.
  """,
  "Which header is needed for pow and sqrt?",
  ans=["<cmath>", "cmath", "#include <cmath>"],
  hint="c + math.",
  fu=[F("""`cout << pow(2, 3) << " " << sqrt(25);`""",
        "What is the output?",
        ans=["8 5"],
        hint="2³ and √25."),
      F("""`<cmath>` functions take and return **double**.""",
        "What type does sqrt return?",
        ans=["double"],
        hint="A decimal type.")],
  mcq=M("Which function is in <cmath>?",
        "sqrt", "strlen", "toupper", "rand"))

S("fn03", T, H + "Library functions · <cctype>",
  """
  **`<cctype>`**: `isalpha`, `isdigit`, `isalnum`, `islower`, `isupper`, `isspace`, `ispunct`, `isprint`, and `toupper`, `tolower`.
  """,
  "Which header is needed for isdigit and toupper?",
  ans=["<cctype>", "cctype", "#include <cctype>"],
  hint="c + c + type.",
  fu=[F("""`isdigit('7')` is true, `isalpha('7')` is false. `toupper('a')` → 'A'.""",
        "Which <cctype> function converts a letter to uppercase?",
        ans=["toupper", "toupper()"],
        hint="to + upper."),
      F("""`isspace` tests for whitespace, `ispunct` tests for punctuation.""",
        "Which function tests whether a character is a digit?",
        ans=["isdigit", "isdigit()"],
        hint="is + digit.")],
  mcq=M("`isupper` is in the header…",
        "<cctype>", "<cmath>", "<cstring>", "<cstdlib>"))

S("fn04", T, H + "Library functions · <cstring>",
  """
  **`<cstring>`**:
  - `strlen`: **length**
  - `strcat`: **join**
  - `strcpy`: **copy**
  - `strcmp`: **compare** (**0 means same**)
  - `strstr`: **find**
  """,
  "What do strlen, strcat, strcpy, strcmp and strstr do?",
  kw=["strlen|length|panjang", "strcat|join|joins|concatenate|sambung|gabung",
      "strcpy|copy|copies|salin", "strcmp|compare|compares|banding", "strstr|find|finds|search|cari"],
  ans="strlen = length, strcat = join, strcpy = copy, strcmp = compare (0 = same), strstr = find.",
  hint="length, join, copy, compare, find.",
  fu=[F("""`strlen("George")`.""",
        "What does it return?",
        ans=["6"],
        hint="Count the letters."),
      F("""`char s[20]; strcpy(s, "Hi"); strcat(s, "!!"); cout << s;`""",
        "What is the output?",
        ans=["Hi!!"],
        hint="Copy, then join.")],
  mcq=M("The function that finds a substring in a C-string is…",
        "strstr", "strcat", "strlen", "strcpy"))

S("fn05", T, H + "Library functions · <cstdlib>",
  """
  **`<cstdlib>`**: `rand()`, `srand(x)`, `atoi`, `atol`, `atof` (**string → number**), `exit(0)`.
  """,
  "Which header contains rand, atoi and exit?",
  ans=["<cstdlib>", "cstdlib", "#include <cstdlib>"],
  hint="c + std + lib.",
  fu=[F("""atoi = string → int, atol = string → long, atof = string → double.""",
        "Which function converts a string to a double?",
        ans=["atof", "atof()"],
        hint="a-to-f."),
      F("""`cout << atoi("42") + 1;`""",
        "What is the output?",
        ans=["43"],
        hint="\"42\" → 42.")],
  mcq=M("`atoi`, `atol` and `atof` convert…",
        "A string to a number", "A number to a string", "Lowercase to uppercase", "double to int"))

S("fn06", T, H + "C-STRINGS warning",
  """
  ⚠ **C-STRINGS**

  You **can't** compare with `==` or assign with `=`. Use **`strcmp`** and **`strcpy`**.

  `strcmp` returns **0 when the strings are equal**.
  """,
  "How do you compare and copy C-strings?",
  kw=["strcmp", "strcpy", "==|=|cannot|can't|cant|not|tidak boleh|tak boleh"],
  ans="Use strcmp to compare (0 = equal) and strcpy to copy; you can't use == or =.",
  hint="Two str… functions.",
  fu=[F("""`strcmp("abc", "abc")`.""",
        "What does it return?",
        ans=["0"],
        hint="They are equal."),
      F("""Condition for C-strings a and b being equal.""",
        "Write the if condition that is true when a and b are equal.",
        ans=["if (strcmp(a, b) == 0)", "strcmp(a, b) == 0", "strcmp(a,b)==0", "if (!strcmp(a, b))"],
        hint="strcmp(...) == 0")],
  mcq=M("The CORRECT way to give `char name[10]` the value \"Ali\" after declaring it is…",
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
  "What are the three parts of a function header?",
  kw=["return type|returntype|return|jenis pulangan", "name|nama", "parameter|parameters|parameter list|senarai parameter"],
  ans="returnType, name, (parameter list).",
  hint="Type, name, brackets.",
  fu=[F("""`return value;` is not needed if the function is `void`.""",
        "When is `return value;` not needed?",
        ans=["void", "when it is void", "if void", "when void"],
        hint="No return type."),
      F("""Header `double average(int a, int b)`.""",
        "What is the return type in this header?",
        ans=["double"],
        hint="The first word.")],
  mcq=M("In `int sum(int a, int b)`, `int a, int b` is the…",
        "Parameter list", "Return type", "Function name", "Function body"))

S("fn08", T, H + "Prototype, definition, call",
  """
  | Prototype | Definition | Call |
  |---|---|---|
  | `int sum(int, int);` | `int sum(int a, int b) { return a + b; }` | `total = sum(x, y);` |
  | Placed **before main**, ends with **`;`** | | |
  """,
  "Where is a prototype placed, and how does it end?",
  kw=["before|above|sebelum|atas", "main", ";|semicolon|titik koma"],
  ans="Before main, and it ends with ;.",
  hint="Location + symbol.",
  fu=[F("""A prototype only needs the parameter types: `int sum(int, int);`""",
        "Write the prototype for `double avg(double a, double b)`.",
        ans=["double avg(double, double);", "double avg(double a, double b);"],
        hint="Header + ;"),
      F("""`int x = 3, y = 4; total = sum(x, y);`""",
        "What is total?",
        ans=["7"],
        hint="a + b.")],
  mcq=M("Which one is a function CALL?",
        "total = sum(x, y);", "int sum(int, int);", "int sum(int a, int b)", "{ return a + b; }"))

S("fn09", T, H + "What the compiler must know before a call",
  """
  The compiler **must know** the function's **name**, **return type**, and the **number and types of its parameters** **before it is called**.

  So use a **prototype**, or **define the function above main**.
  """,
  "What must the compiler know before a function is called, and how do you make sure it does?",
  kw=["name|nama", "return type|return|jenis pulangan",
      "number|type|types|parameter|parameters|bilangan|jenis",
      "prototype|above|before main|atas|sebelum main"],
  ans="Its name, return type, and the number and types of its parameters; use a prototype or define the function above main.",
  hint="Three facts + two ways.",
  fu=[F("""No prototype, and the definition below main → `'f' was not declared in this scope`.""",
        "Besides a prototype, how else can the compiler know a function?",
        kw=["define|definition|write|put|place|definisi|takrif|letak|tulis", "above|before|atas|sebelum"],
        ans="Define the function above main.",
        hint="Its position.")],
  mcq=M("Which does the compiler NOT need to know before a function call?",
        "The function body's contents", "The function name", "The return type", "The number and types of parameters"))

S("fn10", T, H + "void functions",
  """
  **`void`** means the function **returns nothing**.
  """,
  "What does void mean?",
  kw=["nothing|no|not|none|tiada|tidak|tak", "return|returns|value|pulang|memulangkan|nilai"],
  ans="The function returns nothing.",
  hint="Empty.",
  fu=[F("""`void printLine()` returns no value, so `int x = printLine();` is an error.""",
        "Can the result of a void function be stored in a variable? (yes / no)",
        ans=NO,
        hint="There is no value.")],
  mcq=M("The function `void show(int n)`…",
        "Returns no value", "Returns an int", "Returns n", "Can't have parameters"))

S("fn11", T, H + "Arguments vs parameters",
  """
  - **Arguments (actual)** are in the **call**.
  - **Parameters (formal)** are in the **header**.
  - They are matched **by order**, and **their number must match**.
  """,
  "What is the difference between arguments and parameters?",
  kw=["argument|arguments|actual|sebenar", "call|panggil|panggilan",
      "parameter|parameters|formal", "header|definition|definisi",
      "order|number|turutan|bilangan"],
  ans="Arguments (actual) are in the call; parameters (formal) are in the header; they are matched by order and their number must match.",
  hint="Call vs header.",
  fu=[F("""`total = sum(x, y);` with header `int sum(int a, int b)`.""",
        "Which parameter receives the value of y?",
        ans=["b"],
        hint="Second position."),
      F("""The number of arguments must match the parameters. `sum(1, 2, 3)` for `sum(int, int)` → error `too many arguments`.""",
        "What happens if the number of arguments doesn't match? (error / ok)",
        ans=["error", "compile error", "syntax error", "ralat"],
        hint="They must match.")],
  mcq=M("In `total = sum(x, y);`, x and y are…",
        "Arguments (actual)", "Parameters (formal)", "Return values", "Prototypes"))

S("fn12", T, H + "Using a returned value",
  """
  Use a returned value by **assigning it**, **printing it**, or **using it in an expression**.

  ```
  total = sum(3, 4);            // assign
  cout << sum(3, 4);            // print
  int d = sum(3, 4) * 2;        // expression → 14
  ```
  """,
  "What are three ways to use a value returned by a function?",
  kw=["assign|store|=|simpan|umpuk|variable", "print|output|cout|display|cetak|papar", "expression|calculation|ungkapan"],
  ans="Assign it to a variable, print it (cout), or use it in an expression.",
  hint="Store, print, calculate.",
  fu=[F("""`int d = sum(3, 4) * 2;`""",
        "What is d?",
        ans=["14"],
        hint="7 × 2.")],
  mcq=M("Which is NOT a way to use a returned value?",
        "sum(3, 4) = total;", "total = sum(3, 4);", "cout << sum(3, 4);", "d = sum(3, 4) * 2;"))

S("fn13", T, H + "Returning bool",
  """
  A function can return **bool**, e.g.

  ```
  bool isEven(int n) { return n % 2 == 0; }
  ```
  """,
  "Write the header of a function isEven that takes int n and returns bool.",
  ans=["bool isEven(int n)"],
  hint="Return type bool.",
  fu=[F("""`cout << isEven(6) << isEven(7);`""",
        "What is the output?",
        ans=["10"],
        hint="true = 1, false = 0.")],
  mcq=M("`bool isEven(int n)` returns…",
        "true or false", "An even number", "n", "Nothing"))

S("fn14", T, H + "INVALID HEADERS · no return type", trap=True,
  text="""
  ⚠ **INVALID HEADERS**

  `one(int a, int b)`: **no return type** ❌
  """,
  question="What is wrong with the header `one(int a, int b)`?",
  kw=["return type|return|type|jenis pulangan|jenis", "missing|no|none|without|tiada|tertinggal"],
  ans="It has no return type.",
  hint="What should come before the name?",
  fu=[F("""Add a return type, e.g. `int`.""",
        "Write the correct header if the function returns an int.",
        ans=["int one(int a, int b)"],
        hint="int + …")],
  mcq=M("The header `one(int a, int b)` is invalid because…",
        "It has no return type", "A parameter has no type", "It has no ( )", "The name is too short"))

S("fn15", T, H + "INVALID HEADERS · each parameter needs a type", trap=True,
  text="""
  ⚠ **INVALID HEADERS**

  `char another(int a, b)`: **each parameter needs its own type** ❌
  """,
  question="What is wrong with the header `char another(int a, b)`?",
  kw=["type|int|jenis", "each|every|own|b|parameter|setiap"],
  ans="Parameter b has no type; each parameter needs its own type.",
  hint="Look at b.",
  fu=[F("""Correct: `char another(int a, int b)`.""",
        "Write the correct header.",
        ans=["char another(int a, int b)"],
        hint="Add int before b.")],
  mcq=M("Which header is VALID?",
        "char another(int a, int b)", "char another(int a, b)", "another(int a, int b)", "char another"))

S("fn16", T, H + "INVALID HEADERS · no ( )", trap=True,
  text="""
  ⚠ **INVALID HEADERS**

  `double yetanother`: **no `( )`** ❌
  """,
  question="What is wrong with the header `double yetanother`?",
  kw=["( )|()|parentheses|brackets|bracket|kurungan", "missing|no|none|without|tiada|tertinggal"],
  ans="There are no ( ) after the function name.",
  hint="A function must have…",
  fu=[F("""A function with no parameters still needs `( )`: `double yetanother()`.""",
        "Write the correct header (no parameters).",
        ans=["double yetanother()"],
        hint="Add ( ).")],
  mcq=M("`double yetanother` is not a valid function header because…",
        "It has no ( )", "It has no return type", "double is not allowed", "The name is wrong"))

S("fn17", T, H + "Pass by value",
  """
  **By value**: `void f(int n)`

  The function gets a **copy**. Changing it **does not change the original**.

  e.g. `m = 612` → `f(m)` adds 37 inside → **m is still 612**.
  """,
  "What does pass by value mean?",
  kw=["copy|copies|salinan|salin", "original|not change|doesn't change|does not change|unchanged|same|asal|tidak berubah|kekal"],
  ans="The function gets a copy; changes inside it do not change the original variable.",
  hint="A copy.",
  fu=[F("""
        ```
        void f(int n) { n = n + 37; }
        int m = 612;
        f(m);
        cout << m;
        ```""",
        "What is the output?",
        ans=["612"],
        hint="Only the copy changed.")],
  mcq=M("In pass by value, the function works with…",
        "A copy", "The original", "An address", "A constant"))

S("fn18", T, H + "Pass by reference",
  """
  **By reference**: `void f(int &n)`

  The function works on **the original** (an alias), so **changes stay**.
  - Use it to **"return" more than one value**.
  - The `&` goes in **both the prototype and the header**.
  - The argument **must be a variable**, not `5` or `a+b`.
  """,
  "What does pass by reference mean, and when is it used?",
  kw=["original|alias|asal", "change|changes|stay|ubah|perubahan|kekal",
      "more than one|multiple|several|lebih daripada satu|beberapa|banyak"],
  ans="The function works on the original (an alias), so changes stay; it is used to 'return' more than one value.",
  hint="An alias…",
  fu=[F("""
        ```
        void f(int &n) { n = n + 37; }
        int m = 612;
        f(m);
        cout << m;
        ```""",
        "What is the output?",
        ans=["649"],
        hint="612 + 37."),
      F("""The argument for a reference parameter must be a variable. `f(5)` and `f(a+b)` are errors.""",
        "Can you call `f(a+b)` for `void f(int &n)`? (yes / no)",
        ans=NO,
        hint="It must be a variable."),
      F("""The `&` goes in the prototype AND the header.""",
        "Write the prototype for `void f(int &n)`.",
        ans=["void f(int &n);", "void f(int&);", "void f(int &);", "void f(int& n);"],
        hint="Don't forget & and ;")],
  mcq=M("For `void f(int &n)`, which call is VALID?",
        "f(m);", "f(5);", "f(a + b);", "f(&5);"))

S("fn19", T, H + "Memory trick: photocopy vs original",
  """
  💡 **MEMORY TRICK**

  - **Value = photocopy**: scribble on it and the original is fine.
  - **Reference = the original paper**: `&` = "and change the real one".
  """,
  "Explain the photocopy memory trick for value vs reference.",
  kw=["value|nilai", "photocopy|copy|fotostat|salinan",
      "reference|&|rujukan", "original|real|asal|sebenar"],
  ans="Value = photocopy (the original is safe); reference = the original paper (& = and change the real one).",
  hint="Photocopy vs …",
  fu=[F("""`&` = "and change the real one".""",
        "In the memory trick, what does `&` stand for?",
        kw=["change|ubah", "real|original|asal|sebenar"],
        ans="And change the real one.",
        hint="and change the …")],
  mcq=M("In the memory trick, pass by value is like a…",
        "Photocopy", "The original paper", "A pen", "An eraser"))

S("fn20", T, H + "Local variables",
  """
  **Local**: declared **inside a function**. **Created on each call and destroyed at the end**. **Not auto-initialised**.
  """,
  "What are the properties of a local variable?",
  kw=["inside|within|function|dalam", "created|each call|destroyed|every call|dicipta|setiap panggilan|musnah|dimusnahkan",
      "not auto|not initialised|not initialized|garbage|no initial|tidak auto|tak auto|sampah"],
  ans="Declared inside a function; created on each call and destroyed at the end; not auto-initialised.",
  hint="Where, how long, starting value.",
  fu=[F("""A local variable is not given a starting value automatically, so it holds garbage if you don't initialise it.""",
        "Is a local variable automatically set to 0? (yes / no)",
        ans=NO,
        hint="Not auto-initialised.")],
  mcq=M("A local variable…",
        "Is created on each call and destroyed at the end", "Lasts for the whole program", "Is auto-initialised to 0", "Can be used by every function"))

S("fn21", T, H + "Global variables",
  """
  **Global**: declared **outside all functions**. **Visible from that line to the end of the file**. **Auto-initialised to 0**.

  **Avoid them**; prefer **global constants**.
  """,
  "What are the properties of a global variable?",
  kw=["outside|luar", "visible|line|end of file|file|kelihatan|baris|fail",
      "0|zero|auto|sifar",
      "avoid|constant|constants|elak|elakkan|pemalar"],
  ans="Declared outside all functions; visible from that line to the end of the file; auto-initialised to 0; avoid them and prefer global constants.",
  hint="Where, scope, starting value, advice.",
  fu=[F("""`int gx;` outside main, then `cout << gx;` inside main.""",
        "What is the output?",
        ans=["0"],
        hint="Globals are auto-initialised.")],
  mcq=M("An uninitialised global variable has the value…",
        "0", "Garbage", "1", "An error"))

S("fn22", T, H + "Static local variables",
  """
  **Static local**: `static int x;` inside a function. **Keeps its value between calls**. **Initialised only once** (default 0).

  ```
  void showVar() { static int var = 10; cout << var; var++; }
  // called 10×: prints 10 11 12 ... 19    (without static: 10 10 10 ...)
  ```
  """,
  "What are the properties of a static local variable?",
  kw=["keep|keeps|remember|remembers|retain|retains|kekal|ingat",
      "between calls|calls|between|antara panggilan|panggilan",
      "once|sekali"],
  ans="It keeps its value between calls and is initialised only once (default 0).",
  hint="It 'remembers'.",
  fu=[F("""showVar() called 3 times.""",
        "What is the output (values separated by spaces)?",
        ans=["10 11 12"],
        hint="Starts at 10, goes up."),
      F("""Without `static`, var is created again on every call.""",
        "What do 3 calls print without static (with spaces)?",
        ans=["10 10 10"],
        hint="Always 10."),
      F("""Called 10 times with static.""",
        "What is the LAST value printed?",
        ans=["19"],
        hint="10 + 9.")],
  mcq=M("`static int x;` inside a function, with no starting value, begins at…",
        "0", "Garbage", "1", "An error"))

S("fn23", T, H + "Local wins over global",
  """
  If a local variable **has the same name** as a global one, **the local wins** inside that function.

  ```
  int gy = 5;
  void shadow() { int gy = 99; cout << gy; }
  // shadow(); cout << " " << gy;  →  99 5
  ```
  """,
  "If a local and a global have the same name, which one is used inside the function?",
  ans=["local", "the local", "local variable", "the local variable"],
  hint="Local wins.",
  fu=[F("""The shadow code above: `shadow(); cout << " " << gy;`""",
        "What is the output?",
        ans=["99 5"],
        hint="Local inside shadow, global inside main.")],
  mcq=M("Inside a function with a local `x` and a global `x`, `cout << x;` prints…",
        "The local value", "The global value", "An error", "The sum of both"))

S("fn24", T, H + "Default arguments",
  """
  ```
  int getSum(int, int = 0, int = 0);          // in the prototype
  getSum(5); getSum(5, 2); getSum(5, 2, 1);   // all OK
  ```
  - Default values must be at the **right end** of the list: `(int, int=0, int)` ❌
  - When you leave out an argument, you must **leave out everything after it** too: `getSum(a, , c)` ❌
  """,
  "State the two rules for default arguments.",
  kw=["right|end|kanan|hujung",
      "leave out|omit|skip|after|everything after|tinggal|selepas"],
  ans="Defaults must be at the right end of the list; when you leave out an argument, you must leave out everything after it.",
  hint="Right… and what comes after.",
  fu=[F("""`getSum(int a, int b = 0, int c = 0)` returns a + b + c.""",
        "What is getSum(5, 2)?",
        ans=["7"],
        hint="5 + 2 + 0."),
      F("""Prototype `int f(int, int = 0, int);`""",
        "Is this prototype valid? (yes / no)",
        ans=NO,
        hint="A default in the middle."),
      F("""`getSum(a, , c)`""",
        "Is this call valid? (yes / no)",
        ans=NO,
        hint="You can't skip one in the middle.")],
  mcq=M("With `int getSum(int, int = 0, int = 0);`, which call is NOT valid?",
        "getSum(5, , 1);", "getSum(5);", "getSum(5, 2);", "getSum(5, 2, 1);"))

S("fn25", T, H + "Function overloading",
  """
  Functions can **share the same name** if they have **different parameter lists** (number or types). The compiler picks the version that matches the arguments.

  ```
  void getDimensions(int);           void getDimensions(int, int);
  void getDimensions(int, double);   void getDimensions(double, double);
  ```
  """,
  "What is function overloading?",
  kw=["same name|share|nama sama|sama nama|kongsi",
      "different|berbeza|lain", "parameter|parameters|parameter list|list|senarai",
      "number|type|types|bilangan|jenis"],
  ans="Functions sharing the same name but with different parameter lists (number or types); the compiler picks the matching one.",
  hint="Same name, what differs?",
  fu=[F("""The call `getDimensions(1, 2.5)`: an int and a double argument.""",
        "Which version is picked? (write the parameter types, e.g. int, int)",
        ans=["int, double", "(int, double)", "int double", "getDimensions(int, double)"],
        hint="Match the argument types."),
      F("""The call `getDimensions(1.5, 2.5)`.""",
        "Which version is picked?",
        ans=["double, double", "(double, double)", "double double", "getDimensions(double, double)"],
        hint="Two doubles.")],
  mcq=M("Overloading requires…",
        "The same name with different parameter lists", "Different names with the same parameters", "A different return type only", "All parameters to be double"))

S("fn26", T, H + "return vs exit()",
  """
  - **`return`** ends the function and goes **back to the caller**. Code after it doesn't run.
  - **`exit(0)`** ends the **whole program immediately**, from anywhere (`<cstdlib>`). Constants: `EXIT_SUCCESS` / `EXIT_FAILURE`.
  """,
  "What is the difference between return and exit(0)?",
  kw=["return", "function|caller|fungsi|pemanggil",
      "exit", "program|whole|immediately|seluruh|serta-merta"],
  ans="return ends the function and goes back to the caller; exit(0) ends the whole program immediately.",
  hint="Function vs program.",
  fu=[F("""exit is in `<cstdlib>`. Constants: `EXIT_SUCCESS` / `EXIT_FAILURE`.""",
        "Which header is needed for exit()?",
        ans=["<cstdlib>", "cstdlib", "#include <cstdlib>"],
        hint="Same as rand."),
      F("""`return` in an ordinary function goes back to the caller; code after the return in that function doesn't run.""",
        "Does code after return in the same function run? (yes / no)",
        ans=NO,
        hint="Code after it doesn't run.")],
  mcq=M("To end the WHOLE program from inside a function, use…",
        "exit(0)", "return", "break", "continue"))

# =================================================================== CHAPTER 6 cheat sheet
T = "cheat"
H = "6 · Cheat Sheet · "

S("ch01", T, H + "Computational thinking",
  """
  **Computational thinking**: Decomposition · Pattern · Abstraction · Algorithm (**+ Modelling, Evaluation**)
  """,
  "List the four computational thinking skills and the two extras in the extended version.",
  kw=["decomposition|decompose|pecah", "pattern|corak", "abstraction|abstract|abstraksi", "algorithm|algoritma",
      "modelling|modeling|model", "evaluation|evaluate|penilaian"],
  ans="Decomposition, Pattern, Abstraction, Algorithm + Modelling, Evaluation.",
  hint="D-P-A-A + M + E.",
  fu=[F("""The two extras in the extended version: Modelling and Evaluation.""",
        "Name one extra stage in the extended version.",
        ans=["modelling", "modeling", "evaluation"],
        hint="M or E.")],
  mcq=M("Which is an EXTRA stage in the extended version?",
        "Modelling", "Decomposition", "Abstraction", "Pattern"))

S("ch02", T, H + "Problem solving",
  """
  **Problem solving**: IPO → Algorithm → Pseudocode / Flowchart → Trace table → Code
  """,
  "Write the problem-solving flow from the cheat sheet.",
  kw=["ipo|input", "algorithm|algoritma", "pseudocode|flowchart", "trace|trace table", "code|kod"],
  ans="IPO → Algorithm → Pseudocode / Flowchart → Trace table → Code.",
  hint="Starts with IPO, ends with Code.",
  fu=[F("""Trace table comes right before Code in the cheat sheet flow.""",
        "Which step comes right before Code?",
        ans=["trace table", "trace"],
        hint="A table.")],
  mcq=M("In the problem-solving flow, the first step is…",
        "IPO", "Code", "Trace table", "Flowchart"))

S("ch03", T, H + "3 control structures and flowchart shapes",
  """
  - **3 control structures**: Sequence · Selection · Repetition
  - **Flowchart shapes**: **Oval** = start/end · **Rectangle** = process · **Parallelogram** = I/O · **Diamond** = decision
  """,
  "Match the flowchart shapes: Oval, Rectangle, Parallelogram, Diamond.",
  kw=["oval|bujur", "start|end|mula|tamat",
      "rectangle|segi empat tepat", "process|proses",
      "parallelogram|segi empat selari", "i/o|input|output",
      "diamond|berlian", "decision|keputusan"],
  ans="Oval = start/end, Rectangle = process, Parallelogram = I/O, Diamond = decision.",
  hint="4 pairs.",
  fu=[F("""Diamond = decision.""",
        "Which shape is used for a decision?",
        ans=["diamond"],
        hint="Rhombus.")],
  mcq=M("A parallelogram in a flowchart is…",
        "Input/Output", "Process", "Decision", "Start/End"))

S("ch04", T, H + "Integer maths",
  """
  **Integer maths**: `7/3` = 2 · `7%3` = 1 · `7/3.0` = 2.33 (cout prints `2.33333`) · `int x = 3.9` → 3
  """,
  "What are 7/3 and 7%3? (format: a b)",
  ans=["2 1"],
  hint="Integer division and remainder.",
  fu=[F("""`int x = 3.9;` → truncated.""",
        "What is x?",
        ans=["3"],
        hint="Truncated."),
      F("""`7/3.0`: one operand is a double. cout prints 6 significant digits.""",
        "What is the output of `cout << 7/3.0;`?",
        ans=["2.33333", "2.33"],
        hint="2.33…")],
  mcq=M("`7 % 3` is…",
        "1", "2", "2.33", "0"))

S("ch05", T, H + "Precedence",
  """
  **Precedence** (high → low):

  `( )` → `!` unary− → `* / %` → `+ −` → `< > <= >=` → `== !=` → `&&` → `||` → `=`
  """,
  "Between && and ||, which has higher precedence?",
  ans=["&&", "and"],
  hint="AND before OR.",
  fu=[F("""Relational (`< > <= >=`) is higher than equality (`== !=`), which is higher than `&&`.""",
        "What is the output of `cout << (3 + 4 > 6 && 2 == 2);`?",
        ans=["1"],
        hint="7 > 6 true, 2 == 2 true."),
      F("""`=` has the lowest precedence.""",
        "Which operator has the LOWEST precedence in the cheat sheet list?",
        ans=["=", "assignment"],
        hint="End of the list.")],
  mcq=M("Which is evaluated FIRST?",
        "!", "&&", "==", "||"))

S("ch06", T, H + "Truth",
  """
  **Truth**: `0` = false · **any non-zero = true**

  **AND**: all must be T · **OR**: one T is enough
  """,
  "What truth value do 0 and a non-zero number have?",
  kw=["0|zero|sifar", "false|palsu", "non-zero|nonzero|any other|not zero|bukan sifar|bukan-sifar|lain", "true|benar"],
  ans="0 = false; any non-zero = true.",
  hint="Only one value is false.",
  fu=[F("""AND: all must be T. OR: one T is enough.""",
        "What is `true && false`? (true / false)",
        ans=["false", "0"],
        hint="AND is strict.")],
  mcq=M("`if (7)` is treated as…",
        "true", "false", "an error", "7"))

S("ch07", T, H + "= vs ==",
  """
  **`=` assigns · `==` compares**

  `if (x = 5)` is **always true**! (x becomes 5, and 5 is non-zero.)
  """,
  "Why is `if (x = 5)` always true?",
  kw=["assign|assigns|assignment|=|umpuk", "5|non-zero|nonzero|not zero|true|bukan sifar"],
  ans="Because = assigns 5 to x, and 5 (non-zero) counts as true.",
  hint="The value of the assignment is 5.",
  fu=[F("""`int x = 1; if (x = 5) cout << x;`""",
        "What is the output?",
        ans=["5"],
        hint="x is changed.")],
  mcq=M("The operator that COMPARES two values is…",
        "==", "=", "!", "=>"))

S("ch08", T, H + "switch and loops",
  """
  - **switch**: int/char/bool only · constant cases · don't forget `break`
  - **Loops**: `for` = known count · `while` = 0+ times · `do-while` = 1+ times (**ends with `;`**)
  """,
  "What is the minimum number of runs for while and do-while? (format: while do-while)",
  ans=["0 1", "0+ 1+"],
  hint="0+ and 1+.",
  fu=[F("""switch: int/char/bool only.""",
        "List the types allowed in a switch.",
        kw=["int", "char", "bool"],
        ans="int, char, bool.",
        hint="Three.")],
  mcq=M("The loop that ends with ; is…",
        "do-while", "for", "while", "switch"))

S("ch09", T, H + "break / continue and function parts",
  """
  - **break** = leave the loop · **continue** = skip to the next round
  - **Function parts**: prototype `int f(int);` · header `int f(int a)` · call `y = f(x);`
  """,
  "Give the cheat sheet's example prototype, header and call for f.",
  kw=["int f(int);|int f(int)", "int f(int a)", "y = f(x)|f(x)"],
  ans="Prototype: int f(int); Header: int f(int a). Call: y = f(x);",
  hint="The prototype has ;, the header names the parameter, the call has no types.",
  fu=[F("""break leaves; continue skips to the next round.""",
        "Which jump statement skips to the next round?",
        ans=["continue"],
        hint="Not break.")],
  mcq=M("In the cheat sheet, `y = f(x);` is the…",
        "Call", "Prototype", "Header", "Definition"))

S("ch10", T, H + "Value vs reference and variable lifetime",
  """
  - **Value vs reference**: `f(int a)` = copy · `f(int &a)` = original (must pass a variable)
  - **Variable lifetime**: local = per call · static = remembers · global = whole file (avoid)
  """,
  "Match the lifetimes: local, static, global.",
  kw=["local", "per call|each call|every call|setiap panggilan|panggilan",
      "static", "remember|remembers|keeps|kekal|ingat",
      "global", "whole file|file|entire file|seluruh fail|fail"],
  ans="local = per call; static = remembers its value; global = whole file (avoid).",
  hint="Per call, remembers, whole file.",
  fu=[F("""`f(int &a)` works on the original; the argument must be a variable.""",
        "Which header changes the original variable: `f(int a)` or `f(int &a)`?",
        ans=["f(int &a)", "int &a", "&a", "f(int& a)"],
        hint="The one with &.")],
  mcq=M("The variable that 'remembers' its value between calls is…",
        "static", "a plain local", "a by-value parameter", "a literal"))

S("ch11", T, H + "Default args and overloading",
  """
  - **Default args**: defaults go **right to left** · leave out args **from the right**
  - **Overloading**: **same name + different parameter list** (number/type)
  """,
  "What is required for function overloading?",
  kw=["same name|nama sama|sama nama", "different|berbeza", "parameter|parameters|list|senarai"],
  ans="The same name with a different parameter list (number or types).",
  hint="Name + parameters.",
  fu=[F("""Default args: right to left; arguments are left out from the right.""",
        "From which side can arguments be left out?",
        ans=["right", "from the right", "the right", "kanan"],
        hint="The end of the list.")],
  mcq=M("Default arguments are set…",
        "From right to left", "From left to right", "Only in the middle", "Only in the call"))

S("ch12", T, H + "EXAM-DAY CHECKLIST · trace table and traps",
  """
  ✔ **EXAM-DAY CHECKLIST WHEN TRACING CODE**
  1. Draw a **trace table** with **one column per variable**.
  2. Check for **`=` vs `==`**, a **stray `;` after if/while**, and a **missing `break`**.
  """,
  "Which three traps does checklist item 2 tell you to check when tracing code?",
  kw=["= vs ==|==|=", ";|semicolon|stray", "break"],
  ans="= vs ==, a stray ; after if/while, and a missing break.",
  hint="One operator, one punctuation mark, one keyword.",
  fu=[F("""Checklist item 1: a trace table with one column per variable.""",
        "How many columns per variable in a trace table?",
        ans=["1", "one"],
        hint="One column per variable.")],
  mcq=M("The first step of the exam-day checklist is…",
        "Draw a trace table, one column per variable", "Rewrite the code", "Compile it", "Draw a flowchart"))

S("ch13", T, H + "EXAM-DAY CHECKLIST · arithmetic and ++",
  """
  ✔ **EXAM-DAY CHECKLIST**
  3. **Integer division? Truncation? Prefix or postfix `++`?**
  """,
  "What are the three arithmetic questions in checklist item 3?",
  kw=["integer division|integer|int division", "truncation|truncate|truncated",
      "prefix|postfix|++"],
  ans="Integer division? Truncation? Prefix or postfix ++?",
  hint="Divide, cut off, increment.",
  fu=[F("""
        ```
        int a = 7, b = 2;
        double c = a / b;
        cout << c;
        ```""",
        "What is the output?",
        ans=["3"],
        hint="a / b is int ÷ int first.")],
  mcq=M("`int k = 4; int m = k++ + 1;` → m =",
        "5", "6", "4", "An error"))

S("ch14", T, H + "EXAM-DAY CHECKLIST · value/reference and static",
  """
  ✔ **EXAM-DAY CHECKLIST**
  4. **Pass by value** (original unchanged) or **by reference** (original changed)?
  5. **Static variable** (keeps its value) or **normal local** (resets each call)?
  """,
  "What are the two function questions in checklist items 4 and 5?",
  kw=["value", "reference|&", "static", "local|reset|resets"],
  ans="Pass by value or by reference? Static variable or normal local?",
  hint="Parameters and lifetime.",
  fu=[F("""
        ```
        void addOne(int n) { n++; }
        int main() { int k = 9; addOne(k); cout << k; }
        ```""",
        "What is the output?",
        ans=["9"],
        hint="Pass by value.")],
  mcq=M("When tracing, a normal (non-static) local variable…",
        "Resets on each call", "Keeps its value", "Is auto 0 and stays", "Is the same as a global"))
