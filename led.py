from gpiozero import LED
from time import sleep

# GPIO17 as LED output
led = LED(17)

try:
    while True:
        led.on()     # LED ON
        sleep(0.5)
        led.off()    # LED OFF
        sleep(0.5)

except KeyboardInterrupt:
    pass
