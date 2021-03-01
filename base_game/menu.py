import pygame
from base_game.tile import Direction


class Menu:
    score = 0
    high_score = 0
    generation = 0
    individual = 0
    direction = Direction.EAST
    moves = 0
    average_score = 0
    average_fit = 0
    average_move_count = 0

    def __init__(self, menu_width, window_width, window_height, background_color):
        self.font = pygame.font.SysFont("Verdana", 20)
        self.menu_width = menu_width
        self.window_width = window_width
        self.window_height = window_height
        self.background_color = background_color

    def draw(self, display):
        # CLEAR THE MENU
        display.fill(self.background_color, (0, 0, self.window_width, self.window_height))

        score = self.font.render(f"Score: {self.score}", True, pygame.Color("black"))
        display.blit(score, (10, 10))

        high_score = self.font.render(f"High Score: {self.high_score}", True, pygame.Color("black"))
        display.blit(high_score, (10, 30))

        direction = self.font.render(f"Direction: {self.direction.name}", True, pygame.Color("black"))
        display.blit(direction, (10, 50))

        moves = self.font.render(f"Moves: {self.moves}", True, pygame.Color("black"))
        display.blit(moves, (10, 70))

    def draw_ai(self, display):
        generation = self.font.render(f"Generation: {self.generation}", True, pygame.Color("black"))
        display.blit(generation, (10, 90))

        individual = self.font.render(f"Individual: {self.individual}", True, pygame.Color("black"))
        display.blit(individual, (10, 110))

        average_score = self.font.render(f"Avg Score: {self.average_score}", True, pygame.Color("black"))
        display.blit(average_score, (10, 130))

        average_fit = self.font.render(f"Avg Fit: {self.average_fit}", True, pygame.Color("black"))
        display.blit(average_fit, (10, 150))

        average_move_count = self.font.render(f"Avg Moves: {self.average_move_count}", True, pygame.Color("black"))
        display.blit(average_move_count, (10, 170))

    @staticmethod
    def reset_score():
        if Menu.score > Menu.high_score:
            Menu.high_score = Menu.score

        Menu.score = 0
