import pygame
from pygame import font, display, event, draw, Rect
from constants import Display, Text
from textbox import Textbox


class Simulation:
    """
    Displays the application on the screen and creates all functionality
    """
    def __init__(self) -> None:
        pygame.init()
        self.screen = None

    def create_window(self) -> None:
        self.screen = display.set_mode(Display.WINDOW_SIZE)
        self.screen.fill(Display.BACKGROUND_COLOR)
        foreground_rect = Rect(Display.FOREGROUND_POSITION,
                               Display.FOREGROUND_SIZE)
        draw.rect(self.screen, Display.FOREGROUND_COLOR, foreground_rect,
                  width=Display.FOREGROUND_WIDTH,
                  border_radius=Display.FOREGROUND_RADIUS)

    def start(self) -> None:
        objects = []
        textbox_font = font.Font(Text.FONT_FILENAME, Text.FONT_SIZE)
        textbox = Textbox(Text.TEXTBOX_POSITION, Text.TEXTBOX_SIZE,
                          Text.TEXTBOX_BACKGROUND_COLOR,
                          Text.TEXTBOX_OUTLINE_COLOR,
                          Text.TEXTBOX_OUTLINE_WIDTH,
                          Text.TEXTBOX_OUTLINE_RADIUS, textbox_font,
                          Text.COLOR, Text.TEXTBOX_TEXT_POSITION)
        objects.append(textbox)
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
            for object in objects:
                object.update()
                object.render(self.screen)
            # Should be replaced with display.update() at some point
            display.flip()


if __name__ == '__main__':
    sim = Simulation()
    sim.create_window()
    sim.start()
