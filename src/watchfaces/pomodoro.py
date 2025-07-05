import terminalio
import time

from adafruit_display_text.label import Label
from adafruit_display_shapes.rect import Rect

from watch import GC9A01ADisplay


display = GC9A01ADisplay()

# label = Label(terminalio.FONT, text="Timer", color=0xFFFFFF, scale=4)
# label.anchor_point = (0.5, 0.5)
# label.anchored_position = (120, 120)
# display.add("timer", label)

WARMUP_COLOR =  0x6C739C
FOCUS_COLOR =   0x424658
BREAK_COLOR =   0xC56B62

WARMUP_DURATION =   0.2 * 60
FOCUS_DURATION =    5 * 60
BREAK_DURATION =    5 * 60

MAX_RECT_HEIGHT = 120
RECT_WIDTH = 40
CENTER_X = 120
CENTER_Y = 120

warmup_rect =   Rect(x=CENTER_X - int(1.5 * RECT_WIDTH), y=110, width=RECT_WIDTH, height=20, fill=WARMUP_COLOR)
focus_rect =    Rect(x=CENTER_X - int(0.5 * RECT_WIDTH), y=110, width=RECT_WIDTH, height=20, fill=FOCUS_COLOR)
break_rect =    Rect(x=CENTER_X + int(0.5 * RECT_WIDTH), y=110, width=RECT_WIDTH, height=20, fill=BREAK_COLOR)

display.add("warmup", warmup_rect)
display.add("focus", focus_rect)
display.add("break", break_rect)


start_time = time.monotonic()

while True:
    timer_time = time.monotonic() - start_time

    # TODO We definetly want a thing that render one bar, and we just call it 3 times per loop.
    if timer_time < WARMUP_DURATION:
        percent_done = timer_time / WARMUP_DURATION
        bar_height = int(MAX_RECT_HEIGHT * percent_done)
        new_rect = Rect(
            x=CENTER_X - int(1.5 * RECT_WIDTH),
            y=CENTER_Y - int(bar_height / 2),
            width=RECT_WIDTH,
            height=bar_height,
            fill=WARMUP_COLOR
        )

    display.update("warmup", new_rect)

    else:
        start_time = time.monotonic()

