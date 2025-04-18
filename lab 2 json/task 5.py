import json

with open('test.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    address_info = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
        'GeocoderMetaData'][
        'Address']

    address_info['country_code'] = 'RUS'
    address_info['postal_code'] = '675004'
    address_info['formatted'] = 'БГПУ, ул. Ленина, 104'

with open('test.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    print('JSON-файл успешно обновлен!')
