import terminalio
import time

from adafruit_display_shapes.rect import Rect

from watch import GC9A01ADisplay


display = GC9A01ADisplay()

WARMUP_COLOR =  0x6C739C
FOCUS_COLOR =   0x424658
BREAK_COLOR =   0xC56B62

WARMUP_DURATION =   5 * 60
FOCUS_DURATION =    5 * 60
BREAK_DURATION =    5 * 60

MAX_RECT_HEIGHT = 120
RECT_WIDTH = 40
CENTER_X = 120
CENTER_Y = 120

warmup_rect =   Rect(x=CENTER_X - int(1.5 * RECT_WIDTH), y=110, width=RECT_WIDTH, height=20, fill=WARMUP_COLOR)
# focus_rect =    Rect(x=CENTER_X - int(0.5 * RECT_WIDTH), y=110, width=RECT_WIDTH, height=20, fill=FOCUS_COLOR)
# break_rect =    Rect(x=CENTER_X + int(0.5 * RECT_WIDTH), y=110, width=RECT_WIDTH, height=20, fill=BREAK_COLOR)

display.add('w', warmup_rect)
# display.add("focus", focus_rect)
# display.add("break", break_rect)

start_time = time.monotonic()

while True:
    timer_time = time.monotonic() - start_time

    if timer_time < WARMUP_DURATION:
        percent_done = timer_time / WARMUP_DURATION
        bar_height = int(MAX_RECT_HEIGHT * percent_done)
        new_rect = Rect(
            x=int(CENTER_X - int(1.5 * RECT_WIDTH)),
            y=int(CENTER_Y - int(bar_height / 2)),
            width=int(RECT_WIDTH),
            height=int(bar_height),
            fill=WARMUP_COLOR
        )

        display.update('w', new_rect)
    else:
        start_time = time.monotonic()

    time.sleep(5)

