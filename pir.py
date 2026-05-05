import RPi.GPIO as GPIO
import time

pir = 23

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pir, GPIO.IN)

def read_motion():
    while True:
        state = GPIO.input(pir)
        if state == 0:
            print("motion not detected")
        else:
            print("motion detected")
        time.sleep(0.1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()
        read_motion()
    except KeyboardInterrupt:
        destroy()