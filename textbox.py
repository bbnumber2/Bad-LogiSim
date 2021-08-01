from typing import Tuple
from app_object import AppObject
from pygame import font, surface, rect, draw


class Textbox(AppObject):
    """Creates a textbox at the given position"""
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int],
                 background_color: Tuple[int, int, int],
                 outline_color: Tuple[int, int, int],
                 outline_width: int,
                 outline_radius: int,
                 font: font.Font,
                 text_color: Tuple[int, int, int],
                 text_position: Tuple[int, int]) -> None:
        super().__init__(position)
        self.size = size
        self.background_color = background_color
        self.surface = surface.Surface(size)
        self.surface.fill(self.background_color)
        self.outline = rect.Rect(position, size)
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.outline_radius = outline_radius
        self.font = font
        self.text_color = text_color
        self.text_position = text_position
        self.text = ''

    def click(self) -> None:
        self.selected = True

    def update(self) -> None:
        self.surface.fill(self.background_color)
        if self.selected:
            draw.rect(self.surface, self.outline_color, self.outline,
                      border_radius=self.outline_radius,
                      width=self.outline_width)
            text_surface = self.font.render('| ' + self.text, True,
                                            self.text_color)
        else:
            text_surface = self.font.render('  ' + self.text, True,
                                            self.text_color)
        self.surface.blit(text_surface, self.text_position)

    def add_character(self, character) -> None:
        self.text += character

    def remove_character(self) -> None:
        self.text = self.text[:-1]
