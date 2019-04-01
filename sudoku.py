import random, os.path, sys

#import basic pygame modules
import pygame



pygame.init()


# text objects
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


#make buttons clickable and do shit
def start_game():
    pygame.display.blit()
    gameDisplay.fill(WHITE)
    pygame.display.flip()
    #text = font.render("Start game", True, WHITE)
    #dont delete this
    pygame.display.update()
    


    
def instructions_screen():
    gameDisplay.fill(RED)
    pygame.display.flip()
    pygame.display.update()
    #text = font.render("Start game", True, WHITE)
    #dont delete this
    pygame.display.update()
    
    
     
def quit_game():
    gameDisplay.fill(WHITE)
    #text = font.render("You quit", True, WHITE)
        #dont delete this
    gameDisplay.blit()
    
        

    
    
    
    
    

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (132,112,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 50)
gameDisplay = pygame.display.set_mode((800,600))
#gameDisplay.fill(WHITE)

carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
 
     # --- Game logic should go here
 
 # --- Drawing code should go here
 # First, clear the screen to white. 
        
 #The you can draw different shapes and lines or add text to your background stage.
        #pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
        #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
        #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
        pygame.draw.rect(gameDisplay, green,(150,450,100,50))
        pygame.draw.rect(gameDisplay, red,(550,450,100,50))

       # TextSurf, TextRect = text_objects("A bit Racey", 200)
        
        text = font.render("Welcome to Sudoku using Pygame", True, RED)
        #dont delete this
        gameDisplay.blit(text, [10, 10])
        
        # code to make buttons highlight
        mouse = pygame.mouse.get_pos()
       
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
        else:
            #play rect
            pygame.draw.rect(gameDisplay, green,(150,450,100,50))
            #instructions rect
            pygame.draw.rect(gameDisplay, red,(550,450,150,50))
            # quit rectangle
            pygame.draw.rect(gameDisplay, BLUE, (330, 450, 150, 50 ))
        
        #text that goes in play button reactangle
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Play", smallText)
        textRect.center = ( (150+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        #text that goes in the instructions rectangle
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Instructions", smallText)
        textRect.center = ( (575+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        #text that goes in the quit rectangle
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Quit", smallText)
        textRect.center = ( (350+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        #passing arguments to clickable button function
        # if any mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            if mx <= 200 and my <= 500:
                start_game()
            elif mx <= 500 and my<= 900: 
                quit_game()
            elif mx <= 900 and my <= 1200:
                instructions_screen()
        
        pygame.display.update()
        
         
         
         # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
         
         # --- Limit to 60 frames per second
        clock.tick(60)
         
#Once we have exited the main program loop we can stop the game engine
# do not indent this
pygame.quit()
                
       
            
                
                
             
          
        
       



    
