import machine


class LED:
    def __init__(self):
        self.green = machine.Pin(2, machine.Pin.OUT)
        self.orange = machine.Pin(0, machine.Pin.OUT)
        self.red = machine.Pin(16, machine.Pin.OUT)

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
