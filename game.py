import pygame
from pathlib import Path
import random

current_dir = Path(__file__).resolve().parent
static_dir = current_dir / "Static"

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, sx, sy):
        super().__init__()
        
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (sx, sy))

        self.rect = self.image.get_rect()
        
        self.rect.topleft = (x, y)




pygame.init()

flags = pygame.FULLSCREEN | pygame.SCALED | pygame.DOUBLEBUF
logical_size = (1366, 768)
screen = pygame.display.set_mode(logical_size, flags)

board = Sprite(static_dir / "Board.png", 0, 0, 768, 768)


run = True
while run:
    screen.fill((0, 0, 0))

    screen.blit(board.image, board.rect)


    pygame.display.flip()


    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE] == True:
        run = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False