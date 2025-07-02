from adafruit_display_shapes.line import Line

from watch import GC9A01ADisplay


display = GC9A01ADisplay()

line = Line(10, 10, 100, 10, color=0xFFFFFF)
display.add(line)

while True:
    pass
