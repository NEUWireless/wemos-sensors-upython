import time
import led

l = led.LED()
for _ in range(5):
    l.set("GREEN", True)
    l.set("ORANGE", True)
    l.set("RED", True)
    time.sleep(0.3)
    l.set("GREEN", False)
    l.set("ORANGE", False)
    l.set("RED", False)
    time.sleep(0.3)
