import time
import math

from adafruit_display_shapes.line import Line

from watch import GC9A01ADisplay
from utils import create_clock_number_elements


display = GC9A01ADisplay()

CENTER_X = 120
CENTER_Y = 120

ROTATION_OFFSET = -math.pi / 2

number_elements = create_clock_number_elements()
for number in number_elements:
    display.add(f"number_{number.text}", number)

def create_hand(angle, length):
    x = CENTER_X + (length * math.cos(angle))
    y = CENTER_Y + (length * math.sin(angle))

    return Line(
        int(CENTER_X), int(CENTER_Y),
        int(x), int(y),
        color=0xFFFFFF
    )

second_hand = create_hand(0, 0) 
minute_hand = create_hand(0, 0)
hour_hand = create_hand(0, 0)

display.add("s", second_hand)
display.add("m", minute_hand)
display.add("h", hour_hand)

while True:
    total_seconds = time.monotonic()

    seconds = int(total_seconds) % 60
    minute_percent = seconds / 60
    second_hand_angle = ROTATION_OFFSET + (2 * math.pi * minute_percent)

    minutes = (total_seconds / 60) % 60
    hour_percent = minutes / 60
    minute_hand_angle = ROTATION_OFFSET + (2 * math.pi * hour_percent)

    hours = (total_seconds / 3600) % 12
    half_day_percent = hours / 12
    hour_hand_angle = ROTATION_OFFSET + (2 * math.pi * half_day_percent)

    new_second_hand = create_hand(second_hand_angle, 100)
    new_minute_hand = create_hand(minute_hand_angle, 75)
    new_hour_hand = create_hand(hour_hand_angle, 50)

    display.update("s", new_second_hand)
    display.update("m", new_minute_hand)
    display.update("h", new_hour_hand)

