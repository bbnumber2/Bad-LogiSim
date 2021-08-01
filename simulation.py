import pygame
from pygame import font, display, event, draw, Rect
from constants import Display, Text


class Simulation:
    """
    Displays the application on the screen and creates all functionality
    """
    def __init__(self) -> None:
        pygame.init()
        self.window_size = Display.WINDOW_SIZE.value
        self.background_color = Display.BACKGROUND_COLOR.value
        self.foreground_color = Display.FOREGROUND_COLOR.value
        self.foreground_position = Display.FOREGROUND_POSITION.value
        self.foreground_size = Display.FOREGROUND_SIZE.value
        self.foreground_width = Display.FOREGROUND_WIDTH.value
        self.foreground_radius = Display.FOREGROUND_RADIUS.value
        self.font = font.Font(Text.FONT_FILENAME.value, Text.FONT_SIZE.value)
        self.screen = None

    def create_window(self) -> None:
        self.screen = display.set_mode(self.window_size)
        self.screen.fill(self.background_color)
        foreground_rect = Rect(self.foreground_position, self.foreground_size)
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


if __name__ == '__main__':
    sim = Simulation()
    sim.create_window()
    sim.start()
