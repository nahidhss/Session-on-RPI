import time
import requests
import random
import Adafruit_DHT

# =============================
# Configuration
# =============================
CHANNEL_API_KEY = "664K7MP88BN10QX2"
UPDATE_INTERVAL = 20                 # ThingSpeak minimum is 15 seconds
USE_SIMULATION = True                # Set to False when DHT sensor is connected

# DHT Sensor Configuration
DHT_SENSOR = Adafruit_DHT.DHT22       # Change to DHT11 if needed
DHT_PIN = 4                           # GPIO pin number (BCM numbering)

THINGSPEAK_URL = "https://api.thingspeak.com/update"


def read_dht_sensor():
    """Read temperature and humidity from DHT sensor."""
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature


def generate_sensor_data():
    """Generate random temperature and humidity values."""
    temperature = round(random.uniform(20.0, 30.0), 1)
    humidity = round(random.uniform(40.0, 80.0), 1)
    return humidity, temperature


def upload_to_thingspeak(temperature_c, temperature_f, humidity):
    """Upload data to ThingSpeak."""
    payload = {
        'api_key': CHANNEL_API_KEY,
        'field1': temperature_c,
        'field2': temperature_f,
        'field3': humidity
    }

    try:
        response = requests.get(THINGSPEAK_URL, params=payload, timeout=10)
        if response.status_code == 200 and response.text.strip() != '0':
            print(f"Data uploaded successfully. Entry ID: {response.text}")
        else:
            print(f"Upload failed. Response: {response.text}")
    except requests.RequestException as e:
        print(f"Network error: {e}")


def main():
    print("Starting temperature monitoring to ThingSpeak...")
    print("Press Ctrl+C to stop.\n")

    while True:
        if USE_SIMULATION:
            humidity, temperature_c = generate_sensor_data()
        else:
            humidity, temperature_c = read_dht_sensor()

        if humidity is not None and temperature_c is not None:
            temperature_f = round(temperature_c * 9/5 + 32, 1)
            print(f"Temperature: {temperature_c:.1f}°C / {temperature_f:.1f}°F | Humidity: {humidity:.1f}%")
            upload_to_thingspeak(temperature_c, temperature_f, humidity)
        else:
            print("Failed to read sensor data")

        time.sleep(UPDATE_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
