from helpers import S, F, M

# =================================================================== CHAPTER 1
T = "ct"
H = "1 · "

S("ct01", T, H + "Computational thinking (definition)",
  """
  **Computational thinking** = solving a problem **the way a computer would**:

  1. break it into parts,
  2. spot patterns,
  3. design steps a computer can follow.
  """,
  "What is computational thinking?",
  kw=["computer|komputer",
      "break|pecah|pecahkan|bahagian|parts|decompose",
      "pattern|corak",
      "steps|langkah|step|algorithm|algoritma"],
  ans="Solving a problem the way a computer would: break it into parts, spot patterns, and design steps a computer can follow.",
  hint="Three actions: break, patterns, steps. And 'the way ___ would'?",
  fu=[F("""The definition in the notes: "solving a problem **the way a computer would**".""",
        "Complete: Computational thinking = solving a problem the way a ______ would.",
        ans=["computer", "komputer"],
        hint="A machine.")],
  mcq=M("According to the notes, computational thinking is…",
        "Solving a problem the way a computer would: break it up, spot patterns, design steps",
        "Memorising all of C++ syntax",
        "Repairing computer hardware",
        "Typing code as fast as possible"))

S("ct02", T, H + "4 key skills · Decomposition",
  """
  **Decomposition**: break a big problem into small, **manageable** parts.
  """,
  "What is decomposition?",
  kw=["break|pecah|pecahkan|bahagi|split|divide",
      "big|besar|large|kompleks|complex",
      "small|kecil|manageable|mudah diurus|bahagian kecil|parts"],
  ans="Breaking a big problem into small, manageable parts.",
  hint="A BIG problem becomes…",
  fu=[F("""Traffic example (notes): a traffic management system is split into **roads, vehicles, signals, pedestrian crossings**.""",
        "Splitting a traffic system into roads, vehicles, signals and pedestrian crossings uses which skill?",
        ans=["decomposition", "dekomposisi"],
        hint="Breaking it up.")],
  mcq=M("'Break a big problem into small, manageable parts' is…",
        "Decomposition", "Abstraction", "Pattern recognition", "Algorithm design"))

S("ct03", T, H + "4 key skills · Pattern recognition",
  """
  **Pattern recognition**: find similarities between the small parts.
  """,
  "What is pattern recognition?",
  kw=["similar|similarities|persamaan|sama|corak|pattern",
      "parts|bahagian|small|kecil|antara|between"],
  ans="Finding similarities between the small parts.",
  hint="After breaking it up, what do you look for between the parts?",
  fu=[F("""Traffic example: the patterns are **peak hours, accident hotspots, congestion areas**.""",
        "Name one pattern in the traffic system example.",
        kw=["peak|puncak|sibuk|accident|kemalangan|hotspot|congestion|kesesakan|sesak"],
        ans="Peak hours, accident hotspots or congestion areas.",
        hint="Certain times, certain places…")],
  mcq=M("'Find similarities between the small parts' is…",
        "Pattern recognition", "Decomposition", "Abstraction", "Evaluation"))

S("ct04", T, H + "4 key skills · Abstraction",
  """
  **Abstraction**: remove unnecessary details and **keep what matters**.
  """,
  "What is abstraction?",
  kw=["remove|buang|ignore|abaikan|unnecessary|tidak perlu|tak perlu|irrelevant",
      "keep|simpan|kekal|important|penting|matters|essential|fokus|focus"],
  ans="Removing unnecessary details and keeping what matters.",
  hint="Two actions: remove what, keep what?",
  fu=[F("""Traffic example: **only model main roads and busy intersections**.""",
        "In the traffic example, what is done at the abstraction stage?",
        kw=["main|utama|busy|sibuk|only|hanya",
            "road|jalan|intersection|persimpangan|simpang"],
        ans="Only model the main roads and busy intersections.",
        hint="Not every road…")],
  mcq=M("'Remove unnecessary details and keep what matters' is…",
        "Abstraction", "Decomposition", "Modelling", "Pattern recognition"))

S("ct05", T, H + "4 key skills · Algorithm design",
  """
  **Algorithm design**: write **step-by-step instructions** that solve the problem.
  """,
  "What is algorithm design?",
  kw=["step|langkah|step-by-step|langkah demi langkah",
      "instruction|arahan|write|tulis",
      "solve|selesai|menyelesaikan|solution|penyelesaian"],
  ans="Writing step-by-step instructions that solve the problem.",
  hint="Like a recipe.",
  fu=[F("""The four skills: Decomposition, Pattern recognition, Abstraction, **Algorithm design**. Algorithm design comes last: it produces steps that can be carried out.""",
        "Which skill produces the step-by-step instructions a computer follows?",
        ans=["algorithm design", "algorithm", "algoritma"],
        hint="A…")],
  mcq=M("'Write step-by-step instructions that solve it' is…",
        "Algorithm design", "Abstraction", "Evaluation", "Decomposition"))

S("ct06", T, H + "Memory trick: D-P-A-A",
  """
  💡 **MEMORY TRICK: "D-P-A-A"**

  **D**ivide it → find the **P**attern → **A**bstract (simplify) → write the **A**lgorithm.
  """,
  "What is the D-P-A-A memory trick? Give all four steps in order.",
  kw=["divide|decomposition|pecah|bahagi",
      "pattern|corak",
      "abstract|abstraction|simplify|ringkaskan|permudah",
      "algorithm|algoritma"],
  ans="Divide it → find the Pattern → Abstract (simplify) → write the Algorithm.",
  hint="D, P, A, A.",
  fu=[F("""In D-P-A-A, the first A = **Abstract (simplify)**, the second A = **Algorithm**.""",
        "In D-P-A-A, what does the first A stand for?",
        ans=["abstract", "abstraction", "abstract (simplify)", "simplify"],
        hint="Simplify.")],
  mcq=M("In the D-P-A-A memory trick, P stands for…",
        "find the Pattern", "Process", "Pseudocode", "Program"))

