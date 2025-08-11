import pygame

pygame.init()
screen = pygame.display.set_mode((700,500))
c = pygame.display.set_caption('My first game screen')
done = False


while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()