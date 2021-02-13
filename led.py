import machine


class LED:
    def __init__(self, green=2, orange=0, red=16):
        self.green = machine.Pin(green, machine.Pin.OUT)
        self.orange = machine.Pin(orange, machine.Pin.OUT)
        self.red = machine.Pin(red, machine.Pin.OUT)

    def get(self, l: str):
        if (l == "GREEN"):
            return self.green
        elif (l == "RED"):
            return self.red
        elif (l == "ORANGE"):
            return self.orange
        else:
            raise ValueError('LED.get(): invalid LED')

    def set(self, l: str, s: bool):
        if s:
            self.get(l).on()
        else:
            self.get(l).off()