S("ct07", T, H + "5 stages · Decomposition (divide and conquer)",
  """
  **5 stages (extended version)**: Decomposition → Generalisation & Pattern Recognition → Modelling → Abstraction → Evaluation.

  **Stage 1 · Decomposition** = **divide and conquer**: split, solve each part, then **combine**.
  """,
  "Explain the Decomposition stage in the 5-stage version.",
  kw=["divide and conquer|divide|split|pecah|pecahkan",
      "solve|selesai|selesaikan|setiap|each",
      "combine|gabung|gabungkan|cantum|satukan"],
  ans="Divide and conquer: split the problem, solve each part, then combine.",
  hint="Three verbs: split, solve, …",
  fu=[F("""The 5 stages in order: 1 Decomposition, 2 Generalisation & Pattern Recognition, 3 Modelling, 4 Abstraction, 5 Evaluation.""",
        "What is the 5th (last) stage?",
        ans=["evaluation", "penilaian"],
        hint="Test and refine.")],
  mcq=M("The phrase 'divide and conquer' refers to the stage…",
        "Decomposition", "Modelling", "Evaluation", "Abstraction"))

S("ct08", T, H + "5 stages · Generalisation & Pattern Recognition",
  """
  **Stage 2 · Generalisation & Pattern Recognition**: find trends, then **reuse the same approach on similar problems**.
  """,
  "What is Generalisation & Pattern Recognition?",
  kw=["trend|trends|corak|pattern",
      "reuse|guna semula|ulang guna|same approach|pendekatan sama|sama",
      "similar|serupa|seumpama|similar problems"],
  ans="Finding trends, then reusing the same approach on similar problems.",
  hint="Find trends → … on similar problems.",
  fu=[F("""Generalisation means one solution can be applied to **similar** problems, not just one case.""",
        "Which stage number is Generalisation & Pattern Recognition?",
        ans=["2", "two", "dua"],
        hint="Right after Decomposition.")],
  mcq=M("'Find trends, then reuse the same approach on similar problems' is the stage…",
        "Generalisation & Pattern Recognition", "Modelling", "Abstraction", "Evaluation"))

S("ct09", T, H + "5 stages · Modelling",
  """
  **Stage 3 · Modelling**: make a **simplified (often visual) representation** of the real system.

  Traffic example: **simulate traffic flow and signal timing**.
  """,
  "What is Modelling?",
  kw=["simplified|ringkas|simple|mudah|permudah",
      "representation|perwakilan|model|wakil|gambaran",
      "visual|rajah|diagram|simulate|simulasi",
      "real|sebenar|system|sistem"],
  ans="Making a simplified (often visual) representation of the real system.",
  hint="Like a scale model of a building.",
  fu=[F("""Traffic example for Modelling: simulate traffic flow and signal timing.""",
        "What is done at the Modelling stage in the traffic example?",
        kw=["simulate|simulasi|simulation",
            "flow|aliran|signal|isyarat|timing|masa"],
        ans="Simulate traffic flow and signal timing.",
        hint="Simul…")],
  mcq=M("Simulating traffic flow is an example of the stage…",
        "Modelling", "Decomposition", "Evaluation", "Pattern recognition"))

S("ct10", T, H + "5 stages · Abstraction",
  """
  **Stage 4 · Abstraction**: focus on the **essential information** and **ignore the rest**.
  """,
  "In the 5 stages, what is Abstraction?",
  kw=["focus|fokus|essential|penting|important|utama",
      "ignore|abaikan|rest|lain|buang|tidak perlu"],
  ans="Focusing on the essential information and ignoring the rest.",
  hint="Essential vs the rest.",
  fu=[F("""Abstraction is stage 4, after Modelling and before Evaluation.""",
        "Which stage comes AFTER Abstraction?",
        ans=["evaluation", "penilaian"],
        hint="The last stage.")],
  mcq=M("In the 5-stage version, Abstraction comes right after…",
        "Modelling", "Evaluation", "Decomposition only", "Nothing (it is first)"))

S("ct11", T, H + "5 stages · Evaluation",
  """
  **Stage 5 · Evaluation**: **test** → find errors → **refine** and **repeat**.

  Traffic example: **test strategies and measure travel time and safety**.
  """,
  "What is Evaluation?",
  kw=["test|uji|ujian",
      "error|ralat|kesilapan|find|cari",
      "refine|perbaiki|baiki|improve|tambah baik",
      "repeat|ulang|ulangi"],
  ans="Test → find errors → refine and repeat.",
  hint="A cycle: test, find, refine, …",
  fu=[F("""Traffic example for Evaluation: test strategies and measure **travel time** and **safety**.""",
        "Which two things are measured at the Evaluation stage in the traffic example?",
        kw=["travel time|masa perjalanan|time|masa", "safety|keselamatan|selamat|safe"],
        ans="Travel time and safety.",
        hint="Time and …")],
  mcq=M("'Test → find errors → refine and repeat' is…",
        "Evaluation", "Modelling", "Abstraction", "Generalisation"))

