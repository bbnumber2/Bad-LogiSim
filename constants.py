from enum import Enum


class Display(Enum):
    WINDOW_SIZE = (1000, 700)
    BACKGROUND_COLOR = (30, 30, 30)
    FOREGROUND_COLOR = (90, 90, 90)
    FOREGROUND_LOCATION = (40, 90)
    FOREGROUND_SIZE = (920, 550)
    FOREGROUND_WIDTH = 2
    FOREGROUND_RADIUS = 5
    FONT_FILENAME = 'Resources/LiberationSans-Regular.ttf'
    FONT_SIZE = 16


class Text(Enum):
    BACKGROUND_COLOR = (40, 40, 40)
    TEXT_COLOR = (204, 204, 204)
