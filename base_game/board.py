from .tile import Tile


class Board:
    def __init__(self, size: int, num_tiles: int = 10):
        self.num_tiles = num_tiles
        self.tiles = {}

        offset = size // num_tiles // 2  # THIS ALLOWS US TO CENTER THE TILES

        for x in range(num_tiles):
            pos_x = (size // num_tiles) * x + offset

            for y in range(num_tiles):
                pos_y = (size // num_tiles) * y + offset

                self.tiles[(x, y)] = Tile((pos_x, pos_y), size // num_tiles - 2, (255, 255, 255))

        self.setup_references()

    def setup_references(self):
        for x in range(self.num_tiles):
            for y in range(self.num_tiles):
                tile = self.tiles[(x, y)]
                if x != 0:
                    tile.north = self.tiles[x - 1, y]
                if x != self.num_tiles - 1:  # NEEDS THE -1 BECAUSE 0-BASED INDEXING
                    tile.south = self.tiles[x + 1, y]
                if y != 0:
                    tile.west = self.tiles[x, y - 1]
                if y != self.num_tiles - 1:
                    tile.east = self.tiles[x, y + 1]

    def draw(self, display_surface):
        for tile in self.tiles.values():
            tile.draw(display_surface)
