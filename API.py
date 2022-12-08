from zipfile import ZipFile  # Usei para descompactar
import requests  # Usei para receber o link da URL, fiz um input para receber mais de um link
import csv  # Usei para receber o arquivo csv e importar o conteúdo para um biblioteca e depois para uma lista
import json  # Usei para transformar o arquivo em json


# Baixando arquivo pelo url

def file_download(url, end):
    res = requests.get(url)

    with open(end, 'wb') as new_file:
        new_file.write(res.content)
        print(f'Arquivo salvo em {end}')


file_download('https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip',
              'jodi_gas_csv_beta.zip')


# Extrair arquivo zip
with ZipFile('jodi_gas_csv_beta.zip', 'r') as zip_object:
    zip_object.extractall('Zip')

# Pegando o nome do arquivo
nome_arquivo_csv = zip_object.namelist()


# Mexendo no arquivo csv para json

with open('nome_arquivo_csv[0]', 'r') as arquivo_csv:
    leitura = csv.reader(arquivo_csv)

    serial_id = {}
    data = {}
    pib = {}
    api = []

# Estou criando uma lista com o FLOW_BREAKDOWN para puxar com referência de id na procura por lista
    for csv in leitura:
        for c in leitura:
            csv[3] = []
            serial_id['FLOW_BREAKDOWN_id'] = c[3]
            serial_id['REF_AREA'] = csv[0]
            serial_id['ENERGY_PRODUCT'] = csv[2]
            serial_id['UNIT_MEASURE'] = csv[4]
            serial_id['ASSESSMENT_CODE'] = csv[6]
            data['TIME_PERIOD'] = csv[1]
            pib['OBS_VALUE'] = csv[5]
            csv[3].append(serial_id.copy())
            csv[3].append(data.copy())
            csv[3].append(pib.copy())
            api.append(csv[3])


# Transformando em JSON
with open(f'{new_jodi_gas_csv_beta.json}', 'w') as arquivo_csv:
    json.dump(api, arquivo_csv, indent=1)

print('FIM DO PROGRAMA')
