# -- coding: utf-8 --
"""
Created on Mon Jun  7 18:49:20 2021

@author: Hanan
"""

import serial
import time
import mouse

arduino = serial.Serial('COM3', 9600, timeout=0.1)

while True:
        data1 = arduino.readline()
        if (data1):
            data2 = list(map(eval,str(data1)[2:-5].split("/")))
            print(data2)
            finger1=data2[0]
            finger2=data2[1]
            finger3=data2[2]
            finger4=data2[3]

            if (finger1>420 and finger2>250 and finger3>250 and finger4>360):
                print("Terminted")
                break
            elif (finger1>420 and finger2>250 and finger3>250 and finger4<360):
                mouse.move(0,0, absolute=False, duration=0.1)
            elif (finger1>420 and finger2>250 and finger3<250 and finger4>360):
                mouse.move(0,0, absolute=False, duration=0.1)
            elif (finger1>420 and finger2>250 and finger3<250 and finger4<360):
                mouse.click('left')
            elif (finger1>420 and finger2<250 and finger3>250 and finger4>360):
                mouse.move(0,0, absolute=False, duration=0.1)
            elif (finger1>420 and finger2<250 and finger3>250 and finger4<360):
                mouse.move(-20,-20, absolute=False, duration=0.1)
            elif (finger1>420 and finger2<250 and finger3<250 and finger4>360):
                mouse.move(-20,20, absolute=False, duration=0.1)
            elif (finger1>420 and finger2<250 and finger3<250 and finger4<360):
                mouse.move(-20,0, absolute=False, duration=0.1)
            elif (finger1<420 and finger2>250 and finger3>250 and finger4>360):
                mouse.move(0,0, absolute=False, duration=0.1)
            elif (finger1<420 and finger2>250 and finger3>250 and finger4<360):
                mouse.move(20,-20, absolute=False, duration=0.1)
            elif (finger1<420 and finger2>250 and finger3<250 and finger4>360):
                mouse.move(20,20, absolute=False, duration=0.1)
            elif (finger1<420 and finger2>250 and finger3<250 and finger4<360):
                mouse.move(20,0, absolute=False, duration=0.1)
            elif (finger1<420 and finger2<250 and finger3>250 and finger4>360):
                mouse.click('right')
            elif (finger1<420 and finger2<250 and finger3>250 and finger4<360):
                mouse.move(0,-20, absolute=False, duration=0.1)
            elif (finger1<420 and finger2<250 and finger3<250 and finger4>360):
                mouse.move(0,20, absolute=False, duration=0.1)
            elif (finger1<420 and finger2<250 and finger3<250 and finger4<360):
                mouse.move(0,0, absolute=False, duration=0.1)