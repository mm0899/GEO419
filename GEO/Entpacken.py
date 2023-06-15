import os
import zipfile


def unzip(url, path):
    # Diese Funktion wird zum Entpacken der heruntergeladenen Daten verwendet.
    print(f'Die Funktion "Entpacken" wurde gestartet.')
    zip_name = os.path.basename(url)
    unzip_folder = os.path.join(path, os.path.splitext(zip_name)[0])

    if os.path.exists(unzip_folder):
        if len(os.listdir(unzip_folder)) == 0:
            print("Verzeichnis ist leer.")
        else:
            print(f'Ordner: "{unzip_folder}" und Dateien existieren bereits.\n')
        return
    print(f'Entpacken der Dateien wurde gestartet.\n')
    os.mkdir(unzip_folder)
    with zipfile.ZipFile(os.path.join(path, zip_name), 'r') as zip_ref:
        zip_ref.extractall(unzip_folder)
