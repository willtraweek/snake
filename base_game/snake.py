from base_game.tile import Tile, TileType, Direction
from collections import deque


class Snake:
    def __init__(self, head: Tile, tail_direction: Direction = Direction.WEST):
        self.snake = deque([])
        self.length = len(self.snake)

        # SINCE WE'RE USING A DEQUE, SET TAIL FIRST IF YOU CAN -- IF NOT, JUST SET HEAD
        tail = head.border[tail_direction]
        if self.check_tile(tail):
            self.head = tail
        self.head: Tile = head

    def check_move(self, direction: Direction):
        """
        Allows checking for whether or not a move is okay without making that move

        :param direction: the direction you intend to check
        :return: whether or not the direction is safe
        """
        return self.check_tile(self.head.border[direction])

    def check_tile(self, tile: Tile):
        """
        Checks if a tile is okay to move to.

        :param tile: The tile you intend to move to.
        :return: whether or not the tile is safe
        """
        if tile is None or tile.type == TileType.SNAKE:
            return False
        return True

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, new_head: Tile):
        if self.check_tile(new_head):
            if new_head.type == TileType.FOOD or self.length <= 1:
                self.length += 1
            else:
                old_tail = self.snake.pop()
                old_tail.type = TileType.BLANK

            new_head.type = TileType.SNAKE
            self.snake.appendleft(new_head)
            self.__head = new_head
        else:
            raise RuntimeError("Illegal move made")

    def get_distance_to_wall(self, direction):
        tile = self.head
        output = 0
        tile = tile.border[direction]
        while tile is not None:
            output += 1
            tile = tile.border[direction]
        return output

    def get_distance_to_tile_type(self, direction, max_distance, tile_type):
        tile = self.head
        output = 0
        tile = tile.border[direction]
        while True:
            output += 1
            if tile is None:
                return max_distance
            elif tile.type == tile_type:
                return output
            tile = tile.border[direction]

    def get_distance_to_walls_diagonal(self):
        output = [0, 0, 0, 0]
        for i in range(4):
            tile = self.head

            direction_1 = Direction(i)
            direction_2 = Direction(i+1) if i != 3 else Direction(0)

            try:
                tile = tile.border[direction_1].border[direction_2]
            except AttributeError:
                # OCCURS WHEN THE .border[direction_1] is a nonetype
                tile = tile.border[direction_1]
            while tile is not None:
                output[i] += 1

                try:
                    tile = tile.border[direction_1].border[direction_2]
                except AttributeError:
                    # OCCURS WHEN THE .border[direction_1] is a nonetype
                    tile = tile.border[direction_1]
        return output

    def get_distance_to_tile_type_diagonal(self, max_distance, tile_type):
        output = [0, 0, 0, 0]
        for i in range(4):
            tile = self.head

            direction_1 = Direction(i)
            direction_2 = Direction(i+1) if i != 3 else Direction(0)

            try:
                tile = tile.border[direction_1].border[direction_2]
            except AttributeError:
                # OCCURS WHEN THE .border[direction_1] is a nonetype
                tile = tile.border[direction_1]
            while True:
                output[i] += 1
                if tile is None:
                    output[i] = max_distance
                    break
                elif tile.type == tile_type:
                    break
                try:
                    tile = tile.border[direction_1].border[direction_2]
                except AttributeError:
                    # OCCURS WHEN THE .border[direction_1] is a nonetype
                    tile = tile.border[direction_1]
        return output