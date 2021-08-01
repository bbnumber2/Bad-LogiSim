from typing import Tuple
from pygame import surface


class AppObject:
    def __init__(self, position: Tuple[int, int]) -> None:
        self.position = position
        self.surface = None

    def draw(self, screen: surface.Surface) -> None:
        screen.blit(self.surface, self.position)

    def move(self, new_position: Tuple[int, int]) -> None:
        self.position = new_position

    def click(self) -> None:
        pass

    def update(self) -> None:
        pass
