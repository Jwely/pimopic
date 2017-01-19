import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


class Input(object):

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN)

    @property
    def ison(self):
        return GPIO.input(self.pin)


class Output(object):

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        self.set_off()

    def set_on(self):
        GPIO.output(self.pin, True)

    def set_off(self):
        GPIO.output(self.pin, False)


