# KML_to_Geojson

This project was conceived to meet a work demand, where it was necessary to convert a KML file into a GEOJSON and split this file.

It is a KML containing all cataloged favelas in Brazil.

KML_to_GEOJSON.py:
  The first challenge was to convert the KML to GEOJSON. The script I used for this extracts polygon data and locality IDs, creating geometry objects with the extracted coordinates. Additionally, through the locality IDs, it was possible to separate the favelas by locality.

Divide_GEOJSON.py:
  Then I needed to separate the favelas from a single file into several. For example, the favelas of Rio de Janeiro were placed in the "Rio de Janeiro.geojson" file. I created a script to separate them.

Remove_Character.py:
  During the division, I encountered a problem with special characters in the favela IDs, so I created a script to fix this.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Este projeto foi idealizado visando suprir uma demanda de trabalho, onde era necessario converter um arquivo KML em um GEOJSON e realizar a divisao desse arquivo.

Se trata de um kml contendo todas as favelas catalogadas do Brasil.

KML_to_GEOJSON.py:
	O primeiro desafio foi convertar o KML para GEOJSON, o script que usei para isso extrai dados de polígonos e IDs de localidades, criando objetos de geometria com as coordenadas extraídas.
	E tambem atravez dos ID's das localidades foi possivel saperar as favelas por localidade.

Divide_GEOJSON.py:
	Depois precisei separar as favelas de um arquivo unico para varios, por exemplo, as fevalas do Rio de Janeiro, ficaram no arquivo, "Rio de Janeiro.geojson", criei um script para separa-las.

Remove_Caracter.py:
	Durante a divisao, encontrei um problema com caracteres especiais nos ID's da favelas, entao criei um scritp para corrigir isso.
