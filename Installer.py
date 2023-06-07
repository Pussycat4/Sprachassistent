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
    "torch" if torch_available else "tensorflow",
    "opencv-python",
    "pydub"
]

# Aktuelles Arbeitsverzeichnis
current_directory = os.path.dirname(os.path.abspath(__file__))

# Installation der Bibliotheken im aktuellen Verzeichnis
for library in tqdm(libraries, desc="Herunterladen und Installieren"):
    install_package(library)

print("Die Bibliotheken wurden erfolgreich heruntergeladen und installiert.")

# URL des Codes
code_url = "https://raw.githubusercontent.com/Pussycat4/Sprachassistent/main/Start.py"

# Zielpfad zum Speichern des heruntergeladenen Codes
code_file = os.path.join(current_directory, "Start.py")

# Herunterladen des Codes
print("Lade den Code herunter...")
urllib.request.urlretrieve(code_url, code_file)

# Ausführen des heruntergeladenen Codes
print("Führe den heruntergeladenen Code aus...")
exec(open(code_file).read())
