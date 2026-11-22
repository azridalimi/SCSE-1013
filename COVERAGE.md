# COVERAGE: nota → statement

> **Status: provisional.** `SCSE1013_Study_Notes.pdf` was not available when this data was built.
> The statements are based on the SCSE1013 Lab 4, 5 and 6 documents (which follow the Ch3–Ch5 slide order)
> and the standard SCSE1013 syllabus for Ch1, Ch2 and the cheat sheet. When the PDF is added, re-map each PDF
> heading below and add statements for anything missing.

Total: **99 statements**, **155 follow-up questions**, **37 TRAP statements** (used by Kuiz Trap).


## Bab 01 · Computational Thinking

| Heading (tajuk kecil) | ID | TRAP | Follow-ups | Main question |
|---|---|---|---|---|
| 1.1 What is Computational Thinking | `ct01` |  | 1 | Apakah maksud Computational Thinking? |
| 1.2 Four cornerstones of CT | `ct02` |  | 1 | Senaraikan empat tunjang (cornerstones) Computational Thinking. |
| 1.2 Decomposition | `ct03` |  | 1 | Terangkan maksud decomposition. |
| 1.2 Pattern recognition | `ct04` |  | 1 | Apakah pattern recognition dan apakah faedahnya? |
| 1.2 Abstraction | `ct05` |  | 1 | Terangkan abstraction dengan ayat sendiri. |
| 1.2 Algorithm design | `ct06` |  | 1 | Apakah algorithm design? |
| 1.3 Characteristics of a good algorithm | `ct07` |  | 1 | Nyatakan sekurang-kurangnya tiga ciri algorithm yang baik. |
| 1.4 Problem solving steps (program development) | `ct08` |  | 2 | Senaraikan langkah-langkah penyelesaian masalah dalam pembangunan program mengikut turutan. |
| 1.5 TRAP: Abstraction vs Decomposition | `ct09` | ✓ | 1 | Apakah beza utama antara decomposition dan abstraction? |

## Bab 02 · Problem Solving: Algorithms, Pseudocode & Flowcharts

| Heading (tajuk kecil) | ID | TRAP | Follow-ups | Main question |
|---|---|---|---|---|
| 2.1 Algorithm, pseudocode and flowchart | `al01` |  | 1 | Apakah beza pseudocode dan flowchart? |
| 2.2 Pseudocode keywords | `al02` |  | 1 | Tulis DUA kata kunci pseudocode untuk input dan DUA untuk output. |
| 2.3 Flowchart symbols: terminal | `al03` |  | 1 | Apakah bentuk simbol terminal dan apakah fungsinya? |
| 2.3 Flowchart symbols: input/output | `al04` |  | 1 | Simbol flowchart apakah yang digunakan untuk input dan output? |
| 2.3 Flowchart symbols: process | `al05` |  | 1 | Simbol apakah untuk process dalam flowchart? |
| 2.3 Flowchart symbols: decision | `al06` |  | 1 | Terangkan simbol decision dalam flowchart. |
| 2.3 Flowchart symbols: flow lines, connector, predefined process | `al07` |  | 1 | Apakah simbol untuk memanggil modul/function (predefined process)? |
| 2.4 Three control structures | `al08` |  | 1 | Namakan tiga struktur kawalan asas. |
| 2.5 IPO example: income tax (Ch2 slide 9) | `al09` |  | 2 | Tulis formula cukai daripada contoh Ch2 slide 9. |
| 2.6 Counter, accumulator, sentinel in algorithms | `al10` |  | 2 | Apakah beza counter dan accumulator? |
| 2.7 Desk check / trace table | `al11` |  | 1 | Apakah desk check / trace table? |
| 2.8 TRAP: common flowchart mistakes | `al12` | ✓ | 1 | Senaraikan dua kesilapan biasa semasa melukis flowchart. |

## Bab 03 · Basics of C++ Programming

**Source map: Lab 4 · Ch3 Basic of programming (Topics covered)**

| Source section | Statement IDs |
|---|---|
| Parts of a program: keywords, identifiers, operators, punctuation, comments (slides 2–15, 22–25) | cp01, cp02, cp03, cp04, cp05 |
| Variables and literals (slides 16–21, 26–31, 71–72) | cp06 |
| Input and output with cin and cout, strings (slides 33–47) | cp07, cp08 |
| Data types and number systems (slides 48–62, 70) | cp09, cp10, cp11, cp12 |
| Named constants and the string class (slides 63–69) | cp13, cp14 |
| Scope (slides 73–74) | cp15 |
| Arithmetic operators, precedence, / and % (slides 75–86, 92) | cp16, cp17, cp18, cp25 |
| Type conversion and casting (slides 87–91, 99–102) | cp19, cp23 |
| Overflow, ++ and --, combined assignment (slides 94–98, 103–108) | cp20, cp21, cp22 |
| Part A1 compile-error log | cp24, cp01, cp02, cp05, cp07, cp15 |

