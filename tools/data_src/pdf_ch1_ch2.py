from helpers import S, F, M

# =================================================================== BAB 1
T = "ct"
H = "1 · "

S("ct01", T, H + "Computational thinking (definition)",
  """
  **Computational thinking** = menyelesaikan masalah **cara komputer menyelesaikannya**:

  1. pecahkan (break) masalah kepada bahagian,
  2. kenal pasti corak (spot patterns),
  3. reka langkah-langkah yang boleh diikuti oleh komputer (design steps a computer can follow).
  """,
  "Apakah maksud computational thinking?",
  kw=["computer|komputer",
      "break|pecah|pecahkan|bahagian|parts|decompose",
      "pattern|corak",
      "steps|langkah|step|algorithm|algoritma"],
  ans="Menyelesaikan masalah cara komputer: pecahkan kepada bahagian, kenal pasti corak, dan reka langkah yang komputer boleh ikut.",
  hint="Tiga tindakan: pecah, corak, langkah. Dan 'cara siapa'?",
  fu=[F("""Definisi nota: "solving a problem **the way a computer would**".""",
        "Lengkapkan: Computational thinking = solving a problem the way a ______ would.",
        ans=["computer", "komputer"],
        hint="Mesin.")],
  mcq=M("Menurut nota, computational thinking ialah…",
        "Menyelesaikan masalah cara komputer: pecah, cari corak, reka langkah",
        "Menghafal semua sintaks C++",
        "Membaiki perkakasan komputer",
        "Menaip kod secepat mungkin"))

S("ct02", T, H + "4 key skills · Decomposition",
  """
  **Decomposition**: pecahkan masalah besar (break a big problem) kepada bahagian kecil yang **mudah diurus** (small, manageable parts).
  """,
  "Apakah decomposition?",
  kw=["break|pecah|pecahkan|bahagi|split|divide",
      "big|besar|large|kompleks|complex",
      "small|kecil|manageable|mudah diurus|bahagian kecil|parts"],
  ans="Memecahkan masalah besar kepada bahagian kecil yang mudah diurus.",
  hint="Masalah BESAR menjadi…",
  fu=[F("""Contoh trafik (nota): sistem pengurusan trafik dipecahkan kepada **roads, vehicles, signals, pedestrian crossings**.""",
        "Memecahkan sistem trafik kepada jalan, kenderaan, lampu isyarat dan lintasan pejalan kaki ialah skill apa?",
        ans=["decomposition", "dekomposisi"],
        hint="Pecah.")],
  mcq=M("'Break a big problem into small, manageable parts' ialah…",
        "Decomposition", "Abstraction", "Pattern recognition", "Algorithm design"))

S("ct03", T, H + "4 key skills · Pattern recognition",
  """
  **Pattern recognition**: cari persamaan (find similarities) di antara bahagian-bahagian kecil tersebut.
  """,
  "Apakah pattern recognition?",
  kw=["similar|similarities|persamaan|sama|corak|pattern",
      "parts|bahagian|small|kecil|antara|between"],
  ans="Mencari persamaan antara bahagian-bahagian kecil.",
  hint="Selepas dipecahkan, apa yang dicari antara bahagian-bahagian itu?",
  fu=[F("""Contoh trafik: corak yang dicari ialah **peak hours, accident hotspots, congestion areas**.""",
        "Namakan satu corak (pattern) dalam contoh sistem trafik.",
        kw=["peak|puncak|sibuk|accident|kemalangan|hotspot|congestion|kesesakan|sesak"],
        ans="Peak hours, accident hotspots atau congestion areas.",
        hint="Waktu tertentu, tempat tertentu…")],
  mcq=M("'Find similarities between the small parts' ialah…",
        "Pattern recognition", "Decomposition", "Abstraction", "Evaluation"))

S("ct04", T, H + "4 key skills · Abstraction",
  """
  **Abstraction**: buang butiran yang tidak perlu (remove unnecessary details) dan **simpan yang penting** (keep what matters).
  """,
  "Apakah abstraction?",
  kw=["remove|buang|ignore|abaikan|unnecessary|tidak perlu|tak perlu|irrelevant",
      "keep|simpan|kekal|important|penting|matters|essential|fokus|focus"],
  ans="Buang butiran yang tidak perlu dan simpan yang penting.",
  hint="Dua tindakan: buang apa, simpan apa?",
  fu=[F("""Contoh trafik: **hanya model jalan utama dan persimpangan sibuk** (only model main roads and busy intersections).""",
        "Dalam contoh trafik, apakah yang dibuat pada peringkat abstraction?",
        kw=["main|utama|busy|sibuk|only|hanya",
            "road|jalan|intersection|persimpangan|simpang"],
        ans="Hanya model jalan utama dan persimpangan yang sibuk.",
        hint="Bukan semua jalan…")],
  mcq=M("'Remove unnecessary details and keep what matters' ialah…",
        "Abstraction", "Decomposition", "Modelling", "Pattern recognition"))

S("ct05", T, H + "4 key skills · Algorithm design",
  """
  **Algorithm design**: tulis arahan langkah demi langkah (step-by-step instructions) yang menyelesaikan masalah.
  """,
  "Apakah algorithm design?",
  kw=["step|langkah|step-by-step|langkah demi langkah",
      "instruction|arahan|write|tulis",
      "solve|selesai|menyelesaikan|solution|penyelesaian"],
  ans="Menulis arahan langkah demi langkah yang menyelesaikan masalah.",
  hint="Seperti resepi.",
  fu=[F("""Empat skill: Decomposition, Pattern recognition, Abstraction, **Algorithm design**. Algorithm design ialah yang terakhir: hasilnya langkah yang boleh dilaksanakan.""",
        "Skill apakah yang menghasilkan langkah demi langkah untuk diikuti komputer?",
        ans=["algorithm design", "algorithm", "algoritma", "reka bentuk algoritma"],
        hint="A…")],
  mcq=M("'Write step-by-step instructions that solve it' ialah…",
        "Algorithm design", "Abstraction", "Evaluation", "Decomposition"))

