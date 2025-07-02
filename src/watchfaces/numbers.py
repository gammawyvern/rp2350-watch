import terminalio
import time

from adafruit_display_text.label import Label

from watch import GC9A01ADisplay


display = GC9A01ADisplay()

label = Label(terminalio.FONT, text="Classic", color=0xFFFFFF, scale=2)
label.anchor_point = (0.5, 0.5)
label.anchored_position = (120, 120)
display.add("clock", label)

start_hours = 12
start_minutes = 0
start_seconds = 0
start_monotonic = time.monotonic()

while True:
    elapsed = int(time.monotonic() - start_monotonic)
    total_seconds = start_seconds + elapsed

    hours = (start_hours + (start_minutes + total_seconds // 60) // 60) % 24
    minutes = (start_minutes + total_seconds // 60) % 60

    label.text = f"{hours:02}:{minutes:02}"
    time.sleep(1)

