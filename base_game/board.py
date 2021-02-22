from .tile import Tile, TileType, Direction
import random


class Board:
    def __init__(self, size: int, num_tiles: int = 10):
        self.num_tiles = num_tiles
        self.tiles = {}

        offset = size // num_tiles // 2  # THIS ALLOWS US TO CENTER THE TILES

        for x in range(num_tiles):
            pos_x = (size // num_tiles) * x + offset

            for y in range(num_tiles):
                pos_y = (size // num_tiles) * y + offset

                self.tiles[(x, y)] = Tile((pos_x, pos_y), size // num_tiles - 2)

        self.setup_references()

    def setup_references(self):
        """
        Iterates through the list of tiles and gets references to the bordering tiles, then gives the tile that
        information
        """
        for x in range(self.num_tiles):
            for y in range(self.num_tiles):
                tile = self.tiles[(x, y)]
                if x != 0:
                    tile.border[Direction.NORTH] = self.tiles[x - 1, y]
                if x != self.num_tiles - 1:  # NEEDS THE -1 BECAUSE 0-BASED INDEXING
                    tile.border[Direction.SOUTH] = self.tiles[x + 1, y]
                if y != 0:
                    tile.border[Direction.WEST] = self.tiles[x, y - 1]
                if y != self.num_tiles - 1:
                    tile.border[Direction.EAST] = self.tiles[x, y + 1]

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
