import random
import requests

map_types = ['map', 'sat']

def map_set(toponym_to_find):
    geocod_server = "http://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocod_server, params=params)
    if not response:
        print('ERROR')
        return
    json_response = response.json()
    top = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    coord = top["Point"]["pos"]
    point = list(coord.split())
    search_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
    address = ','.join(point)
    search_params = {
        "apikey": api_key,
        "text": "достопримечательность",
        "lang": "ru_RU",
        "ll": address,
        "type": "biz"}
    response = requests.get(search_server, params=search_params)
    json_response = response.json()
    map_params = []
    for i in range(4):
        map_type = map_types[random.randint(0, 1)]
        point_1 = json_response["features"][i]["geometry"]["coordinates"]
        point_2 = "{0},{1}".format(point_1[0], point_1[1])
        d = "0.01"
        map_params.append({
            "ll": point_2,
            "spn": ",".join([d, d]),
            "l": map_type})
    return map_params