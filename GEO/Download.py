import os
import requests


def download(url, path):
    # Diese Funktion wird verwendet, um eine Datei von einer
    # URL in einen vorgegebenen Ordner herunterzuladen.
    print(f'Die Funktion "Download" wurde gestartet.')
    zip_name = url.rsplit('/', 1)[-1]
    zip_path = os.path.join(path, zip_name)

    if os.path.isfile(zip_path):
        print(f'Datei: "{zip_name}" existiert bereits.')
        print(f'Es ist kein Download erforderlich.\n')
        return

    print(f'Download wurde gestartet.\n')
    response = requests.get(url, stream=True)

    with open(zip_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
