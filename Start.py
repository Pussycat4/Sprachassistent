import speech_recognition as sr

# Initialisierung der Spracherkennung

r = sr.Recognizer()

# Schleife für die Spracheingabe

while True:

    with sr.Microphone() as source:

        print("Sage etwas...")

        audio = r.listen(source)

    try:

        # Spracheingabe in Text umwandeln

        text = r.recognize_google(audio, language="de-DE")

        # Überprüfung, ob "Hey Max" im Text enthalten ist

        if "Hey Max" in text:

            print("Spracheingabe geöffnet. Sprechen Sie bitte.")

            while True:

                audio = r.listen(source)

                text = r.recognize_google(audio, language="de-DE")

                print("Sie haben gesagt:", text)

        # Überprüfung, ob "Auf Wiedersehen" im Text enthalten ist

        if "Auf Wiedersehen" in text:

            print("Das Programm wird beendet.")

            break

    except sr.UnknownValueError:

        print("Spracherkennung konnte das Gesprochene nicht verstehen.")

    except sr.RequestError as e:

        print("Fehler bei der Spracherkennung:", str(e))
        
