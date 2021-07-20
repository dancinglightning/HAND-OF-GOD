# -- coding: utf-8 --
"""
Created on Mon Jun  7 18:49:20 2021

@author: Hanan
"""

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import csv
import serial
import time
import pandas as pd
import mouse

def interact():
    t=""
    while t!="1" or t!="2":
        print('''Enter Option Number :
              1. Store Action
              2. Store command
              3. Perform Command
              4. Developer option
              ''')
        t=str(input(">>> "))
        if t=="1":
            return 1
            break
        if t=="2":
            return 2
            break
        if t=="3":
            return 3
            break
        if t=="4":
            return 4
            break
        
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
        if (finger1<600 and finger2<600 and finger3<600 and finger4<600):
            mouse.click('left')
        elif (finger3>600 and finger4>600 and finger1<600 and finger2<600):
             mouse.click('right')
        elif (finger1>600 and finger2<600 and finger3<600 and finger4<600):
            mouse.move(-10,0, absolute=False, duration=0.1)
        elif (finger1<600 and finger2>600 and finger3<600 and finger4<600):
            mouse.move(10,0, absolute=False, duration=0.1)
        elif (finger1<600 and finger2<600 and finger3>600 and finger4<600):
            mouse.move(0,-10, absolute=False, duration=0.1)
        elif (finger1<600 and finger2<600 and finger3<600 and finger4>600):
            mouse.move(0,10, absolute=False, duration=0.1)
        elif (finger1>600 and finger2>600 and finger3>600 and finger4>600):
            print("Terminted")
            break
        