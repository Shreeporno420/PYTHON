import pygame
import random,sys
from pygame.locals import *

#Global Varables
FPS = 32
SCREEN_WIDTH= 289
SCREEN_HEIGHT= 511
SCREE = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
GROUND_Y= SCREEN_HEIGHT * 0.8
GAME_SPRITE={}
GAME_SOUND={}
PLAYER='gallery/sprites/bird.png'
BACKGROUND='gallery/sprites/background.png'
PIPE='gallery/sprites/pipe.png'

def welcomeScreen():
    PlayerX= int(SCREEN_WIDTH/5) 
    PlayerY= int((SCREEN_HEIGHT-GAME_SPRITE['player'].get_height())/2)
    messeageX= int((SCREEN_WIDTH-GAME_SPRITE['message'].get_width())/2)
    messeageY= int(SCREEN_HEIGHT*0.13)
    baseX= 0 
    while True:
        for event in pygame.event.get():
            #For close the game
            if event .type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            
            else:
                SCREE.blit(GAME_SPRITE['background'], (0,0))
                SCREE.blit(GAME_SPRITE['player'], (PlayerX,PlayerY))
                SCREE.blit(GAME_SPRITE['message'], (messeageX,messeageY))
                SCREE.blit(GAME_SPRITE['base'], (baseX,GROUND_Y))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score=0
    playerx=int(SCREEN_WIDTH/5)
    playery=int(SCREEN_HEIGHT/2)
    basex=0
    
    #Creating Pipes
    newPipe1= getRandomPipe()
    newPipe2 = getRandomPipe()

    #My list of upper pipe
    upperPipes=[
        {"x": SCREEN_WIDTH+200, "y":newPipe1[0]['y']},
        {"x": SCREEN_WIDTH+200+(SCREEN_WIDTH/2), "y":newPipe1[0]['y']}
    ]
    #My list of lower pipe
    lowerPipes=[
        {"x": SCREEN_WIDTH+200, "y":newPipe2[1]['y']},
        {"x": SCREEN_WIDTH+200+(SCREEN_WIDTH/2), "y":newPipe2[1]['y']}
    ]

    pipeVelX= -4

    #Player Velocity Variable
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playerVelY > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUND['wing'].play()

        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        if crashTest:
            return

        #Check For Score
        playerMidPos = playerx + GAME_SPRITE['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe["x"] + GAME_SPRITE['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                print(f"Your Score {score}")
                GAME_SOUND['point'].play()
 
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITE['player'].get_height()
        playery = playery + min(playerVelY, GROUND_Y - playery - playerHeight)

        for upperPipe , lowerpipe in zip(upperPipes, lowerPipes):
            upperPipe["x"] += pipeVelX
            lowerpipe["x"] += pipeVelX

        if 0<upperPipes[0]['x']<5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        #Remove pipe
        if upperPipes[0]['x'] < -GAME_SPRITE['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0) 

        #Bliting Sprite
        SCREE.blit(GAME_SPRITE['background'], (0,0))

        #Pipe Bliting
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            SCREE.blit(GAME_SPRITE['pipe'][0], (upperPipe['x'] , upperPipe['y']))
            SCREE.blit(GAME_SPRITE['pipe'][1], (lowerPipe['x'] , lowerPipe['y']))

        SCREE.blit(GAME_SPRITE['base'], (basex,GROUND_Y))
        SCREE.blit(GAME_SPRITE['player'], (playerx, playery))
        myDigit = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigit:
            width += GAME_SPRITE['numbers'][digit].get_width()

        Xoffset= (SCREEN_WIDTH - width)/2

        for digit in myDigit:
            SCREE.blit(GAME_SPRITE['numbers'][digit], (Xoffset, SCREEN_HEIGHT*0.12))
            Xoffset += GAME_SPRITE['numbers'][digit].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUND_Y -25 or playery < 0:
        GAME_SOUND['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITE['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITE['pipe'][0].get_width()):
            GAME_SOUND['hit'].play()
            return True

    for pipe in lowerPipes:
        pipeHeight = GAME_SPRITE['pipe'][0].get_height()
        if(playery + GAME_SPRITE['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITE['pipe'][0].get_width():
            GAME_SOUND['hit'].play()
            return True

    return False

def getRandomPipe():
    #For genarate pipe in random position
    pipeHeight = GAME_SPRITE['pipe'][0].get_height()
    offset = SCREEN_HEIGHT/3
    y2 = offset + random.randrange(0, int(SCREEN_HEIGHT - GAME_SPRITE['base'].get_height()  - 1.2 *offset))
    pipeX= SCREEN_WIDTH + 10
    y1= pipeHeight - y2 + offset
    pipe=[
        {"x":pipeX, "y":-y1}, #Upper pipe
        {"x":pipeX, "y":y2}  #Lower pipe
    ]
    return pipe

if __name__== "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird")
    GAME_SPRITE['numbers'] = ( 
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    GAME_SPRITE['message']=pygame.image.load("gallery/sprites/message.png").convert_alpha()
    GAME_SPRITE['base']=pygame.image.load("gallery/sprites/base.png").convert_alpha()
    GAME_SPRITE['pipe']=(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )
    GAME_SPRITE['background']=pygame.image.load(BACKGROUND).convert()
    GAME_SPRITE['player']=pygame.image.load(PLAYER).convert_alpha()
    
    GAME_SOUND['die']= pygame.mixer.Sound("gallery/audio/die.wav")
    GAME_SOUND['hit']= pygame.mixer.Sound("gallery/audio/hit.wav")
    GAME_SOUND['point']= pygame.mixer.Sound("gallery/audio/point.wav")
    GAME_SOUND['swoosh']= pygame.mixer.Sound("gallery/audio/swoosh.wav")
    GAME_SOUND['wing']= pygame.mixer.Sound("gallery/audio/wing.wav")

    while True:
        welcomeScreen()
        mainGame()
