from helpers import S, F, M

T = "ctrl"
H = "4 · "

NO = ["no", "tidak", "tak"]

S("cs01", T, H + "bool ↔ int",
  """
  - **bool → int**: `true` = **1**, `false` = **0**. e.g. `2 + true` = **3**.
  - **int → bool**: `0` = **false**, **any non-zero = true** (even **−10**).
  """,
  "How is an int converted to a bool?",
  kw=["0|zero|sifar", "false|palsu",
      "non-zero|nonzero|any other|not zero|bukan sifar|bukan-sifar|selain 0|lain", "true|benar"],
  ans="0 = false; any non-zero value (even a negative like −10) = true.",
  hint="Only one value is false.",
  fu=[F("""`cout << 2 + true;`""",
        "What is the output?",
        ans=["3"],
        hint="true = 1."),
      F("""`if (-10) cout << "yes"; else cout << "no";`""",
        "What is the output?",
        ans=["yes"],
        hint="−10 is not zero.")],
  mcq=M("In C++, `-10` used as a condition is…",
        "true", "false", "an error", "-10"))

S("cs02", T, H + "if statement: 3 forms and compound statement",
  """
  ```
  if (cond)          if (cond) {          if (cond) {
      stmt;              stmt1;               ...
                         stmt2;           } else {
                     }                        ...
                                          }
  ```
  - Braces `{ }` are **optional when there's only one statement**.
  - A group of statements inside `{ }` is called a **compound statement**.
  """,
  "What is a compound statement, and when are braces { } optional?",
  kw=["group|several|multiple|more than one|kumpulan|beberapa|lebih", "{ }|{}|braces|curly|kurungan kerinting",
      "one|single|only one|satu|hanya satu"],
  ans="A compound statement is a group of statements inside { }; braces are optional when there is only one statement.",
  hint="Two parts: the definition, and when you can leave them out.",
  fu=[F("""
        ```
        int a = 8;
        if (a > 5) {
            cout << "big ";
            cout << "number";
        }
        ```""",
        "What is the output?",
        ans=["big number"],
        hint="Both are inside the block.")],
  mcq=M("A group of statements inside { } is called a…",
        "Compound statement", "Null statement", "Preprocessor directive", "Literal"))

S("cs03", T, H + "if-else if chain (grade)",
  """
  ```
  if (score > 90)      grade = 'A';
  else if (score > 75) grade = 'B';
  else if (score > 60) grade = 'C';
  else if (score > 50) grade = 'D';
  else                 grade = 'F';
  ```
  Conditions are tested from the top; **only the first true one** runs.
  """,
  "With the code above, what grade does score = 80 get?",
  ans=["B"],
  hint="80 > 90? 80 > 75?",
  fu=[F("""Boundary: `score > 90` means more than 90, so 90 is not an A.""",
        "What grade does score = 90 get?",
        ans=["B"],
        hint="90 > 90 is false."),
      F("""score = 50: 50 > 50 is false.""",
        "What grade does score = 50 get?",
        ans=["F"],
        hint="Falls through to else.")],
  mcq=M("In an if-else if chain, at most how many branches run?",
        "One", "Every true one", "Two", "No limit"))

