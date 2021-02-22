import pygame
from pygame.locals import *
import sys
from base_game.board import Board

pygame.init()
FPS = 60
pygame_clock = pygame.time.Clock()

display = pygame.display.set_mode((400, 400))  # 400 PIXEL SQUARE
display.fill((0, 0, 0))  # SET THE BACKGROUND TO BLACK
pygame.display.set_caption("Snake")

board = Board(400)


def main():
    while True:
        board.draw(display)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame_clock.tick(FPS)


if __name__ == '__main__':
    main()