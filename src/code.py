import time
import board
import busio
import digitalio
import displayio
import terminalio

from adafruit_display_text.label import Label
from adafruit_gc9a01a import GC9A01A
from fourwire import FourWire

import text  

backlight = digitalio.DigitalInOut(board.GP25)
backlight.direction = digitalio.Direction.OUTPUT
backlight.value = True

# --- Display setup (adjust pins for your board) ---
spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
tft_cs = board.GP9
tft_dc = board.GP8
tft_rst = board.GP12

displayio.release_displays()
display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = GC9A01A(display_bus, width=240, height=240)

# --- Create root group ---
main_group = displayio.Group()
display.root_group = main_group

# --- Add time label ---
time_label = Label(terminalio.FONT, text="00:00:00", color=0xFFFFFF, scale=3)
time_label.anchor_point = (0.5, 0.5)
time_label.anchored_position = (120, 120)
main_group.append(time_label)

# --- Simulated time start (boot = 12:00:00) ---
start_hours = 12
start_minutes = 0
start_seconds = 0
start_monotonic = time.monotonic()

# --- Main loop ---
while True:
    elapsed = int(time.monotonic() - start_monotonic)
    total_seconds = start_seconds + elapsed
    hours = (start_hours + (start_minutes + total_seconds // 60) // 60) % 24
    minutes = (start_minutes + total_seconds // 60) % 60
    seconds = total_seconds % 60

    time_str = f"{hours:02}:{minutes:02}"
    time_label.text = time_str

    time.sleep(0.5)

