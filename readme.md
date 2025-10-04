# SoundCloud Playlist Downloader

## Cara Menjalankan (Windows)

1. Ekstrak/kloning repo ke folder bebas, misal C:\Users\NamaAnda\soundcloud-downloader
2. Double-click file run.bat
3. Jika muncul Windows Defender SmartScreen → klik “More info” → “Run anyway”
4. Tunggu beberapa detik:
	* Terminal terbuka (jajaran ditutup)
	* Browser otomatis buka http://localhost:5000
	* Masukan URL playlist SoundCloud → klik Unduh Playlist
	* File ZIP berisi semua lagu akan otomatis ter-download

## Troubleshooting

| Masalah | Solusi |
| --- | --- |
| python tidak dikenali | Install Python 3.9+ dari python.org <img src="https://img.shields.io/badge/python-3.9%2B%2B%203.8%2B%203.9%2B%203.10%2B%203.11%2B%203.12-blue.svg" /> |
| scdl error “401 Unauthorized” | Dapatkan auth-token SoundCloud Anda: Panduan lalu jalankan scdl --set-auth-token TOKEN di terminal biasa satu kali saja |
| Port 5000 sudah dipakai | Edit baris terakhir app.py jadi app.run(debug=True, port=8080) |
| Window terminal langsung hilang | Jalankan run.bat lewat Command Prompt untuk melihat pesan error |

## Lisensi

Projek ini hanya untuk pribadi & edukasi. Patuhi ToS SoundCloud, serta hak cipta setiap lagu.
