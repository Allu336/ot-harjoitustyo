import pygame
import random
from Tetris import Tetris
from block import Block
from block_forms import Forms
from renderer import Renderer


def main():
    display = pygame.display.set_mode((700,800))
    pygame.init()
    forms = Forms.create_forms()
    block = Block()
    block.create_block(forms)
    tetris = Tetris()
    tetris.create_grid()
    clock = pygame.time.Clock()
    clock.tick(60)
    speed = 500
    time2 = 0

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_DOWN:
                    down = True
                if tapahtuma.key == pygame.K_LEFT:
                    results = block.move_block("L")
                    Tetris.update_grid(results)
                if tapahtuma.key == pygame.K_RIGHT:
                    results = Block.move_block("L")
                    Tetris.update_grid(results)
                if tapahtuma.key == pygame.K_UP:
                    Tetris.rotate_block() 
                
            if tapahtuma.type==pygame.KEYUP:
                if tapahtuma.key==pygame.K_DOWN:
                    down = False
                        
            if tapahtuma.type==pygame.QUIT:
                    exit()
            
            time1 = pygame.time.get_ticks()
            if down == True:
                speed = 100
            else:
                speed = 500
            if time1 - time2 > speed:
                self.tiputa()
                time2 = pygame.time.get_ticks()
        render = Renderer()
        pygame.display.flip()
        

if __name__ == "__main__":
    main()