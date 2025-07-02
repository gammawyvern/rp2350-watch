from fourwire import FourWire
import displayio
import digitalio
import board
import busio

from adafruit_gc9a01a import GC9A01A


class GC9A01ADisplay:
    def __init__(self, backlight_on=True):
        # Backlight setup
        self.__backlight = digitalio.DigitalInOut(board.GP25)
        self.__backlight.direction = digitalio.Direction.OUTPUT
        self.__backlight.value = backlight_on

        # Reset display
        displayio.release_displays()

        # Display setup
        spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
        tft_cs = board.GP9
        tft_dc = board.GP8
        tft_rst = board.GP12

        display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
        self.__display = GC9A01A(display_bus, width=240, height=240)
        self.__display.root_group = displayio.Group()

    def set_backlight_on(self, value):
        self.__backlight.value = value

    def wipe(self):
        self.__display.root_group = displayio.Group()

    def add(self, element):
        self.__display.root_group.append(element)

