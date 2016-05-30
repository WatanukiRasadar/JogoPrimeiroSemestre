import pygame

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
    if object.position[0]>=800:
        return True
    else: 
        return False
def bordaDown(object):
    if object.position[1]>=600:
        return True
    else: 
        return False

        
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

class Block():
    """docstring for Block"""
    def __init__(self, image,size,position,tipe):
        self.image =pygame.image.load(image)
        self.size=size
        self.position=position
        self.visibilit=True
        self.tipe=tipe
    def destroi(self):
        self.tipe=self.tipe-1
        if self.tipe==0:
            self.visibilit=False
def blit(screen,Object):
    if Object.visibilit:
        screen.blit(Object.image,(Object.position))

