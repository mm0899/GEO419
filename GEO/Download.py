# Import Pakete
import os
import requests


def download(url, path):
    # Diese Funktion wird verwendet, um eine Datei von einer
    # URL in einen vorgegebenen Ordner herunterzuladen.

    print(f'Die Funktion "Download" wurde gestartet.')
    # Aufsplitten des Dateinamen
    zip_name = url.rsplit('/', 1)[-1]
    zip_path = os.path.join(path, zip_name)

    # Abfrage, ob Datei bereits heruntergeladen
    if os.path.isfile(zip_path):
        print(f'Datei: "{zip_name}" existiert bereits.')
        print(f'Es ist kein Download erforderlich.\n')
        return

    # Download der Datei
    print(f'Download wurde gestartet.\n')
    response = requests.get(url, stream=True)
    with open(zip_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