| Heading (tajuk kecil) | ID | TRAP | Follow-ups | Main question |
|---|---|---|---|---|
| 3.1 Parts of a C++ program | `cp01` |  | 2 | Di manakah pelaksanaan program C++ bermula, dan apakah maksud return 0? |
| 3.1 Comments | `cp02` | ✓ | 1 | Apakah dua jenis komen dalam C++? |
| 3.2 Program elements: keywords, identifiers, operators, punctuation | `cp03` |  | 1 | Apakah beza keyword dan identifier? |
| 3.2 Identifier rules (Ch3 slide 25) | `cp04` | ✓ | 3 | Nyatakan peraturan menamakan identifier. |
| 3.2 Case sensitivity | `cp05` | ✓ | 1 | Mengapa `cout << Total;` menghasilkan ralat jika pemboleh ubah diisytihar sebagai `int total;`? |
| 3.3 Variables and literals (slide 31) | `cp06` |  | 1 | Apakah beza variable dan literal? |
| 3.4 Output and input: cout and cin | `cp07` |  | 2 | Apakah operator yang digunakan dengan cout dan cin? |
| 3.4 cin with char arrays and getline | `cp08` | ✓ | 2 | Apa yang berlaku apabila pengguna menaip `Hello World` ke `cin >> word;`? |
| 3.5 Data types and sizes (slide 62) | `cp09` |  | 2 | Berapakah saiz int dan double dalam byte? |
| 3.5 char vs string literal (slide 61) | `cp10` | ✓ | 2 | Apakah beza 'Z' dan "Z"? |
| 3.5 ASCII codes | `cp11` |  | 2 | Bagaimanakah char disimpan dalam komputer? |
| 3.5 Octal, hexadecimal and long literals | `cp12` | ✓ | 2 | Apakah nilai perpuluhan bagi literal `075`? |
| 3.6 Named constants: const vs #define (slides 63–66) | `cp13` | ✓ | 3 | Mengapakah `const` lebih disyorkan berbanding `#define`? |
| 3.6 The string class | `cp14` |  | 1 | Apakah header yang diperlukan untuk menggunakan string class? |
| 3.7 Scope: declare before use (slide 74) | `cp15` | ✓ | 1 | Adakah program di atas compile? Mengapa? |
| 3.8 Arithmetic operators, / and % | `cp16` | ✓ | 2 | Apakah nilai 13 % 5? |
| 3.8 Operator precedence | `cp17` |  | 3 | Antara * dan +, operator manakah dinilai dahulu? |
| 3.9 Mixed types and evaluation order | `cp18` | ✓ | 1 | Apakah output `cout << 7 / 2 * 2.0;`? |
| 3.9 Type conversion and casting (slides 87–91, 99–102) | `cp19` | ✓ | 2 | Mengapa sum / 3 mencetak 80 tetapi static_cast<double>(sum) / 3 mencetak 80.3333? |
| 3.10 Overflow (slides 94–98) | `cp20` | ✓ | 2 | Apakah yang berlaku apabila unsigned char bernilai 255 ditambah 1? |
| 3.11 Increment ++ and decrement -- (slides 103–108) | `cp21` | ✓ | 3 | Apakah beza ++x dan x++? |
| 3.11 Combined and multiple assignment | `cp22` |  | 3 | Apakah maksud `i *= j + 3;`? |
| 3.12 Default cout precision | `cp23` |  | 1 | Berapakah digit bererti yang dipaparkan cout secara lalai? |
| 3.13 Reading compiler errors (Lab 4 A1) | `cp24` | ✓ | 2 | Mengapa kita patut betulkan ralat pertama sahaja dahulu, kemudian compile semula? |
| 3.14 Using / and % for unit conversion (Lab 4 B3) | `cp25` |  | 1 | Bagaimana mendapatkan bilangan minit (selepas jam) daripada jumlah saat s? |

## Bab 04 · Control Structures (if, switch, loops)

**Source map: Lab 5 · Ch4 Control structures (Topics covered)**