S("cs04", T, H + "Common traps · if (x = 0)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (x = 0)` | This is **assignment, not comparison**. x becomes 0, so the condition is **always false**. | `if (x == 0)` |
  """,
  question="Why is `if (x = 0)` wrong?",
  kw=["assignment|assign|assigns|umpukan|=",
      "not comparison|not compare|comparison|compare|bukan perbandingan|banding|==",
      "always false|false|sentiasa false|0"],
  ans="It is assignment, not comparison: x becomes 0, so the condition is always false. Correct: if (x == 0).",
  hint="= vs ==.",
  fu=[F("""
        ```
        int x = 5;
        if (x = 0) cout << "T";
        else cout << "F";
        cout << " x=" << x;
        ```""",
        "What is the output?",
        ans=["F x=0"],
        hint="x is set to 0, and 0 = false."),
      F("""Fix the condition so it compares x with 0.""",
        "Write the correct condition.",
        ans=["if (x == 0)", "if(x==0)", "x == 0"],
        hint="Two equals signs.")],
  mcq=M("`if (x = 0)` will…",
        "Set x to 0 and always be false", "Compare x with 0", "Always be true", "Fail to compile"))

S("cs05", T, H + "Common traps · if (2 < x < 9)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (2 < x < 9)` | `(2<x)` gives **0 or 1**, which is **always < 9**, so it's **always true** | `if (2<x && x<9)` |
  """,
  question="Why is `if (2 < x < 9)` always true?",
  kw=["0 or 1|0|1|true|false|0 atau 1", "always|sentiasa", "< 9|less than 9|kurang daripada 9|9"],
  ans="(2<x) is evaluated first and gives 0 or 1; both are less than 9, so it is always true.",
  hint="What is the value of (2 < x)?",
  fu=[F("""x = 20: `(2 < 20)` = 1, then `1 < 9` = true.""",
        "With x = 20, what is `(2 < x < 9)`? (1 / 0)",
        ans=["1", "true"],
        hint="1 < 9."),
      F("""Write the range 2 < x < 9 correctly in C++.""",
        "Write the correct condition.",
        ans=["if (2<x && x<9)", "2<x && x<9", "if (2 < x && x < 9)", "x > 2 && x < 9", "(2 < x) && (x < 9)"],
        hint="Use &&.")],
  mcq=M("The correct condition for 'x is between 2 and 9' is…",
        "2 < x && x < 9", "2 < x < 9", "2 < x || x < 9", "x < 2 && x > 9"))

S("cs06", T, H + "Common traps · if (0<x) && (x<10)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (0<x) && (x<10)` | **Syntax error**: the whole condition needs **outer `( )`** | `if ((0<x) && (x<10))` |
  """,
  question="What is wrong with `if (0<x) && (x<10)`?",
  kw=["syntax|sintaks", "outer|outside|whole|entire|luar|seluruh|keseluruhan", "( )|()|parentheses|brackets|bracket|kurungan"],
  ans="Syntax error: the whole condition needs outer brackets. Correct: if ((0<x) && (x<10)).",
  hint="The if's brackets must cover everything.",
  fu=[F("""An if condition must be inside **one pair of outer brackets**.""",
        "Write the correct condition.",
        ans=["if ((0<x) && (x<10))", "if((0<x)&&(x<10))", "if (0<x && x<10)", "if (0 < x && x < 10)"],
        hint="Add ( ) around it.")],
  mcq=M("`if (0<x) && (x<10)` gives…",
        "A syntax error", "Always true", "Always false", "Works normally"))

S("cs07", T, H + "Common traps · if (!n > 9)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (!n > 9)` | `!` runs **first**: `!5` = false = 0, and `0 > 9` is false | `if (!(n > 9))` |
  """,
  question="With n = 5, what is `!n > 9`? (1 / 0)",
  ans=["0", "false"],
  hint="!5 first.",
  fu=[F("""Steps: `!5` = 0, then `0 > 9` = false.""",
        "Why doesn't `!n > 9` mean 'n is not greater than 9'?",
        kw=["!|not", "first|before|precedence|higher|dahulu|dulu|keutamaan",
            "n|5|!n"],
        ans="Because ! is applied to n first (!5 = 0), then 0 > 9 is compared.",
        hint="Operator precedence."),
      F("""Correct form: negate the whole comparison.""",
        "Write the correct condition.",
        ans=["if (!(n > 9))", "!(n > 9)", "if(!(n>9))", "n <= 9", "if (n <= 9)"],
        hint="!( … )")],
  mcq=M("`!n > 9` is evaluated as…",
        "(!n) > 9", "!(n > 9)", "n < 9", "n != 9"))

