'''

O script converte arquivos KML em arquivos GeoJSON, percorrendo todos os arquivos KML em um diretório de entrada, extraindo dados de polígonos e IDs de localidades,
criando objetos de geometria com as coordenadas extraídas, armazenando esses dados em um GeoDataFrame,
e finalmente salvando-os como arquivos GeoJSON em um diretório de saída especificado.

'''



import os
import geopandas as gpd
import xml.etree.ElementTree as ET
from shapely.geometry import Polygon


def kml_to_geojson(input_dir, output_dir):
    # Percorre todos os arquivos KML no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith(".kml"):
            kml_file = os.path.join(input_dir, filename)
            output_folder = os.path.join(output_dir, os.path.splitext(filename)[0])
            os.makedirs(output_folder, exist_ok=True)
            geojson_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".geojson")
            convert_single_kml_to_geojson(kml_file, geojson_file)


def convert_single_kml_to_geojson(kml_file, geojson_file):
    # Lê o arquivo KML usando a biblioteca padrão do Python
    tree = ET.parse(kml_file)
    root = tree.getroot()

    # Extrai os dados de polígonos do KML
    polygons = []
    ids = []  # Lista para armazenar os IDs
    namespace = "{http://www.opengis.net/kml/2.2}"
    for placemark in root.findall(".//{0}Placemark".format(namespace)):
        polygon = placemark.find(".//{0}Polygon".format(namespace))
        if polygon is not None:
            # Extrai o ID da localidade do Placemark
            name = placemark.find(".//{0}name".format(namespace)).text.strip()
            ids.append(name)

            coordinates = polygon.find(".//{0}coordinates".format(namespace)).text.strip()
            coords = [tuple(map(float, coord.split(",")))[:2] for coord in
                      coordinates.split()]  # Apenas latitude e longitude
            polygons.append(Polygon(coords))

    # Converte para GeoDataFrame
    gdf = gpd.GeoDataFrame({'geometry': polygons, 'id': ids})  # Adiciona o ID como uma coluna

    # Salva o GeoJSON
    gdf.to_file(geojson_file, driver='GeoJSON')


if __name__ == "__main__":
    input_dir = "C:/Users/BSOC2/Desktop/Gabriel/Scripts/KML_Favela_2/Favelas"  # Substitua pelo caminho da pasta contendo os arquivos KML
    output_dir = "C:/Users/BSOC2/Desktop/Gabriel/Scripts/KML_Favela_2/Saida"  # Substitua pelo caminho da pasta onde deseja salvar os arquivos GeoJSON
    kml_to_geojson(input_dir, output_dir)
    print("Conversão concluída com sucesso!")
