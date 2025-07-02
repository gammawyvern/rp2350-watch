import math
import terminalio

from adafruit_display_text.label import Label


def create_clock_number_elements():
    CIRCLE = 2 * math.pi
    OFFSET = -3 * (CIRCLE / 12)
    CENTER_X = 120
    CENTER_Y = 120

    RADIUS = 100

    number_elements = []
    for num in range(1, 13):
        angle = OFFSET + (CIRCLE * (num / 12))
        x = CENTER_X + int(RADIUS * math.cos(angle))
        y = CENTER_Y + int(RADIUS * math.sin(angle))

        label = Label(terminalio.FONT, text=str(num), color=0xFFFFFF)
        label.anchor_point = (0.5, 0.5)
        label.anchored_position = (x, y)

        number_elements.append(label)

    return number_elements

