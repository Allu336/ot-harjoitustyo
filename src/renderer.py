import pygame

class Renderer():
    def __init__(self, display, tetris):
        self.display = display
        self.tetris = tetris
    
    def render(self):
        self.display.fill((0,0,0))
        pygame.draw.line(self.display,(255,255,255),(200,100),(500,100),2)
        pygame.draw.line(self.display,(255,255,255),(200,100),(200,700),2)
        pygame.draw.line(self.display,(255,255,255),(470,50),(500,50),2)
        pygame.draw.line(self.display,(255,255,255),(500,100),(500,700),2)
        pygame.draw.line(self.display,(255,255,255),(200,700),(500,700),2)
        for y in range(0,20):
            for x in range(0,10):
                if self.tetris.grid[y][x] == ".":
                    x1=200+x*30
                    y1=100+y*30
                    pygame.draw.rect(self.display,(255,255,255),(x1,y1,30,30),1)
                if self.tetris.grid[y][x] == "1":
                    x1=200+x*30
                    y1=100+y*30
                    pygame.draw.rect(self.display,(255,255,255),(x1,y1,30,30))
                if self.tetris.grid[y][x] == "2":
                    x1=200+x*30
                    y1=100+y*30
                    pygame.draw.rect(self.display,(100,255,100),(x1,y1,30,30))
        pygame.display.update()