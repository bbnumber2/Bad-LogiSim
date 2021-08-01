from typing import Tuple
import pygame
from pygame import font, display, event, draw, Rect


class Simulation:
    """
    Displays the application on the screen and creates all functionality
    """
    def __init__(self,
                 window_size: Tuple[int, int],
                 background_color: Tuple[int, int, int],
                 foreground_color: Tuple[int, int, int],
                 foreground_location: int,
                 foreground_size: int,
                 foreground_width: int,
                 foreground_radius: int,
                 font_filename: str,
                 font_size: int,) -> None:
        pygame.init()
        self.window_size = window_size
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.foreground_color = foreground_color
        self.foreground_location = foreground_location
        self.foreground_size = foreground_size
        self.foreground_width = foreground_width
        self.foreground_radius = foreground_radius
        self.font = font.Font(font_filename, font_size)
        self.screen = None

    def create_window(self) -> None:
        self.screen = display.set_mode(self.window_size)
        self.screen.fill(self.background_color)
        foreground_rect = Rect(self.foreground_location, self.foreground_size)
        draw.rect(self.screen, self.foreground_color, foreground_rect,
                  width=self.foreground_width,
                  border_radius=self.foreground_radius)

    def start(self) -> None:
        running = True
        while running:
            for e in event.get():
                if e.type == pygame.QUIT:
                    running = False
                    break
                if e.type == pygame.KEYDOWN:
                    key = e.key
                    if key == pygame.K_ESCAPE:
                        running = False
                        break
            # Should be replaced with display.update() at some point
            display.flip()


sim = Simulation((1000, 700), (30, 30, 30), (90, 90, 90),
                 (40, 90), (920, 550), 2, 5,
                 'Resources/LiberationSans-Regular.ttf', 16)
sim.create_window()
sim.start()
