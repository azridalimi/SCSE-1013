from helpers import S, F, M

# ---------------------------------------------------------------- BAB 1
T = "ct"

S("ct01", T, "1.1 What is Computational Thinking",
  """
  **Computational Thinking (CT)** ialah proses penyelesaian masalah (problem-solving process) untuk merumus masalah dan menyatakan penyelesaiannya supaya ia boleh dilaksanakan oleh komputer atau manusia.

  CT bukan "berfikir seperti komputer". Ia cara berfikir yang boleh dipakai di luar pengaturcaraan juga (contoh: merancang percutian, memasak).
  """,
  "Apakah maksud Computational Thinking?",
  kw=["problem solving|problem-solving|selesai masalah|penyelesaian masalah|menyelesaikan masalah",
      "formulate|rumus|merumus|nyatakan|express|define",
      "solution|penyelesaian|jalan penyelesaian",
      "computer|komputer|human|manusia|carried out|dilaksanakan"],
  ans="Proses penyelesaian masalah untuk merumus masalah dan menyatakan penyelesaiannya supaya boleh dilaksanakan oleh komputer atau manusia.",
  hint="Ia satu PROSES. Apa yang dirumus, dan siapa yang akan melaksanakan penyelesaiannya?",
  fu=[F("""CT boleh diguna di luar pengaturcaraan. Ia bukan bermaksud "berfikir seperti komputer".""",
        "Betul atau salah: Computational Thinking bermaksud berfikir seperti komputer. (jawab: betul / salah)",
        ans=["salah", "false", "tidak", "tak betul"],
        hint="Ingat: CT ialah cara MANUSIA berfikir untuk menyelesaikan masalah.")],
  mcq=M("Computational Thinking paling tepat ditakrifkan sebagai…",
        "Proses merumus masalah dan penyelesaiannya supaya boleh dilaksanakan oleh komputer atau manusia",
        "Kemahiran menaip kod C++ dengan cepat",
        "Berfikir seperti komputer menggunakan nombor binari",
        "Proses membaiki hardware komputer"))

S("ct02", T, "1.2 Four cornerstones of CT",
  """
  Empat tunjang (four cornerstones) Computational Thinking:

  1. **Decomposition**
  2. **Pattern recognition**
  3. **Abstraction**
  4. **Algorithm design**

  Memory trick: **D-P-A-A** → "**D**ah **P**ecah, **A**mbil yang penting, **A**tur langkah".
  """,
  "Senaraikan empat tunjang (cornerstones) Computational Thinking.",
  kw=["decomposition|pecahkan|penguraian|dekomposisi",
      "pattern recognition|pattern|corak|pengecaman corak",
      "abstraction|abstraksi|abstrak",
      "algorithm|algoritma|algorithm design"],
  ans="Decomposition, Pattern recognition, Abstraction, Algorithm design.",
  hint="Guna memory trick D-P-A-A.",
  fu=[F("""Susunan D-P-A-A: Decomposition → Pattern recognition → Abstraction → Algorithm design.""",
        "Apakah tunjang KETIGA dalam susunan D-P-A-A?",
        ans=["abstraction", "abstraksi"],
        hint="\"Ambil yang penting\"…")],
  mcq=M("Yang manakah BUKAN tunjang Computational Thinking?",
        "Compilation", "Decomposition", "Abstraction", "Pattern recognition"))

S("ct03", T, "1.2 Decomposition",
  """
  **Decomposition**: memecahkan masalah yang besar dan kompleks kepada bahagian-bahagian kecil yang lebih mudah diurus dan diselesaikan.

  Contoh: membuat sistem kedai cetak → (1) terima pesanan, (2) kira harga, (3) cetak resit. Setiap bahagian diselesaikan berasingan.
  """,
  "Terangkan maksud decomposition.",
  kw=["break|pecah|pecahkan|bahagi|divide|memecahkan",
      "complex|besar|kompleks|large|big",
      "smaller|kecil|bahagian kecil|sub-problem|subproblem|parts|manageable|mudah diurus"],
  ans="Memecahkan masalah besar/kompleks kepada bahagian kecil yang lebih mudah diurus.",
  hint="Fikir: apa yang berlaku pada masalah BESAR?",
  fu=[F("""Dalam C++, decomposition dilaksanakan dengan memecahkan program kepada **functions** (Bab 5): setiap function buat satu tugas.""",
        "Dalam C++, binaan apakah yang digunakan untuk melaksanakan decomposition?",
        ans=["function", "functions", "fungsi"],
        hint="Bab 5.")],
  mcq=M("Memecahkan sistem pendaftaran pelajar kepada modul 'daftar', 'cari' dan 'padam' ialah contoh…",
        "Decomposition", "Abstraction", "Pattern recognition", "Debugging"))

