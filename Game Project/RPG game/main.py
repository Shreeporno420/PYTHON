import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Game Window Height, Width
bottom_panel = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + bottom_panel

# Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Battle Game")

# load Images
background_img = pygame.image.load("img/Background/background.png").convert_alpha()
panel_img = pygame.image.load("img/Icons/panel.png").convert_alpha()

# Function Drawing images in Screen
def draw_bg():
    screen.blit(background_img, (0,0))

def draw_panel():
    screen.blit(panel_img, (0, SCREEN_HEIGHT - bottom_panel))

#Fighter Class
class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.alive = True
        self.frame_index = 0 
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        #Animation
        # Load Images: Idle
        temp_list = []
        self.animation_list = []
        for i in range(8):
            img = pygame.image.load(f'img/{self.name}/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)

        # Load Images: Attack
        temp_list = []
        self.animation_list = []
        for i in range(8):
            img = pygame.image.load(f'img/{self.name}/Attack/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)

        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100
        #handle animation
        self.image = self.animation_list[self.action][self.frame_index]

        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        # Reset Animation 
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0 

    def draw(self):
        screen.blit(self.image, self.rect)

Knight = Fighter(200, 260, 'Knight', 30, 10, 3)
Bandit1 = Fighter(550, 270, 'Bandit', 20, 6, 1)
Bandit2 = Fighter(700, 270, 'Bandit', 20, 6, 1)

Bandit_list = []
Bandit_list.append(Bandit1)
Bandit_list.append(Bandit2)

run = True
while run:
    clock.tick(FPS)

    # Bliting Images
    draw_bg()
    draw_panel()

    #Draw fighter
    Knight.update() 
    Knight.draw()
    for bandit in Bandit_list:
        bandit.update()  
        bandit.draw()

    for enent in pygame.event.get():
        if enent.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()