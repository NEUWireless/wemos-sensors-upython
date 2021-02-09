import machine


class ADC:
    def __init__(self):
        self.adc = machine.ADC(0)

    def read(self) -> int:
        return self.adc.read()
