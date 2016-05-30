import pygame,os,sys
from Objects import *
from pygame.locals import *
from random import randint
pygame.init()
screen_size=800,600
clock=pygame.time.Clock()
player=Player('image\player.PNG',(80,9),(400,565))
ball=Ball('image\\ball40.PNG',(18,18),(400,300))
FPS=60
def __fase1__(player,ball,screen_size,FPS,clock):
    screen=pygame.display.set_mode(screen_size)
    A=0
    D=0
    ball.girar(90)
    while 1:
        screen.fill(0)
        blit(screen,player)
        screen.blit(ball.image,(ball.position))
        pygame.display.flip()
        ball.andar(1)
        if bordaRight(ball):
            ball.girar(180)
            print ball.direction
        if bordaLeft(ball):
            ball.girar(180)
            print ball.direction
        if bordaDown(ball):
            ball.girar(180)
            print ball.direction
        if bordaUP(ball):
            print ball.direction
            ball.girar(180)
            print ball.direction


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_a:
                A=True
              if event.key == pygame.K_d:
                D=True
            if event.type == pygame.KEYUP:
              if event.key == pygame.K_a:
                A=False
              if event.key == pygame.K_d:
                D=False

            if event.type == pygame.QUIT:
              pygame.quit()
              exit(0)
        if A == True:
            player.andar(-1)
        if D == True:
            player.andar(1)
        if  colisor(player,ball):  
            if D==True or A==True:
                ball.andar(-1)
                ball.girar(randint(135,225))
                print 'D'
            else:
                ball.andar(-1)
                ball.girar(180)
            print('Barra')                
    
        

__fase1__(player,ball,screen_size,FPS,clock)



