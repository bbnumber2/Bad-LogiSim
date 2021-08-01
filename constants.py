class Display:
    WINDOW_SIZE = (1000, 700)
    BACKGROUND_COLOR = (30, 30, 30)
    FOREGROUND_COLOR = (90, 90, 90)
    FOREGROUND_POSITION = (40, 90)
    FOREGROUND_SIZE = (920, 550)
    FOREGROUND_WIDTH = 2
    FOREGROUND_RADIUS = 5


class Text:
    FONT_FILENAME = 'Resources/LiberationSans-Regular.ttf'
    FONT_SIZE = 16
    COLOR = (204, 204, 204)
    TEXTBOX_BACKGROUND_COLOR = (40, 40, 40)
    TEXTBOX_POSITION = (Display.FOREGROUND_POSITION[0], 20)
    TEXTBOX_SIZE = (Display.FOREGROUND_SIZE[0],
                    Display.FOREGROUND_POSITION[1] - TEXTBOX_POSITION[1])
    TEXTBOX_OUTLINE_COLOR = (90, 90, 90)
    TEXTBOX_OUTLINE_WIDTH = 2
    TEXTBOX_OUTLINE_RADIUS = 5
    TEXTBOX_TEXT_POSITION = (3, 3)
