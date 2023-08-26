import requests
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

#pin mapping
LAMPU_PIN = 17
AC_PIN = 22
TV_PIN = 27

# inisiasi pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LAMPU_PIN, GPIO.OUT)
GPIO.setup(AC_PIN, GPIO.OUT)
GPIO.setup(TV_PIN, GPIO.OUT)

#fungi mati/nyalakan LAMPU dengan parameter state, jika state =1 nyala, state=0 mati
def lampu(state):
    if state == 0:
        GPIO.output(LAMPU_PIN, GPIO.HIGH)
        print("LAMPU turned OFF")
    else:
        GPIO.output(LAMPU_PIN, GPIO.LOW)
        print("LAMPU turned ON")

#fungi mati/nyalakan AC dengan parameter state, jika state =1 nyala, state=0 mati
def ac(state):
    if state == 1:
        GPIO.output(AC_PIN, GPIO.HIGH)
        print("AC turned ON")
    else:
        GPIO.output(AC_PIN, GPIO.LOW)
        print("AC turned OFF")
    
#fungi mati/nyalakan TV dengan parameter state, jika state =1 nyala, state=0 mati
def tv(state):
    if state == 1:
        GPIO.output(TV_PIN, GPIO.HIGH)
        print("TV turned ON")
    else:
        GPIO.output(TV_PIN, GPIO.LOW)
        print("TV turned OFF")

