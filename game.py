import pygame
from pathlib import Path
import random

current_dir = Path(__file__).resolve().parent
static_dir = current_dir / "Static"

class Image(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, sx, sy):
        super().__init__()
        
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (sx, sy))

        self.rect = self.image.get_rect()
        
        self.rect.topleft = (x, y)


class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, name, pos):
        super().__init__()
        
        self.name = name
        self.pos = pos

        radius = 25
        
        diameter = radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        
        self.rect = self.image.get_rect(center=(x, y))



players = int(input("How many people are playing? (1-4) "))

while players < 1 or players > 4:
    print('It needs to be between 1 and four players.')
    players = int(input("How many people are playing? (1-4) "))


if players == 1:
    p1 = input("What is your Player1's name? ")
elif players == 2:
    p1 = input("What is your Player1's name? ")
    p2 = input("What is your Player2's name? ")
elif players == 3:
    p1 = input("What is your Player1's name? ")
    p2 = input("What is your Player2's name? ")
    p3 = input("What is your Player3's name? ")
elif players == 4:
    p1 = input("What is your Player1's name? ")
    p2 = input("What is your Player2's name? ")
    p3 = input("What is your Player3's name? ")
    p4 = input("What is your Player4's name? ")



pygame.init()


all_players = pygame.sprite.Group()
colors = [(255, 0, 255), (255, 255, 0), (0, 255, 0), (0, 0, 255)]

for i in range(players):
    globals()[f'player{i + 1}'] = Player(colors[i], 800, 500, f'p{i + 1}', 0)
    all_players.add(globals()[f'player{i + 1}']) 



flags = pygame.FULLSCREEN | pygame.SCALED | pygame.DOUBLEBUF
logical_size = (1366, 768)
screen = pygame.display.set_mode(logical_size, flags)

board = Image(static_dir / "Board.png", 0, 0, 768, 768)


run = True
while run:
    screen.fill((0, 0, 0))

    screen.blit(board.image, board.rect)

    all_players.draw(screen)

    pygame.display.flip()


    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE] == True:
        run = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False