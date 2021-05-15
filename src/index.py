import pygame
from Tetris import Tetris
from block import Block
from block_forms import Forms
from renderer import Renderer
from stopdrop import Stopdrop


def main():
    display = pygame.display.set_mode((700,800))
    pygame.init()
    forms = Forms.create_forms()
    block = Block()
    coordinates = block.create_block(forms)
    tetris = Tetris()
    tetris.create_grid()
    tetris.update_grid(coordinates[0], coordinates[1])
    clock = pygame.time.Clock()
    clock.tick(60)
    speed = 500
    time1 = 0
    time2 = 0
    down = False
    stopdrop = Stopdrop(tetris, block)
    renderer = Renderer(display, tetris)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    down = True
                if event.key == pygame.K_LEFT:
                    results = block.move_block("L")
                    if results == "no change":
                        continue
                    else:
                        old = results[0]
                        new = results[1]
                        tetris.update_grid(old, new)
                if event.key == pygame.K_RIGHT:
                    results = block.move_block("R")
                    if results == "no change":
                        continue
                    else:
                        old = results[0]
                        new = results[1]
                        tetris.update_grid(old, new)
                if event.key == pygame.K_UP:
                    block.rotate_block() 
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    down = False
                        
            if event.type == pygame.QUIT:
                    exit()
            
        time1 = pygame.time.get_ticks()
        if down == True:
            speed = 100
        else:
            speed = 500
        if time1 - time2 > speed:
            results = stopdrop.drop()
            if results != None:
                block = Block()
                coordinates = block.create_block(forms)
                stopdrop = Stopdrop(tetris, block)
                tetris.update_grid(coordinates[0], coordinates[1])
                print(tetris.grid)
            time2 = pygame.time.get_ticks()
        
        renderer.render()
        

if __name__ == "__main__":
    main()