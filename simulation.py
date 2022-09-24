import pygame
from constants import Display, Text
from textbox import Textbox


class Simulation:
    """
    Displays the application on the screen and creates all functionality
    """
    def __init__(self) -> None:
        pygame.init()
        self.screen = None
        self.textbook = None
        self.objects = []

    def create_window(self) -> None:
        self.screen = pygame.display.set_mode(Display.WINDOW_SIZE)
        self.screen.fill(Display.BACKGROUND_COLOR)
        foreground_rect = pygame.Rect(Display.FOREGROUND_POSITION,
                                      Display.FOREGROUND_SIZE)
        pygame.draw.rect(self.screen, Display.FOREGROUND_COLOR,
                         foreground_rect, width=Display.FOREGROUND_WIDTH,
                         border_radius=Display.FOREGROUND_RADIUS)
    
    def handle_event(self, event: pygame.event) -> bool:
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_ESCAPE:
                return False
            # Should be replaced with better keyboard in future
            if self.textbox.selected:
                if key == pygame.K_BACKSPACE:
                    self.textbox.remove_character()
                else:
                    self.textbox.add_character(chr(key))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button = event.button
            pos = event.pos
            if button == 1:
                for object in self.objects:
                    if object.rect.collidepoint(pos):
                        object.click()
                        continue
                    object.unclick()
        return True

    def start(self) -> None:
        textbox_font = pygame.font.Font(Text.FONT_FILENAME, Text.FONT_SIZE)
        self.textbox = Textbox(Text.TEXTBOX_POSITION, Text.TEXTBOX_SIZE,
                          Text.TEXTBOX_BACKGROUND_COLOR,
                          Text.TEXTBOX_OUTLINE_POSITION,
                          Text.TEXTBOX_OUTLINE_COLOR,
                          Text.TEXTBOX_OUTLINE_WIDTH,
                          Text.TEXTBOX_OUTLINE_RADIUS, textbox_font,
                          Text.COLOR, Text.TEXTBOX_TEXT_POSITION)
        self.objects.append(self.textbox)
        running = True
        while running:
            for e in pygame.event.get():
                running = self.handle_event(e)
            for object in self.objects:
                object.update()
                object.render(self.screen)
            # Should be replaced with pygame.display.update() at some point
            pygame.display.flip()


if __name__ == '__main__':
    sim = Simulation()
    sim.create_window()
    sim.start()
