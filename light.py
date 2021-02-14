import machine


class LightSensor:
    def __init__(self, adc=0):
        self.adc = machine.ADC(adc)

    def read(self) -> int:
        return self.adc.read()
