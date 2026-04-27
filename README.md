# Raspberry Pi & IoT Workshop
## **From Embedded Foundations to Smart Systems**

> **Session Type:** 2-Day Hands-On Technical Workshop  
> **Level:** Beginner to Intermediate  
> **Platform:** Raspberry Pi 5 · Python 3.x · Linux (Raspberry Pi OS)

---

## Table of Contents

1. [Introduction to Raspberry Pi & GPIO](#introduction-to-raspberry-pi--gpio)
   - [What is Raspberry Pi?](#what-is-raspberry-pi)
   - [GPIO Pin Diagram](#gpio-pin-diagram)

2. [Pin Types & Protocols](#pin-types--protocols)
   - [Digital I/O](#1-digital-io)
   - [PWM — Pulse Width Modulation](#2-pwm--pulse-width-modulation)
   - [I²C — Inter-Integrated Circuit](#3-i²c--inter-integrated-circuit)
   - [SPI — Serial Peripheral Interface](#4-spi--serial-peripheral-interface)
   - [UART — Universal Asynchronous Receiver-Transmitter](#5-uart--universal-asynchronous-receiver-transmitter)
   - [Power Pins](#6-power-pins)

3. [Sensors & IoT Fundamentals](#sensors--iot-fundamentals)
   - [Sensor Types](#sensor-types)
   - [IoT Architecture](#iot-architecture)
   - [Protocols Comparison](#protocols-comparison)

4. [Python Installation & Virtual Environment Setup on Ubuntu](#python-installation--virtual-environment-setup-on-ubuntu)
   - [Update System Packages](#1-update-system-packages)
   - [Install Python](#2-install-python)
   - [Install Virtual Environment Support](#3-install-virtual-environment-support)
   - [Create a Project Folder](#4-create-a-project-folder)
   - [Create Virtual Environment](#5-create-virtual-environment)
   - [Activate Virtual Environment](#6-activate-virtual-environment)
   - [Install Python Packages](#7-install-python-packages)
   - [Save & Install Requirements](#8-save--install-requirements)
   - [Deactivate Virtual Environment](#9-deactivate-virtual-environment)
   - [Summary Workflow](#10-summary-workflow)

5. [Project 1: Data Collection using Python/GPIO](#project-1-data-collection-using-pythongpio-overview--requirements)
   - [Overview](#overview)
   - [Requirements](#requirements)
   - [Basic GPIO Control (Drive LED)](#basic-gpio-controldrive-led)
   - [Basic GPIO Control (Taking Input)](#basic-gpio-controltaking-input)

6. [Project 2 — Temperature Monitoring System (Raspberry Pi 5 Version)](#project-2--temperature-monitoring-system-raspberry-pi-5-version)
   - [Overview](#overview-1)
   - [Requirements](#requirements-1)
   - [Working Principle](#working-principle)
   - [Full Python Code](#full-python-code)
   - [Running the Script](#running-the-script)
   - [ThingSpeak Channel Configuration](#thingspeak-channel-configuration)

7. [Project 3 — Smart Parking System using IoT](#project-3--smart-parking-system-using-iot)
   - [Overview](#overview-2)
   - [Requirements](#requirements-2)
   - [Wiring Diagram](#wiring-diagram)
   - [System Architecture](#system-architecture)
   - [Full Python Code](#full-python-code-1)
   - [Expected Console Output](#expected-console-output)

8. [Project 4 — Traffic Signal Automation](#project-4--traffic-signal-automation)
   - [Overview](#overview-3)
   - [Requirements](#requirements-3)
   - [Wiring Diagram](#wiring-diagram-1)
   - [Finite State Machine](#finite-state-machine)
   - [Full Python Code](#full-python-code-2)

9. [Advanced Topics & Next Steps](#advanced-topics--next-steps)
   - [AI / ML at the Edge](#1-ai--ml-at-the-edge)
   - [IoT Security](#2-iot-security)
   - [Cloud Pipelines](#3-cloud-pipelines)
   - [Troubleshooting Common Issues](#4-troubleshooting-common-issues)

---

## **Introduction to Raspberry Pi & GPIO**

### What is Raspberry Pi?

The **Raspberry Pi 5 (RPi 5)** is a **single-board computer (SBC)** that runs a full Linux operating system. Unlike a microcontroller (such as Arduino), it can run multiple processes simultaneously, host web servers, execute Python-based IoT applications, perform edge computing, and interface with sensors through its GPIO pins — making it highly suitable for modern IoT and embedded AI systems.

| Feature | Microcontroller (Arduino) | Single-Board Computer (RPi 5) |
|---|---|---|
| OS | None (bare metal) | Linux (Raspberry Pi OS) |
| CPU | 8/16-bit AVR, ~16 MHz | Quad-core ARM Cortex-A76, ~2.4 GHz (Raspberry Pi 5) |
| RAM | 2 KB – 8 KB | 2 GB – 8 GB |
| GPIO Pins | 14–54 | 40 GPIO pins |
| Analog Input | Yes (built-in ADC) | No (requires external ADC) |
| Network | External module only | Built-in Wi-Fi & Ethernet |
| Best For | Real-time low-power control | IoT, AI, web servers, robotics, edge computing |

---

### GPIO Pin Diagram

The Raspberry Pi 5 exposes a **40-pin GPIO header**. Understanding the pin layout is essential before connecting any sensor or module.

```js
3V3 (Power 3.3V)    (1)     (2)     5V (Power 5V)
GPIO2 (I2C_SDA)     (3)     (4)     5V (Power 5V)
GPIO3 (I2C_SCL)     (5)     (6)     GND (Ground)
GPIO4 (GPIO)        (7)     (8)     GPIO14 (UART_TX)
GND (Ground)        (9)     (10)    GPIO15 (UART_RX)
GPIO17 (GPIO)       (11)    (12)    GPIO18 (PWM/GPIO)
GPIO27 (GPIO)       (13)    (14)    GND (Ground)
GPIO22 (GPIO)       (15)    (16)    GPIO23 (GPIO)
3V3 (Power 3.3V)    (17)    (18)    GPIO24 (GPIO)
GPIO10 (SPI_MOSI)   (19)    (20)    GND (Ground)
GPIO9 (SPI_MISO)    (21)    (22)    GPIO25 (GPIO)
GPIO11 (SPI_SCLK)   (23)    (24)    GPIO8 (SPI_CE0)
GND (Ground)        (25)    (26)    GPIO7 (SPI_CE1)
GPIO0 (I2C_ID)      (27)    (28)    GPIO1 (I2C_ID)
GPIO5 (GPIO)        (29)    (30)    GND (Ground)
GPIO6 (GPIO)        (31)    (32)    GPIO12 (PWM)
GPIO13 (PWM GPIO)   (33)    (34)    GND (Ground)
GPIO19 (PWM/SPI)    (35)    (36)    GPIO16 (GPIO)
GPIO26 (GPIO)       (37)    (38)    GPIO20 (SPI)
GND (Ground)        (39)    (40)    GPIO21 (SPI/I2C)
```

> **Note:** Pin numbers in parentheses are **physical (BOARD)** numbers. GPIO numbers are **BCM** numbers used in Python code.

---

## **Pin Types & Protocols**

### 1. Digital I/O
Standard GPIO pins configurable as **input** or **output**. Output HIGH = 3.3V, LOW = 0V. Used for LEDs, buttons, relays, and simple sensors.

### 2. PWM — Pulse Width Modulation
Rapidly toggles between HIGH and LOW at a set frequency. The **duty cycle** (% of time spent HIGH) controls the effective output voltage. Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19.

```
Duty cycle 0%   → 0.0V effective
Duty cycle 50%  → 1.65V effective
Duty cycle 100% → 3.3V effective
```

### 3. I²C — Inter-Integrated Circuit
Two-wire serial protocol: **SDA** (GPIO2, Pin 3) and **SCL** (GPIO3, Pin 5). Supports up to 127 devices on one bus, each with a unique 7-bit address. Slower than SPI but requires fewer wires.

Common I²C devices: OLED displays, BME280, MPU6050, PCF8574 (LCD backpack)

### 4. SPI — Serial Peripheral Interface
High-speed 4-wire full-duplex protocol: **MOSI** (GPIO10), **MISO** (GPIO9), **CLK** (GPIO11), **CE0/CE1** (GPIO8/7). Typically 10× faster than I²C. Used for ADC chips, TFT displays, SD card modules.

### 5. UART — Universal Asynchronous Receiver-Transmitter
2-wire serial: **TX** (GPIO14) and **RX** (GPIO15). Used to communicate with GPS modules, GSM modems, Bluetooth modules (HC-05), and other microcontrollers.

### 6. Power Pins
Fixed-voltage output pins. Cannot be reconfigured. The 3.3V rail is limited — do not draw more than 50 mA from it for all sensors combined.

> ⚠️ **Critical:** All GPIO pins operate at **3.3V logic**. Never connect a 5V signal directly to a GPIO input — it will permanently damage the SoC.

---

## **Sensors & IoT Fundamentals**

### **Sensor Types:**
- **Digital sensors** output discrete HIGH/LOW signals (e.g., PIR motion, button, DS18B20)
- **Analog sensors** output a continuous voltage proportional to the physical quantity. Raspberry Pi has no ADC — requires an external chip like MCP3008 via SPI

### **IoT Architecture:**
```
[Physical Sensor] → [Raspberry Pi] → [Internet] → [Cloud Platform] → [Dashboard / App]
       ↑                  ↑                               ↑
  Edge Layer         Edge Processing               Cloud Layer
```

### **Protocols Comparison:**

| Protocol | Type | Use Case | Port |
|---|---|---|---|
| HTTP/HTTPS | Request-response | REST APIs, ThingSpeak | 80/443 |
| MQTT | Publish-subscribe | Low-bandwidth IoT, sensors | 1883/8883 |
| WebSocket | Full-duplex | Real-time dashboards | 80/443 |
| CoAP | Lightweight REST | Constrained devices | UDP 5683 |

---

## **Python Installation & Virtual Environment Setup on Ubuntu**

This guide explains how to install Python on Ubuntu, create a virtual environment (venv), and install Python packages safely for development projects.

---

### 1. Update System Packages

Before installing anything, update your system:

```bash
sudo apt update
sudo apt upgrade -y
```

---

### 2. Install Python

Ubuntu usually comes with Python pre-installed. Check version:

```bash
python3 --version
```

If Python is not installed or you want latest tools, install it:

```bash
sudo apt install python3 python3-pip -y
```

Verify installation:

```bash
python3 --version
pip3 --version
```

---

### 3. Install Virtual Environment Support

Install venv module:

```bash
sudo apt install python3-venv -y
```

---

### 4. Create a Project Folder

```bash
mkdir my_python_project
cd my_python_project
```

---

### 5. Create Virtual Environment

Create a venv folder:

```bash
python3 -m venv venv
```

This creates a local isolated Python environment.

---

### 6. Activate Virtual Environment

### Linux / Ubuntu:
```bash
source venv/bin/activate
```

After activation, you will see:
```
(venv) user@ubuntu:~/my_python_project$
```

---

### 7. Install Python Packages

Now install packages inside venv:

```bash
pip install numpy
pip install requests
pip install gpiozero
pip install lgpio
```

Or install multiple packages at once:

```bash
pip install numpy requests gpiozero
```

---

### 8. Save & Install Requirements

Generate requirements file:

```bash
pip freeze > requirements.txt
```

To install from requirements file on another system or later:

```bash
pip install -r requirements.txt
```

---

### 9. Deactivate Virtual Environment

When done:

```bash
deactivate
```

---

### 10. Summary Workflow

```bash
sudo apt install python3 python3-pip python3-venv -y
mkdir project && cd project
python3 -m venv venv
source venv/bin/activate
pip install <packages>
deactivate
```

---

## **Project 1: Data Collection using Python/GPIO: Overview & Requirements**

## **Overview**

This project demonstrates the fundamentals of **GPIO (General Purpose Input/Output) control** on a **Raspberry Pi 5** using Python. It focuses on simple interaction between **input devices (push button)** and **output devices (LED)**.

The system allows:
- Reading a **digital input signal** from a push button  
- Driving an **LED output** based on input state  
- Real-time response using Python event handling or polling  

This is a foundational project for understanding embedded systems, robotics control, and hardware interfacing with Python.

---

## **Requirements**

### **Hardware**
- Raspberry Pi 5  
- LED  
- 330 Ω resistor (for LED protection)  
- Push button  
- Breadboard  
- Jumper wires  

---

### **Software**

```bash
pip install gpiozero --break-system-packages
```

### **Basic GPIO Control (Drive LED)**
```python
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
```

### **Basic GPIO Control (Taking Input)**
```python
from gpiozero import Button
from signal import pause

def main():
    # GPIO17 as input with pull-up resistor
    button = Button(17, pull_up=True)

    def pressed():
        print("Button Pressed!")

    def released():
        print("Button Released!")

    button.when_pressed = pressed
    button.when_released = released

    print("Program running... Press Ctrl+C or Enter to exit")

    try:
        input("Press Enter to exit...\n")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
```

---

## **Project 2 — Temperature Monitoring System (Raspberry Pi 5 Version)**

## Overview

Build a real-time **temperature and humidity monitoring system** using a simulated or real sensor on a **Raspberry Pi 5 (RPi 5)**. The system reads data using Python, displays it locally, and sends it to **ThingSpeak cloud dashboard** for live visualization and logging.

You can run it in:
- 🧪 Simulation mode (no hardware needed)
- 🌡️ Real sensor mode (DHT22 / DHT11)

---

## Requirements

### Hardware
- Raspberry Pi 5 (RPi 5)
- DHT22 or DHT11 sensor (optional for real mode)
- Jumper wires
- Breadboard

### Software

```bash
pip install Adafruit_DHT requests gpiozero --break-system-packages
```

**ThingSpeak Setup:**
```
1. Create a free account at [thingspeak.com](https://thingspeak.com)
2. Create a new Channel with 3 fields: Temperature °C, Temperature °F, Humidity %
3. Copy your **Write API Key** from the API Keys tab
```
```
DHT22 Sensor          Raspberry Pi 5
─────────────         ───────────────
Pin 1 (VCC)   ──────  Pin 1  (3.3V)
Pin 2 (DATA)  ──────  Pin 7  (GPIO4)
Pin 3 (NC)    (not connected)
Pin 4 (GND)   ──────  Pin 6  (GND)

Note: A 10kΩ pull-up resistor between DATA and VCC
      is recommended for cable lengths > 20cm.
```
---
## Working Principle

```
[DHT22 Sensor]
      │  (Single-wire 40-bit protocol)
      ▼
GPIO4 (Raspberry Pi 5)
      │
      ▼
Python Script
(read + validate data)
      │
      ▼
┌──────────────────────────────┐
│                              │
▼                              ▼
Console Output            ThingSpeak Cloud
Live Display              HTTP GET API
                          api.thingspeak.com/update
```

The DHT22 communicates using a **single-wire proprietary protocol**. It sends a 40-bit data packet: 16 bits humidity + 16 bits temperature + 8-bit checksum. The Adafruit library handles the precise timing required to decode this packet.

### Full Python Code

```python
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
```

### Running the Script

```bash
# Run the logger
python3 project2_temperature.py
```

### Expected Console Output

```text
Temperature: 25.3°C / 77.5°F | Humidity: 62.4%
Data uploaded successfully. Entry ID: 70
```

### ThingSpeak Channel Configuration

| Field | Variable | Unit |
|---|---|---|
| Field 1 | Temperature | °C |
| Field 2 | Temperature | °F |
| Field 3 | Relative Humidity | % |

---

## **Project 3 — Smart Parking System using IoT**

### Overview

Simulate a **4-slot smart parking lot** using IR obstacle sensors (or button inputs) to detect vehicle occupancy. Status is displayed on console, indicated by simulated LEDs, and pushed to ThingSpeak for remote monitoring.

### Requirements

**Hardware:**
- Raspberry Pi 5
- 4× IR obstacle sensor modules (or push buttons for simulation)
- 4× Red LEDs + 4× Green LEDs with 330 Ω resistors each (optional for visual feedback)
- Breadboard and jumper wires

**Software:**
```bash
pip install RPi.GPIO RPLCD requests --break-system-packages
```

### Wiring Diagram

```
Slot Sensors (IR / Button)    Raspberry Pi 5
──────────────────────────    ───────────────
Slot 1 Sensor OUT  ─────────→ GPIO17 (Pin 11)
Slot 2 Sensor OUT  ─────────→ GPIO27 (Pin 13)
Slot 3 Sensor OUT  ─────────→ GPIO22 (Pin 15)
Slot 4 Sensor OUT  ─────────→ GPIO10 (Pin 19)
All Sensor VCC     ─────────→ 3.3V   (Pin 1)
All Sensor GND     ─────────→ GND    (Pin 6)
```

### System Architecture

```
IR Sensors (GPIO input)
       │
       ▼
 check_all_slots()  ← polling loop (20s)
       │
       ├──→ update_leds()       [RED=busy, GREEN=free]
       └──→ upload_to_cloud()   [ThingSpeak HTTP GET]
```

### Full Python Code

```python
import time
import requests
from gpiozero import DigitalInputDevice

# =============================
# ThingSpeak Config
# =============================
API_KEY = "RT8HWF7CPMVU8ZE6"
URL = "https://api.thingspeak.com/update"

# =============================
# IR Sensor (Obstacle)
# =============================
ir = DigitalInputDevice(4)  # GPIO17

def upload(value):
    payload = {
        "api_key": API_KEY,
        "field1": value
    }

    try:
        r = requests.get(URL, params=payload, timeout=10)
        print("Uploaded:", value, "Response:", r.text)
    except Exception as e:
        print("Upload error:", e)

print("IR Obstacle Sensor Monitoring...")

last_value = None

while True:
    # gpiozero: 1 = HIGH, 0 = LOW
    # adjust if your sensor is inverted
    value = 0 if ir.is_active else 1

    if value != last_value:
        upload(value)
        last_value = value

    print("Obstacle:", value)
    time.sleep(2)

```

### Expected Console Output

```
===== Smart Parking Status =====
Slot 1: Empty
Slot 2: Occupied
Slot 3: Empty
Slot 4: Occupied
Available Slots: 2/4
===============================
Uploaded successfully. Entry ID: 1843201
```

---

## **Project 4 — Traffic Signal Automation**

### Overview

Implement a **traffic light controller** using LEDs to represent the red, yellow, and green signals. This simulates a basic traffic cycle for one lane.

### Requirements

**Hardware:**
- Raspberry Pi 5
- 3× Red, Yellow, Green LEDs
- 3× 330 Ω current-limiting resistors
- Breadboard and jumper wires

**Software:**
```bash
pip install RPi.GPIO --break-system-packages
```

### Wiring Diagram

```
Traffic Light LEDs            Raspberry Pi 5
──────────────────────────    ───────────────
Red    LED ──[330Ω]──────→ GPIO17 (Pin 11)
Yellow LED ──[330Ω]──────→ GPIO27 (Pin 13)
Green  LED ──[330Ω]──────→ GPIO22 (Pin 15)
All LED GND ─────────────→ GND    (Pin 6)
```

### Finite State Machine

```
           ┌─────────────────────────────────┐
           ↓                                 │
      ┌─────────┐                       ┌─────────┐
      │   RED   │──────────────────────→│  GREEN  │
      └─────────┘                       └─────────┘
           ↑                                  │
           │                                  │ 
      ┌─────────┐                             ↓
      │ YELLOW  │←────────────────────────────┘
      └─────────┘
```

### Full Python Code

```python
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
```

---

## Advanced Topics & Next Steps

### 1. AI / ML at the Edge
Deploy **TensorFlow Lite** on the Raspberry Pi to run inference locally without cloud connectivity:
```bash
pip install tflite-runtime --break-system-packages
```
Use cases: object detection with Pi Camera, keyword spotting, anomaly detection in sensor data.

### 2. IoT Security
- Always use **HTTPS / TLS** for cloud communications
- Use **API keys** with minimum required permissions; rotate regularly
- Disable unused services: `sudo systemctl disable bluetooth`
- Implement **device authentication** using X.509 certificates (AWS IoT Core)
- Never hardcode credentials — use environment variables or a config file outside version control

### 3. Cloud Pipelines
| Platform | Protocol | Best For |
|---|---|---|
| AWS IoT Core | MQTT / HTTP | Enterprise, Lambda triggers |
| Azure IoT Hub | MQTT / AMQP | Microsoft ecosystem |
| Google Cloud IoT | MQTT / HTTP | BigQuery integration |
| ThingSpeak | HTTP REST | Quick prototyping, MATLAB analysis |
| Firebase | HTTP REST / WebSocket | Real-time mobile apps |

### 4. Troubleshooting Common Issues
- **GPIO not responding:** Verify pin numbers (use BCM numbering in code), check for 3.3V logic (not 5V), ensure proper grounding.
- **Sensor readings are unstable or incorrect:** Confirm power supply stability, add pull-up/down resistors if needed, check wiring for shorts.
- **ThingSpeak upload fails:** Check API key validity, ensure internet connection, respect rate limits (minimum 15 seconds between updates), verify payload format.
- **Virtual environment issues:** Ensure venv is activated (check prompt), avoid mixing pip installs, use `--break-system-packages` cautiously on Debian-based systems.
- **LED not lighting:** Test with a simple script, check resistor values (330Ω for LEDs), confirm GPIO is set as output.
- **DHT sensor errors:** Ensure correct pin, wait between readings, handle exceptions for failed reads.
