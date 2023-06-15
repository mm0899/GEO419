import os
import requests


def url_path():
    # Diese Funktion wird verwendet, um den Verzeichnis-Pfad und die URL zu erhalten.
    # Der Benutzer muss den Pfad und die URL über das Terminal eingeben.
    print(f'Die Funktion "Verzeichnis_URL" wurde gestartet.')
    valid_url = False
    valid_path = False

    while not valid_path:
        print('Bitte geben Sie den Pfad des Arbeitsverzeichnisses an.')
        print('Hinweis: Beispielpfad (Windows): "C:/Ordner/".')
        path = input('Eingabe: ')
        if os.path.exists(path):
            print('Arbeitsverzeichnis = gültig.\n')
            valid_path = True
        else:
            print('Arbeitsverzeichnis = ungültig.\n')

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

    return url, path
