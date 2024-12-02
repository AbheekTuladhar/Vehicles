import pygame, sys                                   
pygame.init()                                        

WIDTH=800                                          
HEIGHT=WIDTH*0.8                                                   
size=(WIDTH,HEIGHT)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Vehicles")          


#Color Constants 

BLACK    = (0, 0, 0)
WHITE    = (255, 255, 255)
GREEN    = (0, 255, 0)
GRASS_GREEN = (124, 252, 128)
RED      = (255, 0, 0)
BLUE     = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 80, 0)
PURPLE = (128, 0, 128)
GRAY = (180, 180, 180)
SKYBLUE = (135, 206, 235)


#Converts the screen into a 38 by 24 grid
xu = WIDTH/38
yu = HEIGHT/24


#Program helper functions:
def drawDivider(x, y):
    pygame.draw.rect(surface, YELLOW, (x, y, 2*xu, yu))

def drawScene():
    #ROAD and DIVIDER
    pygame.draw.rect(surface, BLACK, (0, 12*yu, WIDTH, 9*xu), 0)
    drawDivider(1*xu, 15*yu)
    drawDivider(6*xu, 15*yu)
    drawDivider(11*xu, 15*yu)
    drawDivider(16*xu, 15*yu)
    drawDivider(21*xu, 15*yu)
    drawDivider(26*xu, 15*yu)
    drawDivider(31*xu, 15*yu)
    drawDivider(36*xu, 15*yu)

    #Vehicles
    drawCar(5*xu, 16.5*yu, 0.7, RED)
    drawCar(10*xu, 13*yu, 0.5, WHITE)
    drawTruck(15*xu, 16.5*yu, 0.8, PURPLE)
    drawTruck(20*xu, 13*yu, 0.7, GRAY)
    drawCar(25*xu, 16.5*yu, 0.7, GREEN)
    drawTruck(30*xu, 13*yu, 0.4, ORANGE)

    #SKY
    pygame.draw.rect(surface, SKYBLUE, [0, 0, WIDTH, HEIGHT/2.5])
    pygame.draw.ellipse(surface, YELLOW, [9*WIDTH/9.7, -yu, 5*xu, 5*xu], 0)


def drawCar(x, y, sf, color):
    Cw = WIDTH/6 * sf
    Ch = Cw/2
    Cxu = Cw/6
    Cyu = Ch/3
    points = [
        [x+(2*Cxu), y],
        [x+(4*Cxu), y],
        [x+(5*Cxu), y+Cyu],
        [x+(6*Cxu), y+Cyu],
        [x+(6*Cxu), y+(2*Cyu)],
        [x, y+(2*Cyu)],
        [x, y+Cyu], 
        [x+Cxu, y+Cyu]
    ]
    pygame.draw.polygon(surface, color, points, 0)
 
    # WHEELS
    pygame.draw.ellipse(surface, color, [x+Cxu, y+(2*Cyu), Cxu, Cxu], 0)
    pygame.draw.ellipse(surface, color, [x+(4*Cxu), y+(2*Cyu), Cxu, Cxu], 0)

def drawTruck(x, y, sf, color):
    Tw = WIDTH/6 * sf
    Th = Tw/2
    Txu = Tw/6
    Tyu = Th/3
    points = [
        [x, y],
        [x+(5*Txu), y],
        [x+(5*Txu), y+(0.5*Tyu)],
        [x+(5.7*Txu), y+(0.5*Tyu)],
        [x+(5.7*Txu), y+(2*Tyu)],
        [x, y+(2*Tyu)]
    ]
    pygame.draw.polygon(surface, color, points, 0)
 
    # WHEELS
    pygame.draw.ellipse(surface, color, [x+Txu, y+(2*Tyu), Txu, Txu], 0)
    pygame.draw.ellipse(surface, color, [x+(4*Txu), y+(2*Tyu), Txu, Txu], 0)


# -------- Main Program Loop -----------
def main():                                          
    while True:
        for event in pygame.event.get():             
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #end game
                pygame.quit()                          
                sys.exit()
        
        surface.fill(GRASS_GREEN)                             #set background color
        
        #drawing code goes here
        drawScene()
        
        
        
        pygame.display.update()                          #updates the screen-
        
#----------------------------------------------------------------            
main()                                                   #runs the game
