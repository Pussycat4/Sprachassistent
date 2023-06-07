import os

import sys

import subprocess

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