S("ct04", T, "1.2 Pattern recognition",
  """
  **Pattern recognition**: mencari persamaan atau corak (similarities/patterns) di antara masalah-masalah kecil, supaya penyelesaian yang sama boleh **diguna semula** (reuse).

  Contoh: mengira harga untuk kertas A4, A3 dan poster: semuanya ikut corak `harga = kuantiti × harga seunit`.
  """,
  "Apakah pattern recognition dan apakah faedahnya?",
  kw=["similar|similarities|persamaan|sama|corak|pattern",
      "reuse|guna semula|diguna semula|re-use|ulang guna"],
  ans="Mencari persamaan/corak antara masalah supaya penyelesaian boleh diguna semula.",
  hint="Ada dua bahagian: apa yang dicari, dan apa faedahnya.",
  fu=[F("""Corak berulang dalam kod biasanya ditukar menjadi **loop** atau **function** supaya tidak perlu tulis kod yang sama berkali-kali.""",
        "Jika anda nampak corak langkah yang berulang 10 kali, struktur kawalan apakah yang sesuai dalam C++?",
        ans=["loop", "loops", "gelung", "for loop", "for", "while", "repetition"],
        hint="Repetition…")],
  mcq=M("Menyedari bahawa kira luas segi empat, segi tiga dan bulatan semuanya ikut corak 'baca input → kira → papar' ialah…",
        "Pattern recognition", "Decomposition", "Abstraction", "Compilation"))

S("ct05", T, "1.2 Abstraction",
  """
  **Abstraction**: fokus kepada maklumat yang **penting/relevan** sahaja dan **abaikan butiran yang tidak perlu** (irrelevant details).

  Contoh: peta LRT hanya tunjuk stesen dan laluan, bukan bangunan atau pokok. Untuk kira harga cetakan, warna baju pelanggan tidak penting.
  """,
  "Terangkan abstraction dengan ayat sendiri.",
  kw=["important|penting|relevant|relevan|essential|utama|fokus|focus",
      "ignore|abaikan|buang|remove|hide|sembunyi|tidak perlu|irrelevant|unnecessary|tidak penting"],
  ans="Fokus pada maklumat penting dan abaikan butiran yang tidak perlu.",
  hint="Ada dua tindakan: SIMPAN apa, BUANG apa?",
  fu=[F("""Contoh klasik: peta LRT ialah abstraction kerana hanya stesen dan laluan dipaparkan.""",
        "Mengapa peta LRT dikatakan contoh abstraction?",
        kw=["station|stesen|laluan|route|line",
            "ignore|abaikan|tiada|tidak tunjuk|tak tunjuk|buang|tidak perlu|irrelevant|butiran"],
        ans="Ia hanya tunjuk stesen dan laluan, butiran lain (bangunan, pokok) diabaikan.",
        hint="Apa yang ADA dan apa yang TIADA pada peta itu?")],
  mcq=M("Ketika menulis program kira tambang bas, anda abaikan warna bas. Ini ialah…",
        "Abstraction", "Decomposition", "Algorithm design", "Pattern recognition"))

S("ct06", T, "1.2 Algorithm design",
  """
  **Algorithm design**: membina langkah-langkah (step-by-step instructions) yang tersusun dan jelas untuk menyelesaikan masalah.

  Algorithm boleh ditulis sebagai **pseudocode** atau dilukis sebagai **flowchart** (Bab 2), kemudian ditukar kepada kod C++.
  """,
  "Apakah algorithm design?",
  kw=["step|langkah|steps|step-by-step|arahan|instructions",
      "order|tersusun|sequence|turutan|susunan|ordered",
      "solve|selesai|menyelesaikan|solution|penyelesaian"],
  ans="Membina langkah demi langkah yang tersusun untuk menyelesaikan masalah.",
  hint="Fikirkan resepi masakan.",
  fu=[F("""Dua cara utama mewakili algorithm: **pseudocode** (teks) dan **flowchart** (rajah).""",
        "Namakan DUA cara untuk mewakili algorithm.",
        kw=["pseudocode|pseudokod|kod pseudo", "flowchart|carta alir|carta aliran"],
        ans="Pseudocode dan flowchart.",
        hint="Satu ditulis, satu dilukis.")],
  mcq=M("Senarai langkah tersusun dan jelas untuk menyelesaikan masalah dipanggil…",
        "Algorithm", "Compiler", "Identifier", "Abstraction"))

