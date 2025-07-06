import terminalio
import time
import math

from adafruit_display_shapes.rect import Rect

from watch import GC9A01ADisplay


display = GC9A01ADisplay()

WARMUP_COLOR =  0x6C739C
FOCUS_COLOR =   0x424658
BREAK_COLOR =   0xC56B62

WARMUP_DURATION =   5 * 60
FOCUS_DURATION =    5 * 60
BREAK_DURATION =    5 * 60
MAX_DURATION =      5 * 60

CENTER_X = 120
CENTER_Y = 120
MAX_BAR_HEIGHT = 120
BAR_WIDTH = 40

WARMUP_X = CENTER_X + int(-1.5 * BAR_WIDTH)
FOCUS_X = CENTER_X + int(-0.5 * BAR_WIDTH)
BREAK_X = CENTER_X + int(0.5 * BAR_WIDTH)

warmup_rect = Rect(x=WARMUP_X, y=110, width=BAR_WIDTH, height=20, fill=WARMUP_COLOR)
focus_rect = Rect(x=FOCUS_X, y=110, width=BAR_WIDTH, height=20, fill=FOCUS_COLOR)
break_rect = Rect(x=BREAK_X, y=110, width=BAR_WIDTH, height=20, fill=BREAK_COLOR)

display.add('w', warmup_rect)
display.add('f', focus_rect)
display.add('b', break_rect)


def create_bar(x, time_counted, max_time, color):
    if time_counted < 0:
        time_counted = 0

    percent_left = 1 - (time_counted / max_time)
    bar_scale = max_time / MAX_DURATION
    bar_height = int(MAX_BAR_HEIGHT * bar_scale * percent_left)

    if bar_height > 0:
        bar_y = int(CENTER_Y - (bar_height / 2))
    else:
        bar_height = 2
        bar_y = int(CENTER_Y - 1)  
        color = 0xFFFFFF

    return Rect(
        x=x,
        y=bar_y,
        width=BAR_WIDTH,
        height=bar_height, 
        fill=color
    )

start_time = time.monotonic()
while True:
    time_elapsed = time.monotonic() - start_time

    warmup_time_counted = time_elapsed
    focus_time_counted = time_elapsed - WARMUP_DURATION
    break_time_counted = time_elapsed - (WARMUP_DURATION + FOCUS_DURATION)

    next_warmup_rect = create_bar(WARMUP_X, warmup_time_counted, WARMUP_DURATION, WARMUP_COLOR)
    next_focus_rect = create_bar(FOCUS_X, focus_time_counted, FOCUS_DURATION, FOCUS_COLOR)
    next_break_rect = create_bar(BREAK_X, break_time_counted, BREAK_DURATION, BREAK_COLOR)

    display.update('w', next_warmup_rect)
    display.update('f', next_focus_rect)
    display.update('b', next_break_rect)

    if time_elapsed > (WARMUP_DURATION + FOCUS_DURATION + BREAK_DURATION):
        start_time = time.monotonic()

