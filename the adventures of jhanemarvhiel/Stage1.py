import random
import pygame
import math

class cStage1:
    def __init__(self):
        self.bg=pygame.image.load("Ardentryst-Background_Forest_Backing.png")
        self.player_img=pygame.image.load("princess.png").convert()
        self.player_img.set_colorkey(pygame.Color(255,174,201))
        self.player_pos=[0,300]
        self.ListOfBullets=[cBullet()]
        self.ListOfEnemies=[cEnemy()]
        self.enemy_timer=[0, 0, 0]
        self.score=0
        self.font=pygame.font.Font("freesansbold.ttf",32)
        
    def update(self, clock):
#        collision detection
        for bullet in self.ListOfBullets:
            for enemy in self.ListOfEnemies:
                bullet_box=pygame.Rect(bullet.bullet_pos, bullet.bullet_img.get_size())
                enemy_box=pygame.Rect(enemy.enemy_pos, enemy.enemy_img.get_size())
                if(bullet_box.colliderect(enemy_box)):
                    self.ListOfEnemies.remove(enemy)
                    self.ListOfBullets.remove(bullet)
                    self.score+=1
                    print("Score: %i"%(self.score))

                    
                        
            bullet.update()
        for enemy in self.ListOfEnemies:
            enemy.update()

        for i in range(len(self.enemy_timer)):            
            self.enemy_timer[i] += clock.get_time()

        #enemy 1
        if (self.enemy_timer[0]>6000):
            newEnemy=cEnemy()
            self.ListOfEnemies.append(newEnemy)
            self.enemy_timer[0]-=6000
            
        #enemy 2
        if (self.enemy_timer[1]>5000):
            newEnemy=cEnemy2()
            self.ListOfEnemies.append(newEnemy)
            self.enemy_timer[1]-=5000

        #enemy 3
        if (self.enemy_timer[2]>10000):
            newEnemy=cEnemy3()
            self.ListOfEnemies.append(newEnemy)
            self.enemy_timer[2]-=10000

                  
        key_pressed=pygame.key.get_pressed()
        if (key_pressed[pygame.K_SPACE]):
            newBullet=cBullet()
            newBullet.bullet_pos[0]=self.player_pos[0]
            newBullet.bullet_pos[1]=self.player_pos[1]
            self.ListOfBullets.append(newBullet)
        elif (key_pressed[pygame.K_UP]):
            self.player_pos[1]-=10
        elif (key_pressed[pygame.K_DOWN]):
            self.player_pos[1]+=10
        elif (key_pressed[pygame.K_LEFT]):
            self.player_pos[0]-=10
        elif (key_pressed[pygame.K_RIGHT]):
            self.player_pos[0]+=10
        else:
            self.player_pos[0]

    def draw(self,window):
        window.blit(self.bg,[0,0])
        window.blit(self.player_img, self.player_pos)
        textcolor=pygame.Color(216, 137, 184)
        text=self.font.render("Score: %i"%(self.score),False,textcolor)
        window.blit(text,[15,15])
        for bullet in self.ListOfBullets:
            bullet.draw(window)
        for enemy in self.ListOfEnemies:
            enemy.draw(window)

class cEnemy:
    def __init__(self):
        self.enemy_img=pygame.image.load("space armour.png").convert()
        self.enemy_img.set_colorkey(pygame.Color(255,174,201))
        self.enemy_pos=[400,480]
    def update(self):
        self.enemy_pos[0]-=1
        self.enemy_pos[1]=170+(math.sin(math.radians(self.enemy_pos[0]*2))*250)
    def draw(self,window):
        window.blit(self.enemy_img,self.enemy_pos)

class cEnemy2:
    def __init__(self):
        self.enemy_img=pygame.image.load("angel_normal.png").convert()
        self.enemy_img.set_colorkey(pygame.Color(255,174,201))
        self.enemy_pos=[500,random.randrange(0,200)]
        self.pos_y=random.randrange(50, 600)
    def update(self):
        self.enemy_pos[0]-=1
        self.enemy_pos[1]=self.pos_y+(math.sin(math.radians(self.enemy_pos[0]*2))*200)
    def draw(self,window):
        window.blit(self.enemy_img,self.enemy_pos)

class cEnemy3:
    def __init__(self):
        self.enemy_img=pygame.image.load("space armour2.png").convert()
        self.enemy_img.set_colorkey(pygame.Color(255,174,201))
        self.enemy_pos=[600,random.randrange(0,200)]
    def update(self):
        self.enemy_pos[0]-=1
    def draw(self,window):
        window.blit(self.enemy_img,self.enemy_pos)


class cBullet:
    def __init__(self):
        self.bullet_img=pygame.image.load("bullet.png").convert()
        self.bullet_img.set_colorkey(pygame.Color(255,174,201))
        self.bullet_pos=[0,500]

    def update(self):
        self.bullet_pos[0]+=10

    def draw(self,window):
        window.blit(self.bullet_img,self.bullet_pos)





