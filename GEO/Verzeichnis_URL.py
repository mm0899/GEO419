# Import Pakete
import os
import requests


def url_path():
    # Diese Funktion wird verwendet, um den Verzeichnis-Pfad und die URL zu erhalten.
    # Der Benutzer muss den Pfad und die URL über das Terminal eingeben.
    print(f'Die Funktion "Verzeichnis_URL" wurde gestartet.')
    valid_url = False
    valid_path = False
    special_characters = '\/:*?"<>|'

    # Abfrage des Pfads
    while not valid_path:
        print('Bitte geben Sie den Pfad des Arbeitsverzeichnisses an.')
        print('Hinweis: Beispielpfad (Windows): "C:Users\Documents\Directory".')
        print('Hinweis: Beispielpfad (Linux): /home/user/Documents/Directory".')
        print(f'Hinweis: Sonderzeichen wie {special_characters} sind im Pfadnamen nicht erlaubt.')
        path = input('Eingabe: ')
        if os.path.exists(path):
            print('Arbeitsverzeichnis = gültig.\n')
            valid_path = True
        # Erstellen eines neuen Arbeitsverzeichnisses
        else:
            try:
                os.makedirs(path)
                print(f'Arbeitsverzeichnis "{path}" wurde erfolgreich erstellt.\n')
                valid_path = True
            except OSError:
                print(f'Fehler beim Erstellen des Arbeitsverzeichnisses "{path}". Bitte überprüfen Sie den Pfad.\n')

    # Abfrage der URL
    while not valid_url:
        print('Bitte geben Sie die URL an.')
        print('Hinweis: Die URL muss mit "http" anfangen und mit ".zip" enden.')
        url = input('Eingabe: ')
        zip_url = url.rsplit('.', 1)[-1]
        av = requests.head(url).status_code
        is_valid_url = av == 200 and zip_url == 'zip'
        valid_url_msg = 'URL = gültig.\n'
        invalid_url_msg = 'URL ist nicht gültig.\n'
        print((valid_url_msg if is_valid_url else invalid_url_msg))
        if is_valid_url:
            valid_url = True

    # Rückgabe von URL und Pfad
    return url, path
