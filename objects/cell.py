#from settings import *
import pygame as pg


class Cell:
    def __init__(self, x, y):
        self.width = 60
        self.height = 60
        self.x = x
        self.y = y

        self.state = " "
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

        pg.font.init()
    #main-methods
    def update(self):
        pass
    def draw(self, screen):
        font = pg.font.SysFont('Arial', 50)
        text_surface = font.render(self.state, True, "white") 
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width // 2, self.y + self.height // 2)
        pg.draw.rect(screen, "grey", self.rect)
        screen.blit(text_surface, text_rect)
    #set-methodss
    def setState(self, turn):
        if turn: self.state = "X"
        else:self.state = "O"
    #check-methods
    def isClicked(self, pos):
        return self.rect.collidepoint(pos)
    def isEmpty(self):
        return self.state == " "
    #get-methods
    def getState(self):
        return self.state
        

