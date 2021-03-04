import pygame
from pygame.locals import *
import sys
from base_game.board import Board
from base_game.tile import Direction
from base_game.menu import Menu
from enum import Enum
from ai import custom_agent

pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
BOARD_SIZE = 400
BACKGROUND_COLOR = (128, 128, 128)
MENU_WIDTH = WINDOW_WIDTH - BOARD_SIZE
pygame_clock = pygame.time.Clock()

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")


class Player(Enum):
    HUMAN = 0
    AI = 1


def main():
    FPS = 5
    move_count = 0
    board = Board(BOARD_SIZE, offset=MENU_WIDTH)
    custom_agent.DNA.input_length = len(board.get_ai_inputs())
    population = custom_agent.Population(100)
    menu = Menu(MENU_WIDTH, WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR)

    current_direction = Direction.EAST if board.check_move(Direction.EAST) else Direction.WEST
    potential_direction = current_direction

    player = Player.HUMAN

    while True:
        menu.draw(display)
        if player == Player.AI:
            menu.draw_ai(display)
        board.draw(display)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in [K_7]:
                    FPS = 5
                elif event.key in [K_8]:
                    FPS = 30
                elif event.key in [K_9]:
                    FPS = 1000
                # THE BELOW CODE ALLOWS FOR SAFE DIRECTION PICKING.  IT WON'T ALLOW THE SNAKE TO TURN IN A DIRECTION
                # WHERE IT WOULD IMMEDIATELY DIE. FOR EXAMPLE, BY HITTING ITSELF.
                if event.key in [K_UP, K_w] and player == Player.HUMAN:
                    potential_direction = current_direction.NORTH
                elif event.key in [K_RIGHT, K_d] and player == Player.HUMAN:
                    potential_direction = current_direction.EAST
                elif event.key in [K_DOWN, K_s] and player == Player.HUMAN:
                    potential_direction = current_direction.SOUTH
                elif event.key in [K_LEFT, K_a] and player == Player.HUMAN:
                    potential_direction = current_direction.WEST

                # THE CODE BELOW ALLOWS THE USER TO SELECT IF HE WANTS TO PLAY OR IF THE AI SHOULD
                if event.key in [K_1]:
                    player = Player.HUMAN
                    board.reset()
                elif event.key in [K_2]:
                    player = Player.AI
                    board.reset()

        if player == Player.AI:
            potential_direction = custom_agent.predict(population, board.get_ai_inputs())

        if board.check_move(potential_direction):
            current_direction = potential_direction

        try:
            Menu.direction = current_direction
            move_count += 1
            Menu.moves = move_count
            board.move(current_direction)

            if Menu.score < 5 and move_count > 200:
                # AT THIS POINT, THE AI ISN'T DOING ANYTHING, BUT RUNNING IN CIRCLES
                move_count = 10  # WE WANT TO PUNISH THIS ACTIVITY, so we lower the move count
                raise RuntimeError
        except RuntimeError:
            current_direction = Direction.EAST if board.check_move(Direction.EAST) else Direction.WEST
            if player == Player.AI:
                population.set_current_fitness(Menu.score, move_count)
                Menu.generation = population.generation
                Menu.individual = population.current
            board.reset()
            move_count = 0
        pygame.display.flip()
        pygame_clock.tick(FPS)


if __name__ == '__main__':
    main()
