import requests


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
    up_co = list(map(float, top["boundedBy"]["Envelope"]['upperCorner'].split()))
    low_co = list(map(float, top["boundedBy"]["Envelope"]['lowerCorner'].split()))
    points = [i for i in coord.split()]
    spn = [str(up_co[0] - low_co[0]), str(up_co[1] - low_co[1])]
    map_params = {
        "l": "map",
        "pt": "{0},pm2dgl".format(','.join(points)),
        "ll": ','.join(points),
        "spn": ','.join(spn)
    }
    return map_params
