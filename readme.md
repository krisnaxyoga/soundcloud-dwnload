# 🎧 SoundCloud Playlist Downloader  
Python + Flask + HTML/CSS — *Windows Edition*

---

## ⚡ Cara Menjalankan (Windows)

1. **Ekstrak / kloning repo** ke folder bebas, misal  
   `C:\Users\NamaAnda\soundcloud-downloader`
2. **Double-click** `run.bat`  
   ⮕ Jika muncul *Windows Defender SmartScreen* klik **“More info” → “Run anyway”**
3. Tunggu beberapa detik:
   - Terminal terbuka (jangan ditutup)
   - Browser otomatis buka [http://localhost:5000](http://localhost:5000)
4. Masukkan **URL playlist SoundCloud** → klik **Unduh Playlist**  
   File ZIP berisi semua lagu akan otomatis ter-download.

---

## 🔧 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| `python` tidak dikenali | Install Python 3.9+ dari [python.org](https://www.python.org/) — **centang “Add Python to PATH”** |
| scdl error **“401 Unauthorized”** | Dapatkan [auth-token SoundCloud](https://github.com/flyingrub/scdl#authentication), lalu jalankan sekali: <br>`scdl --set-auth-token YOUR_TOKEN` |
| Port 5000 sudah dipakai | Edit baris terakhir `app.py` menjadi: <br>`app.run(debug=True, port=8080)` |
| Window terminal langsung hilang | Jalankan `run.bat` **lewat Command Prompt** untuk melihat pesan error |

---

## 🧪 Developer / Clone dari GitHub

```cmd
git clone https://github.com/krisnaxyoga/soundcloud-dwnload.git
cd soundcloud-downloader
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## 📄 Lisensi

Proyek ini hanya untuk **keperluan pribadi & edukasi**.  
Harap patuhi *Terms of Service* SoundCloud serta hak cipta setiap lagu.