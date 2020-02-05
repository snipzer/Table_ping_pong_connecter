import time
import RPi.GPIO as GPIO

# Définition des pins
pinBtn = 2

GPIO.setmode(GPIO.BCM)

# Définition des pins en entrée / sortie

GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    etat = GPIO.input(pinBtn)

    if etat == 0:
        print("Appui detecte")


    time.sleep(0.2)