S("ct12", T, H + "Example: traffic management system",
  """
  | Stage | What you do |
  |---|---|
  | Decomposition | Split into roads, vehicles, signals, pedestrian crossings |
  | Pattern | Peak hours, accident hotspots, congestion areas |
  | Modelling | Simulate traffic flow and signal timing |
  | Abstraction | Only model main roads and busy intersections |
  | Evaluation | Test strategies and measure travel time and safety |
  """,
  "In the traffic system example, 'Only model main roads and busy intersections' is which stage?",
  ans=["abstraction", "abstraksi"],
  hint="Only what matters.",
  fu=[F("""Table row: Pattern → Peak hours, accident hotspots, congestion areas.""",
        "'Peak hours, accident hotspots, congestion areas' is which stage?",
        ans=["pattern", "pattern recognition", "generalisation & pattern recognition", "corak"],
        hint="Patterns."),
      F("""Table row: Evaluation → Test strategies and measure travel time and safety.""",
        "'Test strategies and measure travel time and safety' is which stage?",
        ans=["evaluation", "penilaian"],
        hint="Testing."),
      F("""Table row: Modelling → Simulate traffic flow and signal timing.""",
        "'Simulate traffic flow and signal timing' is which stage?",
        ans=["modelling", "modeling", "pemodelan"],
        hint="Model.")],
  mcq=M("In the traffic example, 'Split into roads, vehicles, signals, pedestrian crossings' is…",
        "Decomposition", "Abstraction", "Modelling", "Evaluation"))

S("ct13", T, H + "Related ways of thinking · Logical thinking",
  """
  **Logical thinking**: reason clearly so that **conclusions follow from facts**.

  Steps: **Identify → Analyse → Formulate solution → Evaluate**
  """,
  "What is logical thinking and what are its steps?",
  kw=["conclusion|kesimpulan|reason|alasan|jelas|clearly",
      "fact|fakta",
      "identify|kenal pasti|kenalpasti",
      "analyse|analyze|analisis",
      "formulate|rumus|solution|penyelesaian",
      "evaluate|nilai|penilaian"],
  ans="Reasoning clearly so conclusions follow from facts. Identify → Analyse → Formulate solution → Evaluate.",
  hint="4 steps starting with Identify.",
  fu=[F("""Logical thinking: Identify → Analyse → Formulate solution → Evaluate.""",
        "What is the THIRD step of logical thinking?",
        ans=["formulate solution", "formulate", "rumus penyelesaian"],
        hint="F…")],
  mcq=M("The steps of logical thinking are…",
        "Identify → Analyse → Formulate solution → Evaluate",
        "Define → Identify steps → Sequence → Execute → Evaluate",
        "Input → Process → Output",
        "Decomposition → Pattern → Abstraction → Algorithm"))

S("ct14", T, H + "Related ways of thinking · Algorithmic thinking",
  """
  **Algorithmic thinking**: solve a problem as an **ordered list of steps**.

  Steps: **Define → Identify steps → Sequence → Execute → Evaluate**
  """,
  "What is algorithmic thinking and what are its steps?",
  kw=["ordered|tersusun|turutan|order|list|senarai",
      "step|langkah",
      "define|takrif|tentukan",
      "sequence|susun|urutan",
      "execute|laksana|jalankan|run",
      "evaluate|nilai"],
  ans="Solving a problem as an ordered list of steps. Define → Identify steps → Sequence → Execute → Evaluate.",
  hint="5 steps starting with Define.",
  fu=[F("""Algorithmic thinking has 5 steps: Define → Identify steps → Sequence → Execute → Evaluate. Logical thinking has 4.""",
        "Which step comes AFTER Sequence in algorithmic thinking?",
        ans=["execute", "laksana", "jalankan"],
        hint="Run it.")],
  mcq=M("'Define → Identify steps → Sequence → Execute → Evaluate' is…",
        "Algorithmic thinking", "Logical thinking", "The programming process", "The 5 CT stages"))

S("ct15", T, H + "Where it's used",
  """
  Computational thinking is used in:
  - **everyday life**: trip planning, budgeting
  - **software development**
  - **data analysis**
  - **research**
  """,
  "List at least three areas where computational thinking is used.",
  kw=["everyday|harian|daily|trip|budget|bajet|perjalanan",
      "software|perisian|development|pembangunan",
      "data|analysis|analisis",
      "research|penyelidikan|kajian"],
  ans="Everyday life (trip planning, budgeting), software development, data analysis, research.",
  hint="One daily-life, one software, one data, one research.",
  fu=[F("""The two everyday-life examples in the notes: **trip planning** and **budgeting**.""",
        "Give one everyday-life use of CT from the notes.",
        kw=["trip|perjalanan|percutian|travel|budget|bajet|belanjawan"],
        ans="Trip planning or budgeting.",
        hint="Holidays or money.")],
  mcq=M("Which is NOT an example of CT use given in the notes?",
        "Repairing a car engine by hand", "Trip planning", "Data analysis", "Research"))

# =================================================================== CHAPTER 2
T = "alg"
H = "2 · "

S("al01", T, H + "The programming process",
  """
  **Programming is problem solving:**

  **Understand the requirements → Analyse → Design the algorithm → Code → Test**
  """,
  "Write the programming process in order.",
  kw=["understand|faham|requirement|keperluan",
      "analyse|analyze|analisis",
      "design|reka|algorithm|algoritma",
      "code|kod|coding",
      "test|uji|testing"],
  ans="Understand the requirements → Analyse → Design the algorithm → Code → Test.",
  hint="5 steps. Starts with understanding, ends with testing.",
  fu=[F("""Design the algorithm comes **before** Code.""",
        "Which step comes right BEFORE Code?",
        ans=["design the algorithm", "design", "design algorithm", "reka algoritma"],
        hint="Design…")],
  mcq=M("In the programming process, the last step is…",
        "Test", "Code", "Analyse", "Design the algorithm"))

S("al02", T, H + "IPO · Rectangle area",
  """
  **Input → Process → Output (IPO)**, rectangle area example:

  | | Rectangle area |
  |---|---|
  | Input | length, width |
  | Process | area = length × width |
  | Output | area |
  """,
  "What are the Input, Process and Output for the rectangle area problem?",
  kw=["length|panjang", "width|lebar", "area = length|area = length × width|length × width|length * width|panjang darab lebar|area=length"],
  ans="Input: length, width. Process: area = length × width. Output: area.",
  hint="Two inputs, one formula, one output.",
  fu=[F("""length = 10, width = 15 → area = 10 × 15.""",
        "What is the area?",
        ans=["150", "area = 150", "area=150"],
        hint="10 × 15.")],
  mcq=M("In the rectangle area IPO, 'area' is the…",
        "Output", "Input", "Process", "Constant"))

