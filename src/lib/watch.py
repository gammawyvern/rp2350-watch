from fourwire import FourWire
import displayio
import digitalio
import board
import busio

from adafruit_gc9a01a import GC9A01A


class GC9A01ADisplay:
    def __init__(self, backlight=True):
        # Backlight setup
        self.__backlight = digitalio.DigitalInOut(board.GP25)
        self.__backlight.direction = digitalio.Direction.OUTPUT
        self.set_backlight(backlight)

        # Reset display
        displayio.release_displays()

        # Display setup
        spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
        tft_cs = board.GP9
        tft_dc = board.GP8
        tft_rst = board.GP12

        display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
        self.__display = GC9A01A(display_bus, width=240, height=240)
        self.reset()

    def set_backlight(self, value):
        self.__backlight.value = value

    def reset(self):
        self.__display.root_group = displayio.Group()
        self.__element_index = {}

    def add(self, name, element):
        self.__element_index[name] = len(self.__display.root_group)
        self.__display.root_group.append(element)

    def update(self, name, new_element):
        element_index = self.__element_index[name]
        self.__display.root_group[element_index] = new_element

