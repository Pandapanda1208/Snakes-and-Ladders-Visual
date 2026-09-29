import pygame
from pathlib import Path
import random

current_dir = Path(__file__).resolve().parent
img_dir = current_dir / "static"

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        
        self.image = pygame.image.load(image_path).convert_alpha()
        
        self.rect = self.image.get_rect()
        
        self.rect.topleft = (x, y)




pygame.init()

flags = pygame.FULLSCREEN | pygame.SCALED | pygame.DOUBLEBUF
logical_size = (1366, 768)
screen = pygame.display.set_mode(logical_size, flags)
