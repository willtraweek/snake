from .tile import Tile, TileType, Direction
import random
from .snake import Snake


class Board:
    def __init__(self, size: int, num_tiles: int = 10):
        self.num_tiles = num_tiles
        self.tiles = {}

        for x in range(num_tiles):
            pos_x = ((size-num_tiles) // num_tiles) * x + x

            for y in range(num_tiles):
                pos_y = ((size-num_tiles) // num_tiles) * y + y

                self.tiles[(x, y)] = Tile((pos_x, pos_y), size // num_tiles - 1)

        self.setup_references()
        self.setup_snake(num_tiles)

    def setup_references(self):
        """
        Iterates through the list of tiles and gets references to the bordering tiles, then gives the tile that
        information
        """
        for x in range(self.num_tiles):
            for y in range(self.num_tiles):
                tile = self.tiles[(x, y)]
                if x != 0:
                    tile.border[Direction.WEST] = self.tiles[x - 1, y]
                if x != self.num_tiles - 1:  # NEEDS THE -1 BECAUSE 0-BASED INDEXING
                    tile.border[Direction.EAST] = self.tiles[x + 1, y]
                if y != 0:
                    tile.border[Direction.NORTH] = self.tiles[x, y - 1]
                if y != self.num_tiles - 1:
                    tile.border[Direction.SOUTH] = self.tiles[x, y + 1]

    def setup_snake(self, num_tiles):
        middle = num_tiles//2
        self._snake = Snake(self.tiles[(middle, middle)])

    def draw(self, display_surface):
        for tile in self.tiles.values():
            tile.draw(display_surface)

    def get_blank_tiles(self):
        blanks = set()
        for tile in self.tiles.values():
            if tile.type == TileType.BLANK:
                blanks.add(tile)
        return blanks

    def generate_food(self):
        blanks = self.get_blank_tiles()
        tile = random.sample(blanks, 1)[0]
        tile.type = TileType.FOOD
