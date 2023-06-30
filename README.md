# GEO419

Dieses Paket basiert auf einem Projekt aus dem M.Sc Geoinformatik im Modul "GEOG 419 - Modulare Programmierung in der FE" der Friedrich-Schiller-Universität Jena und wurde von Max Marquardt und Justin Volkert entwickelt. 
Es enthält Module/Algorithmen zum Herunterladen, Entpacken, Vorverarbeiten und Visualisieren von Sentinel-1-Bildern. Ein detaillierterer Überblick wird unten gegeben:

-	Download einer .zip-Datei in ein zuvor definiertes Verzeichnis 
-	Entpacken der heruntergeladenen .zip-Datei 
-	Lesen der Datei in ein numpy Array 
-	Logarithmische Skalierung der Rückstreuintensitäten
-	Schreiben des neu berechneten Bildes in eine neue Datei 
-	Visualisierung des logarithmisch skalierten Bildes

## Installation

-	Ablegen der environment.yml-Datei und des Ordners „GEO“ in einem selbstgewählten Verzeichnis
-	Öffnen der Anaconda Prompt
-	Eingeben folgender Zeilen (einzeln):
```
$ cd C:/Users/Verzeichnis/environment.yml
$ conda env create -f environment.yml
$ conda activate GEO419
```
-	Erstellen eines neuen Projektes in PyCharm mit dem zuvor importierten Environment
-	Öffnen des PyCharm Terminals
-	Eingeben folgender Zeilen (einzeln):
```
$ pip install gdal
$ pip install rasterio
```
Die Software kann nun durch Ausführen der "Hauptfunktion.py" gestartet werden.