| Source section | Statement IDs |
|---|---|
| Relational and logical operators (slides 2–8, 11) | cs01, cs02 |
| Complements of conditions (slides 9–10, 36) | cs03 |
| if, if…else, nested and compound statements (slides 12–35) | cs04, cs05, cs06, cs07, cs08, cs09 |
| n%2==1 with negatives (slide 37), leap year | cs10, cs11 |
| Conditional expression ?: (slides 38–39) | cs12 |
| switch and the selection patterns (slides 40–55) | cs13, cs14, cs24 |
| Loop parts and while, for, do…while (slides 56–73) | cs15, cs16, cs17, cs18, cs19, cs20 |
| break and continue (slides 74–80) | cs21 |
| Loop patterns: counting, totals, sentinel (slides 84–91) | cs22 |
| Nested loops (slides 92–94) | cs23 |
| Debugger (Part A) | cs25 |

| Heading (tajuk kecil) | ID | TRAP | Follow-ups | Main question |
|---|---|---|---|---|
| 4.1 Relational operators | `cs01` |  | 1 | Apakah nilai yang dihasilkan oleh ungkapan relational dalam C++? |
| 4.1 Logical operators and short-circuit | `cs02` |  | 2 | Apakah maksud short-circuit evaluation? |
| 4.2 Complements of conditions (De Morgan) | `cs03` | ✓ | 1 | Apakah complement bagi `x > 5`? |
| 4.3 if, if...else and compound statements | `cs04` |  | 1 | Bilakah kita MESTI menggunakan { } dalam if? |
| 4.4 Common trap: = instead of == | `cs05` | ✓ | 2 | Apakah output program tickets di atas? |
| 4.4 Common trap: semicolon after if | `cs06` | ✓ | 1 | Apakah output program di atas? |
| 4.4 Common trap: missing braces | `cs07` | ✓ | 1 | Apakah output program di atas? |
| 4.4 Common trap: dangling else | `cs08` | ✓ | 1 | Apakah output program di atas? |
| 4.5 Nested if / else-if chain (grade classifier) | `cs09` | ✓ | 2 | Dengan kod di atas, apakah gred bagi score = 90? |
| 4.6 Trap: n % 2 == 1 for negative numbers (slide 37) | `cs10` | ✓ | 1 | Apakah nilai -3 % 2 dalam C++? |
| 4.6 Compound condition: leap year | `cs11` |  | 2 | Tulis syarat C++ untuk tahun lompat y. |
| 4.7 Conditional operator ?: (slides 38–39) | `cs12` |  | 2 | Apakah sintaks conditional operator? |
| 4.8 switch statement rules | `cs13` |  | 2 | Apakah jenis data yang dibenarkan untuk expression dalam switch? |
| 4.8 Trap: switch fall-through (missing break) | `cs14` | ✓ | 2 | Apakah output program di atas? |
| 4.9 Loop parts and the while loop | `cs15` |  | 2 | Apakah tiga bahagian sesuatu loop? |
| 4.9 The for loop | `cs16` |  | 2 | Bilakah for loop paling sesuai digunakan? |
| 4.9 The do...while loop | `cs17` |  | 2 | Apakah beza utama do...while dan while? |
| 4.10 Common trap: semicolon after for/while | `cs18` | ✓ | 1 | Apakah output program di atas? |
| 4.10 Common trap: off-by-one (< vs <=) | `cs19` | ✓ | 1 | Berapa kali `for (int i = 0; i <= 5; i++)` berulang? |
| 4.10 Common trap: infinite loop (missing/wrong update) | `cs20` | ✓ | 1 | Namakan dua punca infinite loop. |
| 4.11 break and continue (slides 74–80) | `cs21` | ✓ | 3 | Apakah beza break dan continue? |
| 4.12 Loop patterns: counting, totals, sentinel (slides 84–91) | `cs22` |  | 2 | Apakah sentinel-controlled loop? |
| 4.13 Nested loops (slides 92–94) | `cs23` |  | 2 | Berapa kali inner loop berjalan secara keseluruhan dalam contoh segi tiga 3 baris? |
| 4.14 Choosing the right control structure | `cs24` |  | 1 | Bilakah switch lebih sesuai berbanding if/else if? |
| 4.15 Debugging with breakpoints (Lab 5) | `cs25` |  | 1 | Apakah fungsi breakpoint? |

## Bab 05 · Functions

**Source map: Lab 6 · Ch5 Functions: predefined functions (Topics covered) + user-defined functions**

