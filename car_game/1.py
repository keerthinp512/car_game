import pygame
pygame.init()
import time
import random

gray=(119,118,110)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
yellow=(255,255,102)
display_width=820
display_height=800
carimg=pygame.image.load('car.png')
gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("car game")
clock=pygame.time.Clock
backgroundimg=pygame.image.load('road.jpeg')
grass=pygame.image.load("grass.png")
intro_img=pygame.image.load("intro.png")
car_width=110

def intro_loop():
   intro=True
   while intro:
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
               pygame.quit()
               quit()
               sys.exit()
       gamedisplays.blit(intro_img,(0,0))
       largetext=pygame.font.Font('freesansbold.ttf',115)
       Textsurf,Textrect=text_objects("CAR GAME",largetext)
       Textrect.center=((400,100))
       gamedisplays.blit(Textsurf,Textrect)
       button("START",150,520,100,50,green,bright_green,"play")
       button("QUIT",550,520,100,50,red,bright_red,"quit")
       button("INSTRUCTION",300,520,200,50,blue,bright_blue,"intro")
       pygame.display.update()
       clock().tick(50)        
       
def introduction():
   introduction=True
   while introduction:
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
               pygame.quit()
               quit()
               sys.exit()
       gamedisplays.blit(intro_img,(0,0))
       largetext=pygame.font.Font('freesansbold.ttf',80)
       mediumtext=pygame.font.Font('freesansbold.ttf',40)
       smalltext=pygame.font.Font('freesansbold.ttf',20)
       textSurf,textRect=text_objects("This is a car game in which you need to dodge  other cars",smalltext)
       textRect.center=((400,200))
       TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
       TextRect.center=((400,100))
       gamedisplays.blit(TextSurf,TextRect)
       gamedisplays.blit(textSurf,textRect)
       
       TexTSurf,TexTRect=text_objects("ARROW LEFT : LEFT TURN ",smalltext)
       TexTRect.center=((150,400))
       TExTSurf,TExTRect=text_objects("ARROW RIGHT : RIGHT TURN ",smalltext)
       TExTRect.center=((150,450))
       TEXTSurf,TEXTRect=text_objects("A : ACCELERATION ",smalltext)
       TEXTRect.center=((150,500))
       TEXTSUrf,TEXTREct=text_objects("B : BRAKE ",smalltext)
       TEXTREct.center=((150,550))
       TEXTSURf,TEXTRECt=text_objects("P : PAUSE ",smalltext)
       TEXTRECt.center=((150,600))
       TEXTSURF,TEXTRECT=text_objects("CONTROLS",mediumtext)
       TEXTRECT.center=((150,300))
       gamedisplays.blit(TexTSurf,TexTRect)
       gamedisplays.blit(TExTSurf,TExTRect)
       gamedisplays.blit(TEXTSurf,TEXTRect)
       gamedisplays.blit(TEXTSUrf,TEXTREct)
       gamedisplays.blit(TEXTSURf,TEXTRECt)
       gamedisplays.blit(TEXTSURF,TEXTRECT)
       button("BACK",650,700,100,50,blue,bright_blue,"menu")
       pygame.display.update()
       clock().tick(30)
       
def button(msg,x,y,w,h,ic,ac,action=None):
   mouse=pygame.mouse.get_pos()
   click=pygame.mouse.get_pressed()
   if x+w>mouse[0]>x and y+h>mouse[1]>y:
       pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
       if click[0]==1 and action!=None:
           if action=="play":
               game_loop()
           elif action=="quit":
               pygame.quit()
               quit()
               sys.exit()
           elif action=="intro":
               introduction()
           elif action=="menu":
               intro_loop()
   else:
       pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
       smalltext=pygame.font.Font("freesansbold.ttf",20)
       textsurf,textrect=text_objects(msg,smalltext)
       textrect.center=((x+(w/2)),(y+(h/2)))
       gamedisplays.blit(textsurf,textrect)   
  
    
   
def obstacle(obs_startx,obs_starty,obs):
   if (obs==0):
       obs_pic=pygame.image.load("car.png")
   elif(obs==1):
       obs_pic=pygame.image.load("car.png")
   gamedisplays.blit(obs_pic,(obs_startx,obs_starty))
   
   
def text_objects(text,font):
   textsurface=font.render(text,True,black)
   return textsurface,textsurface.get_rect()

def message_display(text):
   largetext=pygame.font.Font("freesansbold.ttf",80)
   textsurf,textrect=text_objects(text,largetext)
   textrect.center=((display_width/2),(display_height/2))
   gamedisplays.blit(textsurf,textrect)
   pygame.display.update()
   time.sleep(3)
   game_loop()
   
def crash():
   message_display("CAR CRASHED")
   
   
def background():
   gamedisplays.blit(grass,(0,0))
   gamedisplays.blit(grass,(0,400))
   gamedisplays.blit(backgroundimg,(150,0))
   gamedisplays.blit(backgroundimg,(150,400))
   gamedisplays.blit(grass,(675,0))
   gamedisplays.blit(grass,(675,400))

def carsystem(passed,score):
   font=pygame.font.SysFont('Arial',35)
   text=font.render("PASSED: "+str(passed),True,yellow)
   score=font.render("SCORE: "+str(score),True,yellow)
   gamedisplays.blit(text,(0,50))
   gamedisplays.blit(score,(0,80))
def car(x,y):
   gamedisplays.blit(carimg,(x,y))

def game_loop():
   x=display_width*0.45
   y=display_height*0.8
   x_change=0
   obs_speed=10
   obs=0
   y_change=0
   obs_startx=random.randrange(200,(display_width-200))
   obs_starty=-770
   obs_width=110
   obs_height=302
   passed=0
   level=0
   score=0
   
   
   bumped=False
   while not bumped:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
               pygame.quit()
               quit()
          if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_LEFT:
                   x_change=-5
               if event.key==pygame.K_RIGHT:
                   x_change=5
               if event.key==pygame.K_a:
                   obs_speed+=2
               if event.key==pygame.K_b:
                   obs_speed-=2
          if event.type==pygame.KEYUP:
               if (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                   x_change=0
      x+=x_change
               
      gamedisplays.fill(gray)
      background()
      obs_starty-=(obs_speed/4)
      obstacle(obs_startx,obs_starty,obs)
      obs_starty+=obs_speed
      car(x,y)
      carsystem(passed,score)
      if x>675-car_width or x<100:
          crash()
      if x>display_width-(car_width+100) or x<100:
          crash()
      if obs_starty>display_height:
          obs_starty=0-obs_height
          obs_startx=random.randrange(100,(675-car_width))
          obs=random.randrange(0,2)
          passed+=1
          score=passed*10
          if int(passed)%5==0:
              level+=1
              obs_speed+=5
              largetext=pygame.font.Font("freesansbold.ttf",80)
              textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
              textrect.center=((display_width/2),(display_height/2))
              gamedisplays.blit(textsurf,textrect)
              pygame.display.update()
              time.sleep(3)
      if y<obs_starty+obs_height:
          if ((x>obs_startx and x<obs_startx+obs_width) or (x+car_width> obs_startx and x+car_width<obs_startx+obs_width)):
              crash()
      pygame.display.update()
      clock().tick(60)
 
intro_loop()   
game_loop()
pygame.quit()
quit()

