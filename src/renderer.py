import pygame

class Renderer():
    def __init__(self, display, tetris, game):
        self.display = display
        self.tetris = tetris
        self.game = game
        self.font = pygame.font.SysFont("freesansbold.ttf", 50)
    
    def render(self, next):
        self.display.fill((0,0,0))
        score = self.font.render("Score: "+str(self.game.score), True, (255, 255, 255))
        self.display.blit(score, (20, 20))
        next_text = self.font.render("Next:", True, (255, 255, 255))
        self.display.blit(next_text, (540, 250))
        pygame.draw.rect(self.display,(50,50,50),(200,100,300,600))
        pygame.draw.line(self.display,(200,200,200),(200,100),(500,100),2)
        pygame.draw.line(self.display,(200,200,200),(200,100),(200,700),2)
        pygame.draw.line(self.display,(200,200,200),(500,100),(500,700),2)
        pygame.draw.line(self.display,(200,200,200),(200,700),(500,700),2)
        for y in range(0,20):
            for x in range(0,10):
                if self.tetris.grid[y][x] == ".":
                    x1=200+x*30
                    y1=100+y*30
                    pygame.draw.rect(self.display,(0,0,0),(x1,y1,30,30),1)
                if self.tetris.grid[y][x] == "1":
                    x1=200+x*30
                    y1=100+y*30
                    pygame.draw.rect(self.display,(255,255,255),(x1,y1,30,30))
                    pygame.draw.rect(self.display,(0,0,0),(x1,y1,30,30),1)
                if self.tetris.grid[y][x] == "2":
                    x1=200+x*30
                    y1=100+y*30
                    pygame.draw.rect(self.display,(100,255,100),(x1,y1,30,30))
                    pygame.draw.rect(self.display,(0,0,0),(x1,y1,30,30),1)

        if next == 0:
            pygame.draw.rect(self.display, (0,255,255), (580,330,30,30))
            pygame.draw.rect(self.display, (0,255,255), (580,362,30,30))
            pygame.draw.rect(self.display, (0,255,255), (580,394,30,30))
            pygame.draw.rect(self.display, (0,255,255), (580,426,30,30))

        elif next == 1:
            pygame.draw.rect(self.display, (0,0,255), (550,330,30,30))
            pygame.draw.rect(self.display, (0,0,255), (582,330,30,30))
            pygame.draw.rect(self.display, (0,0,255), (614,330,30,30))
            pygame.draw.rect(self.display, (0,0,255), (614,362,30,30))

        elif next == 2:
            pygame.draw.rect(self.display, (255,100,10), (550,330,30,30))
            pygame.draw.rect(self.display, (255,100,10), (582,330,30,30))
            pygame.draw.rect(self.display, (255,100,10), (614,330,30,30))
            pygame.draw.rect(self.display, (255,100,10), (550,362,30,30))

        elif next == 3:
            pygame.draw.rect(self.display, (255,255,0), (570,330,30,30))
            pygame.draw.rect(self.display, (255,255,0), (602,330,30,30))
            pygame.draw.rect(self.display, (255,255,0), (570,362,30,30))
            pygame.draw.rect(self.display, (255,255,0), (602,362,30,30))

        elif next == 4:
            pygame.draw.rect(self.display, (0,255,0), (572,330,30,30))
            pygame.draw.rect(self.display, (0,255,0), (604,330,30,30))
            pygame.draw.rect(self.display, (0,255,0), (572,362,30,30))
            pygame.draw.rect(self.display, (0,255,0), (540,362,30,30))

        elif next == 5:
            pygame.draw.rect(self.display, (0,0,255), (582,330,30,30))
            pygame.draw.rect(self.display, (0,0,255), (582,362,30,30))
            pygame.draw.rect(self.display, (0,0,255), (614,362,30,30))
            pygame.draw.rect(self.display, (0,0,255), (550,362,30,30))

        elif next == 6:
            pygame.draw.rect(self.display, (255,0,0), (542,330,30,30))
            pygame.draw.rect(self.display, (255,0,0), (574,330,30,30))
            pygame.draw.rect(self.display, (255,0,0), (606,362,30,30))
            pygame.draw.rect(self.display, (255,0,0), (574,362,30,30))
        
        pygame.display.update()
    
    def gameover_screen(self):
        self.display.fill((0,0,0))