S("al03", T, H + "IPO · Income tax",
  """
  | | Income tax |
  |---|---|
  | Input | name, monthly income, number of kids |
  | Process | tax = 0.25 × (income × 11 − kids × 450) |
  | Output | name, tax |
  """,
  "Write the process formula for income tax.",
  kw=["0.25", "11", "450", "income|pendapatan", "kids|anak"],
  ans="tax = 0.25 × (income × 11 − kids × 450)",
  hint="Rate 0.25; income times 11; 450 off per kid.",
  fu=[F("""Income = 4000, kids = 2: 0.25 × (4000 × 11 − 2 × 450) = 0.25 × 43100.""",
        "What is the tax?",
        ans=["10775", "rm10775", "rm 10775", "10775.0"],
        hint="0.25 × 43100."),
      F("""The income tax outputs are **name** and **tax**.""",
        "What are the outputs of the income tax problem?",
        kw=["name|nama", "tax|cukai"],
        ans="name and tax.",
        hint="Two things are displayed.")],
  mcq=M("In the income tax IPO, 'number of kids' is an…",
        "Input", "Process", "Output", "Formula"))

S("al04", T, H + "TIP: finding IPO in an exam question",
  """
  💡 **TIP**: in an exam question,
  - the **nouns** you are given are usually the **inputs**,
  - the **formula** is the **process**,
  - what you must **"display"** is the **output**.
  """,
  "How do you spot the input, process and output in an exam question?",
  kw=["noun|nouns|kata nama|nama|given|diberi",
      "formula|rumus",
      "display|papar|paparkan|tunjuk"],
  ans="The nouns given are the inputs, the formula is the process, and what you must display is the output.",
  hint="Nouns, formula, display.",
  fu=[F("""Question: "Given the radius, calculate the area using area = 3.14 × r × r and display the area." """,
        "What is the output of this question?",
        ans=["area", "the area", "luas"],
        hint="What is displayed?")],
  mcq=M("In an exam question, the formula is usually the…",
        "Process", "Input", "Output", "Sentinel"))

S("al05", T, H + "Procedural vs Object-Oriented",
  """
  - **Procedural (structured)**: built around **functions/procedures**. e.g. **C**.
  - **Object-oriented (OOP)**: built around **objects** (data + procedures). e.g. **C++**.
  """,
  "What is the difference between procedural and object-oriented programming?",
  kw=["procedural|structured|berstruktur",
      "function|procedure|fungsi|prosedur",
      "object|objek|oop",
      "data"],
  ans="Procedural is built around functions/procedures (e.g. C); OOP is built around objects that combine data and procedures (e.g. C++).",
  hint="One is built around functions, the other around objects.",
  fu=[F("""Notes: C = procedural, C++ = object-oriented.""",
        "Which language is the procedural example in the notes?",
        ans=["c", "c language"],
        hint="One letter.")],
  mcq=M("An object in OOP is made of…",
        "Data + procedures", "Functions only", "Global variables only", "A flowchart"))

S("al06", T, H + "Algorithm · definition",
  """
  **Algorithm**: a **finite sequence of steps** in a **logical order** that solves a problem.
  """,
  "Define an algorithm.",
  kw=["finite|terhingga|terhad",
      "sequence|turutan|steps|langkah",
      "logical|logik|order|susunan",
      "solve|selesai|menyelesaikan|problem|masalah"],
  ans="A finite sequence of steps in a logical order that solves a problem.",
  hint="Finite… sequence… logical order…",
  fu=[F("""Key words of the definition: **finite**, **sequence of steps**, **logical order**.""",
        "An algorithm must have a limited number of steps. What is the English word for this?",
        ans=["finite"],
        hint="F…")],
  mcq=M("An algorithm is…",
        "A finite sequence of steps in a logical order that solves a problem",
        "A programming language",
        "A diagram with oval symbols",
        "A compiled program"))

S("al07", T, H + "Algorithm · requirements",
  """
  Requirements of an algorithm:

  **has input** · **produces output** · **unambiguous** · **general** · **correct** · **finite** · **efficient**
  """,
  "List the requirements of an algorithm (at least five).",
  kw=["input", "output",
      "unambiguous|jelas|tidak samar|tak samar|clear",
      "general|umum",
      "correct|betul",
      "finite|terhingga|terhad",
      "efficient|cekap"],
  ans="Has input, produces output, unambiguous, general, correct, finite, efficient.",
  hint="7 of them: input, output, and five adjectives.",
  fu=[F("""'Unambiguous' = every step has **only one meaning**.""",
        "The step 'add a little salt' breaks which requirement?",
        ans=["unambiguous", "unambiguity"],
        hint="How much is 'a little'?"),
      F("""'General' = the algorithm works for **all valid inputs**, not just one case.""",
        "An algorithm that only works when length = 10 breaks which requirement?",
        ans=["general", "umum"],
        hint="Not specific.")],
  mcq=M("Which is NOT an algorithm requirement in the notes?",
        "Colourful", "Finite", "Efficient", "Unambiguous"))