S("cs08", T, H + "Common traps · if (x<3);", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | `if (x<3);` | The `;` is a **null statement**, so the next line **always** runs | No `;` after `if (...)` |
  """,
  question="What happens when there is a ; after `if (x<3)`?",
  kw=["null|empty|kosong", "always|sentiasa", "next|following|seterusnya|line|baris|run|runs|jalan"],
  ans="The ; is a null statement, so the next line always runs.",
  hint="The if's body becomes empty.",
  fu=[F("""
        ```
        int x = 7;
        if (x < 3);
            cout << "small";
        ```""",
        "What is the output?",
        ans=["small"],
        hint="The cout has nothing to do with the if.")],
  mcq=M("`if (x<3); cout << \"A\";` with x = 10 prints…",
        "A", "Nothing", "An error", "10"))

S("cs09", T, H + "Common traps · 2 statements before else with no { }", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | 2 statements before `else` with no `{ }` | **Syntax error: misplaced else** | Wrap them in `{ }` |

  ```
  if (x > 0)
      x = 1;
      x = 2;        // not part of the if
  else              // error: 'else' without a previous 'if'
      x = 3;
  ```
  """,
  question="What error do you get with two statements before else and no { }?",
  kw=["syntax|sintaks|error|ralat", "misplaced|without|salah tempat|tanpa|else"],
  ans="A syntax error: misplaced else ('else' without a previous 'if'). Wrap the statements in { }.",
  hint="The else can't find its if.",
  fu=[F("""Fix: wrap both statements in `{ }`.""",
        "What must be added to fix it?",
        ans=["{ }", "{}", "braces", "curly braces", "kurungan kerinting"],
        hint="A compound statement.")],
  mcq=M("Two statements before else with no braces gives…",
        "Syntax error: misplaced else", "else runs twice", "An infinite loop", "No problem"))

S("cs10", T, H + "Common traps · nested if with no braces (dangling else)", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | Nested if with no braces | The `else` pairs with the **nearest if** (dangling else) | Use `{ }` to show which if |

  ```
  int a = 5, b = 1;
  if (a > 3)
      if (b > 3) cout << "X";
  else cout << "Y";
  ```
  """,
  question="With a = 5, b = 1, what does the code above print?",
  ans=["Y"],
  hint="The else belongs to if (b > 3).",
  fu=[F("""The else pairs with the **nearest** if, not by indentation.""",
        "In a nested if with no braces, which if does the else pair with?",
        kw=["nearest|closest|inner|last|terdekat|dekat|dalam|terakhir"],
        ans="The nearest if.",
        hint="Dangling else.")],
  mcq=M("Dangling else means the else pairs with…",
        "The nearest if", "The first if", "The outermost if", "The if with the same indentation"))

S("cs11", T, H + "Common traps · indentation only", trap=True,
  text="""
  ⚠ **Common trap**

  | Wrong | Why | Correct |
  |---|---|---|
  | Indentation only | **Indentation means nothing** to the compiler | Use `{ }` |

  ```
  int age = 15;
  if (age >= 18)
      cout << "Adult ";
      cout << "Can vote";
  ```
  """,
  question="What does the code above print?",
  ans=["Can vote"],
  hint="Only the first line belongs to the if.",
  fu=[F("""The compiler ignores spaces and indentation. Only `{ }` define a block.""",
        "What decides which statements belong to an if: indentation or braces?",
        ans=["braces", "{ }", "{}", "curly braces"],
        hint="Not spaces.")],
  mcq=M("To the C++ compiler, indentation…",
        "Means nothing", "Defines blocks", "Is required", "Replaces ;"))

S("cs12", T, H + "Shortcuts · if (a), if (!a), if (n%2)",
  """
  | Long | Short |
  |---|---|
  | `if (a != 0)` | `if (a)` |
  | `if (a == 0)` | `if (!a)` |
  | `if (n%2 == 1)` (odd) | `if (n%2)` |
  """,
  "Write the short form of `if (a != 0)`.",
  ans=["if (a)", "if(a)"],
  hint="Non-zero = true.",
  fu=[F("""`if (a == 0)` → `if (!a)`.""",
        "Write the short form of `if (a == 0)`.",
        ans=["if (!a)", "if(!a)"],
        hint="NOT a."),
      F("""A non-zero `n % 2` means n is odd.""",
        "Write the short form that tests whether n is odd.",
        ans=["if (n%2)", "if (n % 2)", "if(n%2)"],
        hint="A non-zero remainder.")],
  mcq=M("`if (!a)` is the same as…",
        "if (a == 0)", "if (a != 0)", "if (a > 0)", "if (a = 0)"))

S("cs13", T, H + "Conditional (ternary) operator",
  """
  `cond ? value1 : value2`: **if true, take value1; otherwise, value2**.

  ```
  p = (p<5) ? q+1 : 5;
  ```
  """,
  "Explain the conditional (ternary) operator.",
  kw=["?|ternary|conditional", "true|value1|first|benar|nilai pertama",
      "otherwise|false|else|value2|second|jika tidak|kedua"],
  ans="cond ? value1 : value2 — if cond is true take value1, otherwise take value2.",
  hint="? and :",
  fu=[F("""`int p = 3, q = 8; p = (p<5) ? q+1 : 5;`""",
        "What is p?",
        ans=["9"],
        hint="3 < 5 is true → q+1."),
      F("""`int p = 7, q = 8; p = (p<5) ? q+1 : 5;`""",
        "What is p?",
        ans=["5"],
        hint="7 < 5 is false.")],
  mcq=M("`x = (a > b) ? a : b;` stores…",
        "The larger of a and b", "The smaller one", "Always a", "Always b"))

S("cs14", T, H + "Complement a condition",
  """
  **Complement** a condition by putting **`!( )`** around it:

  `!(n==0)` is the same as `n != 0`.

  Use it when the flowchart's **"Yes" branch is on the wrong side**.
  """,
  "How do you complement a condition, and when is it useful?",
  kw=["!( )|!()|!|not", "around|wrap|surround|sekeliling|keliling|balut",
      "yes|flowchart|wrong side|wrong|chart|carta|salah"],
  ans="Put !( ) around the condition; it's useful when the flowchart's Yes branch is on the wrong side.",
  hint="e.g. !(n==0).",
  fu=[F("""`!(n==0)` = `n != 0`.""",
        "Write another form of `!(n==0)`.",
        ans=["n != 0", "n!=0"],
        hint="Not equal."),
      F("""The complement of `x > 5` can be written `!(x > 5)` or `x <= 5`.""",
        "Write the complement of `x > 5` without using !.",
        ans=["x <= 5", "x<=5"],
        hint="Not x < 5.")],
  mcq=M("`!(n == 0)` is the same as…",
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
  The expression must be an **integral type**: **`int`, `char`, `bool`**. **Not float and not string.**
  """,
  "Which types are allowed for a switch expression?",
  kw=["int|integer|integral", "char|character|aksara", "bool"],
  ans="Integral types: int, char, bool (not float, not string).",
  hint="Three types.",
  fu=[F("""With `grade = 'B'` in the code above.""",
        "What is the output?",
        ans=["Very good!"],
        hint="case 'B'."),
      F("""`double d = 1; switch (d) { ... }` → error `switch quantity not an integer`.""",
        "Can a string be used as a switch expression? (yes / no)",
        ans=NO,
        hint="Not float and not string.")],
  mcq=M("Which type can NOT be used in a switch?",
        "float", "int", "char", "bool"))

