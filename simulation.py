from typing import Tuple
import pygame


class Simulation:
    """
    Creates the simulation window for the application.
    """
    def __init__(self,
                 window_size: Tuple[int, int],
                 background_color: Tuple[int, int, int],
                 foreground_color: Tuple[int, int, int],
                 font_filename: str,
                 font_size: int) -> None:
        pygame.init()
        self.window_size = window_size
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.font = pygame.font.Font(font_filename, font_size)
        self.screen = None

    def create_window(self):
        self.screen = pygame.display.set_mode(self.window_size)
        self.screen.fill(self.background_color)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()


sim = Simulation((500, 500), (30, 30, 30), (0, 0, 0),
                 'Resources/LiberationSans-Regular.ttf', 16)
sim.create_window()