S("al08", T, H + "Algorithm · three ways to design",
  """
  Three ways to design an algorithm:
  1. **Pseudocode**
  2. **Flowchart**
  3. **Top-down design (structure chart)**
  """,
  "What are the three ways to design an algorithm?",
  kw=["pseudocode|pseudokod", "flowchart|carta alir",
      "top-down|top down|structure chart|carta struktur"],
  ans="Pseudocode, flowchart and top-down design (structure chart).",
  hint="Two common ones, plus one 'from the top down'.",
  fu=[F("""Top-down design is also known as a **structure chart**.""",
        "Top-down design is drawn as a…?",
        ans=["structure chart", "carta struktur"],
        hint="S… chart.")],
  mcq=M("Top-down design is also known as a…",
        "Structure chart", "Trace table", "Pseudocode", "Truth table"))

S("al09", T, H + "Pseudocode",
  """
  **Pseudocode**: English-like steps with **no programming syntax**, so the logic is easy to read.

  ```
  1. Start
  2. Get name, monthly_income, num_kids
  3. tax = 0.25 * (monthly_income * 11 - num_kids * 450)
  4. Display name and tax
  5. End
  ```
  """,
  "What is pseudocode?",
  kw=["english|inggeris|bahasa",
      "no syntax|tiada sintaks|tanpa sintaks|no programming syntax|bukan kod|syntax|sintaks",
      "logic|logik|easy|mudah|read|baca|steps|langkah"],
  ans="English-like steps with no programming syntax, so the logic is easy to read.",
  hint="Like which language, and without what?",
  fu=[F("""In the tax pseudocode, input is read with the verb **Get** and output with **Display**.""",
        "Which verb reads the input in the pseudocode example?",
        ans=["get"],
        hint="Step 2."),
      F("""The tax pseudocode has 5 steps: Start, Get, tax = …, Display, End.""",
        "What is the LAST step?",
        ans=["end", "5. end"],
        hint="The opposite of Start.")],
  mcq=M("Pseudocode is written…",
        "In English-like steps, with no programming syntax",
        "In full C++ syntax",
        "In binary",
        "Using ovals and diamonds"))

S("al10", T, H + "Flowchart symbols · Terminal",
  """
  **Terminal** (**oval**): **Start / End**.

  A **function's** flowchart ends with **Return** (not End).
  """,
  "What is the Terminal symbol, and how does a function's flowchart end?",
  kw=["oval|bujur|kapsul|rounded|capsule",
      "start|end|mula|tamat",
      "return"],
  ans="The Terminal is an oval for Start/End; a function's flowchart ends with Return.",
  hint="Capsule shape; a function ends with the word R…",
  fu=[F("""A function chart starts with the function's name and ends with **Return**.""",
        "Which word ends a function's flowchart?",
        ans=["return"],
        hint="R…")],
  mcq=M("The oval in a flowchart is the…",
        "Terminal (Start/End)", "Process", "Decision", "Input/Output"))

S("al11", T, H + "Flowchart symbols · Process",
  """
  **Process** (**rectangle**): calculations and assignments.
  """,
  "Which symbol is used for Process, and what is it for?",
  kw=["rectangle|segi empat tepat|segiempat tepat|kotak|box",
      "calculation|kira|pengiraan|assignment|umpukan|calculations"],
  ans="A rectangle; for calculations and assignments.",
  hint="A plain box.",
  fu=[F("""`area = length * width` is a calculation → Process.""",
        "`sum = sum + counter` is drawn in which symbol?",
        ans=["rectangle", "process", "segi empat tepat", "box"],
        hint="An assignment.")],
  mcq=M("'tax = 0.25 * income' is drawn in a…",
        "Rectangle (Process)", "Parallelogram", "Diamond", "Oval"))

S("al12", T, H + "Flowchart symbols · Input/Output",
  """
  **Input/Output** (**parallelogram**): **Read / Display**.
  """,
  "Which symbol is used for Input/Output?",
  kw=["parallelogram|segi empat selari|selari|jajaran genjang"],
  ans="A parallelogram (Read / Display).",
  hint="A slanted box.",
  fu=[F("""Read and Display both use the parallelogram.""",
        "'Display sum' is drawn in which symbol?",
        ans=["parallelogram", "input/output", "segi empat selari"],
        hint="Same as Read.")],
  mcq=M("'Read length, width' is drawn in a…",
        "Parallelogram", "Rectangle", "Diamond", "Circle"))

S("al13", T, H + "Flowchart symbols · Decision",
  """
  **Decision** (**diamond**): **one line in, two out** (Yes/No).
  """,
  "Describe the Decision symbol.",
  kw=["diamond|berlian|wajik|rhombus",
      "one in|satu masuk|1 masuk|one line in|satu garis|1 in",
      "two out|dua keluar|2 keluar|2 out|yes|no|ya|tidak"],
  ans="A diamond; one line in, two out (Yes/No).",
  hint="Shape, how many in, how many out.",
  fu=[F("""Decision: 1 in, 2 out.""",
        "How many lines come OUT of a Decision?",
        ans=["2", "two", "dua"],
        hint="Yes and No.")],
  mcq=M("A Decision symbol has…",
        "One line in, two out (Yes/No)", "Two in, one out", "One in, one out", "No lines out"))

S("al14", T, H + "Flowchart symbols · Function/Subroutine",
  """
  **Function/Subroutine** (rectangle with **vertical lines on both sides**): **calls another flowchart**.
  """,
  "What does the Function/Subroutine symbol do?",
  kw=["call|calls|panggil|memanggil", "another|lain|separate|berasingan|flowchart|carta|chart"],
  ans="It calls another flowchart (a function).",
  hint="It doesn't do the work itself, it…",
  fu=[F("""Its shape: a rectangle with an extra line on the left and right edges.""",
        "What does the Function/Subroutine symbol look like?",
        kw=["rectangle|segi empat|kotak|box", "line|lines|garis|side|sides|tepi|double|berganda|bar"],
        ans="A rectangle with vertical lines on both sides.",
        hint="Like Process, plus something on the edges.")],
  mcq=M("A rectangle with vertical lines on both sides means…",
        "Call a function/subroutine (another flowchart)", "Input", "Decision", "Comment"))

