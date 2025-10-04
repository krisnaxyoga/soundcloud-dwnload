@echo off
title SoundCloud Downloader
cd /d "%~dp0"

:: Cek apakah venv sudah ada
if not exist "venv\Scripts\activate.bat" (
    echo venv belum ada, membuat virtual environment...
    python -m venv venv
)

:: Aktifkan venv
call venv\Scripts\activate.bat

:: Install / update dependensi (opsional, bisa di-comment jika sudah ada)
pip install -q flask scdl yt-dlp

:: Jalankan aplikasi
start http://localhost:5000
python app.py

:: Tunggu user tekan tombol agar window tidak langsung tertutup
pause