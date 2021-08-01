from typing import Tuple
from pygame import font


class Textbox:
    """Creates a textbox at the given x and y coordinates"""
    def __init__(self, x: int, y: int, size: Tuple[int, int],
                 cursor_color: Tuple[int, int, int],
                 font: font.Font) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.cursor_color = cursor_color

    def click(self) -> None:
        pass

    def type(self, character: str) -> None:
        pass
