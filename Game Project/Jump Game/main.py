import pygame
import random
import os

from pygame.sprite import Group
pygame.init()

#Game window
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#Creating game window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(" Endless Vertical Platformer")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

#Game Variables
SCROLL_TRESH = 200
GRAVITY = 1
MAX_PLATFORM = 10
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0 

if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        high_score = int(file.read())
else:
    high_score = 0

#define colors
WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
PANEL = (153, 217, 234)

#define font
font_small = pygame.font.SysFont('Lucida Sans', 20)
font_big = pygame.font.SysFont('Lucida Sans', 24)

#Function for draw pannel
def draw_panel():
    pygame.draw.rect(SCREEN, PANEL, (0, 0, SCREEN_WIDTH, 30))
    pygame.draw.line(SCREEN, WHITE, (0,30), (SCREEN_WIDTH, 30) , 2)
    draw_text('SCORE: '+str(score), font_small, WHITE, 0, 0)

# load images
jumpy_image = pygame.image.load('assets/jump.png').convert_alpha()
bg_image = pygame.image.load('assets/bg.png').convert_alpha()
platform_image = pygame.image.load('assets/wood.png').convert_alpha()

# show text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x,y))

#fuction for BG
def draw_bg(bg_scroll):
    SCREEN.blit(bg_image, (0,0 + bg_scroll))
    SCREEN.blit(bg_image, (0,-600 + bg_scroll))

# player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(jumpy_image, (45,45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = (x,y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        # reset Variables
        scroll = 0
        dx = 0
        dy = 0

        #Process Keypress
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10 
            self.flip = True
        if key[pygame.K_d]:
            dx = 10
            self.flip = False
        
        #GAVITY
        self.vel_y += GRAVITY
        dy += self.vel_y

        # player doesn,t go off the screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right +dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        #check collision with platform
        for platform in platform_group:
            # collision in the Y 
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20                       

        if self.rect.top <= SCROLL_TRESH:
            if self.vel_y < 0:
                scroll = -dy

        #update rectangel position
        self.rect.x += dx
        self.rect.y += dy + scroll
        return scroll

    def draw(self):
        SCREEN.blit(pygame.transform.flip(self.image, self.flip, False) , (self.rect.x - 12, self.rect.y - 5))
        pygame.draw.rect(SCREEN, WHITE, self.rect, 2)

# platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, moving):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.moving = moving
        self.move_counter = random.randint(0, 50)
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(1,2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

    def update(self, scroll):
        #Moving platform
        if self.moving == True:
            self.move_counter += 1 
            self.rect.x += self.direction * self.speed

        #Change platform direction
        if self.direction >=100 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1
            self.move_counter = 0

        #Update platform vertical position
        self.rect.y += scroll

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

jumpy = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT - 150)

# Creating sprite groups
platform_group = pygame.sprite.Group()

#create starting platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
platform_group.add(platform)

run = True
while run:
    clock.tick(FPS)

    if game_over == False:
        scroll = jumpy.move()

        # bliting bg
        bg_scroll += scroll
        if bg_scroll >= 600:
            bg_scroll = 0 
        draw_bg(bg_scroll)

        #genarate platforms
        if len(platform_group) < MAX_PLATFORM:
            p_w = random.randint(40,60)
            p_x = random.randint(0, SCREEN_WIDTH - p_w)
            p_y = platform.rect.y - random.randint(80, 120)
            p_type =random.randint(1, 2)
            if p_type == 1 and score > 450:
                p_moving = True
            else:
                p_moving = False

            platform = Platform(p_x, p_y, p_w, p_moving)
            platform_group.add(platform)

        #Update platforms
        platform_group.update(scroll)

        #Update Score
        if scroll > 0:
            score += scroll

        #line of High Score
        pygame.draw.line(SCREEN, WHITE, (0, score - high_score + SCROLL_TRESH), (SCREEN_WIDTH, score - high_score + SCROLL_TRESH), 3)
        draw_text('HIGH SCORE', font_small, WHITE, SCREEN_WIDTH - 130, score - high_score + SCROLL_TRESH)

        #Sprite bliting
        platform_group.draw(SCREEN)
        jumpy.draw()

        #draw panel
        draw_panel()

        #game over
        if jumpy.rect.top > SCREEN_HEIGHT:
            game_over = True 

    else:
        if fade_counter < SCREEN_WIDTH:
            fade_counter += 5
            for y in range(0, 6, 2):
                pygame.draw.rect(SCREEN, BLACK, (0, y * 100, fade_counter, 100))
                pygame.draw.rect(SCREEN, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1)* 100, SCREEN_WIDTH, 100))

        else:
            draw_text("GAME OVER!", font_big, WHITE, 130, 200)
            draw_text("SCORE: "+str(score), font_big, WHITE, 130, 250)
            draw_text("PRESS SPACE TO PLAY AGAIN", font_big, WHITE, 40, 300)

            #update High Score
            if score > high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                #reset variables
                game_over = False
                score = 0
                scroll = 0
                fade_counter = 0
                #resposition Player
                jumpy.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT - 150)
                #reset platforms
                platform_group.empty()
                #create starting platform
                platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
                platform_group.add(platform)

    # close window 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #update High Score
            if score > high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))
            run = False
    
    # Update display
    pygame.display.update()
pygame.quit()