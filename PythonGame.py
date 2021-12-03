#from turtle import *
#from random import randrange
import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#load images
sun_img = pygame.image.load('Website/sun.png')
bg_img = pygame.image.load('Website/sky.png')

run = True
while run:

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (-10,-10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()