S("al15", T, H + "Flowchart symbols · Connectors, flowline, comment",
  """
  - **Connectors**: **circle** = same page, **pentagon** = another page.
  - **Flowline** (arrow): shows the **direction of flow**.
  - **Comment symbol**: adds notes.
  """,
  "What is the difference between a circle connector and a pentagon connector?",
  kw=["circle|bulatan|bulat", "same|sama", "pentagon", "another|lain|other|different|berbeza"],
  ans="A circle connects on the same page; a pentagon connects to another page.",
  hint="One round, one five-sided.",
  fu=[F("""The flowline arrow shows the direction of flow.""",
        "What does a flowline do?",
        kw=["direction|arah", "flow|aliran"],
        ans="Shows the direction of flow.",
        hint="Arrow."),
      F("""The comment symbol is used to add notes.""",
        "Which symbol adds notes to a flowchart?",
        ans=["comment", "comment symbol", "komen"],
        hint="C…")],
  mcq=M("A pentagon connector links to…",
        "Another page", "The same page", "A function", "A decision"))

S("al16", T, H + "3 control structures",
  """
  **3 control structures (the foundation of everything):**

  - **Sequence**: steps run in order, top to bottom.
  - **Selection**: choose a path: `if`, `if-else`, nested if.
  - **Repetition**: repeat while a condition is true: **pre-test** or **post-test** loop.
  """,
  "Name and explain the three control structures.",
  kw=["sequence|jujukan|turutan",
      "selection|pilihan|pemilihan|if",
      "repetition|ulangan|loop|pengulangan|gelung"],
  ans="Sequence (steps run in order, top to bottom), Selection (choose a path: if, if-else, nested if), Repetition (repeat while a condition is true: pre-test/post-test).",
  hint="S, S, R.",
  fu=[F("""Repetition: repeat **while a condition is true**, either pre-test or post-test.""",
        "The two kinds of loop in repetition are pre-test and …?",
        ans=["post-test", "post test", "posttest"],
        hint="The opposite of 'pre'.")],
  mcq=M("'Steps run in order, top to bottom' is…",
        "Sequence", "Selection", "Repetition", "Decomposition"))

S("al17", T, H + "Selection forms",
  """
  | Form | Idea | Pseudocode |
  |---|---|---|
  | One choice (if) | "do or don't" | `if cond … end_if` |
  | Two choices (if-else) | "do this or that" | `if cond … else … end_if` |
  | Multi (if-else if-else) | several ranges | `if … else if … else if … else … end_if` |
  """,
  "What is the idea behind 'one choice (if)'?",
  ans=["do or don't", "do or dont"],
  hint="\"do or …\"",
  fu=[F("""Two choices (if-else) = "do this or that".""",
        "What is the idea behind if-else?",
        ans=["do this or that"],
        hint="\"do this or …\""),
      F("""Multi (if-else if-else) is for **several ranges**.""",
        "Which selection form suits several ranges (e.g. grades A–F)?",
        ans=["multi", "if-else if-else", "if else if else", "else if", "multi (if-else if-else)"],
        hint="Several ranges.")],
  mcq=M("The pseudocode `if cond … else … end_if` is the form…",
        "Two choices (if-else)", "One choice (if)", "Multi (if-else if-else)", "Repetition"))

S("al18", T, H + "Operators · Relational",
  """
  | Relational | Meaning |
  |---|---|
  | `>  <  >=  <=` | compare size |
  | `==` | equal to |
  | `!=` | not equal to |
  """,
  "What does the operator `!=` mean?",
  ans=["not equal to", "not equal", "tidak sama dengan"],
  hint="! = not.",
  fu=[F("""`==` means **equal to** (comparison). It is different from `=` (assignment).""",
        "Which relational operator means 'equal to'?",
        ans=["=="],
        hint="Two equals signs.")],
  mcq=M("Which operator compares size?",
        ">=", "==", "&&", "!"))

S("al19", T, H + "Operators · Logical",
  """
  | Logical | True when… |
  |---|---|
  | `&&` AND | **both** are true |
  | `||` OR | **at least one** is true |
  | `!` NOT | flips true ↔ false |
  """,
  "When are && (AND) and || (OR) true?",
  kw=["&&|and", "both|kedua-dua|keduanya|semua|all",
      "\\|\\||or", "at least one|sekurang-kurangnya satu|salah satu|one|satu"],
  ans="&& is true when both are true; || is true when at least one is true.",
  hint="AND = both; OR = …",
  fu=[F("""`!` NOT flips the value: true ↔ false.""",
        "What is the value of `!true`?",
        ans=["false", "0"],
        hint="Flip it.")],
  mcq=M("`||` is true when…",
        "At least one operand is true", "Both operands are true", "Both operands are false", "Never"))

S("al20", T, H + "Memory trick: AND is strict, OR is generous",
  """
  💡 **MEMORY TRICK**: **AND is strict** (any F gives F). **OR is generous** (any T gives T).

  e.g. x = 12, y = 5, z = −4:
  - `(x>y)&&(y>z)` = **true**
  - `(x<=z)||(y==z)` = **false**
  - `!(x>=z)` = **false**
  """,
  "Explain the memory trick 'AND is strict, OR is generous'.",
  kw=["and|&&", "strict|ketat", "any f|mana-mana f|f memberi f|mana-mana false|satu false|any false|f gives f|false",
      "or|\\|\\|", "generous|murah hati|pemurah", "any t|mana-mana t|t memberi t|mana-mana true|satu true|any true|t gives t|true"],
  ans="AND is strict: any F gives F. OR is generous: any T gives T.",
  hint="Strict / generous… F gives F, T gives T.",
  fu=[F("""x = 12, y = 5, z = −4. `(x>y)`: 12 > 5 = T; `(y>z)`: 5 > −4 = T.""",
        "What is `(x>y)&&(y>z)`? (true / false)",
        ans=["true", "1"],
        hint="T && T."),
      F("""`(x<=z)`: 12 <= −4 = F; `(y==z)`: 5 == −4 = F.""",
        "What is `(x<=z)||(y==z)`? (true / false)",
        ans=["false", "0"],
        hint="F || F."),
      F("""`(x>=z)`: 12 >= −4 = T.""",
        "What is `!(x>=z)`? (true / false)",
        ans=["false", "0"],
        hint="!T.")],
  mcq=M("With x=12, y=5, z=−4, `(x<=z)||(y==z)` is…",
        "false", "true", "−4", "an error"))

