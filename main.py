import pygame
from pygame.locals import *
import sys
from base_game.board import Board
from base_game.tile import Direction
from base_game.menu import Menu

pygame.init()
FPS = 5
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
BOARD_SIZE = 400
BACKGROUND_COLOR = (128, 128, 128)
MENU_WIDTH = WINDOW_WIDTH - BOARD_SIZE
pygame_clock = pygame.time.Clock()

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")


def main():
    board = Board(BOARD_SIZE, offset=MENU_WIDTH)
    menu = Menu(MENU_WIDTH, WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR)

    current_direction = Direction.EAST
    potential_direction = current_direction

    while True:
        menu.draw(display)
        board.draw(display)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # THE BELOW CODE ALLOWS FOR SAFE DIRECTION PICKING.  IT WON'T ALLOW THE SNAKE TO TURN IN A DIRECTION
                # WHERE IT WOULD IMMEDIATELY DIE. FOR EXAMPLE, BY HITTING ITSELF.
                if event.key in [K_UP, K_w]:
                    potential_direction = current_direction.NORTH
                elif event.key in [K_RIGHT, K_d]:
                    potential_direction = current_direction.EAST
                elif event.key in [K_DOWN, K_s]:
                    potential_direction = current_direction.SOUTH
                elif event.key in [K_LEFT, K_a]:
                    potential_direction = current_direction.WEST

                if board.check_move(potential_direction):
                    current_direction = potential_direction

        try:
            board.move(current_direction)
        except RuntimeError:
            board.reset()
        pygame.display.flip()
        pygame_clock.tick(FPS)


if __name__ == '__main__':
    main()
