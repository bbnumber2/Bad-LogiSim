import pygame
from constants import Display, Text, Component
from textbox import Textbox
from power_node import PowerNode


class Simulation:
    """
    Displays the application on the screen and creates all functionality
    """
    def __init__(self) -> None:
        pygame.init()
        self.screen = None

    def create_window(self) -> None:
        self.screen = pygame.display.set_mode(Display.WINDOW_SIZE)
        self.screen.fill(Display.BACKGROUND_COLOR)
        foreground_rect = pygame.Rect(Display.FOREGROUND_POSITION,
                                      Display.FOREGROUND_SIZE)
        pygame.draw.rect(self.screen, Display.FOREGROUND_COLOR,
                         foreground_rect, width=Display.FOREGROUND_WIDTH,
                         border_radius=Display.FOREGROUND_RADIUS)

    def start(self) -> None:
        objects = []
        textbox_font = pygame.font.Font(Text.FONT_FILENAME, Text.FONT_SIZE)
        textbox = Textbox(Text.TEXTBOX_POSITION, Text.TEXTBOX_SIZE,
                          Text.TEXTBOX_BACKGROUND_COLOR,
                          Text.TEXTBOX_OUTLINE_POSITION,
                          Text.TEXTBOX_OUTLINE_COLOR,
                          Text.TEXTBOX_OUTLINE_WIDTH,
                          Text.TEXTBOX_OUTLINE_RADIUS, textbox_font,
                          Text.COLOR, Text.TEXTBOX_TEXT_POSITION)
        power_node = PowerNode((300, 300), (25, 25),
                               Component.PowerNode.OUTLINE_COLOR,
                               Component.PowerNode.OUTLINE_THICKNESS,
                               Component.PowerNode.UNPOWERED_COLOR,
                               Component.PowerNode.POWERED_COLOR)
        objects.append(textbox)
        objects.append(power_node)
        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    break
                elif e.type == pygame.KEYDOWN:
                    key = e.key
                    if key == pygame.K_ESCAPE:
                        running = False
                        break
                    # Should be replaced with more versatile keyboard in future
                    if textbox.selected:
                        if key == pygame.K_BACKSPACE:
                            textbox.remove_character()
                        else:
                            textbox.add_character(chr(key))
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    button = e.button
                    pos = e.pos
                    if button == 1:
                        for object in objects:
                            if object.rect.collidepoint(pos):
                                object.click()
                                continue
                            object.unclick()
            for object in objects:
                object.update()
                object.render(self.screen)
            # Should be replaced with pygame.display.update() at some point
            pygame.display.flip()


if __name__ == '__main__':
    sim = Simulation()
    sim.create_window()
    sim.start()
