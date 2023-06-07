import os
import urllib.request
import logging

def download_file(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        logging.info(f"Die Datei '{filename}' wurde erfolgreich heruntergeladen.")
    except Exception as e:
        logging.error(f"Fehler beim Herunterladen der Datei: {e}")

# Konfigurieren des Loggings
logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'download.log'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL der Datei zum Herunterladen
url = "https://raw.githubusercontent.com/Pussycat4/Sprachassistent/main/Start.py"

# Pfad zur aktuellen Verzeichnis
current_directory = os.path.dirname(os.path.abspath(__file__))

# Dateiname für die heruntergeladene Datei
filename = os.path.join(current_directory, "Start.py")

# Herunterladen der Datei
download_file(url, filename)
