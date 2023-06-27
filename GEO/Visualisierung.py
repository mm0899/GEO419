# Import Pakete
import os
import glob
import numpy as np
import rasterio as rio
from rasterio.plot import show
from matplotlib import pyplot as plt
from matplotlib import colors, cm
from matplotlib.ticker import FormatStrFormatter


def plot(path):
    # Diese Funktion dient der Darstellung des Ergebnisses.
    print(f'Die Funktion "Visualisierung" wurde gestartet.')

    # Festlegung Ausgabeordner
    proc_folder = 'Bild_prozessiert'
    raster_path = os.path.join(path, proc_folder)
    file_list = glob.glob(os.path.join(raster_path, '*.tif'))
    file_list = [w.replace('\\', '/') for w in file_list]

    # Verfügbare Colormaps
    available_cmaps = ["Accent", "Accent_r", "Blues", "Blues_r", "BrBG", "BrBG_r", "BuGn", "BuGn_r", "BuPu", "BuPu_r",
                       "CMRmap", "CMRmap_r", "Dark2", "Dark2_r", "GnBu", "GnBu_r", "Greens", "Greens_r", "Greys",
                       "Greys_r",
                       "OrRd", "OrRd_r", "Oranges", "Oranges_r", "PRGn", "PRGn_r", "Paired", "Paired_r", "Pastel1",
                       "Pastel1_r",
                       "Pastel2", "Pastel2_r", "PiYG", "PiYG_r", "PuBu", "PuBuGn", "PuBuGn_r", "PuBu_r", "PuOr",
                       "PuOr_r", "PuRd",
                       "PuRd_r", "Purples", "Purples_r", "RdBu", "RdBu_r", "RdGy", "RdGy_r", "RdPu", "RdPu_r", "RdYlBu",
                       "RdYlBu_r",
                       "RdYlGn", "RdYlGn_r", "Reds", "Reds_r", "Set1", "Set1_r", "Set2", "Set2_r", "Set3", "Set3_r",
                       "Spectral",
                       "Spectral_r", "Wistia", "Wistia_r", "YlGn", "YlGnBu", "YlGnBu_r", "YlGn_r", "YlOrBr", "YlOrBr_r",
                       "YlOrRd",
                       "YlOrRd_r", "afmhot", "afmhot_r", "autumn", "autumn_r", "binary", "binary_r", "bone", "bone_r",
                       "brg", "brg_r",
                       "bwr", "bwr_r", "cividis", "cividis_r", "cool", "cool_r", "coolwarm", "coolwarm_r", "copper",
                       "copper_r",
                       "cubehelix", "cubehelix_r", "flag", "flag_r", "gist_earth", "gist_earth_r", "gist_gray",
                       "gist_gray_r",
                       "gist_heat", "gist_heat_r", "gist_ncar", "gist_ncar_r", "gist_rainbow", "gist_rainbow_r",
                       "gist_stern",
                       "gist_stern_r", "gist_yarg", "gist_yarg_r", "gnuplot", "gnuplot2", "gnuplot2_r", "gnuplot_r",
                       "gray", "gray_r",
                       "hot", "hot_r", "hsv", "hsv_r", "inferno", "inferno_r", "jet", "jet_r", "magma", "magma_r",
                       "nipy_spectral",
                       "nipy_spectral_r", "ocean", "ocean_r", "pink", "pink_r", "plasma", "plasma_r", "prism",
                       "prism_r", "rainbow",
                       "rainbow_r", "seismic", "seismic_r", "spring", "spring_r", "summer", "summer_r", "tab10",
                       "tab10_r", "tab20",
                       "tab20_r", "tab20b", "tab20b_r", "tab20c", "tab20c_r", "terrain", "terrain_r", "twilight",
                       "twilight_r",
                       "twilight_shifted", "twilight_shifted_r", "viridis", "viridis_r", "winter", "winter_r"]

    print('Bitte geben Sie den Namen der gewünschten Colormap an.')
    print('Beispiele: gist_gray, viridis, plasma, magma, autumn')
    print('Weitere Colormaps sind zu finden unter: https://matplotlib.org/stable/tutorials/colors/colormaps.html')
    cmap_name = input('Eingabe: ')

    while cmap_name not in available_cmaps:
        print('Die eingegebene Colormap existiert nicht oder ist nicht erlaubt.')
        print('Verfügbare Farbkarten:', ', '.join(available_cmaps))
        print('\n')
        cmap_name = input('Eingabe: ')

    # Festlegung der Visualisierungs-Attribute
    for file_path in file_list:

        raster = rio.open(file_path)
        data = raster.read()
        min_per = np.nanpercentile(data, 2)
        max_per = np.nanpercentile(data, 98)
        fig, ax = plt.subplots(figsize=(10, 8))
        title = os.path.basename(file_path)[:-4]
        cmap = plt.get_cmap(cmap_name)
        colb = plt.colorbar(cm.ScalarMappable(norm=colors.Normalize(vmin=min_per, vmax=max_per), cmap=cmap))

        ax.set_xlabel('Östliche Ausrichtung')
        ax.set_ylabel('Nördliche Ausrichtung')
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
        colb.set_label('Rückstreuung in dB')

        # Visualisierung und Speichern
        show(raster, transform=raster.transform, vmin=min_per, vmax=max_per, ax=ax, cmap=cmap, title=title)
        plt.tight_layout()
        plt.savefig(os.path.join(path, f'{title}.pdf'), bbox_inches='tight')
        plt.show()

    file_list.clear()
