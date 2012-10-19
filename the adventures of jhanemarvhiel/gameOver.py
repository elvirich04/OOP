import pygame

class cGameOver:
    def __init__(self):
        self.font=pygame.font.Font("freesansbold.ttf",100)
        self.bgcolor=pygame.Color(0,0,0)
            
    def update(self,clock):
        return "QUIT"
        if(self.bgcolor.r<255-10):
            self.bgcolor.r+=10
        if(self.bgcolor.g<255-8):
            self.bgcolor.g+=8
        if(self.bgcolor.b<255-5):
            self.bgcolor.b+=5
    
    def draw(self,window):
        window.fill(self.bgcolor)
        text="Game Over"
        render=self.font.render(text, False,pygame.Color(0,0,0))
        window.blit(render,[50,200])
