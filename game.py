from settings import *
from objects import *
import pygame as pg
import random as rd


class Game:
    def __init__(self):
        self.objects = []
        self.running = True

    #loop methods
    def update(self):
        pass
    def draw(self, screen):
        screen.fill("black")
    
    #check-methods
    def isRunning(self):
        return self.running
    #get-methods
     
    #set-methods
    def end(self):
        self.running = False
