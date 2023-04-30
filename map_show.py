import pygame
import requests


def show(i, map_params, screen):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params[i % len(map_params)])
    if not response:
        print('Ошибка')
    map_image = 'map.png'
    with open(map_image, "wb") as f:
        f.write(response.content)
    screen.blit(pygame.image.load(map_image), (0, 0))
    pygame.display.flip()