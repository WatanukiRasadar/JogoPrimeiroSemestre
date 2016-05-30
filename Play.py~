# -*- coding: utf-8 -*-
import pygame,math,random
from Objects import *
from pygame.locals import *
from BlockFone import *

pygame.init()
screen_size=800,600
clock=pygame.time.Clock()
player=Player('image\player.gif',(80,9),(400,565))
ball=Ball('image\\ball40.gif',(18,18),(400,300))
score=Score()
FPS=60

class __menu__():
    runing=True
    def run(self,ask):
        screen=pygame.display.set_mode(screen_size)
        pygame.display.set_caption( " BlockBreaker " )
        backgroud=pygame.image.load('image\\back2.png')
        arcade=button('image\\arcade.png',(568,154),'arcade')
        suvivor=button('image\suvivor.png',(568,230),'suvivor')
        close=buttonExit('image\exit.png',(568,380),'exit')
        mouse=mousedefault()
        while self.runing:
            print clock.get_fps()
            mouse.update(screen)
            screen.blit(backgroud,(0,0))
            arcade.action(screen,mouse,selec,player,ball,screen_size,FPS,clock,score,ask)
            suvivor.action(screen,mouse,faseRandom,player,ball,screen_size,FPS,clock,score,ask)
            close.action(screen,mouse)
            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      self.runing=False
                      pygame.quit()
                      
            
           
            
            
    
       


class __fase1__():
    blocks={}
    speciais={1:special("slow",(270,81)),2:special("big",(0,0)),3:special("xp",(0,0)),4:special("life",(0,0))}
    runing=True
    tipe="arcade"
    back=pygame.image.load('image\\back\\1.gif')
    lock="locked"


    def run(self,player,ball,screen_size,FPS,clock,Score,ask):
        for key in self.blocks:
            self.blocks[key].visibilit=True
            self.blocks[key].resistence=self.blocks[key].original
        if self.tipe!="arcade":
            rand(BlFase1,BlRand)
            self.blocks=BlRand
        screen=pygame.display.set_mode(screen_size)
        A=0
        D=0
        ball.girar(0)
        life=3
        over=pygame.image.load('image\game over.png')
        status="inicio"
        font = pygame.font.Font(None, 16)
        imaglife=pygame.image.load('image\life.png')
        pause=pygame.image.load('image\pause2.gif')
        print status
        space=False
        while self.runing:
            clock.tick(FPS)
            score = font.render("Score: "+str(Score.score), 1, (10, 10, 10))
            ilife = font.render(str(life), 1, (10, 10, 10))
            
            if status=="inicio":
                ball.position=player.position[0]+32,player.position[1]-20
            screen.fill(0)
            screen.blit(self.back,(0,0))
            screen.blit(score,(20,20))
            if status=="Pause":
                screen.blit(pause,(400,20))
            screen.blit(imaglife,(693,15))
            screen.blit(ilife,(700,20))
            blit(screen,player)
            screen.blit(ball.image,(ball.position))
            for key in self.blocks:
                if self.blocks[key].visibilit==True:
                    screen.blit(self.blocks[key].image,self.blocks[key].position)
            for key in self.blocks:
                if colisor(self.blocks[key],ball):
                    self.blocks[key].destroi(status,self.speciais,screen,ball,player,life,score)
                    ball.position = ball.position[0],(ball.position[1]+3)
                    ball.direction = math.pi - ball.direction
                    ball.forca=9
            if status=='special':
                for key in self.speciais:
                    if self.speciais[key].runing==True:
                        screen.blit(self.speciais[key].image2,(0,0))
            if self.complet():
                status = "completed nivel"
            if status=="completed nivel":
                ask.run(screen_size,FPS,clock,score)
                if self.tipe !='arcade':
                    rand(BlFase1,BlRand)
                    self.blocks=BlRand
                    status="normal"
            #print clock.get_fps()
                
                
                
            if life <0:
                    screen.blit(over,(200,300))
                    status='died'
                    ball.position=player.position[0]+32,player.position[1]-20
            pygame.display.flip()
            if status!='died' and status!='Pause' :
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
                ball.didirection=0
                print (str(ball.didirection)+'º')
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
                    if status != "Pause":
                      status="normal"
                  if event.key == pygame.K_F10:
                    if status != "Pause":
                      status="Pause"
                    else: status="normal"
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
                    self.runing=False
                    return
                    
                  
            if status!= "Pause":
            	if A == True:
                  if bordaLeft(player)== False:
                    player.andar(-4)
            	if D == True:
                  if bordaRight(player)== False:
                    player.andar(4)
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
		

               
                

                
    def complet(self):
        a=False
        for key in self.blocks:
            if self.blocks[key].visibilit==True:
                a=True
            

        if a:
            return False
        else:
            return True
