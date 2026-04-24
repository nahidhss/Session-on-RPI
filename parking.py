import time
import random
import requests
from gpiozero import DigitalInputDevice

# ============================================
# Configuration
# ============================================
CHANNEL_API_KEY = "RT8HWF7CPMVU8ZE6"
THINGSPEAK_URL = "https://api.thingspeak.com/update"
UPDATE_INTERVAL = 20  # ThingSpeak minimum is 15 seconds

USE_SIMULATION = True  # True = simulate sensors, False = use real IR sensors

# GPIO pins for 4 IR sensors (BCM numbering)
IR_PINS = [17, 27, 22, 10]

# ============================================
# Sensor Setup
# ============================================
if not USE_SIMULATION:
    sensors = [DigitalInputDevice(pin) for pin in IR_PINS]


def read_ir_sensors():
    """Read actual IR sensor states."""
    return [sensor.value for sensor in sensors]


def simulate_ir_sensors():
    """Generate random parking occupancy states."""
    return [random.randint(0, 1) for _ in range(4)]


def upload_to_thingspeak(sensor_data):
    """Upload parking slot data to ThingSpeak."""
    payload = {
        'api_key': CHANNEL_API_KEY,
        'field1': sensor_data[0],
        'field2': sensor_data[1],
        'field3': sensor_data[2],
        'field4': sensor_data[3]
    }

    try:
        response = requests.get(THINGSPEAK_URL, params=payload, timeout=10)
        if response.status_code == 200 and response.text.strip() != '0':
            print(f"Uploaded successfully. Entry ID: {response.text}")
        else:
            print(f"Upload failed: {response.text}")
    except requests.RequestException as e:
        print(f"Network error: {e}")


def display_status(sensor_data):
    """Display parking slot status."""
    available = sensor_data.count(0)
    print("\n===== Smart Parking Status =====")
    for i, status in enumerate(sensor_data, start=1):
        state = "Occupied" if status else "Empty"
        print(f"Slot {i}: {state}")
    print(f"Available Slots: {available}/4")
    print("===============================")


def main():
    print("Smart Parking System Started")
    print(f"Mode: {'Simulation' if USE_SIMULATION else 'Real Sensor'}")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            if USE_SIMULATION:
                sensor_data = simulate_ir_sensors()
            else:
                sensor_data = read_ir_sensors()

            display_status(sensor_data)
            upload_to_thingspeak(sensor_data)

            time.sleep(UPDATE_INTERVAL)

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")


if __name__ == "__main__":
    main()
