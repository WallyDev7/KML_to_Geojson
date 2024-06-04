'''

O script percorre todas as pastas dentro de um diretório específico, ler os arquivos GeoJSON em cada pasta e, em seguida, dividir esses dados GeoJSON.
Cada pedaço dividido é salvo em um arquivo separado dentro de uma pasta 'Saida' correspondente, criada dentro da mesma pasta onde o arquivo original foi encontrado.
O processo de divisão é realizado com base em um campo 'id' presente em cada arquivo GeoJSON, e o tamanho dos pedaços pode ser ajustado conforme necessário.

'''



import os
import json


def divide_json(json_data, chunk_size):
    features = json_data['features']
    chunks = [features[i:i + chunk_size] for i in range(0, len(features), chunk_size)]
    divided_json = [{'type': 'FeatureCollection', 'features': chunk} for chunk in chunks]
    return divided_json

def get_name_value(feature):
    return feature['properties'].get('id', None)

def main():
    input_dir = 'C:/Users/BSOC2/Desktop/Gabriel/Scripts/KML_Favela_2/Saida'  # Modifique esta linha com o caminho do diretório de entrada
    chunk_size = 1  # ajuste o tamanho do chunk conforme necessário

    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith(".geojson"):
                geojson_file = os.path.join(root, filename)
                with open(geojson_file, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                divided_data = divide_json(data, chunk_size)

                output_dir = os.path.join(root, 'Favelas_Divididas')
                os.makedirs(output_dir, exist_ok=True)  # Garante que o diretório de saída exista

                for i, chunk in enumerate(divided_data):
                    name_value = get_name_value(chunk['features'][0])

                    if name_value is not None:
                        output_path = os.path.join(output_dir, f'{name_value}_{i + 1}.geojson')
                        with open(output_path, 'w', encoding='utf-8') as output_file:
                            json.dump(chunk, output_file, ensure_ascii=False, indent=2)
                    else:
                        print(f"Erro: Campo 'id' não encontrado no chunk {i + 1} do arquivo {filename}.")


if __name__ == "__main__":
    main()
