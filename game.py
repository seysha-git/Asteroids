from settings import *
from objects.cell import Cell
import pygame as pg
import random as rd


class Game:
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.running = True

    #main methods
    def init(self):
        for r in range(self.rows):
            for c in range(self.columns):
                self.cells[r][c] = Cell(150 + 70*c, 150 + 70*r)
    def loop(self, event, screen):
        screen.fill("black")
        for r in range(self.rows):
            for c in range(self.columns):
                self.update(r, c, event)
                self.draw(r, c, screen)
        #test
    def update(self, r, c, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.type == 1:
                if self.cells[r][c].isClicked(event.pos):
                    print("hit")
    def draw(self, r, c, screen):
        self.cells[r][c].draw(screen)

    #check-methods
    def isRunning(self):
        return self.running
    #get-methods
     
    #set-methods
    def end(self):
        self.running = False