S("cs16", T, H + "switch · case values must be constants",
  """
  Each `case` value must be a **constant**: a **literal, `const` or `#define`**, **not a variable**.
  """,
  "What can be used as a case value?",
  kw=["constant|constants|pemalar|tetap", "literal|const|#define|define"],
  ans="Constants only: a literal, const or #define; not a variable.",
  hint="Three kinds of constant.",
  fu=[F("""`int c = 2; switch (x) { case c: ... }` → error: c is not a constant.""",
        "Can an ordinary variable be a case value? (yes / no)",
        ans=NO,
        hint="It must be a constant.")],
  mcq=M("Which case label is VALID?",
        "case 'A':", "case x:", "case x > 5:", "case 2.5:"))

S("cs17", T, H + "switch · fall-through (missing break)",
  """
  If **`break` is missing**, it **"falls through"** and runs **the next case too**.

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
  "What does the code above (no breaks) print?",
  ans=["GoodFail"],
  hint="Starts at case 'C', continues into default.",
  fu=[F("""With grade = 'B' in the code without breaks.""",
        "What is the output?",
        ans=["Very good!GoodFail"],
        hint="Falls through to the end.")],
  mcq=M("What happens if break is missing in a case?",
        "The next case runs too (fall-through)", "A compile error", "The program ends", "The case is skipped"))

S("cs18", T, H + "switch · default",
  """
  **`default`** runs when **no case matches**.
  """,
  "When does default run in a switch?",
  kw=["no case|none|not match|no match|nothing matches|doesn't match|tiada case|tidak sepadan|tak sepadan"],
  ans="When no case matches.",
  hint="The last resort.",
  fu=[F("""The grade switch (with breaks) and `grade = 'Z'`.""",
        "What is the output?",
        ans=["Fail"],
        hint="There is no case 'Z'.")],
  mcq=M("In a switch, the part that runs when no case matches is…",
        "default", "break", "else", "continue"))

S("cs19", T, H + "Loops · 4 parts",
  """
  Every loop has **4 parts**: **initialise**, **condition**, **body**, **update**.

  If you **forget to update**, you get an **infinite loop**.
  """,
  "What are the four parts of a loop?",
  kw=["initialise|initialize|initialization|initialisation|inisialisasi|nilai awal|init|start",
      "condition|test|syarat",
      "body|badan",
      "update|increment|decrement|kemas kini"],
  ans="Initialise, condition, body, update.",
  hint="Start, test, work, change.",
  fu=[F("""Without an update, the condition never changes.""",
        "What happens if you forget the update?",
        ans=["infinite loop", "an infinite loop", "infinite"],
        hint="It never stops.")],
  mcq=M("Forgetting the update part of a loop usually causes…",
        "An infinite loop", "A syntax error", "The loop to run 0 times", "A faster program"))

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
  All three print **10 9 8 7 6 5 4 3 2 1**. Note the **`;` after `while (n > 0)` in the do-while**.
  """,
  "What do all three loops above print?",
  ans=["10 9 8 7 6 5 4 3 2 1"],
  hint="From 10 down to 1.",
  fu=[F("""A do-while ends with `} while (n > 0);`""",
        "Which symbol must come after `while (n > 0)` in a do-while?",
        ans=[";", "semicolon", "a semicolon"],
        hint="← ;"),
      F("""If `n = 0` at the start: the while doesn't run (pre-test), the do-while runs once (post-test).""",
        "With n = 0 at the start, how many times does the do-while body run?",
        ans=["1", "once", "one"],
        hint="Post-test.")],
  mcq=M("Which loop is post-test?",
        "do-while", "while", "for", "All three"))

