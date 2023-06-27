# Import Pakete
import os
import numpy as np
import rasterio as rio
import glob


def calculation(band_1):
    # Mit dieser Funktion können lineare Werte in dB-Werte umgewandelt werden.
    temp_log = np.log10(band_1) * 10
    temp_log[temp_log == -np.inf] = np.nan
    temp_log[temp_log == -0] = -1
    return temp_log


def process_raster(url, path):
    # Diese Funktion dient der Verarbeitung der entpackten Daten.
    print(f'Die Funktion "Prozessierung" wurde gestartet.')
    zip_name = url.rsplit('/', 1)[-1]
    unzip_folder = zip_name.split('.')[0]
    raster_path = os.path.join(path, unzip_folder)
    file_list = glob.glob(os.path.join(raster_path, '*.tif'))
    file_list = [w.replace('\\', '/') for w in file_list]
    out_folder = 'Bild_prozessiert'
    out_folder_path = os.path.join(path, out_folder)

    # Abfrage, ob Datei bereits prozessiert
    if not os.path.isdir(out_folder_path):
        os.makedirs(out_folder_path)
    else:
        print(f'Ausgabeordner "Bild_prozessiert" existiert bereits.')

    # Schleife, um jede Datei in file_list zu verarbeiten
    for file_path in file_list:
        file_name = os.path.basename(file_path)

        # Rasterdaten lesen und zu schreiben
        with rio.open(file_path) as src:
            band_1 = src.read(1)
            band_1 = np.array(band_1)
            np.seterr(divide='ignore', invalid='ignore')

            # Anwendung der Funktion "calculation(band_1)"
            db_pixel = calculation(band_1)
            ras_meta = src.profile
            ras_meta.update(count=1, dtype=rio.float32, nodata=-9999)
            img_out_name = os.path.join(out_folder_path, f'linear_to_db_{file_name}')

            # Prozessierung des Bildes
            if not os.path.isfile(img_out_name):
                print(f'Die Prozessierung wurde gestartet.\n')
                with rio.open(img_out_name, 'w', **ras_meta) as dst:
                    dst.write(db_pixel, 1)
            else:
                print(f'Das prozessierte Bild existiert bereits.\n')
