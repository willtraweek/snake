import pygame
from enum import Enum
from typing import Optional

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class TileType(Enum):
    BLANK = 0
    FOOD = 1


class Tile:
    def __init__(self, pos: (int, int), size: int, color: (int, int, int) = (0, 0, 0)):
        self.surface = pygame.Surface((size, size))
        self.pos = pos
        self.color = color
        self.rect = self.surface.get_rect(center=pos)
        self.type = TileType.BLANK

        self.north: Optional[Tile] = None
        self.east: Optional[Tile] = None
        self.south: Optional[Tile] = None
        self.west: Optional[Tile] = None

    def draw(self, display_surface):
        display_surface.blit(self.surface, self.rect)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: (int, int, int) = (0, 0, 0)):
        self.__color = color
        self.surface.fill(color)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: TileType):
        self.__type = type
        if type == TileType.BLANK:
            self.color = BLACK
        elif type == TileType.FOOD:
            self.color = RED
