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
playerx_change = 0
enemyx = []
enemyy = []
enemy_velocityx = []
enemy_velocityy = []
num_of_enemies = 6
background = pygame.image.load("background.png")
for i in range(num_of_enemies):
    enemy_images.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(0, 536))
    enemy_velocityx.append(random.randint(0, 4))
    enemy_velocityy.append(random.randint(0, 40))
    
bullet_image = pygame.image.load("bullet.png")
bulletx = 0
bullety = playery
bullet_change = 25
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10
over_font = pygame.font.Font("freesansbold.ttf", 64)
win_font = pygame.font.Font("freesansbold.ttf", 64)
def show_score(x,y):
    score_display = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_display, (x,y))

def win_text():
    win_text = win_font.render("YOU WIN" , True, (255,255,255))
    screen.blit(win_text, (200, 250))



def game_over_text():
    over_text = over_font.render("GAME OVER " , True, (255,255,255))
    screen.blit(over_text, (200, 250))


        
def player(x, y):
    screen.blit(player_image, (x, y))
    
def enemy(x, y, i):
    screen.blit(enemy_images[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))
def is_collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(((enemyx - bulletx) ** 2) + ((enemyy - bullety) ** 2))
    return distance < 27

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx -= 5
            if event.key == pygame.K_LEFT:
                playerx += 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerx
                fire_bullet(bulletx, bullety)
        
            
        playerx = playerx
        
        
        if playerx <= 0:
            playerx = 0 
            
        elif playerx >= 800:
            playerx = 800  
                
        for i in range((num_of_enemies)):
            if enemyy[i] > (playery - 40): 
                for j in range(num_of_enemies):
                    enemyy[j] = 2000
                game_over_text()
                break
            
            enemyx[i] += enemy_velocityx[i]
            if enemyx[i] <= 0 or enemyx[i] >= 736: # bounce back
                enemy_velocityx[i] *= -1
                enemyy[i] += enemy_velocityy[i]
                
            if is_collision(enemyx[i], enemyy[i], bulletx, bullety):
                bullety = playery
                bullet_state = "ready"
                score += 5
                
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(50, 150)
             
            enemy(enemyx[i], enemyy[i], i)
        
        if bullety <= 0:
            bullety = playery
            bullet_state = "ready"
        
        elif bullet_state == "fire":
            fire_bullet(bulletx, bullety)
            while bullety > 0:
              bullety -= bullet_change
            
        player(playerx, playery)
        show_score(text_x, text_y)
        pygame.display.update()