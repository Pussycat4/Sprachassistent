import os
import urllib.request

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)

# URL der Datei zum Herunterladen
url = "https://raw.githubusercontent.com/Pussycat4/Sprachassistent/main/Start.py"

# Pfad zur aktuellen Verzeichnis
current_directory = os.getcwd()

# Dateiname für die heruntergeladene Datei
filename = os.path.join(current_directory, "Start.py")

# Herunterladen der Datei
download_file(url, filename)

print("Die Datei 'Start.py' wurde erfolgreich heruntergeladen.")
