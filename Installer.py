import os
import sys
import subprocess
import urllib.request

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--target", "."])

# Installation von tqdm
install_package("tqdm")

# Liste der Bibliotheken
libraries = [
    "SpeechRecognition",
    "PyAudio",
    "pyttsx3",
    "nltk",
    "torch",
    "opencv-python",
    "pydub"
]

# Aktuelles Arbeitsverzeichnis
current_directory = os.path.dirname(os.path.abspath(__file__))

# Installation der Bibliotheken im aktuellen Verzeichnis
for library in tqdm(libraries, desc="Herunterladen und Installieren"):
    install_package(library)

print("Die Bibliotheken wurden erfolgreich heruntergeladen und installiert.")

# URL zum Herunterladen des Codes
code_url = "https://raw.githubusercontent.com/Pussycat4/Sprachassistent/main/Start.py"

# Zielverzeichnis zum Speichern des Codes
code_file = os.path.join(current_directory, "Start.py")

# Herunterladen des Codes
print("Lade den Code herunter...")
urllib.request.urlretrieve(code_url, code_file)

print("Der Code wurde erfolgreich heruntergeladen.")
