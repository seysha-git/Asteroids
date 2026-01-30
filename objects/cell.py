from settings import *
import pygame as pg


class Cell:
    def __init__(self, x, y):
        self.width = 60
        self.height = 60
        self.x = x
        self.y = y

        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
    def update(self):
        pass
    def draw(self, screen):
        pg.draw.rect(screen, "grey", self.rect)