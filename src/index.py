import pygame
import random
from Tetris import Tetris
from block import Block
from block_forms import Forms
from renderer import Renderer
from stopdrop import Stopdrop
from gameover import Game


def main():
    display = pygame.display.set_mode((700,800))
    pygame.init()
    forms = Forms.create_forms()
    block = Block()
    block.first = True
    tetris = Tetris()
    tetris.create_grid()
    next = random.randint(0,6)
    coordinates = block.create_block(forms, tetris.grid, next)
    tetris.update_grid(coordinates[0], coordinates[1])
    clock = pygame.time.Clock()
    clock.tick(60)
    time1 = 0
    time2 = 0
    time3 = 0
    time4 = 0
    down = False
    game = Game(0, display, tetris)
    game.speed = 500
    game.exc = 0
    stopdrop = Stopdrop(tetris, block)
    renderer = Renderer(display, tetris, game)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    down = True
                if event.key == pygame.K_LEFT:
                    results = block.move_block("L", tetris.grid)
                    if results == "no change":
                        continue
                    else:
                        old = results[0]
                        new = results[1]
                        tetris.update_grid(old, new)
                if event.key == pygame.K_RIGHT:
                    results = block.move_block("R", tetris.grid)
                    if results == "no change":
                        continue
                    else:
                        old = results[0]
                        new = results[1]
                        tetris.update_grid(old, new)
                if event.key == pygame.K_UP:
                    block.rotate_block(tetris.grid) 
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    down = False
                        
            if event.type == pygame.QUIT:
                    exit()
        
        time3 = pygame.time.get_ticks()
        time1 = pygame.time.get_ticks()

        if time3 - time4 > 100000:
            if game.exc < 50:
                game.exc = game.exc + 100
            elif game.exc < 200:
                game.exc = game.exc + 50
            elif game.exc < 210:
                game.exc = game.exc + 30
            elif game.exc < 250:
                game.exc = game.exc + 20
            else:
                game.exc = game.exc + 10
            time4 = pygame.time.get_ticks()
        if down == True:
            game.speed = 100
        else:
            game.speed = 500 - game.exc
        if time1 - time2 > game.speed:
            results = stopdrop.drop()
            if results != None:
                for y in range(20):
                    for x in range(10):
                        if tetris.grid[y][x] == "1":
                            tetris.grid[y][x] = "."
                block = Block()
                coordinates = block.create_block(forms, tetris.grid, next)
                next = random.randint(0,6)
                game.score = game.score + 1
                if coordinates[2] == True:
                    game.gameover()
                stopdrop = Stopdrop(tetris, block)
                tetris.update_grid(coordinates[0], coordinates[1])
            time2 = pygame.time.get_ticks()
        renderer.render(next)
        


if __name__ == "__main__":
    main()
