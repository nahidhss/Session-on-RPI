import time
import random
from gpiozero import LED

# =========================
# CONFIGURATION
# =========================
USE_SIMULATION = True   # False = real LEDs on Raspberry Pi

# GPIO pins (BCM numbering)
RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22

# =========================
# HARDWARE SETUP
# =========================
if not USE_SIMULATION:
    red = LED(RED_PIN)
    yellow = LED(YELLOW_PIN)
    green = LED(GREEN_PIN)


# =========================
# SIMULATION FUNCTIONS
# =========================
def simulate_light(name):
    print(f"{name} LIGHT ON")


def all_off():
    if USE_SIMULATION:
        print("ALL LIGHTS OFF\n")
    else:
        red.off()
        yellow.off()
        green.off()


# =========================
# TRAFFIC LOGIC
# =========================
def traffic_cycle():
    # RED LIGHT
    all_off()
    if USE_SIMULATION:
        simulate_light("RED")
    else:
        red.on()
    time.sleep(5)

    # GREEN LIGHT
    all_off()
    if USE_SIMULATION:
        simulate_light("GREEN")
    else:
        green.on()
    time.sleep(5)

    # YELLOW LIGHT
    all_off()
    if USE_SIMULATION:
        simulate_light("YELLOW")
    else:
        yellow.on()
    time.sleep(2)


# =========================
# MAIN LOOP
# =========================
def main():
    print("Traffic Light System Started")
    print("Mode:", "SIMULATION" if USE_SIMULATION else "HARDWARE")

    try:
        while True:
            traffic_cycle()

    except KeyboardInterrupt:
        print("\nStopping system...")
        all_off()


if __name__ == "__main__":
    main()