S("cs21", T, H + "Loops · which loop to use",
  """
  | Loop | Use when… |
  |---|---|
  | `for` | you know **how many times** (counter) |
  | `while` | you might run it **0 times** (sentinel, unknown count) |
  | `do-while` | it must run **at least once** (menus, input validation) |
  """,
  "When is do-while the best choice?",
  kw=["at least once|once|sekurang-kurangnya sekali|sekali",
      "menu|menus|validation|validate|input|validasi|pengesahan"],
  ans="When the loop must run at least once, e.g. menus and input validation.",
  hint="Menus…",
  fu=[F("""for = known count (counter).""",
        "Which loop suits printing a times table from 1 to 12?",
        ans=["for", "for loop"],
        hint="Known count."),
      F("""while = might run 0 times (sentinel, unknown count).""",
        "Which loop suits reading data until the sentinel -999?",
        ans=["while", "while loop"],
        hint="Unknown count.")],
  mcq=M("The loop for a menu that must show at least once is…",
        "do-while", "for", "while", "switch"))

S("cs22", T, H + "Jump statements · break",
  """
  **`break`** exits the loop (or switch) **immediately**. In **nested loops**, it **only exits the inner one**.

  Notes example: `for(n=10;n>0;n--){ if(n<8) break; cout<<n; }` gives the values **10 9 8** (with no space in the cout it actually prints `1098`).
  ```
  for (n = 10; n > 0; n--) {
      if (n < 8) break;
      cout << n << " ";
  }
  ```
  Output: `10 9 8`
  """,
  "What does the break loop above (with spaces) print?",
  ans=["10 9 8"],
  hint="It stops when n < 8.",
  fu=[F("""In nested loops, break only exits the **inner** loop.""",
        "In nested loops, which loop does break exit?",
        kw=["inner|innermost|inside|dalam|terdalam"],
        ans="Only the inner loop.",
        hint="Not both."),
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
        "What is the output?",
        ans=["6"],
        hint="For each i, only j = 0 and 1.")],
  mcq=M("`break` in an inner loop will…",
        "Exit the inner loop only", "Exit every loop", "End the program", "Skip one round"))