S("ct07", T, "1.3 Characteristics of a good algorithm",
  """
  Ciri-ciri algorithm yang baik:

  - **Finite**: mesti berhenti selepas bilangan langkah yang terhad.
  - **Definite / unambiguous**: setiap langkah jelas, hanya satu maksud.
  - **Input**: sifar atau lebih input.
  - **Output**: sekurang-kurangnya satu output.
  - **Effective**: setiap langkah boleh dilaksanakan.
  """,
  "Nyatakan sekurang-kurangnya tiga ciri algorithm yang baik.",
  kw=["finite|terhad|berhenti|end|tamat|stop",
      "definite|unambiguous|jelas|clear|tidak samar|precise|tepat",
      "input|output|effective|berkesan|boleh dilaksana"],
  ans="Finite, definite (jelas), ada input/output, effective.",
  hint="Satu ciri berkaitan BERHENTI, satu berkaitan JELAS.",
  fu=[F("""Loop yang tidak pernah berhenti (infinite loop) melanggar ciri **finite**.""",
        "Algorithm yang tidak pernah berhenti melanggar ciri apa?",
        ans=["finite", "finiteness", "terhad"],
        hint="Lawan bagi 'infinite'.")],
  mcq=M("Langkah 'Tambah sedikit gula' dalam algorithm melanggar ciri…",
        "Definite (unambiguous)", "Finite", "Output", "Input"))

S("ct08", T, "1.4 Problem solving steps (program development)",
  """
  Langkah penyelesaian masalah / pembangunan program:

  1. **Problem analysis**: fahami masalah, kenal pasti **input, process, output** (IPO).
  2. **Design**: bina algorithm (pseudocode / flowchart).
  3. **Implementation / coding**: tukar algorithm ke C++.
  4. **Testing & debugging**: uji dengan data, betulkan ralat.
  5. **Maintenance & documentation**: kemas kini dan dokumentasi.
  """,
  "Senaraikan langkah-langkah penyelesaian masalah dalam pembangunan program mengikut turutan.",
  kw=["analysis|analisis|analyse|analyze|fahami|understand",
      "design|reka bentuk|algorithm|algoritma",
      "implement|implementation|coding|code|kod|tulis kod",
      "test|testing|uji|debug|debugging",
      "maintenance|maintain|penyelenggaraan|documentation|dokumentasi"],
  ans="Analysis → Design → Implementation (coding) → Testing & debugging → Maintenance/documentation.",
  hint="Ada 5 langkah. Bermula dengan memahami masalah, berakhir dengan menjaga program.",
  fu=[F("""Dalam langkah **Problem analysis**, kita kenal pasti tiga perkara: Input, Process, Output (IPO).""",
        "Apakah tiga perkara yang dikenal pasti semasa problem analysis?",
        kw=["input", "process|proses", "output"],
        ans="Input, Process, Output.",
        hint="Singkatan IPO."),
      F("""Langkah **Design** datang SEBELUM coding. Kesilapan biasa pelajar: terus menaip kod tanpa algorithm.""",
        "Apakah langkah yang mesti dibuat SEBELUM coding?",
        ans=["design", "algorithm design", "reka bentuk", "design algorithm"],
        hint="Lukis flowchart / tulis pseudocode dulu.")],
  mcq=M("Langkah manakah yang datang terus SELEPAS problem analysis?",
        "Design (algorithm)", "Testing", "Coding", "Maintenance"))

