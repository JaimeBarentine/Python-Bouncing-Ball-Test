import pygame

# used for randomness of velocity
import random


# the ball image
ball = pygame.image.load('ballimage.gif')

pygame.display.set_caption("Watch as the balls collide")


# variables for the size of the screen
width = 600
height = 500
fps = 30

# colours for future reference
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



#initialize the display
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
#pygame.display.set_caption("My Game")

clock = pygame.time.Clock()



# create ball template to be cloned
class Test(pygame.sprite.Sprite):

    
    #initiation of object specifities
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        #self.image.fill(GREEN)
        self.image = ball
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        xVel = 5
        yVel = 5

# the velocity of the ball
    xVel = 5
    yVel = 5

# happens every frame
    def update(self):

        
        #always change x and y position by velocity respectively
        
        self.rect.x += self.xVel
        self.rect.y += self.yVel

        self.yVel += 1

        # this doesn't work in classes for some reason
        #if keys[pygame.K_q]:
         #   pygame.quit()

        # if ball hits the ground, set upward velocity to a random number from 15 to 25
        if self.rect.y > 400:
            
            self.yVel = -(random.randrange(15, 25))

        # when you hit the ceiling, have downward velocity
        if self.rect.y < 0:

            self.yVel = 5

        # turn around when hitting the edge of the screen
        if self.rect.x > (width - 100):
            self.rect.x = 499
            self.xVel = -(self.xVel)
        
        if self.rect.x < 0:
            self.rect.x = 1
            self.xVel = -(self.xVel)

        #check for collision
        for sprite in all_sprites:
            if sprite == self:
                continue
            if self.rect.colliderect(sprite.rect):
                #determine which direction ball should go based on point of collision
                if (self.rect.x > (sprite.rect.x + 50) or self.rect.x < (sprite.rect.x - 50)):
                    if self.rect.x > sprite.rect.x:
                        self.xVel = random.randrange(5, 15)
                    elif self.rect.x < sprite.rect.x:
                        self.xVel = -(random.randrange(5, 15))

                if (self.rect.y > (sprite.rect.x + 50) or self.rect.y < (sprite.rect.x - 50)):
                    if self.rect.y > sprite.rect.y:
                        self.yVel = random.randrange(5, 15)
                    elif self.rect.y < sprite.rect.y:
                        self.yVel = -(random.randrange(5, 15))
        



# define all sprites to be rendered and put them in a group
all_sprites = pygame.sprite.Group()
test = Test()
test2 = Test()
test3 = Test()
test4 = Test()
all_sprites.add(test)


# timer for spawning multiple balls over time
timer = 0


running = True
while running:

    
    
    #keeps loop running at the right speed
    clock.tick(fps)

    # spawns the balls in over the course of 90 game frames
    if timer < 90:
        timer += 1
    if timer == 30:
        all_sprites.add(test2)

    if timer == 60:
        all_sprites.add(test3)

    if timer == 90:
        all_sprites.add(test4)
        timer = 91

    #process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False


    # update
    all_sprites.update()
    
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    # flip the display
    pygame.display.flip()
    
            
pygame.quit()
