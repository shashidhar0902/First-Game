import pygame
import m_constants
from m_constants import *
from pygame import *

init()
screen = display.set_mode(size)
font = font.Font(None,50)
pygame.display.set_caption("Mario Game")
clock = time.Clock()
click_sound = pygame.mixer.Sound("s.ogg")
st = 0
sound = Surface([190,50])
sound.fill(blue)
level = Surface([190,50])
level.fill(blue)
exiti = Surface([190,50])
exiti.fill(blue)
back = Surface([190,50])
back.fill(blue)

class Player(sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.width = 19
        self.height = 19
        self.image = Surface([self.width,self.height])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        
        self.rect.x += self.change_x

        

        block_hit_list = sprite.spritecollide(self,self.walls,False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        block_hit_list = sprite.spritecollide(self,self.walls,False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = Surface([20,20])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = Surface([20,20])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0




bound = pygame.sprite.Group()

wall_list = pygame.sprite.Group()
#boundaries 1,2,3,4
li = [ "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
       "W W W W W W W W W W W W W W W W W W W W W W W",
       "W  W W W                   W W W W W W W W WW",
       "W W W W W W     W W W W W   W W W W W W W W W",
       "W  W W W W W W W W W W W W   W W W W W W W WW",
       "W W W W W W W W W W W                 W W W W",
       "W  W W W W W W W       W   W W W   W W W W WW",
       "W W W W W W W W W W W W W W W W W     W W W W",
       "W  W W W W W W W W W W W W W W W W   W W W WW",
       "W W W W W W W W W W W W W W W W W W      W W",
       "W  W W W W W W W W W W W W W W W W W W W W WW",
       "W WWWWWWWWWWWW               WWW            W",
       "W W                        W                W",
       "W W                                         W",
       "W W     WWWWWWWW                            W",
       "W W                                         W",
       "W               WWW                         W",
       "W           WWWWW                W          W",
       "W W                                         W",
       "W W             WWWWWWW                     W",
       "W W                         WWWWWWWWW       W",
       "W WWWWWWWWW                         W       W",
       "W                                   W       W",
       "W       WWWWW                       W       W",
       "W           WWWWWWWWWWW             W       W",
       "W                       P           W       W",
       "W   WWWWWWWWW                       W       W",
       "W       W                                   W",
       "W       W                                   W",
       "W       WWWWWWWWW                           W",
       "W                                           W",
       "W                                           W",
       "W                                           W",
       "W                                           W",
       "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"]
x=y=0
for row in li:
    for col in row:
        if col == "W":
            wall = Wall(x,y)
            wall_list.add(wall)
            bound.add(wall)
        if col == "P":
            player = Player(x,y)
            player.walls = wall_list
            bound.add(player)
        x +=20
    y +=20
    x =0

def play():
    click_sound.play()
def game():
    run = True
    level2 = True
    while level2 and run:
        if st:
            play()
        else:
            pass
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_ESCAPE:
                    run = False
                    level2 = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3,0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0,3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0,-3)
                elif event.key == pygame.K_ESCAPE:
                    run = False
                    
                

        bound.update()

        screen.fill(black)

        bound.draw(screen)

        clock.tick(125)
        
        display.flip()
def ins(instructions):
    while instructions:
        ke= key.get_pressed()
        for event in pygame.event.get():
            pass
        
        mouse_x,mouse_y = mouse.get_pos()
        screen.fill(white)
        #introducion to game page
        if instructions == 1:
            
            #play
            if (mouse_x > (sc_width/3 -200) and mouse_x < ((sc_width/3) - 200+90) and (mouse_y > sc_height-200) and (mouse_y < sc_height -200+90) and event.type == MOUSEBUTTONDOWN):
                game()
            
            #settings
            if mouse_x > (sc_width/2 -100) and mouse_x < ((sc_width/2) - 100+90) and (mouse_y > sc_height-200) and (mouse_y < sc_height -200+90) and event.type == MOUSEBUTTONDOWN:
                instructions = 5

            #quit
            if mouse_x > (sc_width/2+150) and mouse_x < ((sc_width/2+150)+90) and (mouse_y > sc_height-200) and (mouse_y < sc_height -200+90) and event.type == MOUSEBUTTONDOWN:
                pygame.quit()
                    
            #image displaying
            play = image.load("play.jpg").convert()
            play = transform.scale(play,(90,90))

            setting = image.load("setting.png").convert()
            setting = transform.scale(setting,(90,90))
            

            out = image.load("exit.jpg").convert()
            out = transform.scale(out,(100,90))
            
            #text displaying
            text = font.render("",True,white)
            screen.blit(text,[50,50])
            screen.blit(setting,[sc_width/2-100,sc_height - 200])       
            screen.blit(play,(sc_width/3-200,sc_height -200))
            screen.blit(out,[sc_width/2+150,sc_height - 200])
        #inside level
        if instructions == 3:
            
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 100 and mouse_y < (100+50) and event.type == MOUSEBUTTONDOWN):
                level1 = True

            #level setting
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 200 and mouse_y < (200+50) and event.type == MOUSEBUTTONDOWN):
                level2 = True
                print(level2)
            
            #position of back to main menu
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 300 and mouse_y < (300+50) and event.type == MOUSEBUTTONDOWN):
                level3 = True

            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 400 and mouse_y < (400+50) and event.type == MOUSEBUTTONDOWN):
                instructions = 5
                
            box1 = sound.get_rect()
            box1.x,box1.y = 350,100
            screen.blit(sound,box1)
            text = font.render("Easy",True,white)
            screen.blit(text,[400,110])

            box2 = level.get_rect()
            box2.x,box2.y = 350,200
            screen.blit(level,box2)
            text = font.render("Medium",True,white)
            screen.blit(text,[385,210])

            box3 = exiti.get_rect()
            box3.x,box3.y = 350,300
            screen.blit(exiti,box3)
            text = font.render("Hard",True,white)
            screen.blit(text,[405,310])

            box4 = back.get_rect()
            box4.x,box4.y = 350,400
            screen.blit(back,box4)
            text = font.render("Back",True,white)
            screen.blit(text,[405,410])

            #easy
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 100 and mouse_y < (100+50) ):
                sound.fill(black)
            else:
                sound.fill(blue)

            #medium
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 200 and mouse_y < (200+50) ):
                level.fill(black)
            else:
                level.fill(blue)
            
            #hard
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 300 and mouse_y < (300+50) ):
                exiti.fill(black)
            else:
                exiti.fill(blue)

            #exit
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 400 and mouse_y < (400+50) ):
                back.fill(black)
            else:
                back.fill(blue)

        #inside settings
        if instructions == 5 :

            #sound setting
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 100 and mouse_y < (100+50) and event.type == MOUSEBUTTONDOWN):
                st=0

            #level setting
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 200 and mouse_y < (200+50) and event.type == MOUSEBUTTONDOWN):
                instructions = 3
            
            #position of back to main menu
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 300 and mouse_y < (300+50) and event.type == MOUSEBUTTONDOWN):
                instructions = 1
                    
            
            
            box1 = sound.get_rect()
            box1.x,box1.y = 350,100
            screen.blit(sound,box1)
            text = font.render("Sound",True,white)
            screen.blit(text,[390,110])

            box2 = level.get_rect()
            box2.x,box2.y = 350,200
            screen.blit(level,box2)
            text = font.render("Level",True,white)
            screen.blit(text,[400,210])

            box3 = exiti.get_rect()
            box3.x,box3.y = 350,300
            screen.blit(exiti,box3)
            text = font.render("Exit",True,white)
            screen.blit(text,[410,310])

            #color change
            #sound
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 100 and mouse_y < (100+50) ):
                sound.fill(black)
            else:
                sound.fill(blue)

            #level
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 200 and mouse_y < (200+50) ):
                level.fill(black)
            else:
                level.fill(blue)
            
            #exiti
            if (mouse_x > 350 and mouse_x < 350+190 and mouse_y > 300 and mouse_y < (300+50) ):
                exiti.fill(black)
            else:
                exiti.fill(blue)
        
        display.flip()

#calling the instructions
ins(1)        
            
