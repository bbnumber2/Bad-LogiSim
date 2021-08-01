from typing import Tuple
from app_object import AppObject
from pygame import font, surface


class Textbox(AppObject):
    """Creates a textbox at the given position"""
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int],
                 background_color: Tuple[int, int, int],
                 text_color: Tuple[int, int, int],
                 font: font.Font) -> None:
        super().__init__(position)
        self.size = size
        self.background_color = background_color
        self.surface = surface.Surface(size).fill(background_color)
        self.text_color = text_color
        self.text = ''

    def click(self) -> None:
        self.text = '|' + self.text[1:]

    def type(self, character: str) -> None:
        pass