S("al21", T, H + "Repetition · Pre-test vs post-test",
  """
  - **Pre-test (while)**: checks the condition **first**, so the body may run **0 times**.
  - **Post-test (do-while)**: runs the body **first** and checks after, so it runs **at least once**.
  """,
  "What is the difference between a pre-test loop and a post-test loop?",
  kw=["pre-test|pre test|while",
      "first|dahulu|dulu|0 times|0 kali|sifar|zero|mungkin tidak|before",
      "post-test|post test|do-while|do while",
      "at least once|sekurang-kurangnya sekali|sekali|once"],
  ans="A pre-test loop (while) checks the condition first, so it may run 0 times. A post-test loop (do-while) runs the body first, so it runs at least once.",
  hint="When is the condition checked?",
  fu=[F("""do-while is a post-test loop.""",
        "What is the MINIMUM number of times a do-while body runs?",
        ans=["1", "once", "one", "1 time"],
        hint="At least…"),
      F("""while is a pre-test loop.""",
        "What is the MINIMUM number of times a while body runs?",
        ans=["0", "zero", "0 times"],
        hint="The condition may be false from the start.")],
  mcq=M("Which loop is guaranteed to run at least once?",
        "Post-test (do-while)", "Pre-test (while)", "for", "None"))

S("al22", T, H + "Counter-controlled loop · 3 parts",
  """
  A **counter-controlled loop** has 3 parts:

  1. **initialise**: `cnt = 0`
  2. **test**: `cnt < n`
  3. **update**: `cnt = cnt + 1`
  """,
  "What are the three parts of a counter-controlled loop?",
  kw=["initialise|initialize|initialization|initialisation|inisialisasi|nilai awal|cnt = 0",
      "test|condition|syarat|uji|cnt < n",
      "update|kemas kini|cnt = cnt + 1|tambah|increment"],
  ans="Initialise (cnt = 0), test (cnt < n), update (cnt = cnt + 1).",
  hint="Start, test, change.",
  fu=[F("""Notes example: ① `cnt = 0` ② `cnt < n` ③ `cnt = cnt + 1`.""",
        "Write the update part from the notes example.",
        ans=["cnt = cnt + 1", "cnt=cnt+1", "cnt++", "cnt += 1"],
        hint="cnt plus one.")],
  mcq=M("In a counter-controlled loop, `cnt < n` is the…",
        "Test", "Initialise", "Update", "Body"))

S("al23", T, H + "Counter-controlled loop · sum 1 to 10 pseudocode",
  """
  ```
  Start
  Set sum = 0, counter = 1
  While counter <= 10
      sum = sum + counter
      counter = counter + 1
  End_While
  Display sum            → 55
  End
  ```
  """,
  "What value of sum does the pseudocode above display?",
  ans=["55"],
  hint="1 + 2 + … + 10.",
  fu=[F("""Change the condition to `While counter <= 5`.""",
        "What is sum now?",
        ans=["15"],
        hint="1 + 2 + 3 + 4 + 5."),
      F("""The While block is closed with `End_While`.""",
        "Which keyword closes the While loop in the notes' pseudocode?",
        ans=["end_while", "endwhile", "end while"],
        hint="End_…")],
  mcq=M("In the sum 1–10 pseudocode, what is counter after the loop ends?",
        "11", "10", "55", "0"))

S("al24", T, H + "User-controlled loop and sentinel",
  """
  - **User-controlled loop**: the user enters **how many times** to repeat (`limit`).
  - **Sentinel**: a special value that **ends the input**, e.g. **`-999`** or the name **`"OK"`**. Use it when you **don't know how many items** there will be.
  """,
  "What is a sentinel, and when is it used?",
  kw=["special|khas|nilai khas",
      "end|ends|tamat|stop|berhenti|hentikan|menamatkan",
      "don't know|dont know|do not know|tidak tahu|tak tahu|unknown|tidak diketahui|berapa banyak|how many"],
  ans="A special value (e.g. -999 or \"OK\") that ends the input; used when you don't know how many items there will be.",
  hint="For example -999.",
  fu=[F("""Sentinel examples in the notes: `-999` and the name `"OK"`.""",
        "Give a numeric sentinel value from the notes.",
        ans=["-999"],
        hint="Negative, three identical digits."),
      F("""User-controlled loop: the user enters `limit`.""",
        "In a user-controlled loop, who decides how many times to repeat?",
        ans=["user", "the user", "pengguna"],
        hint="It's in the name.")],
  mcq=M("A loop that reads marks until the user types -999 is a…",
        "Sentinel-controlled loop", "Counter-controlled loop", "Nested loop", "Infinite loop"))