S("ct09", T, "1.5 TRAP: Abstraction vs Decomposition", trap=True,
  text="""
  **TRAP**: pelajar selalu terkeliru antara dua ini.

  - **Decomposition** = PECAHKAN masalah kepada bahagian kecil (bilangan bahagian bertambah).
  - **Abstraction** = BUANG butiran tidak penting (maklumat berkurang).

  Petua: Decomposition → "pecah". Abstraction → "tapis".
  """,
  question="Apakah beza utama antara decomposition dan abstraction?",
  kw=["decomposition|dekomposisi", "break|pecah|pecahkan|bahagi|smaller|kecil",
      "abstraction|abstraksi", "ignore|abaikan|buang|tapis|filter|tidak penting|irrelevant|penting"],
  ans="Decomposition memecahkan masalah kepada bahagian kecil; abstraction membuang/abaikan butiran yang tidak penting.",
  hint="Satu 'pecah', satu 'tapis'.",
  fu=[F("""Contoh: "Abaikan jenama pen pelajar semasa kira markah" → menapis butiran.""",
        "\"Abaikan jenama pen pelajar semasa kira markah\". Decomposition atau abstraction?",
        ans=["abstraction", "abstraksi"],
        hint="Ia menapis.")],
  mcq=M("Pernyataan manakah BETUL?",
        "Abstraction membuang butiran yang tidak penting",
        "Abstraction memecahkan masalah kepada modul kecil",
        "Decomposition membuang butiran yang tidak penting",
        "Decomposition dan abstraction adalah sama"))

# ---------------------------------------------------------------- BAB 2
T = "alg"

S("al01", T, "2.1 Algorithm, pseudocode and flowchart",
  """
  **Algorithm** ialah turutan langkah terhingga untuk menyelesaikan masalah. Ia boleh diwakili dengan:

  - **Pseudocode**: penerangan teks seperti bahasa Inggeris yang berstruktur. Tidak boleh di-compile/run.
  - **Flowchart**: rajah yang menggunakan simbol piawai disambung dengan anak panah (flow lines).
  """,
  "Apakah beza pseudocode dan flowchart?",
  kw=["pseudocode|pseudokod", "text|teks|tulis|written|english|ayat|perkataan",
      "flowchart|carta alir", "diagram|rajah|symbol|simbol|graphical|grafik|lukis|gambar"],
  ans="Pseudocode ialah teks berstruktur seperti bahasa Inggeris; flowchart ialah rajah grafik guna simbol piawai.",
  hint="Satu ditulis, satu dilukis dengan simbol.",
  fu=[F("""Pseudocode **tidak** boleh di-compile. Ia hanya untuk manusia merancang logik.""",
        "Bolehkah pseudocode di-compile dan dijalankan? (ya / tidak)",
        ans=["tidak", "no", "tak", "tidak boleh"],
        hint="Ia bukan bahasa pengaturcaraan sebenar.")],
  mcq=M("Pseudocode ialah…",
        "Penerangan algorithm dalam teks berstruktur seperti bahasa Inggeris",
        "Kod C++ yang telah di-compile",
        "Rajah dengan simbol oval dan diamond",
        "Bahasa mesin (binary)"))

S("al02", T, "2.2 Pseudocode keywords",
  """
  Kata kunci pseudocode yang biasa:

  - Mula/tamat: `START` … `END`
  - Input: `READ`, `GET`, `INPUT`
  - Output: `DISPLAY`, `PRINT`
  - Proses: `SET`, `CALCULATE`, `=`
  - Selection: `IF … THEN … ELSE … ENDIF`
  - Repetition: `WHILE … ENDWHILE`, `FOR … ENDFOR`

  ```
  START
     READ length, width
     area = length * width
     DISPLAY area
  END
  ```
  """,
  "Tulis DUA kata kunci pseudocode untuk input dan DUA untuk output.",
  kw=["read|get|input|baca", "display|print|output|papar|show|write"],
  ans="Input: READ / GET. Output: DISPLAY / PRINT.",
  hint="Satu untuk membaca, satu untuk memaparkan.",
  fu=[F("""Selection dalam pseudocode ditutup dengan `ENDIF`, loop while ditutup dengan `ENDWHILE`.""",
        "Apakah kata kunci yang menutup blok IF dalam pseudocode?",
        ans=["endif", "end if", "end-if"],
        hint="END + …")],
  mcq=M("Kata kunci pseudocode yang sesuai untuk memaparkan hasil ialah…",
        "DISPLAY", "READ", "ENDIF", "WHILE"))

