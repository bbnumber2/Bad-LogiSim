from typing import Tuple
from pygame import surface, Rect


class AppObject:
    def __init__(self, position: Tuple[int, int],
                 size: Tuple[int, int]) -> None:
        self.position = position
        self.size = size
        self.rect = Rect(position, size)
        self.surface = None
        self.selected = False

    def render(self, screen: surface.Surface) -> None:
        screen.blit(self.surface, self.position)

    def move(self, new_position: Tuple[int, int]) -> None:
        self.position = new_position

    def click(self) -> None:
        pass

    def unclick(self) -> None:
        pass

    def update(self) -> None:
        pass
