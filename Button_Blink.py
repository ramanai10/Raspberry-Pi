from tkinter import *
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
def normal():
    while True:
        GPIO.output(13, True)
        time.sleep(0.5)
        GPIO.output(13, False)
        time.sleep(0.5)

def btnCLick(s):
    if s == True
        GPIO.output(13, True)
        time.sleep(0.5)
    else:
        pass

normal()

root = Tk()
mybtn = Button(root, text="Push!", command= lambda f=True:btnClick, padx=55)
mybtn.pack()
root.mainloop()

