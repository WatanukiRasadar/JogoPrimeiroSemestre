import pygame,os,sys,math
from Objects import *
from pygame.locals import *
from random import randint
from BlockFone import *
pygame.init()
screen_size=800,600
clock=pygame.time.Clock()
player=Player('image/player.PNG',(80,9),(400,565))
ball=Ball('image//ball40.PNG',(18,18),(400,300))
score=Score()
FPS=60
print(block1c1)
class __fase1__():
    blocks=[]

    
    def run(self,player,ball,screen_size,FPS,clock,Score):
        screen=pygame.display.set_mode(screen_size)
        A=0
        D=0
        ball.girar(0)
        life=3
        over=pygame.image.load('image/game over.png')
        status="inicio"
        space=False
        while 1:
            if status=="inicio":
                ball.position=player.position[0]+32,player.position[1]-20
            screen.fill(0)
            blit(screen,player)
            screen.blit(ball.image,(ball.position))
            for Block in self.blocks:
                if Block.visibilit==True:
                    screen.blit(Block.image,Block.position)
            for Block in self.blocks:
                if colisor(Block,ball):
                    Block.destroi()
                    ball.position = ball.position[0],(ball.position[1]+3)
                    ball.direction = math.pi - ball.direction
                    ball.forca=9
            if life <0:
                    screen.blit(over,(200,300))
                    status='died'
                    ball.position=player.position[0]+32,player.position[1]-20
            pygame.display.flip()
            if status!='died':
                ball.move()
            if bordaRight(ball):
                ball.position = (ball.position[0]-ball.size[0]), ball.position[1]
                ball.direction = - ball.direction
            if bordaLeft(ball):
                ball.position = (ball.position[0]+ball.size[0]),ball.position[1]
                ball.direction = - ball.direction
            if bordaDown(ball):
                life-=1
                status='inicio'
            if bordaUP(ball):
                ball.position = ball.position[0],(ball.position[1]+3)
                ball.direction = math.pi - ball.direction
            
                


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_a:
                    A=True
                  if event.key == pygame.K_d:
                    D=True
                  if event.key == pygame.K_w:
                    status="normal"
                  if event.key == pygame.K_SPACE:
                    space=True
                if event.type == pygame.KEYUP:
                  if event.key == pygame.K_a:
                    A=False
                  if event.key == pygame.K_d:
                    D=False
                  if event.key == pygame.K_SPACE:
                    space=False

                if event.type == pygame.QUIT:
                  pygame.quit()
                  exit(0)
            if A == True:
                player.andar(-2)
            if D == True:
                player.andar(2)
            if  colisor(player,ball):
                if space:
                    ball.forca=6
                    print "space"
                if D==True:
                    ball.position = ball.position[0],(player.position[1]-ball.size[1]-1)
                    ball.direction = math.pi - ball.direction+135
                    
                    if ball.direction >= 180:
                        ball.didirection=ball.direction-45
                if A==True:
                    ball.position = ball.position[0],(player.position[1]-ball.size[1]-1)
                    ball.direction = math.pi - ball.direction-45
                    print(ball.direction)
                    
                    if ball.direction >= 180:
                        ball.didirection=ball.direction-45
                else:
                    ball.position = ball.position[0],(player.position[1]-ball.size[1]-1)
                    ball.direction = math.pi - ball.direction
                    
                print('Barra')                
        
            clock.tick(FPS)
fase1=__fase1__()
fase1.blocks=[block4c1,block4c2,block4c3,block4c4,block4c5,block4c6,block4c7,block4c8,block4c9,block4c15,block3c1,block3c2,block3c3,block3c4,block3c5,block3c6,block3c7,block3c8,block3c9,block3c10,block3c11,block3c12,block3c13,block3c14,block3c15,block1c1,block1c2,block1c3,block1c4,block1c5,block1c6,block1c7,block1c8,block1c9,block1c10,block1c11,block1c12,block1c13,block1c14,block1c15,block2c1,block2c2,block2c3,block2c4,block2c5,block2c6,block2c7,block2c8,block2c9,block2c10,block2c11,block2c12,block2c13,block2c14,block2c15,block4c10,block4c11,block4c12,block4c13,block4c14,block4c15,]


fase1.run(player,ball,screen_size,FPS,clock,score)



