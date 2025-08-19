import math
import random
import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader Project")
pygame.display.set_icon(pygame.image.load("ufo.png"))
player_image = pygame.image.load("player.png")
enemy_images = []
playerx = 370
playery = 480
enemyx = []
enemyy = []
enemy_velocityx = []
enemy_velocityy = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_images.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0, 736))
    enemyx.append(random.randint(0, 536))
    enemy_velocityx.append(random.randint(0, 4))
    enemy_velocityy.append(random.randint(0, 40))
    
bullet_image = pygame.image.load("bullet.png")
bulletx = 0
bullety = playery
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10




