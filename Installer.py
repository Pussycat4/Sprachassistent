import os
import urllib.request
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

# Erstellen eines Log-Eintrags
create_log_entry(filename, "Datei erfolgreich heruntergeladen.")
