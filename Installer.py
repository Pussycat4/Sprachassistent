import os
import subprocess
import urllib.request

import pkg_resources

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--target", "."])

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def install_missing_packages(required_packages):
    installed_packages = [pkg.key for pkg in pkg_resources.working_set]
    missing_packages = [pkg for pkg in required_packages if pkg not in installed_packages]

    if missing_packages:
        print("Folgende Pakete werden installiert: ")
        for package in missing_packages:
            print(package)
            install_package(package)

# Erforderliche Pakete
required_packages = [
    "SpeechRecognition",
    "PyAudio",
    "pyttsx3",
    "nltk",
    "torch" if torch_available else "tensorflow",
    "opencv-python",
    "pydub"
]

# Installieren der fehlenden Pakete
install_missing_packages(required_packages)

# Aktuelles Arbeitsverzeichnis
current_directory = os.path.dirname(os.path.abspath(__file__))

# Download des Codes von der URL
download_file("https://raw.githubusercontent.com/Pussycat4/Sprachassistent/main/Start.py", "Start.py")

# Ausführen des heruntergeladenen Codes
subprocess.check_call([sys.executable, "Start.py"])
