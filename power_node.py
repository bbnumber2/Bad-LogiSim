from component import Component
from typing import Tuple
import pygame


class PowerNode(Component):
    def __init__(self,  position: Tuple[int, int], size: Tuple[int, int],
                 outline_color: Tuple[int, int, int],
                 outline_thickness: Tuple[int, int, int],
                 unpowered_color: Tuple[int, int, int],
                 powered_color: Tuple[int, int, int]) -> None:
        super().__init__(position, size)
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        self.outline_thickness = outline_thickness
        self.unpowered_color = unpowered_color
        self.powered_color = powered_color
        # relative to self.surface
        self.center = (size[0] // 2, size[1] // 2)
        self.surface.fill(unpowered_color)
        pygame.draw.circle(self.surface, outline_color, self.center,
                           size[0] // 2, width=outline_thickness)

    def send_signal(self) -> None:
        for wire in self.wires:
            wire.power()

    def click(self):
        self.selected = not self.selected
        if self.selected:
            color = self.powered_color
            self.send_signal()
        else:
            color = self.unpowered_color
        pygame.draw.circle(self.surface, color, self.center,
                           self.size[0] // 2 - self.outline_thickness)
