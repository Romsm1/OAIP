import json


with open('test.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    country = \
        data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData'][
            'Address']['Components'][0]['name']
    cords = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

    print(country, cords)
