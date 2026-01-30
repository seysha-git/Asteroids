from settings import *
from objects.cell import Cell
from objects.players import Player, Enemy
import pygame as pg
import random as rd


class Game:
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.running = True
        self.turn = True
        self.count = 0

        #self.player = Player()
        pg.font.init()

    #main methods
    def init(self):
        for r in range(self.rows):
            for c in range(self.columns):
                self.cells[r][c] = Cell(150 + 70*c, 150 + 70*r)
    def loop(self, event, screen):
        screen.fill("black")
        for r in range(self.rows):
            for c in range(self.columns): 
                self.draw(r, c, screen)
                self.update_key(r, c, event)
        self.update_game_state()
        self.draw_turn_text(self.turn, screen)
    def update_game_state(self):
        win_rows = [
            [(0, 0), (0, 1), (0, 2)], 
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)]
        ]
        win_cols = [
            [(0, 0), (1, 0), (2,0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)]
        ]
        win_diags = [
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        for row in win_rows:
            if(
            (
            self.cells[row[0][0]][row[0][1]].getState() \
            == self.cells[row[1][0]][row[1][1]].getState() \
            == self.cells[row[2][0]][row[2][1]].getState()\
            ) and (
            not self.cells[row[0][0]][row[0][1]].isEmpty() and
            not self.cells[row[1][0]][row[1][1]].isEmpty() and
            not self.cells[row[2][0]][row[2][1]].isEmpty()\
            )):
                if not self.turn:
                    print("player won")
                else: print("enemy won")
        for col in win_cols:
            if(
            (
            self.cells[col[0][0]][col[0][1]].getState() \
            == self.cells[col[1][0]][col[1][1]].getState() \
            == self.cells[col[2][0]][col[2][1]].getState()\
            ) and (
            not self.cells[col[0][0]][col[0][1]].isEmpty() and
            not self.cells[col[1][0]][col[1][1]].isEmpty() and
            not self.cells[col[2][0]][col[2][1]].isEmpty()\
            )):
                if not self.turn:
                    print("player won")
                else: print("enemy won")
        for diag in win_diags:
            if(
            (
            self.cells[diag[0][0]][diag[0][1]].getState() \
            == self.cells[diag[1][0]][diag[1][1]].getState() \
            == self.cells[diag[2][0]][diag[2][1]].getState()\
            ) and (
            not self.cells[diag[0][0]][diag[0][1]].isEmpty() and
            not self.cells[diag[1][0]][diag[1][1]].isEmpty() and
            not self.cells[diag[2][0]][diag[2][1]].isEmpty()\
            )):
                if not self.turn:
                    print("player won")
                else: print("enemy won")
        if self.count == 9:
            print("full board")
        
        
        
                
    def update_key(self, r, c, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.cells[r][c].isClicked(event.pos) and self.cells[r][c].isEmpty():
                    self.cells[r][c].setState(self.turn)
                    self.toggleTurn()
                    self.count += 1
        
    def draw_turn_text(self, turn, screen):
        if turn:
            turn_text = "Player turn"
        else: turn_text = "Enemy turn"
        font = pg.font.SysFont('Arial', 30)
        text_surface = font.render(turn_text, True, "white") 
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH//2, 100)

        screen.blit(text_surface, text_rect)
    def draw(self, r, c, screen):
        self.cells[r][c].draw(screen)

    #check-methods
    def isRunning(self):
        return self.running
    #get-methods
     
    #set-methods
    def end(self):
        self.running = False
    def toggleTurn(self):
        if self.turn: self.turn = False
        else: self.turn = True
