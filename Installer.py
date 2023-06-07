import os
import urllib.request
import subprocess
import logging

# URL zum Herunterladen des Codes
url = "https://raw.githubusercontent.com/Pussycat4/Sprachassistent/main/Start.py"
# Name der heruntergeladenen Datei
filename = "Start.py"
# Name der Log-Datei
log_filename = "Installation.log"

# Funktion zum Herunterladen der Datei von der URL
def download_file(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Datei {filename} erfolgreich heruntergeladen.")
    except urllib.error.URLError as e:
        print(f"Fehler beim Herunterladen der Datei: {e}")

# Funktion zum Erstellen des Log-Eintrags
def create_log_entry(filename, message):
    logging.basicConfig(filename=log_filename, level=logging.INFO)
    logging.info(f"{filename}: {message}")

# Herunterladen des Codes von der URL
download_file(url, filename)

# Installieren des Sprache-zu-Text-Programms
try:
    subprocess.check_call(["pip", "install", "SpeechRecognition"])
    create_log_entry("SpeechRecognition", "Erfolgreich installiert.")
except subprocess.CalledProcessError as e:
    create_log_entry("SpeechRecognition", f"Fehler beim Installieren: {e}")

# Erstellen eines Log-Eintrags
create_log_entry(filename, "Datei erfolgreich heruntergeladen.")