class __selec__():
    def __init__(self,BlFase1,BlFase2):
        self.stages={1:__fase1__(),2:__fase1__(),3:__fase1__(),4:__fase1__()}
        self.stages[1].blocks=BlFase1
	self.stages[1].lock="unlocked"
        self.stages[2].blocks=BlFase2
        self.stages[2].back=pygame.image.load('image\\back\\2.gif')
        self.stages[3].blocks=BlFase3
        self.stages[3].back=pygame.image.load('image\\back\\3.gif')
        self.stages[4].blocks=BlFase4
        self.stages[4].back=pygame.image.load('image\\back\\4.gif')
	
    def run(self,player,ball,screen_size,FPS,clock,score,ask):
        screen=pygame.display.set_mode(screen_size)
        run=True
        backgroud=pygame.image.load('image\\back.png')
        voltar=buttonVoltar('image\exit.png',(568,510),'exit')
        mouse=mousedefault()
        nest=self.button_change('image\Button\\right.png',(540,220))
        back=self.button_back('image\Button\left.png',(20,220),nest)
        select=button('image\select.png',(568,380),'select')
	unlock=self.button('image\unlock.png',(568,380),'unlock')
        
        while run:
            print clock.get_fps()
            mouse.update(screen)
            screen.blit(backgroud,(0,0))
            screen.blit(nest.stageimage,(100,100))
            voltar.action(screen,mouse,menu,ask)
            nest.action(screen,mouse,clock)
            back.action(screen,mouse,clock,nest)
	    if self.stages[nest.var].lock == 'unlocked':
                select.action(screen,mouse,self.stages[nest.var],player,ball,screen_size,FPS,clock,score,ask)
	    if self.stages[nest.var].lock == 'locked':
                unlock.action(screen,mouse,player,ball,screen_size,FPS,clock,score,ask)
            pygame.display.flip()
            #clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                    return
                      
    class button_change():
        def __init__(self,image,position):
            self.image=pygame.image.load(image)
            self.position=position
            self.size=(50,59)
            self.visibilit=True
            self.lista={1:pygame.image.load('image\mini\\1.png'),2:pygame.image.load('image\mini\\2.png'),3:pygame.image.load('image\mini\\3.png'),4:pygame.image.load('image\mini\\4.png')}
            self.var=1
            self.stageimage=self.lista[self.var]
        def action(self,screen,mouse,clock):
            blit(screen,self)
            if colisor(mouse,self):
                clock.tick(5)
                if mouse.keys[0]:
                    if self.var<4:
                        self.var+=1
                        self.stageimage=self.lista[self.var]
                    else:
                        self.var=1
                        self.stageimage=self.lista[self.var]

    class button_back():
        def __init__(self,image,position,nest):
            self.image=pygame.image.load(image)
            self.position=position
            self.size=(50,59)
            self.visibilit=True
        def action(self,screen,mouse,clock,nest):
            blit(screen,self)
            if colisor(mouse,self):
                print nest.var
                clock.tick(5)
                if mouse.keys[0]:
                    if nest.var>1:
                        nest.var-=1
                        nest.stageimage=nest.lista[nest.var]
                    else:
                        nest.var=4
                        nest.stageimage=nest.lista[nest.var]
    class button():
    	def __init__(self,image,position,nome):
        	self.image=pygame.image.load(image)
        	self.position=position
        	self.size=(198,62)
        	self.visibilit=True
        	self.nome=nome

    	def destroi(self):
       		self.visibilit=False
    	def action(self,screen,mouse,player,ball,screen_size,FPS,clock,score,ask):
        	blit(screen,self)
        	if colisor(mouse,self):
            		self.image=pygame.image.load('image\\'+self.nome+'2.png')
            		if mouse.keys[0]:
                		ask.run(screen_size,FPS,clock,score)
        	else:
            		self.image=pygame.image.load('image\\'+self.nome+'.png')

