import pygame as pg
import random as rd
from settings import *
from objects import *
from game import *

pg.init()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Tic Tac Toe")
clock = pg.time.Clock()
game = Game()

game.init()


def main():
    while game.isRunning():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game.end()

        game.loop(event, screen)
        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    main()
