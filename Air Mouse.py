# -- coding: utf-8 --
"""
Created on Mon Jun  7 18:49:20 2021

@author: Hanan
"""

import serial
import time
import mouse
from subprocess import call
        
arduino = serial.Serial('COM5', 9600, timeout=0.1)

while True:
    try:
        data1 = arduino.readline()
        if (data1):
            data2 = list(map(eval,str(data1)[2:-5].split("/")))
            print(data2)
            finger1=data2[0]
            finger2=data2[1]
            finger3=data2[2]
            finger4=data2[3]

            if (finger1<600 and finger2<600 and finger3<600 and finger4<600):
                mouse.click('left')
            if (finger3>600 and finger4>600 and finger1<600 and finger2<600):
                mouse.click('right')
            if (finger1>600 and finger2<600 and finger3<600 and finger4<600):
                mouse.move(-10,0, absolute=False, duration=0.1)
            if (finger1<600 and finger2>600 and finger3<600 and finger4<600):
                mouse.move(10,0, absolute=False, duration=0.1)
            if (finger1<600 and finger2<600 and finger3>600 and finger4<600):
                mouse.move(0,-10, absolute=False, duration=0.1)
            if (finger1<600 and finger2<600 and finger3<600 and finger4>600):
                mouse.move(0,10, absolute=False, duration=0.1)
            if (finger1>600 and finger2>600 and finger3>600 and finger4>600):
                print("Terminted")
                break
        
    except KeyboardInterrupt:
        break