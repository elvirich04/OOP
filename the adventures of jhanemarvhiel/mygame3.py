import math
import pygame
import sys
import Stage1
import TitleScreen
import gameOver
pygame.init()
clock=pygame.time.Clock()
clock.tick()
window=pygame.display.set_mode([640,480])
pygame.display.set_caption("Team JhaneMarVhiel")
font=pygame.font.Font("freesansbold.ttf",32)
#font=pygame.font.Font("HARNGTON.TTF",60)
TitleScreen=TitleScreen.cTitleScreen()
Stage1=Stage1.cStage1()
gameOver=gameOver.cGameOver()
#CurrentScreen=gameOver
CurrentScreen=TitleScreen
while True:
    newScreen=CurrentScreen.update(clock)
    if (newScreen=="Stage1"):
        CurrentScreen=Stage1
    CurrentScreen.draw(window)
    events=pygame.event.get()

     
    for event in events:
        if ((event.type==pygame.QUIT)or
            (newScreen=="QUIT")or
            (event.type==pygame.KEYDOWN
             and event.key==pygame.K_ESCAPE)):
            pygame.quit()
            sys.exit()
    clock.tick(30)        
    pygame.display.update()


