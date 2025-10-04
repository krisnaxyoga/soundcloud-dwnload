git clone https://github.com/username/repo.git
cd soundcloud-downloader
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

🎧 SoundCloud Playlist Downloader
Python + Flask + HTML/CSS — Windows Edition
📦 Fitur
Download seluruh lagu dalam playlist SoundCloud (publik & downloadable)
Interface web sederhana (buka browser otomatis)
Tidak perlu buka terminal – cukup double-click run.bat
Semua dependensi terisolasi di virtual environment
📁 Struktur Project
Copy
soundcloud-downloader/
├── venv/                 # otomatis dibuat saat 1x run
├── app.py                # Flask backend
├── templates/
│   └── index.html        # UI
├── static/
│   └── style.css         # styling
├── downloads/            # lagu terunduh (auto-created)
├── run.bat               # 1-klik jalankan aplikasi
└── requirements.txt      # daftar package (opsional)
🚀 Cara Menjalankan (Windows)
Extract / clone repo ke folder bebas, misal C:\Users\NamaAnda\soundcloud-downloader
Double-click file run.bat
Jika muncul Windows Defender SmartScreen → klik “More info” → “Run anyway”
Tunggu beberapa detik:
Terminal terbuka (jangan ditutup)
Browser otomatis buka http://localhost:5000
Masukkan URL playlist SoundCloud → klik Unduh Playlist
File ZIP berisi semua lagu akan otomatis ter-download
🔧 Troubleshooting
Table
Copy
Masalah	Solusi
python tidak dikenali	Install Python 3.9+ dari python.org ☑ Centang “Add Python to PATH”
scdl error “401 Unauthorized”	Dapatkan auth-token SoundCloud Anda: Panduan lalu jalankan scdl --set-auth-token TOKEN di terminal biasa satu kali saja
Port 5000 sudah dipakai	Edit baris terakhir app.py jadi app.run(debug=True, port=8080)
Window terminal langsung hilang	Jalankan run.bat lewat Command Prompt untuk melihat pesan error
🧪 Developer? Jalankan Manual
cmd

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

Atau bisa jalankan run.bat jika kamu pake windows

📄 Lisensi
Projek ini hanya untuk pribadi & edukasi. Patuhi ToS SoundCloud serta hak cipta setiap lagu.