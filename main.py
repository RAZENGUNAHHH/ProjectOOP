import pygame
from fighter import Fighter
pygame.init()

#  create game window


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

YELLOW = (255,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
#   intial Screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Figther')

#   set framerate
clock = pygame.time.Clock()
FPS = 60

# load bg_image and  giving transparent Image
#  convert_alpha() set transparent image
bg_image = pygame.image.load('assets/images/background/background.jpg').convert_alpha()


# 
def draw_health_bar(health,x,y):
    ratio = health / 100
    pygame.draw.rect(screen , WHITE ,(x -2,y-2,404, 34))
    pygame.draw.rect(screen , RED ,(x,y,400,30))
    pygame.draw.rect(screen , YELLOW ,(x,y,400 * ratio , 30))

# define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72,56]
WARRIOR_DATA = [WARRIOR_SIZE , WARRIOR_SCALE , WARRIOR_OFFSET]


WIZARD_SIZE = 250
WIZARD_SCALE = 3
WARRIOR_OFFSET = [112,107]
WIZARD_DATA = [WIZARD_SIZE,WIZARD_SCALE , WARRIOR_OFFSET] 

# load spritesheets
warrior_sheet = pygame.image.load('assets/images/warrior/Sprites/warrior.png').convert_alpha()
wizard_sheet = pygame.image.load('assets/images/wizard/Sprites/wizard.png').convert_alpha()

#  define number of steps in each animated
WARRIOR_ANIMATION_STEPS  = [10,8,1,7,7,3,7]
WIZARD_ANIMATION_STEPS  = [8,8,1,8,8,3,7]


#  function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg , (0,0))


# created Figther player
Fighter_1 = Fighter(1,200,310 ,False ,WARRIOR_DATA , warrior_sheet , WARRIOR_ANIMATION_STEPS)
Fighter_2 = Fighter(2,700,310 , True ,WIZARD_DATA , wizard_sheet ,WIZARD_ANIMATION_STEPS)


# game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    draw_bg()

    #  show health bar for each player
    draw_health_bar(Fighter_1.health , 20,20)
    draw_health_bar(Fighter_2.health , 580,20)

    # move fighters
    Fighter_1.move(SCREEN_WIDTH , SCREEN_HEIGHT , screen , Fighter_2)
    Fighter_2.move(SCREEN_WIDTH , SCREEN_HEIGHT , screen , Fighter_1)
    # update frame_index
    Fighter_1.update()
    Fighter_2.update()
    # Fighter_2.move()
    #  draw fighters
    Fighter_1.draw(screen)
    Fighter_2.draw(screen)

    # event quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # update display
    pygame.display.update()

# exit pygame
pygame.quit()