S("al03", T, "2.3 Flowchart symbols: terminal",
  """
  **Terminal** (bentuk **oval / bujur**): menandakan **START** dan **END** sesuatu flowchart.

  Setiap flowchart bermula dengan satu Start dan berakhir dengan End.
  """,
  "Apakah bentuk simbol terminal dan apakah fungsinya?",
  kw=["oval|bujur|ellipse|elips|rounded|bulat panjang",
      "start|mula|end|tamat|begin|stop|akhir"],
  ans="Oval; menandakan Start dan End.",
  hint="Bentuknya seperti kapsul.",
  fu=[F("""Oval = Start/End. Jangan guna oval untuk proses di tengah-tengah flowchart.""",
        "Simbol oval dipakai untuk apa? (dua perkataan)",
        ans=["start end", "start and end", "start/end", "mula tamat", "mula dan tamat", "begin end"],
        hint="Permulaan dan …")],
  mcq=M("Simbol flowchart untuk START/END ialah…",
        "Oval", "Diamond", "Parallelogram", "Rectangle"))

S("al04", T, "2.3 Flowchart symbols: input/output",
  """
  **Input/Output** (bentuk **parallelogram / segi empat selari**): untuk membaca input (READ) atau memaparkan output (DISPLAY).
  """,
  "Simbol flowchart apakah yang digunakan untuk input dan output?",
  kw=["parallelogram|segi empat selari|selari|jajaran genjang"],
  ans="Parallelogram.",
  hint="Bentuk segi empat yang 'senget'.",
  fu=[F("""`READ length` dan `DISPLAY area` kedua-duanya dilukis dalam parallelogram.""",
        "`DISPLAY area` dilukis dalam simbol apa?",
        ans=["parallelogram", "segi empat selari"],
        hint="Sama dengan simbol input.")],
  mcq=M("Langkah 'READ marks' dalam flowchart dilukis menggunakan…",
        "Parallelogram", "Rectangle", "Oval", "Diamond"))

S("al05", T, "2.3 Flowchart symbols: process",
  """
  **Process** (bentuk **rectangle / segi empat tepat**): untuk pengiraan atau tugasan (assignment), contoh `area = length * width`.
  """,
  "Simbol apakah untuk process dalam flowchart?",
  kw=["rectangle|segi empat tepat|segiempat tepat|kotak|box"],
  ans="Rectangle (segi empat tepat).",
  hint="Bentuk kotak biasa.",
  fu=[F("""`total = total + price` ialah process → rectangle.""",
        "`total = total + price` dilukis dalam simbol apa?",
        ans=["rectangle", "segi empat tepat", "kotak"],
        hint="Ia pengiraan.")],
  mcq=M("Pengiraan 'tax = income * 0.25' dilukis dalam…",
        "Rectangle", "Parallelogram", "Diamond", "Circle"))

S("al06", T, "2.3 Flowchart symbols: decision",
  """
  **Decision** (bentuk **diamond / berlian**): untuk syarat (condition) yang jawapannya **Yes/No** atau **True/False**.

  Diamond mempunyai **satu** anak panah masuk dan **dua** anak panah keluar, setiap satu dilabel (Yes/No).
  """,
  "Terangkan simbol decision dalam flowchart.",
  kw=["diamond|berlian|rhombus|wajik",
      "condition|syarat|keputusan|decision|test",
      "yes|no|true|false|dua|two|ya|tidak"],
  ans="Diamond; mewakili syarat; ada dua keluaran Yes/No (True/False).",
  hint="Bentuk, apa yang diuji, dan berapa anak panah keluar.",
  fu=[F("""Diamond: 1 masuk, 2 keluar (Yes / No). Kedua-dua anak panah keluar MESTI dilabel.""",
        "Berapakah bilangan anak panah KELUAR dari simbol decision?",
        ans=["2", "dua", "two"],
        hint="Yes dan …")],
  mcq=M("Simbol decision (diamond) mempunyai berapa laluan keluar?",
        "2 (Yes/No)", "1", "3", "Tiada had"))

