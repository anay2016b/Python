import pygame

pygame.init()

screen = pygame.display.set_mode((450,400))

pygame.display.set_caption("My robot")
done = False
while not done:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
         done = True
    pygame.draw.circle(screen, (0, 0,150), (237.5, 137.5), 7.5)
    pygame.draw.circle(screen, (0, 175, 255), (282.5, 137.5), 5)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(225, 160, 75, 7.5))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(175, 225, 50, 15))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(300, 225, 50, 15))
    pygame.draw.rect(screen, (255, 240, 0), pygame.Rect(225, 200, 75, 100))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(230, 300, 15, 60))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(275, 300, 15, 60))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(195, 360, 50, 15))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(275, 360, 50, 15))
    pygame.draw.circle(screen, (0, 255, 255), (260, 152.5), 50, 5)
   
    pygame.display.flip()
    