import pygame


class Menu:
    score = 0
    high_score = 0

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
    @staticmethod
    def reset_score():
        if Menu.score > Menu.high_score:
            Menu.high_score = Menu.score

        Menu.score = 0
