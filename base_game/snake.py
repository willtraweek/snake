from .tile import Tile, TileType, Direction
from collections import deque


class Snake:
    def __init__(self, head: Tile, tail_direction: Direction = Direction.WEST):
        self.snake = deque([head])
        self.head: Tile = head

        if self.check_move(tail_direction):
            self.head.border[tail_direction].type = TileType.SNAKE
            self.snake.append(head.border[tail_direction])

        self.length = len(self.snake)

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
            new_head.type = TileType.SNAKE
            self.snake.append(new_head)
            self.__head = new_head

            if new_head.type == TileType.FOOD:
                self.length += 1
            else:
                old_tail = self.snake.pop()
                old_tail.type == TileType.BLANK
        else:
            RuntimeError("Illegal move made")
