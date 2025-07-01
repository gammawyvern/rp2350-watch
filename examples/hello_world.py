import board

import busio
import displayio
import digitalio
import terminalio

from fourwire import FourWire
from vectorio import Circle

from adafruit_display_text.bitmap_label import Label
from adafruit_gc9a01a import GC9A01A

# Backlight (optional)
backlight = digitalio.DigitalInOut(board.GP25)
backlight.direction = digitalio.Direction.OUTPUT
backlight.value = True  # turn on display backlight

# Setup display SPI
spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)

# Setup control pins
tft_cs = board.GP9
tft_dc = board.GP8
tft_reset = board.GP12

displayio.release_displays()

# Setup display bus
display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset)
display = GC9A01A(display_bus, width=240, height=240)

# Create display group
main_group = displayio.Group()
display.root_group = main_group

# Background
bg_bitmap = displayio.Bitmap(240, 240, 2)
palette = displayio.Palette(2)
palette[0] = 0x003366  # Dark Blue
palette[1] = 0xFF8800  # Orange

bg_tile = displayio.TileGrid(bg_bitmap, pixel_shader=palette)
main_group.append(bg_tile)

# Circle
circle = Circle(pixel_shader=palette, x=120, y=120, radius=80, color_index=1)
main_group.append(circle)

# Text
text_group = displayio.Group(scale=2, x=40, y=120)
text = Label(terminalio.FONT, text="Hello GC9A01A", color=0xFFFFFF)
text_group.append(text)
main_group.append(text_group)

while True:
    pass