S("al07", T, "2.3 Flowchart symbols: flow lines, connector, predefined process",
  """
  Simbol lain:

  - **Flow line** (anak panah): tunjuk arah aliran.
  - **On-page connector** (**bulatan kecil**): sambung bahagian flowchart pada halaman yang sama.
  - **Off-page connector** (bentuk pentagon/rumah): sambung ke halaman lain.
  - **Predefined process** (rectangle dengan garis menegak di kedua-dua tepi): panggil modul/function yang ditakrif di tempat lain.
  """,
  "Apakah simbol untuk memanggil modul/function (predefined process)?",
  kw=["rectangle|segi empat|kotak|box", "double|garis|lines|side|tepi|dua garis|menegak|vertical"],
  ans="Rectangle dengan garis menegak di kedua-dua tepi.",
  hint="Seperti simbol process, tetapi ada tambahan di tepi.",
  fu=[F("""On-page connector ialah bulatan kecil yang biasanya mengandungi huruf/nombor, contoh (A).""",
        "Apakah bentuk on-page connector?",
        ans=["circle", "bulatan", "bulat", "small circle", "bulatan kecil"],
        hint="Bentuk paling ringkas.")],
  mcq=M("Bulatan kecil berlabel 'A' dalam flowchart ialah…",
        "On-page connector", "Terminal", "Decision", "Predefined process"))

S("al08", T, "2.4 Three control structures",
  """
  Semua algorithm boleh dibina dengan **tiga struktur kawalan** (control structures):

  1. **Sequence**: langkah dilaksanakan satu demi satu mengikut turutan.
  2. **Selection**: pilih laluan berdasarkan syarat (IF, IF-ELSE, switch).
  3. **Repetition (loop / iteration)**: ulang langkah selagi syarat benar (WHILE, FOR, DO-WHILE).
  """,
  "Namakan tiga struktur kawalan asas.",
  kw=["sequence|jujukan|turutan|urutan",
      "selection|pilihan|pemilihan|decision|if",
      "repetition|loop|ulangan|pengulangan|iteration|gelung"],
  ans="Sequence, selection, repetition.",
  hint="S, S, R.",
  fu=[F("""Dalam flowchart, **repetition** dikenali dengan anak panah yang **berpatah balik** ke diamond sebelumnya.""",
        "Dalam flowchart, bagaimana kita tahu ada repetition?",
        kw=["arrow|anak panah|garis|line|flow", "back|balik|kembali|patah balik|loop back|semula|naik"],
        ans="Ada anak panah yang kembali (loop back) ke decision sebelumnya.",
        hint="Ke mana arah anak panah itu pergi?")],
  mcq=M("Menu yang terus dipaparkan sehingga pengguna pilih 'Exit' menggunakan struktur…",
        "Repetition", "Sequence", "Selection sahaja", "Abstraction"))

S("al09", T, "2.5 IPO example: income tax (Ch2 slide 9)",
  """
  Contoh analisis IPO, cukai pendapatan:

  - **Input**: nama, monthly income, number of kids
  - **Process**: `Tax = 0.25 * (monthly income * 11 - number of kids * 450)`
  - **Output**: nama dan Tax

  Dengan income RM4000 dan 2 anak: `0.25 * (4000*11 - 2*450) = 0.25 * 43100 = 10775`.
  """,
  "Tulis formula cukai daripada contoh Ch2 slide 9.",
  kw=["0.25", "11", "450", "income|pendapatan|kids|anak"],
  ans="Tax = 0.25 * (monthly income * 11 - number of kids * 450)",
  hint="Kadar 0.25, gaji didarab berapa bulan, potongan setiap anak berapa?",
  fu=[F("""Trace: income = 4000, kids = 2.
        `4000 * 11 = 44000`, `2 * 450 = 900`, `44000 - 900 = 43100`, `0.25 * 43100 = ?`""",
        "Berapakah Tax untuk income 4000 dan 2 anak?",
        ans=["10775", "rm 10775", "rm10775", "10775.0"],
        hint="0.25 × 43100."),
      F("""Dalam C++ (Lab 4 B2), 0.25, 11 dan 450 disimpan sebagai `const` supaya tiada "magic number" dalam formula.""",
        "Dalam analisis IPO, 'number of kids' ialah input, process atau output?",
        ans=["input"],
        hint="Pengguna yang taip nilai ini.")],
  mcq=M("Dalam formula Tax = 0.25 * (income * 11 - kids * 450), nombor 450 mewakili…",
        "Potongan bagi setiap anak", "Kadar cukai", "Bilangan bulan", "Gaji bulanan"))