S("ct06", T, H + "Memory trick: D-P-A-A",
  """
  💡 **MEMORY TRICK: "D-P-A-A"**

  **D**ivide it → find the **P**attern → **A**bstract (simplify) → write the **A**lgorithm.
  """,
  "Apakah memory trick D-P-A-A? Tulis keempat-empat langkah mengikut turutan.",
  kw=["divide|decomposition|pecah|bahagi",
      "pattern|corak",
      "abstract|abstraction|simplify|ringkaskan|permudah",
      "algorithm|algoritma"],
  ans="Divide it → find the Pattern → Abstract (simplify) → write the Algorithm.",
  hint="D, P, A, A.",
  fu=[F("""Dalam D-P-A-A, huruf A pertama = **Abstract (simplify)**, A kedua = **Algorithm**.""",
        "Dalam D-P-A-A, A yang pertama bermaksud apa?",
        ans=["abstract", "abstraction", "abstract (simplify)", "simplify"],
        hint="Permudahkan.")],
  mcq=M("Dalam memory trick D-P-A-A, huruf P bermaksud…",
        "find the Pattern", "Process", "Pseudocode", "Program"))

S("ct07", T, H + "5 stages · Decomposition (divide and conquer)",
  """
  **5 stages (extended version)**: Decomposition → Generalisation & Pattern Recognition → Modelling → Abstraction → Evaluation.

  **Stage 1 · Decomposition** = **divide and conquer**: pecahkan (split), selesaikan setiap bahagian (solve each part), kemudian **gabungkan** (then combine).
  """,
  "Terangkan stage Decomposition dalam versi 5 stages.",
  kw=["divide and conquer|divide|split|pecah|pecahkan",
      "solve|selesai|selesaikan|setiap|each",
      "combine|gabung|gabungkan|cantum|satukan"],
  ans="Divide and conquer: pecahkan, selesaikan setiap bahagian, kemudian gabungkan.",
  hint="Tiga kata kerja: split, solve, …",
  fu=[F("""Turutan 5 stages: 1 Decomposition, 2 Generalisation & Pattern Recognition, 3 Modelling, 4 Abstraction, 5 Evaluation.""",
        "Apakah stage yang KE-5 (terakhir)?",
        ans=["evaluation", "penilaian"],
        hint="Uji dan perbaiki.")],
  mcq=M("Frasa 'divide and conquer' merujuk kepada stage…",
        "Decomposition", "Modelling", "Evaluation", "Abstraction"))

S("ct08", T, H + "5 stages · Generalisation & Pattern Recognition",
  """
  **Stage 2 · Generalisation & Pattern Recognition**: cari trend (find trends), kemudian **guna semula pendekatan yang sama** pada masalah yang serupa (reuse the same approach on similar problems).
  """,
  "Apakah Generalisation & Pattern Recognition?",
  kw=["trend|trends|corak|pattern",
      "reuse|guna semula|ulang guna|same approach|pendekatan sama|sama",
      "similar|serupa|seumpama|similar problems"],
  ans="Cari trend, kemudian guna semula pendekatan yang sama pada masalah yang serupa.",
  hint="Cari trend → … pada masalah serupa.",
  fu=[F("""Generalisation bermaksud penyelesaian yang sama boleh dipakai pada masalah yang **serupa**, bukan hanya satu kes.""",
        "Stage ke berapakah Generalisation & Pattern Recognition? (nombor)",
        ans=["2", "dua", "two"],
        hint="Selepas Decomposition.")],
  mcq=M("'Find trends, then reuse the same approach on similar problems' ialah stage…",
        "Generalisation & Pattern Recognition", "Modelling", "Abstraction", "Evaluation"))

S("ct09", T, H + "5 stages · Modelling",
  """
  **Stage 3 · Modelling**: buat **perwakilan ringkas** (simplified representation), selalunya **visual**, bagi sistem sebenar.

  Contoh trafik: **simulate traffic flow and signal timing**.
  """,
  "Apakah Modelling?",
  kw=["simplified|ringkas|simple|mudah|permudah",
      "representation|perwakilan|model|wakil|gambaran",
      "visual|rajah|diagram|simulate|simulasi",
      "real|sebenar|system|sistem"],
  ans="Membuat perwakilan ringkas (selalunya visual) bagi sistem sebenar.",
  hint="Seperti maket bangunan.",
  fu=[F("""Contoh trafik bagi Modelling: simulasi aliran trafik dan masa lampu isyarat.""",
        "Apakah yang dibuat pada peringkat Modelling dalam contoh trafik?",
        kw=["simulate|simulasi|simulation",
            "flow|aliran|signal|isyarat|timing|masa"],
        ans="Simulasi aliran trafik dan masa lampu isyarat.",
        hint="Simul…")],
  mcq=M("Membuat simulasi aliran trafik ialah contoh stage…",
        "Modelling", "Decomposition", "Evaluation", "Pattern recognition"))

S("ct10", T, H + "5 stages · Abstraction",
  """
  **Stage 4 · Abstraction**: fokus kepada **maklumat penting** (essential information) dan **abaikan yang lain** (ignore the rest).
  """,
  "Dalam 5 stages, apakah Abstraction?",
  kw=["focus|fokus|essential|penting|important|utama",
      "ignore|abaikan|rest|lain|buang|tidak perlu"],
  ans="Fokus pada maklumat penting dan abaikan yang lain.",
  hint="Penting vs yang lain.",
  fu=[F("""Abstraction ialah stage ke-4, selepas Modelling dan sebelum Evaluation.""",
        "Stage apakah yang datang SELEPAS Abstraction?",
        ans=["evaluation", "penilaian"],
        hint="Stage terakhir.")],
  mcq=M("Dalam versi 5 stages, Abstraction datang selepas…",
        "Modelling", "Evaluation", "Decomposition sahaja", "Tiada (ia yang pertama)"))