class __ask__():
    runing=True
    def __init__(self):
	self.perguntas={1:["Defina computador.",'Sistema progamavel(CORRETA)','Sistema de conversao binaria','Calculadora',1],2:['Para nao ocupar tanta memoria sao criada as:','Variaveis(CORRETA)','Vetores.','if , else',1],3:['O MarkI e de que geracao?','Primeira Geracao(CORRETA)','Segunda Geracao','Terceira Geracao',1],4:['Qual e o nome dado a parte fisica do computador?','Perifericos','Hardware(CORRETA)','Software',2],5:['Como comecar um codigo javascript?','<script>(CORRETA)','<algoritmo>','Inicio',1]}
    def run(self,screen_size,FPS,clock,score):
	randspergunta=self.perguntas[random.randint(1,5)]
        screen=pygame.display.set_mode(screen_size)
        backgroud=pygame.image.load('image\\back.png')
	font = pygame.font.Font(None, 28)
	pergunta = font.render(randspergunta[0], 1, (10, 10, 10))
        r1= font.render(randspergunta[1], 1, (10, 10, 10))
        r2 = font.render(randspergunta[2], 1, (10, 10, 10))
        r3 = font.render(randspergunta[3], 1, (10, 10, 10))
	br1=self.button((100,180),1,randspergunta[4])
	br2=self.button((100,260),2,randspergunta[4])
	br3=self.button((100,340),3,randspergunta[4])
        mouse=mousedefault()
        while self.runing:
            print clock.get_fps()
            mouse.update(screen)
            screen.blit(backgroud,(0,0))
	    screen.blit(pergunta,(70,100))
	    screen.blit(r1,(100,180))
	    screen.blit(r2,(100,260))
	    screen.blit(r3,(100,340))
	    br1.action(screen,mouse,clock,selec)
	    br2.action(screen,mouse,clock,selec)
	    br3.action(screen,mouse,clock,selec)
            pygame.display.flip()
            #clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
    class button():
        def __init__(self,position,resposta,rep):
            self.position=position
            self.size=(470,59)
            self.visibilit=True
	    self.resposta=resposta
	    self.randspegunta=rep
        def action(self,screen,mouse,clock,selec):
            if colisor(mouse,self):
                clock.tick(10)
                if mouse.keys[0]:
                    if self.resposta==self.randspegunta:
			c=1
			for key in selec.stages:
				if c:
					if selec.stages[key].lock=="locked":
						selec.stages[key].lock="unlocked"
						c=0
			run=False
			selec.run(player,ball,screen_size,FPS,clock,score,ask)
		    else: 
   			run=False
			selec.run(player,ball,screen_size,FPS,clock,score,ask)

				
		    

        
ask=__ask__()
fase1=__fase1__()
f1(BlFase1)
fase1.blocks=BlFase1
faseRandom=__fase1__()
faseRandom.tipe="suvivor"
menu=__menu__()
selec=__selec__(BlFase1,BlFase2)
menu.run(ask)
#ask.run(screen_size,FPS,clock,score)






#fase1.run(player,ball,screen_size,FPS,clock,score)