S("al10", T, "2.6 Counter, accumulator, sentinel in algorithms",
  """
  Pemboleh ubah khas dalam algorithm:

  - **Counter**: kira bilangan, `count = count + 1`.
  - **Accumulator**: kumpul jumlah, `sum = sum + number` (mesti mula dengan 0).
  - **Sentinel value**: nilai khas untuk tamatkan input, contoh `-1`.
  """,
  "Apakah beza counter dan accumulator?",
  kw=["counter|pembilang|kira bilangan|count",
      "+ 1|tambah 1|tambah satu|increment|bilangan|how many|berapa kali",
      "accumulator|pengumpul|sum|jumlah|total"],
  ans="Counter tambah 1 setiap kali (kira bilangan); accumulator tambah nilai ke jumlah (sum = sum + x).",
  hint="Satu kira BERAPA BANYAK, satu kira JUMLAH.",
  fu=[F("""Accumulator **mesti** diberi nilai awal `0` sebelum loop. Jika tidak, ia mengandungi nilai sampah (garbage).""",
        "Apakah nilai awal yang betul untuk accumulator sum?",
        ans=["0", "sifar", "zero", "sum = 0", "sum=0"],
        hint="Jumlah sebelum apa-apa ditambah."),
      F("""Sentinel = nilai yang tidak mungkin jadi data sebenar, contoh -1 untuk markah.""",
        "Apakah fungsi sentinel value?",
        kw=["stop|tamat|berhenti|end|hentikan|terminate", "input|loop|data|bacaan"],
        ans="Nilai khas yang menandakan tamat input / hentikan loop.",
        hint="Contoh: 'Masukkan -1 untuk berhenti'.")],
  mcq=M("Dalam 'total = total + price', total ialah…",
        "Accumulator", "Counter", "Sentinel", "Constant"))

S("al11", T, "2.7 Desk check / trace table",
  """
  **Desk check** (trace table): uji algorithm secara manual dengan data contoh. Tulis setiap pemboleh ubah sebagai lajur dan catat nilainya selepas setiap langkah.

  Ini juga cara terbaik untuk menjawab soalan "trace code" dalam peperiksaan.
  """,
  "Apakah desk check / trace table?",
  kw=["manual|tangan|sendiri|by hand|kertas",
      "test|uji|semak|check|trace|jejak",
      "variable|pemboleh ubah|nilai|value|table|jadual"],
  ans="Uji algorithm secara manual dengan data contoh, catat nilai setiap pemboleh ubah dalam jadual.",
  hint="Dibuat tanpa komputer.",
  fu=[F("""Algorithm: `sum = 0; FOR i = 1 TO 4: sum = sum + i`. Trace: i=1 sum=1, i=2 sum=3, i=3 sum=6, i=4 sum=?""",
        "Apakah nilai akhir sum?",
        ans=["10"],
        hint="6 + 4.")],
  mcq=M("Tujuan utama trace table ialah…",
        "Menjejak nilai pemboleh ubah langkah demi langkah",
        "Menukar pseudocode ke C++ secara automatik",
        "Melukis simbol flowchart",
        "Mempercepat compile"))

S("al12", T, "2.8 TRAP: common flowchart mistakes", trap=True,
  text="""
  **TRAP flowchart** yang selalu hilang markah:

  - Guna **rectangle** untuk input/output (sepatutnya **parallelogram**).
  - Diamond tanpa label **Yes/No** pada anak panah keluar.
  - Tiada simbol **Start/End** (oval).
  - Anak panah tiada arah, atau aliran bercabang tanpa diamond.
  """,
  question="Senaraikan dua kesilapan biasa semasa melukis flowchart.",
  kw=["rectangle|segi empat|parallelogram|input|output",
      "label|yes|no|true|false|ya|tidak",
      "start|end|oval|mula|tamat|terminal|arrow|anak panah"],
  ans="Guna rectangle untuk input/output; diamond tanpa label Yes/No; tiada Start/End; anak panah tanpa arah.",
  hint="Fikir simbol yang salah bentuk, dan label yang tertinggal.",
  fu=[F("""Pelajar melukis `READ marks` dalam rectangle. Ini salah.""",
        "Simbol yang betul untuk READ marks ialah?",
        ans=["parallelogram", "segi empat selari"],
        hint="Input/Output.")],
  mcq=M("Kesilapan manakah dalam flowchart ini: 'DISPLAY total' dalam kotak segi empat tepat?",
        "Output sepatutnya dalam parallelogram",
        "Output sepatutnya dalam diamond",
        "Output sepatutnya dalam oval",
        "Tiada kesilapan"))
