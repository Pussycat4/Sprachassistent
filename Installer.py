import os
import urllib.request

def download_file(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Die Datei '{filename}' wurde erfolgreich heruntergeladen.")
    except Exception as e:
        print(f"Fehler beim Herunterladen der Datei: {e}")

# URL der Datei zum Herunterladen
url = "https://raw.githubusercontent.com/Pussycat4/Sprachassistent/main/Start.py"

# Pfad zur aktuellen Verzeichnis
current_directory = os.path.dirname(os.path.abspath(__file__))

# Dateiname für die heruntergeladene Datei
filename = os.path.join(current_directory, "Start.py")

# Herunterladen der Datei
download_file(url, filename)
