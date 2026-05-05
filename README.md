# PIR-Motion-Detection-System-using-Raspberry-Pi
PIR-based motion detection system using Raspberry Pi that detects human movement and displays status via GPIO input, useful for security and automation applications.

## Description

This project demonstrates a motion detection system using a PIR (Passive Infrared) sensor and Raspberry Pi. The PIR sensor detects human movement based on infrared radiation and sends signals to the Raspberry Pi, which displays the motion status.

## Components Used

* Universal IOT trainer kit with raspberry pi
* PIR Sensor
* Jumper Wires
* Connecting Wires
* USB Cables

## Software Used

* Thonny Python IDE
* Raspbian OS

## Connections

* PIR OUT → GPIO Pin 23 (BCM mode)
* PIR VCC → 5V
* PIR GND → GND

## Circuit Diagram Explanation

The PIR sensor detects infrared radiation from moving objects such as humans. When motion is detected, the sensor outputs a HIGH signal to the Raspberry Pi. The Raspberry Pi reads this signal through GPIO and prints the motion status.

## Code

[pir.py](pir.py)

## Applications

* Security systems
* Motion alarms
* Automatic lighting
* Smart home systems

## Author

HimagnaMovva27
