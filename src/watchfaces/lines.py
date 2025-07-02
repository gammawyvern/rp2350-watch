import time
import math

from adafruit_display_shapes.line import Line

from watch import GC9A01ADisplay


display = GC9A01ADisplay()

ARM_LENGTH = 20
CENTER_X = 120
CENTER_Y = 120

line = Line(
    CENTER_X, CENTER_Y,
    CENTER_X, CENTER_Y,
    color=0xFFFFFF
)

display.add("seconds", line)

while True:
    seconds = time.monotonic() % 60
    minute_percent = seconds / 60
    rotation = minute_percent * math.pi

    x = CENTER_X + (ARM_LENGTH * math.cos(rotation))
    y = CENTER_Y + (ARM_LENGTH * math.sin(rotation))

    next_line = Line(
        CENTER_X, CENTER_Y,
        int(x), int(y),
        color=0xFFFFFF
    )

    display.update("seconds", next_line)

