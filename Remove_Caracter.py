'''

Este script percorre todas as pastas dentro do diretório especificado em input_dir,
verifica os arquivos GeoJSON em cada pasta e substitui todos os caracteres '/' por '-' dentro das propriedades 'id' de cada feature.

'''



import os
import json


def replace_slash_with_dash_in_geojson(geojson_file):
    with open(geojson_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Substitui os caracteres '/' por '-' nas propriedades 'id' de cada feature
    for feature in data['features']:
        properties = feature.get('properties', {})
        id_value = properties.get('id', None)
        if id_value is not None:
            properties['id'] = id_value.replace('/', '-')

    # Salva o arquivo GeoJSON com as substituições
    with open(geojson_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def main():
    input_dir = 'C:/Users/BSOC2/Desktop/Gabriel/Scripts/KML_Favela_2/Saida'  # Modifique esta linha com o caminho do diretório de entrada

    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith(".geojson"):
                geojson_file = os.path.join(root, filename)
                replace_slash_with_dash_in_geojson(geojson_file)
                print(f"Substituição concluída em '{filename}'.")


if __name__ == "__main__":
    main()
