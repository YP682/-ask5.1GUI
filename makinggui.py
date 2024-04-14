from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

# Constants for pin numbers
RED_PIN = 40
BLUE_PIN = 38
GREEN_PIN = 36

# Initialise GPIO
def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.setup(BLUE_PIN, GPIO.OUT)
    GPIO.output(BLUE_PIN, GPIO.LOW)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    GPIO.output(GREEN_PIN, GPIO.LOW)

# Initialise Tkinter
win = Tk()
win.title("GUI")

# Define font
myFont = tkinter.font.Font(family='Helvetica', size = 30, weig>

# Setup GPIO
setup_gpio()

# Button callbacks
def redledON():
    print("Red LED button pressed")
if GPIO.input(40):
        GPIO.output(40, GPIO.LOW)
        redButton["text"] = "RED LED ON"
    else:
        GPIO.output(40, GPIO.HIGH)
        redButton["text"] = "RED LED OFF"

def blueledON():
    print("Blue LED button pressed")
    if GPIO.input(38):
        GPIO.output(38, GPIO.LOW)
        blueButton["text"] = "BLUE LED ON"
    else:
        GPIO.output(38, GPIO.HIGH)
        blueButton["text"] = "BLUE LED OFF"

def greenledON():
    print("Green LED button pressed")
    if GPIO.input(36):
        GPIO.output(36, GPIO.LOW)
        greenButton["text"] = "GREEN LED ON"
    else:
        GPIO.output(36, GPIO.HIGH)
        greenButton["text"] = "GREEN LED OFF"

def exitProgram():
    print("Exit button pressed")
    GPIO.cleanup()
    win.quit()

# Create buttons
exitButton = Button(win, text = "EXIT", font = myFont, command>exitButton.pack()

redButton = Button(win, text = "RED led ON", font = myFont, co>redButton.pack()

blueButton = Button(win, text = "BLUE led ON", font = myFont, >blueButton.pack()

greenButton = Button(win, text = "GREEN led ON", font = myFont>greenButton.pack()

win.mainloop()
