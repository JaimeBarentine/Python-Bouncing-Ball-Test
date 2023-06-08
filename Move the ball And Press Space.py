import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))


pygame.display.set_caption("Press The Space Bar For A Good Time")

d = {'moon' : 0, 'pressed' : 1}
moon : False
pressed : False


# variables for the coordinates of the ball
x = 50
y = 50
# variables for the size of the screen
width = 800
height = 600
#speed of movement
vel = 5
#background colour
black = (0,0,0)

#initialize the display
gameDisplay = pygame.display.set_mode((width,height))



ball = pygame.image.load('ballimage.gif')

run = True
while run:
    #erases the previous instances of the ball image by
    #filling the background with black
    gameDisplay.fill(black)
    
    #displays the ball
    gameDisplay.blit(ball, (x, y))
    
    if d['moon'] == False:
        pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    if keys[pygame.K_q]:
        pygame.quit()

    if x > 800:
        x = -99

    if x < -100:
        x = 799

    if y > 600:
        y = -99

    if y < -100:
        y = 599

    if keys[pygame.K_SPACE]:
        if d['pressed'] == False:
            d['pressed'] = True
            if d['moon'] == True:
                d['moon'] = False
            else:
                d['moon'] = True
    else:
        d['pressed'] = False
    
        

    #win.fill((0, 0, 0))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    
    pygame.display.update()
    

            
pygame.quit()






    
    
        



def leftDoor():
    d['currentRoom'] = "left"
    ##print("I'm in the left room.")

def middleDoor():
    d['currentRoom'] = "middle"
    ##print("I'm in the middle room.")

def rightDoor():
    d['currentRoom'] = "right"
    ##print("I'm in the right room.")



