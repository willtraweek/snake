from .tile import Tile


class Board:
    def __init__(self, size: int, num_tiles: int = 10):
        self.tiles = {}

        offset = size//num_tiles // 2  # THIS ALLOWS US TO CENTER THE TILES

        for x in range(num_tiles):
            pos_x = (size//num_tiles) * x + offset

            for y in range(num_tiles):
                pos_y = (size//num_tiles) * y + offset

                self.tiles[(x, y)] = Tile((pos_x, pos_y), size//num_tiles)

    def draw(self, display_surface):
        for tile in self.tiles.values():
            tile.draw(display_surface)
