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

def interact():
    t=""
    while t!="1" or t!="2":
        print('''Enter Option Number :
              1. Store Action
              2. Store command
              3. Perform Command
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
        
def X_maker(hand):
    l=[]
    for i in range(1,len(hand)):
       l=l+[[hand[i][0],hand[i][1],hand[i][2]]]
    return np.array(l)
    
def y_maker(hand):
    l=[]
    for i in range(1,len(hand)):
       l=l+[hand[i][3]] 
    return np.array(l)

option = interact()
arduino = serial.Serial('COM3', 19200, timeout=0.1)

#Storing values
if option==1:
    csv_path = open('D:\\Codes\\Python\\PROJECTS\\ITSP\\Hand.csv')
    writer1 = csv.writer(csv_path)
    action_name = input(str("Action name >>> "))
    print("Analyzing Input...")
    for rep in range(100):
        data1 = arduino.readline()
        if (data1):
            data2 = list(map(float,str(data1)[2:-5].split("/")))
            data2 = data2[0:3] + [action_name]
            writer1.writerow(data2)
    csv_path.close()

#Storing Action sequences
if option==2:
    file1 = open("D:\\Codes\\Python\\PROJECTS\\ITSP\\Commands.txt","r")
    file1.seek(0) 
    file2 = file1.read()
    file2 = dict(file2)
    print(file2, type(file2))

#Machine Learning with SVM classification algorithm
if option==3:

    actions=[[1,2,3]]
    file_CSV=open('D:\\Codes\\Python\\PROJECTS\\ITSP\\Hand.csv')
    reader1=csv.reader(file_CSV)

    hand=list(reader1)
    X=X_maker(hand)
    y=y_maker(hand)
    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
    svm_model_linear=SVC(kernel='linear',C=1).fit(X_train,y_train)

    print("Predicting the performed action...")
    print()

    train_len = 0
    final_predictions = []
    while 1>0:
        data1 = arduino.readline()
        if (data1):
            data2 = list(map(eval,str(data1)[2:-5].split("/")))
            actions = actions + [svm_model_linear.predict(np.array([data2[0:3]]))]
            if len(actions)>0 and len(final_predictions)>0:
                if actions[-1]!=final_predictions[-1]:
                    final_predictions = final_predictions + [actions[-1]]

            if len(actions)>0 and len(final_predictions)==0:
                final_predictions = final_predictions + [actions[-1]]

            if train_len != len(final_predictions):
                train_len = len(final_predictions)
                print(final_predictions[-1][0])
            

    accuracy=svm_model_linear.score(X_test,y_test)        
    print("Predictions :",final_predictions)
    print("Training Accuracy :",100*accuracy,"%")

    file_CSV.close()