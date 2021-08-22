from typing import Tuple
import pygame
from app_object import AppObject


class Wire:
    def __init__(self, start_object: AppObject,
                 unpowered_color: Tuple[int, int, int],
                 powered_color: Tuple[int, int, int],
                 width: int,
                 screen: pygame.Surface) -> None:
        self.start_object = start_object
        self.end_object = None
        self.end_position = None
        self.powered = False
        self.unpowered_color = unpowered_color
        self.powered_color = powered_color
        self.width = width
        self.screen = screen

    def connect(self, end_object: AppObject) -> None:
        self.end_object = end_object
        self.end_position = None
    
    def power(self) -> None:
        self.powered = True
        self.end_object.power()

    def render(self) -> None:
        start_pos = (self.start_object.rect.right,
                     self.start_object.rect.centery)
        if self.end_object:
            end_pos = (self.end_object.rect.left,
                       self.end_object.rect.centery)
        else:
            end_pos = self.end_position
        color = self.powered_color if self.powered else self.unpowered_color
        pygame.draw.line(self.screen, color, start_pos, end_pos, self.width)
