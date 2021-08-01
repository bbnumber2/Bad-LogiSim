from typing import Tuple
from pygame import pygame, font, display, event


class Simulation:
    """
    Displays the application on the screen and creates all functionality
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
        self.font = font.Font(font_filename, font_size)
        self.screen = None

    def create_window(self) -> None:
        self.screen = display.set_mode(self.window_size)
        self.screen.fill(self.background_color)

    def start(self) -> None:
        quit = event.Event(pygame.QUIT)
        while not event.get(pygame.QUIT):
            for e in event.get():
                if e.type == pygame.KEYDOWN:
                    key = e.key
                    if key == pygame.K_ESCAPE:
                        pygame.event.post(quit)
            # Should be replaced with display.update() at some point
            display.flip()


sim = Simulation((500, 500), (30, 30, 30), (0, 0, 0),
                 'Resources/LiberationSans-Regular.ttf', 16)
sim.create_window()
sim.start()