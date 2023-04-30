import pygame
from main import map_set
from map_show import show
import random


cities_pack = ['Москва', 'Минск', 'Cтарый Петергоф']
city = cities_pack[random.randint(0, 3)]
map = map_set(city)
if not map:
    print('ERROR')
    exit()
n = 1
cn = 1
fps = 10
pygame.init()
screen = pygame.display.set_mode((600, 450))
clock = pygame.time.Clock()
for event in pygame.event.get():
    if event.type == pygame.QUIT: pygame.quit()
    else:
        n += 5
        show(n, map, screen)
        clock.tick(fps)
