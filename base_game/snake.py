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
