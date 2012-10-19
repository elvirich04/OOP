import pygame
class cTitleScreen:
    def __init__(self):
        self.font=pygame.font.Font("freesansbold.ttf",32)
        self.bg=pygame.image.load("Ardentryst-Background_Forest_Backing.png")
    def draw(self,window):
        window.blit(self.bg,[0,0])
        textColor=pygame.Color(216, 137, 184)
        text=self.font.render("Team JhaneMarVhiel:",False,textColor)
        textColor2=pygame.Color(216, 137, 184)
        text2=self.font.render("Jane Claudette Alambra",False,textColor2)
        textColor3=pygame.Color(216, 137, 184)
        text3=self.font.render("Ma. Elvira Oco",False,textColor3)
        textColor4=pygame.Color(216, 137, 184)
        text4=self.font.render("Margarita Labid",False,textColor4)
        window.blit(text,[0,0])
        window.blit(text2,[50,64])
        window.blit(text3,[50,96])
        window.blit(text4,[50,128])
        
    def update(self,clock):
        mouse_pressed=pygame.mouse.get_pressed()
        if(mouse_pressed[0]==True):
            return "Stage1"
