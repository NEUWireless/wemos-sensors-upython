import machine

class TempSensor:
    def __init__(self, scl=5, sda=4, freq=400000, address=72):
        self.addresss = address
        self.scl = scl
        self.sda = sda
        self.freq = freq
        self.i2c = machine.I2C(freq=400000, scl=machine.Pin(5, machine.Pin.OUT), sda=machine.Pin(4))

    def get():
        # write to configure temperature register
        self.i2c.writeto(72, b'00000000')

        # read from temperature register
        output = self.i2c.readfrom(72, 2)
        output = int.from_bytes(output, "big")
        output = output >> 5
        output = output / 8
        return output