| Source section | Statement IDs |
|---|---|
| Library functions and header files (slides 4–7) | fn01, fn02 |
| Math functions in <cmath> (slides 8–13) | fn03, fn04 |
| General-purpose library: rand (slide 14) | fn05 |
| Character functions in <cctype> (slides 15–23) | fn06 |
| C-string functions in <cstring> (slides 24–33) | fn07 |
| String and number conversion: atoi, atol, atof (slides 34–36) | fn08 |
| User-defined functions: prototype, parameters, return, void | fn09, fn10, fn11, fn12 |
| Pass by value / reference, scope, static | fn13, fn14, fn15, fn16 |
| Default arguments, overloading | fn17, fn18 |
| Invalid headers and call errors | fn19, fn20 |

| Heading (tajuk kecil) | ID | TRAP | Follow-ups | Main question |
|---|---|---|---|---|
| 5.1 What is a function | `fn01` |  | 1 | Nyatakan dua jenis function dan dua kelebihan menggunakan function. |
| 5.2 Library header files (slide 6) | `fn02` |  | 3 | Header apakah diperlukan untuk sqrt dan pow? |
| 5.3 Math functions in <cmath> (slides 8–13) | `fn03` | ✓ | 2 | Apakah nilai floor(-2.5)? |
| 5.3 Getting pi with acos(-1.0) (Lab 6 B2) | `fn04` |  | 1 | Mengapa kita guna acos(-1.0) dan bukan M_PI? |
| 5.4 Random numbers: rand and srand (slide 14) | `fn05` | ✓ | 2 | Apakah julat nilai `rand() % 6 + 1`? |
| 5.5 Character functions in <cctype> (slides 15–23) | `fn06` | ✓ | 2 | Apakah output `cout << toupper('a');`? |
| 5.6 C-string functions in <cstring> (slides 24–33) | `fn07` | ✓ | 2 | Apakah nilai pulangan strcmp jika dua string sama? |
| 5.7 atoi, atol, atof (slides 34–36) | `fn08` | ✓ | 2 | Apakah nilai atoi("12abc")? |
| 5.8 User-defined function: definition, prototype, call | `fn09` |  | 2 | Bilakah function prototype diperlukan? |
| 5.9 Parameters vs arguments | `fn10` |  | 1 | Apakah beza parameter dan argument? |
| 5.10 return and void functions | `fn11` |  | 2 | Apakah beza void function dan value-returning function? |
| 5.10 Trap: integer division inside a function | `fn12` | ✓ | 1 | Apakah output `cout << avg(3, 4);`? |
| 5.11 Pass by value | `fn13` |  | 2 | Apakah maksud pass by value? |
| 5.11 Pass by reference (&) | `fn14` |  | 3 | Bilakah kita perlu menggunakan pass by reference? |
| 5.12 Scope: local and global variables | `fn15` |  | 2 | Apakah beza local dan global variable? |
| 5.13 static local variables | `fn16` |  | 2 | Apakah keistimewaan static local variable? |
| 5.14 Default arguments | `fn17` |  | 1 | Apakah output add(2) dan add(2, 3)? (tulis: x y) |
| 5.15 Function overloading | `fn18` |  | 2 | Apakah syarat untuk function overloading? |
| 5.16 Invalid function headers | `fn19` | ✓ | 2 | Apakah kesilapan dalam header `int sum(int a, b)`? |
| 5.17 Common function call errors | `fn20` |  | 2 | Apakah mesej ralat jika function dipanggil dengan bilangan argument yang kurang? |

## Bab 06 · Ulangkaji Cheat Sheet

| Heading (tajuk kecil) | ID | TRAP | Follow-ups | Main question |
|---|---|---|---|---|
| 6.1 Exam-day checklist: read the question (IPO) | `ch01` |  | 1 | Apakah langkah pertama dalam checklist peperiksaan apabila membaca soalan program? |
| 6.2 Exam-day checklist: tracing code | `ch02` |  | 1 | Senaraikan dua perkara yang mesti diperhatikan semasa trace code. |
| 6.3 Exam-day checklist: semicolons | `ch03` | ✓ | 1 | Namakan TIGA tempat di mana ; TIDAK boleh diletakkan. |
| 6.4 Exam-day checklist: control structure traps | `ch04` | ✓ | 1 | Senaraikan tiga trap yang perlu disemak dalam if/switch/loop. |
| 6.5 Exam-day checklist: functions | `ch05` |  | 1 | Bilakah kita letak & pada parameter? |
| 6.6 Exam-day checklist: flowchart symbols recap | `ch06` |  | 1 | Padankan: Decision dan Input/Output masing-masing berbentuk apa? |
| 6.7 Exam-day checklist: output format | `ch07` |  | 2 | Bagaimana cout mencetak nilai double 7.0? |
| 6.8 Exam-day checklist: compile and test habits | `ch08` |  | 1 | Mengapa kita perlu menguji nilai sempadan seperti 90 dan 91? |
