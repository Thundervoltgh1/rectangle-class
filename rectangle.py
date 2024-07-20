import pygame,sys
pygame.init()
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption("TEST GAME")
screen.fill("white")


class Rectangle:
    def __init__(self,clr,dimension):
        self.rect_surf=screen
        self.rect_color=clr
        self.rect_dimension=dimension
    def draw(self):
        pygame.draw.rect(self.rect_surf,self.rect_color,self.rect_dimension)

rect1=Rectangle("blue",(50,50,100,100))
rect1.draw()
rect2=Rectangle("red",(150,150,100,100))
rect2.draw()
rect3=Rectangle("yellow",(250,250,100,100))
rect3.draw()
rect4=Rectangle("green",(350,350,100,100))
rect4.draw()
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.display.update()