#This ideas to write this code were got from:https://pythonprogramming.net/pygame-python-3-part-1-intro/
#this is a python program to play space invaders, we have 5 lifes to play,
#we can count the points we have, the alien's velocity increase while we have
#more points, if we colish with aliens we lose life and we cannot touch the boundaries
import pygame
import time
import random
from time import sleep
#starting pygame
pygame.init()

#window size
display_width = 800
display_height = 600

#color to be used
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#nave size
nave_width = 169
nave_height = 192

#alien's size
alien_width = 109
alien_height = 77

#bomb size
bomb_width = 162
bomb_height = 192

#shot size
shot_width = 39
shot_height = 52

#creating the display
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space invaders')
clock = pygame.time.Clock()

#loading the pictures
naveImag = pygame.image.load('nave.jpg')
alienImag = pygame.image.load('alien.png')
bombImag = pygame.image.load('bomb.jpg')
shotImag = pygame.image.load('shot.png')

#functions to draw the objects
def shot(x, y):
    gameDisplay.blit(shotImag,(x, y))

def alien(x1,y1):
    gameDisplay.blit(alienImag,(x1, y1))


def nave(x,y):
    gameDisplay.blit(naveImag,(x,y))

def bomb(x,y):
    gameDisplay.blit(bombImag,(x,y))

#function to count the points we get
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("scores: "+str(count), True, white)
    gameDisplay.blit(text,(0,0))

#function to count the lifes
def counter_life(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Lifes: "+str(count), True, white)
    gameDisplay.blit(text,(0,20))

#main loop
def game_loop():
    #nave coordinates
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    #alien coordinates
    x1 = random.randrange(0 + alien_width, display_width - alien_width)
    y1= 0
    alien_speed = 1

    #shot parameters
    shotx = x
    shoty = y
    shot_speed = -7

    #score counter
    counter = 0

    #life counter
    li_coun = 5

    #condition to keep the game
    gameExit = False

    while not gameExit:

        #we get the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

          #if we perform motion with the keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                #if event.key == pygame.K_UP:
                   #if the user push space the nave shoot to the alien

          #if we don't push the button the alien does not move
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
       #moving the images
        x += x_change
        #alien_velocity
        y1 += alien_speed
        shoty += shot_speed

       #gives color to the display
        gameDisplay.fill(black)
       #draw the objects
        nave(x,y)
        things_dodged(counter)
        counter_life(li_coun)
        alien(x1, y1)
        shot(shotx, shoty)

        #Adding boundarys, we cannot touch the height
        if x > display_width - nave_width or x < 0:
            li_coun -= 1
            x = 400


        #the shot will appear again and again
        if shoty < 0:
           shotx = x + (nave_width/2)
           shoty = y

        #if the alien cross the screen will appear again at the top
        if y1 > display_height:
           y1 = 0 - alien_height
           x1 = random.randrange(0 + alien_width, display_width - alien_width)


        #if the objects collide the game is over, the alien vs nave
        if y < y1 + alien_height:
            print('y crossover')

            if x > x1 and x < x1 + alien_width  or x + nave_width > x1 and x + nave_width < x1 + alien_width:
                print('x crossover')
                #drawing the explosion
                bomb(x1, y1)
                li_coun -= 1
                x = 400

       #if the shot collide with the alien, alien vs shot
        if y1 > shoty - shot_height:
            print('you shoot it')
            if shotx + (nave_width/2) > x1 and shotx < x1 + alien_width or shotx + shot_width > x1 and shotx + shot_width < x1 + alien_width:
               #drawing the explosion
               counter += 1     #increasing the points
               alien_speed += 1 #increasing the alien velocity
               shot_speed -= 1
               bomb(x1, y1)
               #drawing other alien
               y1 = 0 - alien_height
               x1 = random.randrange(0 + alien_width, display_width - alien_width)
        if li_coun < 1:
            gameExit = True

       #updating the display
        pygame.display.update()
        clock.tick(60) #fps


#calling the loop
game_loop()
pygame.quit()
quit()