S("cs23", T, H + "Jump statements · continue",
  """
  **`continue`** skips the rest of this round.
  - In a **for** loop it goes to the **update**.
  - In **while / do-while** it goes to the **condition**.

  ```
  for (n = 10; n > 0; n--) {
      if (n % 2 == 1) continue;
      cout << n << " ";
  }
  ```
  Prints only even numbers: **10 8 6 4 2**.
  """,
  "What does the continue loop above print?",
  ans=["10 8 6 4 2"],
  hint="Odd numbers are skipped.",
  fu=[F("""In a for loop, continue jumps to the update (`n--`). In while/do-while, it jumps to the condition.""",
        "In a for loop, where does continue jump to?",
        ans=["update", "the update"],
        hint="n--."),
      F("""In a while loop, continue jumps straight to the condition.""",
        "In a while loop, where does continue jump to?",
        ans=["condition", "the condition"],
        hint="Not the update.")],
  mcq=M("`continue` in a loop…",
        "Skips the rest of this round and goes on to the next", "Exits the loop", "Ends the function", "Restarts the round without testing the condition"))

S("cs24", T, H + "Jump statements · return and goto",
  """
  - **`return`**: ends the **whole function**.
  - **`goto`**: jumps to a label. **Avoid it**, because it makes code **unstructured**.
  """,
  "Why should goto be avoided?",
  kw=["unstructured|not structured|structure|structured|messy|hard|tidak berstruktur|struktur"],
  ans="Because it makes code unstructured.",
  hint="The opposite of 'structured programming'.",
  fu=[F("""`return` ends the whole function, not just a loop.""",
        "Which jump statement ends the whole function?",
        ans=["return"],
        hint="R…")],
  mcq=M("The jump statement that jumps to a label and should be avoided is…",
        "goto", "break", "continue", "return"))

S("cs25", T, H + "TRAP: continue before the update in a while loop", trap=True,
  text="""
  ⚠ **TRAP**

  In a **while** loop, if `continue` comes **before the update** (`n = n - 1`), the update **never runs**. The loop prints **9 9 9 …** forever.

  ```
  int n = 9;
  while (n > 0) {
      cout << n << " ";
      if (n % 2 == 1) continue;   // odd n: jump to the condition
      n = n - 1;                  // never reached
  }
  ```
  """,
  question="Why does the loop above print 9 9 9 … forever?",
  kw=["continue", "before|skip|skips|sebelum|langkau",
      "update|n = n - 1|n-1|never|not run|tidak pernah|tak pernah"],
  ans="Because continue comes before the update, so n = n - 1 never runs and n stays 9.",
  hint="Does n ever change?",
  fu=[F("""Fix: put the update **before** continue, or use a for loop (continue in a for goes to the update).""",
        "Where should the update go to avoid this trap?",
        kw=["before|above|first|earlier|sebelum|atas|dahulu"],
        ans="Before the continue.",
        hint="Order of lines.")],
  mcq=M("In a while loop, continue before the update causes…",
        "An infinite loop", "The loop to end early", "A syntax error", "The update to run twice"))

S("cs26", T, H + "Nested loops",
  """
  The **inner loop runs all its rounds for each round of the outer loop**.

  Total inner runs = **outer × inner**. e.g. a 3 × 3 loop body runs **9 times**.
  """,
  "How many times does the body of a 3 × 3 nested loop run?",
  ans=["9", "nine", "9 times"],
  hint="outer × inner.",
  fu=[F("""Outer 4 times, inner 2 times.""",
        "How many times does the inner body run?",
        ans=["8"],
        hint="4 × 2."),
      F("""
        ```
        for (int i = 1; i <= 2; i++)
            for (int j = 1; j <= 3; j++)
                cout << i << j << " ";
        ```""",
        "What is the output?",
        ans=["11 12 13 21 22 23"],
        hint="j runs fully for each i.")],
  mcq=M("The total number of inner-loop runs in a nested loop is…",
        "outer × inner", "outer + inner", "inner only", "outer only"))
