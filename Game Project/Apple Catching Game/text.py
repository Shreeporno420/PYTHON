import pygame
import random
import colorama
from colorama import *

colorama.init()

screen_size = [360, 600]
score = 0
screen = pygame.display.set_mode(screen_size) 

backgound = pygame.image.load("forest.png")
player = pygame.image.load("bowl.svg")
chicken = pygame.image.load("apple.svg")

# define color
green = Fore.GREEN
red = Fore.RED 

def random_offset():
    return -1 * random.randint(100, 2000)

chicken_y = [random_offset(), random_offset(), random_offset()]
user_x = 150

def chicken_position(idx):
    if chicken_y[idx] > 600:
        chicken_y[idx] = random_offset() 
    else:
        chicken_y[idx] = chicken_y[idx] + 5

keep_alive = True
clock = pygame.time.Clock()
while keep_alive:
    # Event controler
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 303:
        user_x += 10
    elif keys[pygame.K_LEFT] and user_x > 0:
        user_x -= 10
 
    chicken_position(0)
    chicken_position(1)
    chicken_position(2) 

    screen.blit(backgound, [0, 0]) 
    screen.blit(player, [user_x, 520]) 
    screen.blit(chicken, [0, chicken_y[0]])   
    screen.blit(chicken, [150, chicken_y[1]])
    screen.blit(chicken, [280, chicken_y[2]]) 

    if chicken_y[0] > 500 and user_x < 70  or chicken_y[2] > 500 and user_x < 220 or chicken_y[1] > 500 and user_x > 100 and user_x < 200:
        score += 1 
        print("Score:"+green+str(score))
        chicken_y = [random_offset(), random_offset(), random_offset()]

    else:
        if chicken_y[0] > screen_size[1] or chicken_y[1] > screen_size[1] or chicken_y[2] > screen_size[1]:
            print(red+"Game Over")  
            keep_alive = False 

    pygame.display.update() 
    clock.tick(60)
pygame.quit()