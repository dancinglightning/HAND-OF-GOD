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

            if (finger1>525 and finger2>525 and finger3>525 and finger4>525):
                print("Terminted")
                break
            elif (finger1>525 and finger2>525 and finger3>525 and finger4<525):
                mouse.move(0,0, absolute=False, duration=0.1)
            elif (finger1>525 and finger2>525 and finger3<525 and finger4>525):
                mouse.move(0,0, absolute=False, duration=0.1)
            elif (finger1>525 and finger2>525 and finger3<525 and finger4<525):
                mouse.click('left')
            elif (finger1>525 and finger2<525 and finger3>525 and finger4>525):
                mouse.move(0,0, absolute=False, duration=0.1)
            elif (finger1>525 and finger2<525 and finger3>525 and finger4<525):
                mouse.move(-20,-20, absolute=False, duration=0.1)
            elif (finger1>525 and finger2<525 and finger3<525 and finger4>525):
                mouse.move(-20,20, absolute=False, duration=0.1)
            elif (finger1>525 and finger2<525 and finger3<525 and finger4<525):
                mouse.move(-20,0, absolute=False, duration=0.1)
            elif (finger1<525 and finger2>525 and finger3>525 and finger4>525):
                mouse.move(0,0, absolute=False, duration=0.1)
            elif (finger1<525 and finger2>525 and finger3>525 and finger4<525):
                mouse.move(20,-20, absolute=False, duration=0.1)
            elif (finger1<525 and finger2>525 and finger3<525 and finger4>525):
                mouse.move(20,20, absolute=False, duration=0.1)
            elif (finger1<525 and finger2>525 and finger3<525 and finger4<525):
                mouse.move(20,0, absolute=False, duration=0.1)
            elif (finger1<525 and finger2<525 and finger3>525 and finger4>525):
                mouse.click('right')
<<<<<<< HEAD
            elif (finger1<525 and finger2<525 and finger3>525 and finger4<525):
                mouse.move(0,-20, absolute=False, duration=0.1)
            elif (finger1<525 and finger2<525 and finger3<525 and finger4>525):
                mouse.move(0,20, absolute=False, duration=0.1)
            elif (finger1<525 and finger2<525 and finger3<525 and finger4<525):
                mouse.move(0,0, absolute=False, duration=0.1)
=======
            elif (finger1<600 and finger2<600 and finger3>600 and finger4<600):
                mouse.move(0,-10, absolute=False, duration=0.1)
            elif (finger1<600 and finger2<600 and finger3<600 and finger4>600):
                mouse.move(0,10, absolute=False, duration=0.1)
            elif (finger1<600 and finger2<600 and finger3<600 and finger4<600):
                mouse.move(0,0, absolute=False, duration=0.1)


                
>>>>>>> 706ff3f08fea9cc7210fc4972eaad2c980c3dc07
