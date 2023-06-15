# Import Funktionen
from GEO import Verzeichnis_URL, Download, Entpacken, Prozessierung, Visualisierung


# Hauptfunktion
def main():
    url, path = Verzeichnis_URL.url_path()
    Download.download(url, path)
    Entpacken.unzip(url, path)
    Prozessierung.process_raster(url, path)
    Visualisierung.plot(path)
    print(f"\nProzesse abgeschlossen!\n")

# Aufruf der Hauptfunktion "main"
if __name__ == '__main__':
    main()
