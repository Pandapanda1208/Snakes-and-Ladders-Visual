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

        radius = 30
        
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



places = [(0, (0, 800)), (1, (65, 702)), (2, (135, 702)), (3, (205, 702)), (4, (277, 702)), (5, (347, 702)), (6, (419, 702)), (7, (489, 702)), (8, (559, 702)), (9, (631, 702)), (10, (703, 702)), (11, (703, 632)), (12, (631, 632)), (13, (559, 632)), (14, (489, 632)), (15, (419, 632)), (16, (347, 632)), (17, (277, 632)), (18, (205, 632)), (19, (135, 632)), (20, (65, 632)), (21, (65, 562)), (22, (135, 562)), (23, (205, 7562)), (24, (277, 562)), (25, (347, 562)), (26, (419, 562)), (27, (489, 562)), (28, (559, 562)), (29, (631, 562)), (30, (703, 562)), (31, (703, 490)), (32, (631, 490)), (33, (559, 490)), (34, (489, 490)), (35, (419, 490)), (36, (347, 490)), (37, (277, 490)), (38, (205, 490)), (39, (135, 490)), (40, (65, 490)), (41, (65, 420)), (42, (135, 420)), (43, (205, 420)), (44, (277, 420)), (45, (347, 420)), (46, (419, 420)), (47, (489, 420)), (48, (559, 420)), (49, (631, 420)), (50, (703, 420)), (51, (703, 348)), (52, (631, 348)), (53, (559, 348)), (54, (489, 348)), (55, (419, 348)), (56, (347, 348)), (57, (277, 348)), (58, (205, 348)), (59, (135, 348)), (60, (65, 348)), (61, (65, 278)), (62, (135, 278)), (63, (205, 278)), (64, (277, 278)), (65, (347, 278)), (66, (419, 278)), (67, (489, 278)), (68, (559, 278)), (69, (631, 278)), (70, (703, 278)), (71, (703, 208)), (72, (631, 208)), (73, (559, 208)), (74, (489, 208)), (75, (419, 208)), (76, (347, 208)), (77, (277, 208)), (78, (205, 208)), (79, (135, 208)), (80, (65, 208)), (81, (65, 136)), (82, (135, 136)), (83, (205, 136)), (84, (277, 136)), (85, (347, 136)), (86, (419, 136)), (87, (489, 136)), (88, (559, 136)), (89, (631, 136)), (90, (703, 136)), (91, (703, 65)), (92, (631, 65)), (93, (559, 65)), (94, (489, 65)), (95, (419, 65)), (96, (347, 65)), (97, (277, 65)), (98, (205, 65)), (99, (135, 65)), (100, (65, 65))]

globals()['player1'].pos = 1

run = True
while run:
    screen.fill((0, 0, 0))

    screen.blit(board.image, board.rect)

    all_players.draw(screen)

    pygame.display.flip()


    for i in range(players):
        globals()[f'player{i + 1}'].rect.centerx = places[globals()[f'player{i + 1}'].pos][1][0]
        globals()[f'player{i + 1}'].rect.centery = places[globals()[f'player{i + 1}'].pos][1][1]




    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE] == True:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(players):
                globals()[f'player{i + 1}'].pos += 1