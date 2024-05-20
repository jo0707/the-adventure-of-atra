class Quiz:
    def __init__(self, question: str, options: list[str], answer: str):
        self.question = question
        self.options = options
        self.answer = answer

    def isCorrect(self, answer: str) -> bool:
        return self.answer == answer

quizLampung = [
    Quiz(
        "Raden Intan II merupakan pahlawan nasional dari Lampung, ia dinobatkan sebagai Ratu pada usia 16 tahun. Apa yang pertama kali dilakukan Raden Intan II setelah dinobatkan sebagai Ratu?",
        [
            "Membangun Istana Baru di Lampung",
            "Memimpin rakyat melawan Belanda",
            "Menjalin perdamaian dengan Belanda",
            "Menjalankan pemerintah secara Otoriter"
        ],
        "Memimpin rakyat melawan Belanda"
    ),
    Quiz(
        "Raden Intan II merupakan pahlawan Nasional dari Lampung, ia wafat pada tanggal 5 Oktober 1856. Apa yang membuat kematiannya pada saat itu menjadi simbol perlawanan?",
        [
            "Karena ia tewas dalam pertempuran besar melawan Belanda",
            "Karena ia menyerah kepada Belanda",
            "Karena ia menjadi tahanan perang setelah melawan Belanda"
        ],
        "Karena ia tewas dalam pertempuran besar melawan Belanda"
    ),
    Quiz(
        "Siger merupakan mahkota pengantin wanita Lampung yang terbuat dari kuningan berlapis emas. Apa yang menjadi simbolis dari Siger Lampung?",
        [
            "Keberanian dan kekuatan",
            "Kekayaan dan kemegahan",
            "Keanggunan, kesuburan, kewibawaan dan kemuliaan",
            "Kebijaksanaan dan kedamaian"
        ],
        "Keanggunan, kesuburan, kewibawaan dan kemuliaan"
    ),
    Quiz(
        "Apa yang membedakan keris Lampung dengan Keris jenis lainnya?",
        [
            "Bilahnya yang lurus",
            "Ukirannya yang sederhana",
            "Bilahnya yang bengkok dan ukirannya yang rumit",
            "Ukirannya warna-warni"
        ],
        "Bilahnya yang bengkok dan ukirannya yang rumit"
    ),
    Quiz(
        "Prasasti Bungkuk ditemukan pada tahun 1985, di Desa Bungkuk, Kecamatan Jabung, Kabupaten Lampung Timur. Apa isi dari prasasti tersebut?",
        [
            "Berisi tentang penjelasan peminjaman tanah",
            "Berisi tentang kutukan untuk siapapun yang tidak tunduk kepada pemerintahan",
            "Berisi tentang penjelasan terkait kejayaan kerajaan Sriwijaya",
            "Memberikan nasihat kepada rakyat"
        ],
        "Berisi tentang penjelasan terkait kejayaan kerajaan Sriwijaya"
    )
]

quizSumateraBarat = [
    Quiz(
        "Berapa tahun Imam Bonjol diasingkan ke Pulau Ambon setelah tertangkap oleh Belanda?",
        [
            "11 tahun",
            "13 tahun",
            "15 tahun",
            "17 tahun"
        ],
        "13 tahun"
    ),
    Quiz(
        "Bahan utama yang digunakan dalam pembangunan Miniatur Rumah Gadang adalah…",
        [
            "Batu dan Bambu",
            "Kayu dan Bambu",
            "Bambu dan Genteng",
            "Bambu dan Tanah Liat"
        ],
        "Kayu dan Bambu"
    ),
    Quiz(
        "Apa fungsi dari Prasasti Kuburajo II dalam masa Raja Adityawarman?",
        [
            "Sebagai tanda pemakaman para bangsawan",
            "Sebagai markah tanah untuk menandai batas wilayah",
            "Sebagai sandaran duduk penghulu atau kepala adat ketika rapat",
            "Sebagai sarana ritual keagamaan"
        ],
        "Sebagai sandaran duduk penghulu atau kepala adat ketika rapat"
    )
]

quizSumateraUtara = [
    Quiz(
        "Senjata apa yang digunakan oleh pahlawan Sisingamangaradja XII ketika melakukan perlawanan terhadap penjajah Belanda di tanah Batak?",
        [
            "Piso gaja Dompak",
            "Prasasti Lobu Tua",
            "Prasasti Batugana"
        ],
        "Piso gaja Dompak"
    ),
    Quiz(
        "Dimanakah prasasti Batugana I ditemukan?",
        [
            "Desa Lobu Tua",
            "Desa Bahal",
            "Kabupaten Tapanuli Tengah",
            "Kabupaten Padang Lawas Utara"
        ],
        "Desa Bahal"
    ),
    Quiz(
        "Apa nama bagian pakaian adat Batak Toba yang merupakan bagian atas untuk pria?",
        [
            "Hoba-Hoba",
            "Hean",
            "Singkot",
            "Ampe-ampe"
        ],
        "Ampe-ampe"
    )
]