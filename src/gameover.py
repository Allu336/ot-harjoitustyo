import pygame

class Game:
    def __init__(self, score, display, tetris):
        self.display = display
        self.score = score
        self.tetris = tetris
        self.speed = 0
        self.exc = 0

    def gameover(self):
        font = pygame.font.SysFont("freesansbold.ttf", 80)
        font2 = pygame.font.SysFont("freesansbold.ttf", 60)
        self.display.fill((0,0,0))
        pygame.draw.rect(self.display, (100,100,100), (230,380,250,80))
        gameover = font.render("Game Over", True, (255, 255, 255))
        self.display.blit(gameover, (200,200))
        again = font2.render("Try again", True, (255, 255, 255))
        self.display.blit(again, (255, 400))
        pygame.display.update()
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if 230<pos[0]<480 and 380<pos[1]<460:
                        loop = False
                        break


                if event.type == pygame.QUIT:
                    exit()
        self.score = 0
        self.tetris.grid = []
        self.speed = 500
        self.exc = 0
        for row in range(0,23):
            self.tetris.grid.append([".",".",".",".",".",".",".",".",".","."])
        print(self.tetris.grid)
        return