S("al25", T, H + "Trace table",
  """
  **Trace table**: write each variable as a **column** and fill in **a row for each step or input**. It helps you find **logic errors**.

  | Length | Width | Area | Perimeter | Output |
  |---|---|---|---|---|
  | 10 | 15 | 150 | 50 | Area=150, Perimeter=50 |
  | 20 | 20 | 400 | 80 | Area=400, Perimeter=80 |
  """,
  "What is a trace table and what is it for?",
  kw=["column|lajur|variable|pemboleh ubah",
      "row|baris|step|langkah|input",
      "logic error|ralat logik|error|errors|ralat|kesilapan"],
  ans="A table with each variable as a column and a row for each step or input; it helps you find logic errors.",
  hint="Columns = ?, rows = ?, purpose = ?",
  fu=[F("""Perimeter = 2 × (length + width). Second row: length 20, width 20.""",
        "What is the Perimeter in the second row?",
        ans=["80"],
        hint="2 × 40."),
      F("""Length = 10, width = 15.""",
        "What is the Perimeter in the first row?",
        ans=["50"],
        hint="2 × 25.")],
  mcq=M("A trace table mainly helps you find…",
        "Logic errors", "Only syntax errors", "Viruses", "Missing headers"))

S("al26", T, H + "Modular flowcharts · call vs definition",
  """
  **Modular flowcharts (functions):**
  - The **function call** (in the main chart) says **what** to do.
  - The **function definition** (a separate chart) says **how** to do it.
  """,
  "What is the difference between a function call and a function definition in a modular flowchart?",
  kw=["call|panggilan|panggil", "what|apa",
      "definition|definisi|takrif", "how|bagaimana|cara"],
  ans="The function call (main chart) says what to do; the function definition (a separate chart) says how to do it.",
  hint="What vs how.",
  fu=[F("""The function definition is drawn in **a separate chart**.""",
        "Where is the function definition drawn?",
        kw=["separate|berasingan|lain|another|own|sendiri|asing"],
        ans="In a separate chart (flowchart).",
        hint="Not in the main chart.")],
  mcq=M("In a modular flowchart, the chart that says HOW a task is done is the…",
        "Function definition", "Function call", "Main chart", "Connector"))

S("al27", T, H + "Modular flowcharts · function chart start and end",
  """
  A **function chart** starts with the **function name**, e.g. `AVRG(R, a, b, c)`, and ends with **Return**.
  """,
  "How does a function chart start and end?",
  kw=["name|nama|avrg", "return"],
  ans="It starts with the function name (e.g. AVRG(R, a, b, c)) and ends with Return.",
  hint="Starts with the N…, ends with R…",
  fu=[F("""Example function chart name: `AVRG(R, a, b, c)`.""",
        "In `AVRG(R, a, b, c)`, what is the function name?",
        ans=["avrg"],
        hint="Before the brackets.")],
  mcq=M("A function chart ends with…",
        "Return", "End", "Stop", "Exit"))

S("al28", T, H + "Modular flowcharts · actual vs formal parameters",
  """
  - **Actual parameters** are in the **call**: `(n1, n2, n3)`.
  - **Formal parameters** are in the **definition**: `(a, b, c)`.
  - They are matched **by order, not by name**.
  """,
  "What is the difference between actual and formal parameters, and how are they matched?",
  kw=["actual|sebenar", "call|panggilan|panggil",
      "formal", "definition|definisi|takrif",
      "order|turutan|kedudukan|susunan|position"],
  ans="Actual parameters are in the call (n1, n2, n3); formal parameters are in the definition (a, b, c); they are matched by order, not by name.",
  hint="One in the call, one in the definition; matched by what?",
  fu=[F("""Call `AVRG(R, n1, n2, n3)` and definition `AVRG(R, a, b, c)`. Matched by order.""",
        "Which formal parameter receives the value of n2?",
        ans=["b"],
        hint="Second position."),
      F("""The names don't have to match; only the **order** matters.""",
        "Must actual and formal parameter names be the same? (yes / no)",
        ans=["no", "tidak", "tak"],
        hint="By order, not by name.")],
  mcq=M("Actual and formal parameters are matched by…",
        "Order", "Name", "Data type only", "Alphabetical order"))

S("al29", T, H + "Modular flowcharts · variables in the current chart",
  """
  In a modular flowchart, **only use variables that exist in the current chart**.

  e.g. inside the `AVRG(R, a, b, c)` chart, use a, b, c, not n1, n2, n3.
  """,
  "Which variables can a function chart use?",
  kw=["exist|exists|wujud|ada", "current|semasa|this|ini|same|sama|chart|carta"],
  ans="Only variables that exist in the current chart.",
  hint="Not the main chart's variables.",
  fu=[F("""In the definition `AVRG(R, a, b, c)`, n1 belongs to the main chart.""",
        "Can the AVRG chart use n1 directly? (yes / no)",
        ans=["no", "tidak", "tak"],
        hint="It doesn't exist in the AVRG chart.")],
  mcq=M("Inside the function chart AVRG(R, a, b, c), the valid variables are…",
        "a, b, c and R", "n1, n2, n3", "All main-chart variables", "None"))

S("al30", T, H + "From flowchart to code",
  """
  **From flowchart to code:**

  Problem → Flowchart → rough **"intermediate" code** → **complete code** (add `#include`, variable declarations and **prompts**).
  """,
  "What is the path from a problem to complete code?",
  kw=["problem|masalah", "flowchart|carta alir",
      "intermediate|rough|kasar|pertengahan",
      "complete|lengkap|full|penuh"],
  ans="Problem → Flowchart → rough intermediate code → complete code.",
  hint="4 stages, including a 'rough' code.",
  fu=[F("""Complete code adds three things to the intermediate code: `#include`, variable declarations, prompts.""",
        "Name two things added to make the code complete.",
        kw=["#include|include|header", "declaration|declarations|pengisytiharan|isytihar|declare|variable", "prompt|prompts|gesaan"],
        ans="#include, variable declarations and prompts.",
        hint="Header, variables, messages to the user.")],
  mcq=M("Which is NOT added when turning intermediate code into complete code?",
        "A diamond symbol", "#include", "Variable declarations", "Prompts"))
