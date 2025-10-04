import os
import zipfile
import shutil
from flask import Flask, request, render_template, send_file, jsonify
import subprocess

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    if not url:
        return jsonify({"error": "URL tidak boleh kosong"}), 400

    # Bersihkan folder download
    if os.path.exists(DOWNLOAD_FOLDER):
        shutil.rmtree(DOWNLOAD_FOLDER)
    os.makedirs(DOWNLOAD_FOLDER)

    try:
        # Gunakan scdl untuk download playlist
        subprocess.run([
            "scdl", "-l", url, "--path", DOWNLOAD_FOLDER, "--onlymp3", "--addtofile"
        ], check=True)
    except subprocess.CalledProcessError:
        return jsonify({"error": "Gagal mengunduh playlist"}), 500

    # Buat ZIP
    zip_path = "soundcloud_playlist.zip"
    with zipfile.ZipFile(zip_path, 'w') as zf:
        for root, _, files in os.walk(DOWNLOAD_FOLDER):
            for file in files:
                zf.write(os.path.join(root, file), file)

    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)