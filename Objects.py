import pygame
import math
import random

def graus(x,vel,angulo):
    while x<0:
        x=360+x

    angulo=(float(x)+angulo)*(float(vel)/90)
    while angulo>4*vel:
        angulo=angulo-4*vel

    return angulo

def giroscope(x,grau):
    vel=3
    angulo=graus(x,vel,grau)
    if angulo==vel:
        x=0
        return x,angulo*-1
    if angulo==2*vel:
        angulo=0
        x=vel*-1
        return x,angulo
    if angulo==3*vel:
        angulo=vel*-1
        x=0
        return x,angulo*-1
    if angulo==4*vel:
        angulo=0
        x=vel
        return x,angulo
    if angulo==0:
        x=vel
        angulo=0
        return x,angulo
    if angulo>0*vel and angulo<vel:
        x=vel-angulo
        return x,angulo*-1
    if angulo>1*vel and angulo<2*vel:
        x=(vel-angulo)
        angulo=(vel+x)
        return x,angulo*-1
    if angulo>2*vel and angulo<3*vel:
        angulo=(angulo-2*vel)*-1
        x=(vel+angulo)*-1
        return x,angulo*-1
    if angulo>3*vel and angulo<4*vel:
        angulo=(angulo-3*vel)*-1
        x=(vel+angulo)
        return x,angulo*-1
def bordaUP(object):
    if object.position[1]<=0:
        return True
    else:
        return False
def bordaLeft(object):
    if object.position[0]<=0:
        return True
    else:
        return False
def bordaRight(object):
    if object.position[0]+object.size[0]>=800:
        return True
    else:
        return False
def bordaDown(object):
    if object.position[1]>=600:
        return True
    else:
        return False
class mousedefault():
    position=None
    keys=None
    size=(1,1)
    visibilit=True
    def update(self,screen):
        self.position=pygame.mouse.get_pos()
        self.keys=pygame.mouse.get_pressed()
        screen.fill(0)

def colisor(object1,object2):
    class x(object):
       x=None
       y=None
       y2=None
       x2=None
    class y(object):
        x=None
        y=None
        x2=None
        y2=None
    x.x=object1.position[0]
    x.y=object1.position[1]
    x.x2=object1.size[0]
    x.y2=object1.size[1]
    y.x=object2.position[0]
    y.y=object2.position[1]
    y.x2=object2.size[0]
    y.y2=object2.size[1]
    X=False
    Y=False
    if object1.visibilit and object2.visibilit:
        if (x.x<y.x+y.x2 and x.x+x.x2 >y.x):
            X=True
        if (y.x<x.x+x.x2 and y.x+y.x2 >x.x):
            X=True
        if (x.y+x.y2>y.y and x.y<y.y+y.y2):
            Y=True
        if (y.y+y.y2>x.y and y.y<x.y+x.y2):
            Y=True
        if X==True and Y==True:
            return True
        else: return False
    else: return False
class Player:
    """docstring for Player"""
    def __init__(self, image,size,position):
        self.image = pygame.image.load(image)
        self.size=size
        self.position=position
        self.direction=90
        self.passo=3
        self.visibilit=True
    def andar(self,passos):
        x=self.position[0]+(passos*self.passo)
        self.position=(x,self.position[1])

class Ball:
    """docstring for Player"""
    def __init__(self, image,size,position):
        self.image = pygame.image.load(image)
        self.size=size
        self.position=position
        self.direction=0
        self.visibilit=True
        self.velocidade=10
        self.forca=10
    def girar(self,angulo):
        self.direction=self.direction+angulo
        if self.direction<0:
            self.direction=360+self.direction
        if self.direction>=360:
            self.direction=self.direction-360
    def andar(self,passos):
        x=self.position[0]+passos*giroscope(0,self.direction)[0]
        y=self.position[1]+passos*giroscope(0,self.direction)[1]
        self.position=(x,y)
    def move(self):
        self.velocidade=(self.velocidade+self.forca)/2
        self.position= self.position[0] + math.sin(self.direction) * self.velocidade, self.position[1] - math.cos(self.direction) * self.velocidade
        self.forca=self.velocidade


class Block():
    """docstring for Block"""
    def __init__(self,image,size,position,tipe,resistence):
        self.image =pygame.image.load(image)
        self.size=size
        self.position=position
        self.visibilit=True
        self.tipe=tipe
        self.resistence=int(resistence)
        self.original=int(resistence)
    def destroi(self,status,speciais,screen,ball,player,life,score):
        self.resistence=self.resistence-1
        if self.resistence==0:
            self.visibilit=False
            y=self.tipe*5
            Score.score=Score.score+y
            print(Score.score)
            if str(self.tipe)=='6':
                a=random.randint(1,4)
                speciais[a].position=self.position
                speciais[a].visibilit=True
                speciais[a].runing=True
                speciais[a].run(screen,ball,player,life,score)
                status='special'

                print "true"
                return True

class Score():
    score=0





def blit(screen,Object):
    if Object.visibilit:
        screen.blit(Object.image,(Object.position))

class buttonExit():
    def __init__(self,image,position,nome):
        self.image=pygame.image.load(image)
        self.position=position
        self.size=(198,62)
        self.visibilit=True
        self.nome=nome

    def destroi(self):
        self.visibilit=False
    def action(self,screen,mouse):
        blit(screen,self)
        if colisor(mouse,self):
            self.image=pygame.image.load('image/'+self.nome+'2.png')
            if mouse.keys[0]:
                pygame.quit()
        else:
            self.image=pygame.image.load('image/'+self.nome+'.png')

class button():
    def __init__(self,image,position,nome):
        self.image=pygame.image.load(image)
        self.position=position
        self.size=(198,62)
        self.visibilit=True
        self.nome=nome

    def destroi(self):
        self.visibilit=False
    def action(self,screen,mouse,fase,player,ball,screen_size,FPS,clock,score,ask):
        blit(screen,self)
        if colisor(mouse,self):
            self.image=pygame.image.load('image/'+self.nome+'2.png')
            if mouse.keys[0]:
                fase.runing=True
                fase.run(player,ball,screen_size,FPS,clock,score,ask)
        else:
            self.image=pygame.image.load('image/'+self.nome+'.png')

class buttonVoltar():
    def __init__(self,image,position,nome):
        self.image=pygame.image.load(image)
        self.position=position
        self.size=(198,62)
        self.visibilit=True
        self.nome=nome

    def destroi(self):
        self.visibilit=False
    def action(self,screen,mouse,menu,ask):
        blit(screen,self)
        if colisor(mouse,self):
            self.image=pygame.image.load('image/'+self.nome+'2.png')
            if mouse.keys[0]:
                menu.run(ask)
        else:
            self.image=pygame.image.load('image/'+self.nome+'.png')

class special():
    """docstring for Block"""
    def __init__(self,bonus,position):
        self.image =pygame.image.load('image/bonus/'+bonus+".gif")
        self.image2 =pygame.image.load('image/bonus/'+bonus+"2.gif")
        self.size=(40,21)
        self.position=position
        self.visibilit=False
        self.runing=False
        self.tipe=bonus
    def run(self,screen,ball,player,life,score):
        if self.tipe=='slow':
            ball.velocidade=6
        if self.tipe=="big":
            player.image=pygame.image.load("image/playerBig.gif")
            player.size=(150,9)
        if self.tipe=="life":
            life+=1
        if self.tipe=="xp":
            Score.score=int(Score.score+(Score.score/3))
def especialblit(screen,speciais):
    for key in speciais:
        if speciais[key].visibilit==True:
            screen.blit((speciais[key].image),(speciais[key].position))