S("ct11", T, H + "5 stages · Evaluation",
  """
  **Stage 5 · Evaluation**: **uji** (test) → cari ralat (find errors) → **perbaiki** (refine) dan **ulang** (repeat).

  Contoh trafik: **test strategies and measure travel time and safety**.
  """,
  "Apakah Evaluation?",
  kw=["test|uji|ujian",
      "error|ralat|kesilapan|find|cari",
      "refine|perbaiki|baiki|improve|tambah baik",
      "repeat|ulang|ulangi"],
  ans="Uji → cari ralat → perbaiki dan ulang.",
  hint="Kitaran: test, find, refine, …",
  fu=[F("""Contoh trafik bagi Evaluation: uji strategi dan ukur **travel time** dan **safety**.""",
        "Dua perkara apakah yang diukur pada peringkat Evaluation dalam contoh trafik?",
        kw=["travel time|masa perjalanan|time|masa", "safety|keselamatan|selamat"],
        ans="Masa perjalanan (travel time) dan keselamatan (safety).",
        hint="Masa dan …")],
  mcq=M("'Test → find errors → refine and repeat' ialah…",
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
  "Dalam contoh sistem trafik, 'Only model main roads and busy intersections' ialah stage apa?",
  ans=["abstraction", "abstraksi"],
  hint="Hanya yang penting.",
  fu=[F("""Baris jadual: Pattern → Peak hours, accident hotspots, congestion areas.""",
        "'Peak hours, accident hotspots, congestion areas' ialah stage apa?",
        ans=["pattern", "pattern recognition", "corak", "generalisation & pattern recognition"],
        hint="Corak."),
      F("""Baris jadual: Evaluation → Test strategies and measure travel time and safety.""",
        "'Test strategies and measure travel time and safety' ialah stage apa?",
        ans=["evaluation", "penilaian"],
        hint="Uji."),
      F("""Baris jadual: Modelling → Simulate traffic flow and signal timing.""",
        "'Simulate traffic flow and signal timing' ialah stage apa?",
        ans=["modelling", "modeling", "pemodelan"],
        hint="Model.")],
  mcq=M("Dalam contoh trafik, 'Split into roads, vehicles, signals, pedestrian crossings' ialah…",
        "Decomposition", "Abstraction", "Modelling", "Evaluation"))

S("ct13", T, H + "Related ways of thinking · Logical thinking",
  """
  **Logical thinking**: berfikir dengan jelas supaya **kesimpulan mengikut fakta** (conclusions follow from facts).

  Langkah: **Identify → Analyse → Formulate solution → Evaluate**
  """,
  "Apakah logical thinking dan apakah langkah-langkahnya?",
  kw=["conclusion|kesimpulan|reason|alasan|jelas|clearly",
      "fact|fakta",
      "identify|kenal pasti|kenalpasti",
      "analyse|analyze|analisis",
      "formulate|rumus|solution|penyelesaian",
      "evaluate|nilai|penilaian"],
  ans="Berfikir jelas supaya kesimpulan mengikut fakta. Identify → Analyse → Formulate solution → Evaluate.",
  hint="4 langkah bermula dengan Identify.",
  fu=[F("""Logical thinking: Identify → Analyse → Formulate solution → Evaluate.""",
        "Apakah langkah KETIGA dalam logical thinking?",
        ans=["formulate solution", "formulate", "rumus penyelesaian"],
        hint="F…")],
  mcq=M("Turutan langkah logical thinking ialah…",
        "Identify → Analyse → Formulate solution → Evaluate",
        "Define → Identify steps → Sequence → Execute → Evaluate",
        "Input → Process → Output",
        "Decomposition → Pattern → Abstraction → Algorithm"))

S("ct14", T, H + "Related ways of thinking · Algorithmic thinking",
  """
  **Algorithmic thinking**: selesaikan masalah sebagai **senarai langkah yang tersusun** (an ordered list of steps).

  Langkah: **Define → Identify steps → Sequence → Execute → Evaluate**
  """,
  "Apakah algorithmic thinking dan apakah langkah-langkahnya?",
  kw=["ordered|tersusun|turutan|order|list|senarai",
      "step|langkah",
      "define|takrif|tentukan",
      "sequence|susun|urutan",
      "execute|laksana|jalankan|run",
      "evaluate|nilai"],
  ans="Selesaikan masalah sebagai senarai langkah tersusun. Define → Identify steps → Sequence → Execute → Evaluate.",
  hint="5 langkah bermula dengan Define.",
  fu=[F("""Algorithmic thinking ada 5 langkah: Define → Identify steps → Sequence → Execute → Evaluate. Logical thinking ada 4.""",
        "Apakah langkah SELEPAS Sequence dalam algorithmic thinking?",
        ans=["execute", "laksana", "jalankan"],
        hint="Jalankan.")],
  mcq=M("'Define → Identify steps → Sequence → Execute → Evaluate' ialah…",
        "Algorithmic thinking", "Logical thinking", "Program development", "5 stages CT"))

S("ct15", T, H + "Where it's used",
  """
  Computational thinking digunakan dalam:
  - **kehidupan harian** (everyday life): merancang perjalanan (trip planning), bajet (budgeting)
  - **software development**
  - **data analysis**
  - **research** (penyelidikan)
  """,
  "Senaraikan sekurang-kurangnya tiga bidang di mana computational thinking digunakan.",
  kw=["everyday|harian|daily|trip|budget|bajet|perjalanan",
      "software|perisian|development|pembangunan",
      "data|analysis|analisis",
      "research|penyelidikan|kajian"],
  ans="Kehidupan harian (trip planning, budgeting), software development, data analysis, research.",
  hint="Satu harian, satu perisian, satu data, satu kajian.",
  fu=[F("""Dua contoh kehidupan harian dalam nota: **trip planning** dan **budgeting**.""",
        "Berikan satu contoh penggunaan CT dalam kehidupan harian (ikut nota).",
        kw=["trip|perjalanan|percutian|travel|budget|bajet|belanjawan"],
        ans="Trip planning atau budgeting.",
        hint="Cuti atau wang.")],
  mcq=M("Yang manakah BUKAN contoh penggunaan CT dalam nota?",
        "Membaiki enjin kereta secara manual", "Trip planning", "Data analysis", "Research"))

# =================================================================== BAB 2
T = "alg"
H = "2 · "

S("al01", T, H + "The programming process",
  """
  **Programming is problem solving:**

  **Understand the requirements → Analyse → Design the algorithm → Code → Test**
  """,
  "Tulis proses pengaturcaraan mengikut turutan.",
  kw=["understand|faham|requirement|keperluan",
      "analyse|analyze|analisis",
      "design|reka|algorithm|algoritma",
      "code|kod|coding",
      "test|uji|testing"],
  ans="Understand the requirements → Analyse → Design the algorithm → Code → Test.",
  hint="5 langkah. Bermula dengan memahami, berakhir dengan menguji.",
  fu=[F("""Design the algorithm datang **sebelum** Code.""",
        "Apakah langkah tepat SEBELUM Code?",
        ans=["design the algorithm", "design", "design algorithm", "reka algoritma"],
        hint="Reka bentuk…")],
  mcq=M("Dalam proses pengaturcaraan, langkah terakhir ialah…",
        "Test", "Code", "Analyse", "Design the algorithm"))

S("al02", T, H + "IPO · Rectangle area",
  """
  **Input → Process → Output (IPO)**, contoh luas segi empat tepat:

  | | Rectangle area |
  |---|---|
  | Input | length, width |
  | Process | area = length × width |
  | Output | area |
  """,
  "Apakah Input, Process dan Output bagi masalah luas segi empat tepat?",
  kw=["length|panjang", "width|lebar", "area = length|area = length × width|length × width|length * width|panjang darab lebar|area=length"],
  ans="Input: length, width. Process: area = length × width. Output: area.",
  hint="Dua input, satu formula, satu output.",
  fu=[F("""length = 10, width = 15 → area = 10 × 15.""",
        "Berapakah area?",
        ans=["150", "area = 150", "area=150"],
        hint="10 × 15.")],
  mcq=M("Dalam IPO luas segi empat tepat, 'area' ialah…",
        "Output", "Input", "Process", "Constant"))

S("al03", T, H + "IPO · Income tax",
  """
  | | Income tax |
  |---|---|
  | Input | name, monthly income, number of kids |
  | Process | tax = 0.25 × (income × 11 − kids × 450) |
  | Output | name, tax |
  """,
  "Tulis formula process bagi income tax.",
  kw=["0.25", "11", "450", "income|pendapatan", "kids|anak"],
  ans="tax = 0.25 × (income × 11 − kids × 450)",
  hint="Kadar 0.25; income didarab 11; potongan 450 setiap anak.",
  fu=[F("""Income = 4000, kids = 2: 0.25 × (4000 × 11 − 2 × 450) = 0.25 × 43100.""",
        "Berapakah tax?",
        ans=["10775", "rm10775", "rm 10775", "10775.0"],
        hint="0.25 × 43100."),
      F("""Output income tax ialah **name** dan **tax**.""",
        "Apakah output bagi masalah income tax?",
        kw=["name|nama", "tax|cukai"],
        ans="name dan tax.",
        hint="Dua perkara dipaparkan.")],
  mcq=M("Dalam IPO income tax, 'number of kids' ialah…",
        "Input", "Process", "Output", "Formula"))

S("al04", T, H + "TIP: finding IPO in an exam question",
  """
  💡 **TIP**: dalam soalan peperiksaan,
  - **kata nama** (nouns) yang diberi biasanya **input**,
  - **formula** ialah **process**,
  - apa yang anda mesti **"display"** ialah **output**.
  """,
  "Bagaimana mengenal pasti input, process dan output dalam soalan peperiksaan?",
  kw=["noun|nouns|kata nama|nama|given|diberi",
      "formula|rumus",
      "display|papar|paparkan|tunjuk"],
  ans="Kata nama yang diberi = input, formula = process, apa yang mesti di-display = output.",
  hint="Kata nama, formula, display.",
  fu=[F("""Soalan: "Given the radius, calculate the area using area = 3.14 × r × r and display the area." """,
        "Apakah output soalan ini?",
        ans=["area", "luas", "the area"],
        hint="Apa yang di-display?")],
  mcq=M("Dalam soalan peperiksaan, formula biasanya ialah…",
        "Process", "Input", "Output", "Sentinel"))

S("al05", T, H + "Procedural vs Object-Oriented",
  """
  - **Procedural (structured)**: dibina di sekitar **functions/procedures**. Contoh: **C**.
  - **Object-oriented (OOP)**: dibina di sekitar **objects** (data + procedures). Contoh: **C++**.
  """,
  "Apakah beza procedural dan object-oriented programming?",
  kw=["procedural|structured|berstruktur",
      "function|procedure|fungsi|prosedur",
      "object|objek|oop",
      "data"],
  ans="Procedural dibina sekitar functions/procedures (contoh C); OOP dibina sekitar objects yang menggabungkan data dan procedures (contoh C++).",
  hint="Satu sekitar fungsi, satu sekitar objek.",
  fu=[F("""Nota: C = procedural, C++ = object-oriented.""",
        "Bahasa apakah contoh procedural dalam nota?",
        ans=["c", "bahasa c", "c language"],
        hint="Satu huruf.")],
  mcq=M("Object dalam OOP terdiri daripada…",
        "Data + procedures", "Hanya functions", "Hanya variables global", "Flowchart"))

S("al06", T, H + "Algorithm · definition",
  """
  **Algorithm**: satu **turutan langkah yang terhingga** (finite sequence of steps) dalam **susunan logik** (logical order) yang menyelesaikan masalah.
  """,
  "Takrifkan algorithm.",
  kw=["finite|terhingga|terhad",
      "sequence|turutan|steps|langkah",
      "logical|logik|order|susunan",
      "solve|selesai|menyelesaikan|problem|masalah"],
  ans="Turutan langkah terhingga dalam susunan logik yang menyelesaikan masalah.",
  hint="Finite… sequence… logical order…",
  fu=[F("""Kata kunci definisi: **finite**, **sequence of steps**, **logical order**.""",
        "Algorithm mesti ada bilangan langkah yang terhingga. Apakah istilah English untuk 'terhingga'?",
        ans=["finite"],
        hint="F…")],
  mcq=M("Algorithm ialah…",
        "Turutan langkah terhingga dalam susunan logik yang menyelesaikan masalah",
        "Bahasa pengaturcaraan",
        "Rajah dengan simbol oval",
        "Program yang telah di-compile"))

S("al07", T, H + "Algorithm · requirements",
  """
  Keperluan (requirements) algorithm yang baik:

  **has input** · **produces output** · **unambiguous** · **general** · **correct** · **finite** · **efficient**
  """,
  "Senaraikan keperluan sesuatu algorithm (sekurang-kurangnya lima).",
  kw=["input", "output",
      "unambiguous|jelas|tidak samar|tak samar",
      "general|umum",
      "correct|betul",
      "finite|terhingga|terhad",
      "efficient|cekap"],
  ans="Has input, produces output, unambiguous, general, correct, finite, efficient.",
  hint="Ada 7: input, output, dan lima kata sifat.",
  fu=[F("""'Unambiguous' = setiap langkah hanya ada **satu maksud**.""",
        "Langkah 'tambah sedikit garam' melanggar keperluan apa?",
        ans=["unambiguous", "unambiguity", "jelas"],
        hint="Berapa banyak 'sedikit'?"),
      F("""'General' = algorithm berfungsi untuk **semua input yang sah**, bukan hanya satu kes.""",
        "Algorithm yang hanya berfungsi untuk length = 10 melanggar keperluan apa?",
        ans=["general", "umum"],
        hint="Bukan spesifik.")],
  mcq=M("Yang manakah BUKAN keperluan algorithm dalam nota?",
        "Colourful", "Finite", "Efficient", "Unambiguous"))

S("al08", T, H + "Algorithm · three ways to design",
  """
  Tiga cara mereka bentuk algorithm:
  1. **Pseudocode**
  2. **Flowchart**
  3. **Top-down design (structure chart)**
  """,
  "Apakah tiga cara mereka bentuk algorithm?",
  kw=["pseudocode|pseudokod", "flowchart|carta alir",
      "top-down|top down|structure chart|carta struktur"],
  ans="Pseudocode, flowchart dan top-down design (structure chart).",
  hint="Dua yang biasa, satu lagi 'atas ke bawah'.",
  fu=[F("""Top-down design juga dikenali sebagai **structure chart**.""",
        "Top-down design dilukis sebagai apa?",
        ans=["structure chart", "carta struktur"],
        hint="S… chart.")],
  mcq=M("Top-down design juga dikenali sebagai…",
        "Structure chart", "Trace table", "Pseudocode", "Truth table"))

S("al09", T, H + "Pseudocode",
  """
  **Pseudocode**: langkah seperti bahasa Inggeris **tanpa sintaks pengaturcaraan** (no programming syntax), supaya logik mudah dibaca.

  ```
  1. Start
  2. Get name, monthly_income, num_kids
  3. tax = 0.25 * (monthly_income * 11 - num_kids * 450)
  4. Display name and tax
  5. End
  ```
  """,
  "Apakah pseudocode?",
  kw=["english|inggeris|bahasa",
      "no syntax|tiada sintaks|tanpa sintaks|no programming syntax|bukan kod|syntax|sintaks",
      "logic|logik|easy|mudah|read|baca|steps|langkah"],
  ans="Langkah seperti bahasa Inggeris tanpa sintaks pengaturcaraan supaya logik mudah dibaca.",
  hint="Seperti bahasa apa, dan tanpa apa?",
  fu=[F("""Dalam contoh pseudocode cukai, input dibaca dengan kata kerja **Get** dan output dengan **Display**.""",
        "Kata kerja apakah yang digunakan untuk membaca input dalam contoh pseudocode?",
        ans=["get"],
        hint="Langkah 2."),
      F("""Pseudocode cukai ada 5 langkah: Start, Get, tax = …, Display, End.""",
        "Apakah langkah TERAKHIR?",
        ans=["end", "5. end"],
        hint="Lawan Start.")],
  mcq=M("Pseudocode ditulis…",
        "Seperti bahasa Inggeris, tanpa sintaks pengaturcaraan",
        "Dalam sintaks C++ penuh",
        "Dalam binary",
        "Menggunakan simbol oval dan diamond"))

S("al10", T, H + "Flowchart symbols · Terminal",
  """
  **Terminal** (bentuk **oval**): **Start / End**.

  Flowchart sebuah **function** berakhir dengan **Return** (bukan End).
  """,
  "Apakah simbol Terminal dan bagaimana flowchart function berakhir?",
  kw=["oval|bujur|kapsul|rounded",
      "start|end|mula|tamat",
      "return"],
  ans="Terminal ialah oval untuk Start/End; flowchart function berakhir dengan Return.",
  hint="Bentuk kapsul; function tamat dengan perkataan R…",
  fu=[F("""Function chart: bermula dengan nama function dan berakhir dengan **Return**.""",
        "Flowchart sebuah function berakhir dengan perkataan apa?",
        ans=["return"],
        hint="R…")],
  mcq=M("Simbol oval dalam flowchart ialah…",
        "Terminal (Start/End)", "Process", "Decision", "Input/Output"))

S("al11", T, H + "Flowchart symbols · Process",
  """
  **Process** (bentuk **rectangle / segi empat tepat**): pengiraan dan assignment (calculations and assignments).
  """,
  "Simbol apakah untuk Process dan apakah gunanya?",
  kw=["rectangle|segi empat tepat|segiempat tepat|kotak|box",
      "calculation|kira|pengiraan|assignment|umpukan|calculations"],
  ans="Rectangle; untuk pengiraan dan assignment.",
  hint="Kotak biasa.",
  fu=[F("""`area = length * width` ialah pengiraan → Process.""",
        "`sum = sum + counter` dilukis dalam simbol apa?",
        ans=["rectangle", "process", "segi empat tepat", "kotak"],
        hint="Assignment.")],
  mcq=M("'tax = 0.25 * income' dilukis dalam…",
        "Rectangle (Process)", "Parallelogram", "Diamond", "Oval"))

S("al12", T, H + "Flowchart symbols · Input/Output",
  """
  **Input/Output** (bentuk **parallelogram**): **Read / Display**.
  """,
  "Simbol apakah untuk Input/Output?",
  kw=["parallelogram|segi empat selari|selari|jajaran genjang"],
  ans="Parallelogram (Read / Display).",
  hint="Kotak yang senget.",
  fu=[F("""Read dan Display kedua-duanya menggunakan parallelogram.""",
        "'Display sum' dilukis dalam simbol apa?",
        ans=["parallelogram", "segi empat selari", "input/output"],
        hint="Sama seperti Read.")],
  mcq=M("'Read length, width' dilukis dalam…",
        "Parallelogram", "Rectangle", "Diamond", "Circle"))

S("al13", T, H + "Flowchart symbols · Decision",
  """
  **Decision** (bentuk **diamond**): **satu garis masuk, dua keluar** (one line in, two out), iaitu **Yes/No**.
  """,
  "Terangkan simbol Decision.",
  kw=["diamond|berlian|wajik|rhombus",
      "one in|satu masuk|1 masuk|one line in|satu garis",
      "two out|dua keluar|2 keluar|yes|no|ya|tidak"],
  ans="Diamond; satu garis masuk, dua keluar (Yes/No).",
  hint="Bentuk, berapa masuk, berapa keluar.",
  fu=[F("""Decision: 1 masuk, 2 keluar.""",
        "Berapakah garis yang KELUAR dari Decision?",
        ans=["2", "dua", "two"],
        hint="Yes dan No.")],
  mcq=M("Simbol Decision mempunyai…",
        "Satu garis masuk, dua keluar (Yes/No)", "Dua masuk, satu keluar", "Satu masuk, satu keluar", "Tiada garis keluar"))

S("al14", T, H + "Flowchart symbols · Function/Subroutine",
  """
  **Function/Subroutine** (rectangle dengan **garis menegak di kedua-dua tepi**): **memanggil flowchart lain** (calls another flowchart).
  """,
  "Apakah fungsi simbol Function/Subroutine?",
  kw=["call|panggil|memanggil", "another|lain|separate|berasingan|flowchart|carta"],
  ans="Memanggil flowchart lain (function).",
  hint="Ia tidak buat kerja sendiri, ia…",
  fu=[F("""Bentuknya: rectangle dengan garis tambahan di tepi kiri dan kanan.""",
        "Bagaimanakah bentuk simbol Function/Subroutine?",
        kw=["rectangle|segi empat|kotak", "line|garis|side|tepi|double|berganda|bar"],
        ans="Rectangle dengan garis menegak di kedua-dua tepi.",
        hint="Seperti Process, tambah sesuatu di tepi.")],
  mcq=M("Simbol rectangle dengan garis menegak di kedua-dua tepi bermaksud…",
        "Panggil function/subroutine (flowchart lain)", "Input", "Decision", "Komen"))

S("al15", T, H + "Flowchart symbols · Connectors, flowline, comment",
  """
  - **Connectors**: **circle** = halaman yang **sama** (same page), **pentagon** = halaman **lain** (another page).
  - **Flowline** (anak panah): tunjuk **arah aliran**.
  - **Comment symbol**: tambah nota/catatan.
  """,
  "Apakah beza connector circle dan pentagon?",
  kw=["circle|bulatan|bulat", "same|sama", "pentagon", "another|lain|other|different|berbeza"],
  ans="Circle untuk sambungan pada halaman yang sama; pentagon untuk sambungan ke halaman lain.",
  hint="Satu bulat, satu bersegi lima.",
  fu=[F("""Flowline arrow menunjukkan arah aliran (direction of flow).""",
        "Apakah fungsi flowline?",
        kw=["direction|arah", "flow|aliran"],
        ans="Menunjukkan arah aliran.",
        hint="Anak panah."),
      F("""Simbol komen digunakan untuk menambah nota.""",
        "Simbol apakah digunakan untuk menambah nota pada flowchart?",
        ans=["comment", "comment symbol", "komen", "simbol komen"],
        hint="C…")],
  mcq=M("Pentagon connector bermaksud sambungan ke…",
        "Halaman lain", "Halaman yang sama", "Function", "Decision"))

S("al16", T, H + "3 control structures",
  """
  **3 control structures (the foundation of everything):**

  - **Sequence**: langkah dilaksanakan mengikut turutan, atas ke bawah.
  - **Selection**: pilih laluan: `if`, `if-else`, nested if.
  - **Repetition**: ulang selagi syarat benar: **pre-test** atau **post-test** loop.
  """,
  "Namakan dan terangkan tiga control structures.",
  kw=["sequence|jujukan|turutan",
      "selection|pilihan|pemilihan|if",
      "repetition|ulangan|loop|pengulangan|gelung"],
  ans="Sequence (ikut turutan atas ke bawah), Selection (pilih laluan: if, if-else, nested if), Repetition (ulang selagi syarat benar: pre-test/post-test).",
  hint="S, S, R.",
  fu=[F("""Repetition: ulang **selagi syarat benar** (while a condition is true), sama ada pre-test atau post-test.""",
        "Dua jenis loop dalam repetition ialah pre-test dan …?",
        ans=["post-test", "post test", "posttest"],
        hint="Lawan 'pre'.")],
  mcq=M("'Steps run in order, top to bottom' ialah…",
        "Sequence", "Selection", "Repetition", "Decomposition"))

S("al17", T, H + "Selection forms",
  """
  | Form | Idea | Pseudocode |
  |---|---|---|
  | One choice (if) | "do or don't" | `if cond … end_if` |
  | Two choices (if-else) | "do this or that" | `if cond … else … end_if` |
  | Multi (if-else if-else) | several ranges | `if … else if … else if … else … end_if` |
  """,
  "Apakah idea bagi selection 'one choice (if)'?",
  ans=["do or don't", "do or dont", "buat atau tidak"],
  hint="\"do or …\"",
  fu=[F("""Two choices (if-else) = "do this or that".""",
        "Apakah idea bagi if-else?",
        ans=["do this or that", "buat ini atau itu"],
        hint="\"do this or …\""),
      F("""Multi (if-else if-else) digunakan untuk **several ranges** (beberapa julat).""",
        "Bentuk selection manakah sesuai untuk beberapa julat (contoh gred A–F)?",
        ans=["multi", "if-else if-else", "if else if else", "else if", "multi (if-else if-else)"],
        hint="Several ranges.")],
  mcq=M("Pseudocode `if cond … else … end_if` ialah bentuk…",
        "Two choices (if-else)", "One choice (if)", "Multi (if-else if-else)", "Repetition"))

S("al18", T, H + "Operators · Relational",
  """
  | Relational | Meaning |
  |---|---|
  | `>  <  >=  <=` | compare size |
  | `==` | equal to |
  | `!=` | not equal to |
  """,
  "Apakah maksud operator `!=`?",
  ans=["not equal to", "tidak sama dengan", "not equal", "tidak sama"],
  hint="! = tidak.",
  fu=[F("""`==` bermaksud **equal to** (perbandingan). Ia berbeza dengan `=` (assignment).""",
        "Operator relational apakah bermaksud 'equal to'?",
        ans=["=="],
        hint="Dua simbol sama.")],
  mcq=M("Operator manakah membandingkan saiz (compare size)?",
        ">=", "==", "&&", "!"))

S("al19", T, H + "Operators · Logical",
  """
  | Logical | True when… |
  |---|---|
  | `&&` AND | **both** are true |
  | `||` OR | **at least one** is true |
  | `!` NOT | flips true ↔ false |
  """,
  "Bilakah && (AND) dan || (OR) bernilai true?",
  kw=["&&|and", "both|kedua-dua|keduanya|semua|all",
      "\\|\\||or", "at least one|sekurang-kurangnya satu|salah satu|one|satu"],
  ans="&& true apabila kedua-dua true; || true apabila sekurang-kurangnya satu true.",
  hint="AND = kedua-dua; OR = …",
  fu=[F("""`!` NOT menyongsangkan nilai: true ↔ false.""",
        "Apakah nilai `!true`?",
        ans=["false", "0", "palsu"],
        hint="Flip.")],
  mcq=M("`||` bernilai true apabila…",
        "Sekurang-kurangnya satu operand true", "Kedua-dua operand true", "Kedua-dua operand false", "Tidak pernah"))

S("al20", T, H + "Memory trick: AND is strict, OR is generous",
  """
  💡 **MEMORY TRICK**: **AND is strict** (any F gives F). **OR is generous** (any T gives T).

  Contoh: x = 12, y = 5, z = −4:
  - `(x>y)&&(y>z)` = **true**
  - `(x<=z)||(y==z)` = **false**
  - `!(x>=z)` = **false**
  """,
  "Terangkan memory trick 'AND is strict, OR is generous'.",
  kw=["and|&&", "strict|ketat", "any f|mana-mana f|f memberi f|mana-mana false|satu false|any false|f gives f|false",
      "or|\\|\\|", "generous|murah hati|pemurah", "any t|mana-mana t|t memberi t|mana-mana true|satu true|any true|t gives t|true"],
  ans="AND ketat: mana-mana F memberi F. OR pemurah: mana-mana T memberi T.",
  hint="Strict / generous… F gives F, T gives T.",
  fu=[F("""x = 12, y = 5, z = −4. Nilai `(x>y)`: 12 > 5 = T; `(y>z)`: 5 > −4 = T.""",
        "Apakah nilai `(x>y)&&(y>z)`? (true / false)",
        ans=["true", "1", "benar"],
        hint="T && T."),
      F("""`(x<=z)`: 12 <= −4 = F; `(y==z)`: 5 == −4 = F.""",
        "Apakah nilai `(x<=z)||(y==z)`? (true / false)",
        ans=["false", "0", "palsu"],
        hint="F || F."),
      F("""`(x>=z)`: 12 >= −4 = T.""",
        "Apakah nilai `!(x>=z)`? (true / false)",
        ans=["false", "0", "palsu"],
        hint="!T.")],
  mcq=M("Dengan x=12, y=5, z=−4, `(x<=z)||(y==z)` bernilai…",
        "false", "true", "−4", "ralat"))

S("al21", T, H + "Repetition · Pre-test vs post-test",
  """
  - **Pre-test (while)**: semak syarat **dahulu**, jadi badan mungkin berjalan **0 kali**.
  - **Post-test (do-while)**: jalankan badan **dahulu**, semak kemudian, jadi ia berjalan **sekurang-kurangnya sekali**.
  """,
  "Apakah beza pre-test loop dan post-test loop?",
  kw=["pre-test|pre test|while",
      "first|dahulu|dulu|0 times|0 kali|sifar|zero|mungkin tidak",
      "post-test|post test|do-while|do while",
      "at least once|sekurang-kurangnya sekali|sekali|once"],
  ans="Pre-test (while) semak syarat dahulu, jadi mungkin 0 kali. Post-test (do-while) jalankan badan dahulu, jadi sekurang-kurangnya sekali.",
  hint="Bila syarat disemak?",
  fu=[F("""do-while ialah post-test loop.""",
        "Berapa kali MINIMUM badan do-while dijalankan?",
        ans=["1", "sekali", "once", "satu", "1 kali"],
        hint="At least…"),
      F("""while ialah pre-test loop.""",
        "Berapa kali MINIMUM badan while dijalankan?",
        ans=["0", "sifar", "zero", "0 kali"],
        hint="Syarat mungkin false dari awal.")],
  mcq=M("Loop yang pasti berjalan sekurang-kurangnya sekali ialah…",
        "Post-test (do-while)", "Pre-test (while)", "for", "Tiada"))

S("al22", T, H + "Counter-controlled loop · 3 parts",
  """
  **Counter-controlled loop** ada 3 bahagian:

  1. **initialise**: `cnt = 0`
  2. **test**: `cnt < n`
  3. **update**: `cnt = cnt + 1`
  """,
  "Apakah tiga bahagian counter-controlled loop?",
  kw=["initialise|initialize|initialization|inisialisasi|nilai awal|cnt = 0",
      "test|condition|syarat|uji|cnt < n",
      "update|kemas kini|cnt = cnt + 1|tambah"],
  ans="Initialise (cnt = 0), test (cnt < n), update (cnt = cnt + 1).",
  hint="Mula, uji, ubah.",
  fu=[F("""Contoh nota: ① `cnt = 0` ② `cnt < n` ③ `cnt = cnt + 1`.""",
        "Tulis bahagian update dalam contoh nota.",
        ans=["cnt = cnt + 1", "cnt=cnt+1", "cnt++", "cnt += 1"],
        hint="cnt tambah satu.")],
  mcq=M("Dalam counter-controlled loop, `cnt < n` ialah bahagian…",
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
  "Apakah nilai sum yang dipaparkan oleh pseudocode di atas?",
  ans=["55"],
  hint="1 + 2 + … + 10.",
  fu=[F("""Jika syarat ditukar kepada `While counter <= 5`.""",
        "Apakah nilai sum sekarang?",
        ans=["15"],
        hint="1 + 2 + 3 + 4 + 5."),
      F("""Blok While ditutup dengan `End_While`.""",
        "Kata kunci apakah menutup loop While dalam pseudocode nota?",
        ans=["end_while", "endwhile", "end while"],
        hint="End_…")],
  mcq=M("Dalam pseudocode sum 1–10, nilai counter selepas loop tamat ialah…",
        "11", "10", "55", "0"))

S("al24", T, H + "User-controlled loop and sentinel",
  """
  - **User-controlled loop**: pengguna memasukkan **berapa kali** untuk diulang (`limit`).
  - **Sentinel**: nilai khas yang **menamatkan input**, contoh **`-999`** atau nama **`"OK"`**. Gunakan apabila anda **tidak tahu berapa banyak item**.
  """,
  "Apakah sentinel dan bilakah ia digunakan?",
  kw=["special|khas|nilai khas",
      "end|tamat|stop|berhenti|hentikan|menamatkan",
      "don't know|tidak tahu|tak tahu|unknown|tidak diketahui|berapa banyak|how many"],
  ans="Nilai khas (contoh -999 atau \"OK\") yang menamatkan input; digunakan apabila tidak tahu berapa banyak item.",
  hint="Contoh -999.",
  fu=[F("""Contoh sentinel dalam nota: `-999` dan nama `"OK"`.""",
        "Berikan contoh nilai sentinel nombor dalam nota.",
        ans=["-999"],
        hint="Negatif, tiga digit sama."),
      F("""User-controlled loop: pengguna masukkan `limit`.""",
        "Dalam user-controlled loop, siapa yang menentukan bilangan ulangan?",
        ans=["user", "pengguna", "the user"],
        hint="Namanya sendiri.")],
  mcq=M("Loop yang membaca markah sehingga pengguna menaip -999 ialah…",
        "Sentinel-controlled loop", "Counter-controlled loop", "Nested loop", "Infinite loop"))

S("al25", T, H + "Trace table",
  """
  **Trace table**: tulis setiap pemboleh ubah sebagai **lajur** (column) dan isi **satu baris bagi setiap langkah atau input**. Ia membantu mencari **logic errors**.

  | Length | Width | Area | Perimeter | Output |
  |---|---|---|---|---|
  | 10 | 15 | 150 | 50 | Area=150, Perimeter=50 |
  | 20 | 20 | 400 | 80 | Area=400, Perimeter=80 |
  """,
  "Apakah trace table dan apakah fungsinya?",
  kw=["column|lajur|variable|pemboleh ubah",
      "row|baris|step|langkah|input",
      "logic error|ralat logik|error|ralat|kesilapan"],
  ans="Jadual dengan setiap pemboleh ubah sebagai lajur dan satu baris bagi setiap langkah/input; membantu mencari logic errors.",
  hint="Lajur = ?, baris = ?, tujuan = ?",
  fu=[F("""Perimeter = 2 × (length + width). Baris kedua: length 20, width 20.""",
        "Berapakah Perimeter baris kedua?",
        ans=["80"],
        hint="2 × 40."),
      F("""Length = 10, width = 15.""",
        "Berapakah Perimeter baris pertama?",
        ans=["50"],
        hint="2 × 25.")],
  mcq=M("Trace table terutamanya membantu mencari…",
        "Logic errors", "Syntax errors sahaja", "Virus", "Header yang hilang"))

S("al26", T, H + "Modular flowcharts · call vs definition",
  """
  **Modular flowcharts (functions):**
  - **Function call** (dalam carta utama) menyatakan **apa** (what) yang perlu dibuat.
  - **Function definition** (carta berasingan) menyatakan **bagaimana** (how) melakukannya.
  """,
  "Apakah beza function call dan function definition dalam modular flowchart?",
  kw=["call|panggilan|panggil", "what|apa",
      "definition|definisi|takrif", "how|bagaimana|cara"],
  ans="Function call (carta utama) menyatakan apa yang dibuat; function definition (carta berasingan) menyatakan bagaimana.",
  hint="What vs how.",
  fu=[F("""Function definition dilukis dalam **carta berasingan** (a separate chart).""",
        "Di manakah function definition dilukis?",
        kw=["separate|berasingan|lain|another|sendiri|asing"],
        ans="Dalam carta (flowchart) berasingan.",
        hint="Bukan dalam carta utama.")],
  mcq=M("Dalam modular flowchart, carta yang menyatakan BAGAIMANA tugas dibuat ialah…",
        "Function definition", "Function call", "Main chart", "Connector"))

S("al27", T, H + "Modular flowcharts · function chart start and end",
  """
  **Function chart**: bermula dengan **nama function**, contoh `AVRG(R, a, b, c)`, dan berakhir dengan **Return**.
  """,
  "Bagaimanakah function chart bermula dan berakhir?",
  kw=["name|nama|avrg", "return"],
  ans="Bermula dengan nama function (contoh AVRG(R, a, b, c)) dan berakhir dengan Return.",
  hint="Bermula dengan N…, berakhir dengan R…",
  fu=[F("""Contoh nama function chart: `AVRG(R, a, b, c)`.""",
        "Dalam `AVRG(R, a, b, c)`, apakah nama function?",
        ans=["avrg"],
        hint="Sebelum kurungan.")],
  mcq=M("Function chart berakhir dengan…",
        "Return", "End", "Stop", "Exit"))

S("al28", T, H + "Modular flowcharts · actual vs formal parameters",
  """
  - **Actual parameters** berada dalam **call**: `(n1, n2, n3)`.
  - **Formal parameters** berada dalam **definition**: `(a, b, c)`.
  - Dipadankan **mengikut turutan, bukan nama** (matched by order, not by name).
  """,
  "Apakah beza actual parameters dan formal parameters, dan bagaimana ia dipadankan?",
  kw=["actual|sebenar", "call|panggilan|panggil",
      "formal", "definition|definisi|takrif",
      "order|turutan|kedudukan|susunan"],
  ans="Actual parameters dalam call (n1, n2, n3); formal parameters dalam definition (a, b, c); dipadankan mengikut turutan, bukan nama.",
  hint="Satu dalam call, satu dalam definition; padan ikut apa?",
  fu=[F("""Call `AVRG(R, n1, n2, n3)` dan definition `AVRG(R, a, b, c)`. Dipadankan ikut turutan.""",
        "Parameter formal manakah menerima nilai n2?",
        ans=["b"],
        hint="Kedudukan kedua."),
      F("""Nama tidak perlu sama; hanya **turutan** penting.""",
        "Adakah nama actual dan formal parameter mesti sama? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="By order, not by name.")],
  mcq=M("Actual dan formal parameters dipadankan mengikut…",
        "Turutan", "Nama", "Jenis data sahaja", "Abjad"))

S("al29", T, H + "Modular flowcharts · variables in the current chart",
  """
  Dalam modular flowchart, **hanya gunakan pemboleh ubah yang wujud dalam carta semasa** (only use variables that exist in the current chart).

  Contoh: dalam carta `AVRG(R, a, b, c)`, gunakan a, b, c, bukan n1, n2, n3.
  """,
  "Pemboleh ubah apakah boleh digunakan dalam sebuah function chart?",
  kw=["exist|wujud|ada", "current|semasa|this|ini|same|sama|chart|carta"],
  ans="Hanya pemboleh ubah yang wujud dalam carta semasa.",
  hint="Bukan pemboleh ubah carta utama.",
  fu=[F("""Dalam definition `AVRG(R, a, b, c)`, n1 milik carta utama.""",
        "Bolehkah carta AVRG menggunakan n1 secara terus? (ya / tidak)",
        ans=["tidak", "no", "tak"],
        hint="Ia tidak wujud dalam carta AVRG.")],
  mcq=M("Dalam function chart AVRG(R, a, b, c), pemboleh ubah yang sah digunakan ialah…",
        "a, b, c dan R", "n1, n2, n3", "Semua pemboleh ubah carta utama", "Tiada"))

S("al30", T, H + "From flowchart to code",
  """
  **From flowchart to code:**

  Problem → Flowchart → rough **"intermediate" code** → **complete code** (tambah `#include`, pengisytiharan pemboleh ubah (variable declarations) dan **prompts**).
  """,
  "Apakah turutan daripada masalah kepada kod lengkap?",
  kw=["problem|masalah", "flowchart|carta alir",
      "intermediate|rough|kasar|pertengahan",
      "complete|lengkap|full|penuh"],
  ans="Problem → Flowchart → rough intermediate code → complete code.",
  hint="4 peringkat; ada satu kod 'kasar'.",
  fu=[F("""Kod lengkap menambah tiga perkara kepada intermediate code: `#include`, variable declarations, prompts.""",
        "Namakan dua perkara yang ditambah untuk menjadikan kod lengkap.",
        kw=["#include|include|header", "declaration|pengisytiharan|isytihar|declare|variable", "prompt|prompts|gesaan"],
        ans="#include, variable declarations dan prompts.",
        hint="Header, pemboleh ubah, mesej kepada pengguna.")],
  mcq=M("Apakah yang BUKAN ditambah semasa menukar intermediate code kepada kod lengkap?",
        "Simbol diamond", "#include", "Variable declarations", "Prompts"))
