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
              4. Developer Option
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
        
def X_maker(hand):
    l=[]
    for i in range(1,len(hand)):
       l=l+[[hand[i][0],hand[i][1],hand[i][2],hand[i][3]]]
    return np.array(l)
    
def y_maker(hand):
    l=[]
    for i in range(1,len(hand)):
       l=l+[[hand[i][4]]] 
    return np.array(l)

option = interact()
arduino = serial.Serial('COM5', 19200, timeout=0.1)

#Storing Action photograph values
if option==1:
    csv_path = open('D:\\Codes\\Python\\PROJECTS\\ITSP-Hand_of_God\\Hand.csv')
    writer1 = csv.writer(csv_path)
    action_name = input(str("Action name >>> "))
    print("Analyzing Input...")
    for rep in range(100):
        data1 = arduino.readline()
        if (data1):
            data2 = list(map(eval,str(data1)[2:-5].split("/")))
            data2 = data2[0:4] + [action_name]
            writer1.writerow(data2)
    csv_path.close()

#Storing Action sequences
if option==2:
    file1 = open("D:\\Codes\\Python\\PROJECTS\\ITSP-Hand_of_God\\Commands.txt","r")
    file1.seek(0) 
    file2 = file1.readline()
    file2 = eval(file2)

    actions=[]
    file_CSV=open('D:\\Codes\\Python\\PROJECTS\\ITSP-Hand_of_God\\Hand.csv')
    reader1 = csv.reader(file_CSV)

    hand=list(reader1)
    X=X_maker(hand)
    y=y_maker(hand)
    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
    svm_model_linear=SVC(kernel='linear',C=1).fit(X_train,y_train)
    accuracy=svm_model_linear.score(X_test,y_test)        
    print("Training Accuracy :",100*accuracy,"%")
    print()
    print("Predicting the performed action...")
    print()

    train_len = 0
    final_predictions = []
    for learn_i in range(100):
        data1 = arduino.readline()
        if (data1):
            data2 = list(map(eval,str(data1)[2:-5].split("/")))
            actions = actions + [svm_model_linear.predict([data2[0:4]])[0]]
            if len(actions)>0 and len(final_predictions)>0:
                if actions[-1] != final_predictions[-1]:
                    final_predictions = final_predictions + [actions[-1]]

            if len(actions)>0 and len(final_predictions)==0:
                final_predictions = final_predictions + [actions[-1]]

            if train_len != len(final_predictions):
                train_len = len(final_predictions)
                print(final_predictions[-1])

    command_name = str(input("Enter command name : "))
    print(command_name,":",final_predictions)
    file_CSV.close()
    file1.close()
    agree = str(input("Store (Y/N) > "))    
    if agree in ["Y","y","Yes","yes"]:
        file2[command_name] = final_predictions
        file3 = open("D:\\Codes\\Python\\PROJECTS\\ITSP-Hand_of_God\\Commands.txt","w")
        file3.seek(0)
        file3.write(str(file2))
        file3.close()

#Machine Learning with SVM classification algorithm
if option==3:
    actions=[]
    file_CSV=open('D:\\Codes\\Python\\PROJECTS\\ITSP-Hand_of_God\\Hand.csv')
    reader1=csv.reader(file_CSV)

    hand=list(reader1)
    X=X_maker(hand)
    y=y_maker(hand)
    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
    svm_model_linear=SVC(kernel='linear',C=1).fit(X_train,y_train)
    accuracy=svm_model_linear.score(X_test,y_test)        
    print("Training Accuracy :",100*accuracy,"%")
    print()
    print("Predicting the performed action...")
    print()

    train_len = 0
    final_predictions = []
    clutch = True
    standby = True
    while True:
        if clutch:
            final_predictions = []
            data1 = arduino.readline()
            if (data1):
                data2 = list(map(eval,str(data1)[2:-5].split("/")))
                actions = actions + [svm_model_linear.predict([data2[0:4]])[0]]
                if len(actions)>0 and len(final_predictions)>0:
                    if actions[-1] != final_predictions[-1]:
                        final_predictions = final_predictions + [actions[-1]]

                if len(actions)>0 and len(final_predictions)==0:
                    final_predictions = final_predictions + [actions[-1]]

                if train_len != len(final_predictions):
                    train_len = len(final_predictions)
                    print(final_predictions[-1])
        
        if (not clutch) and standby:
            standby = False
            print("Glove is on Standby ...")
            print()


    file_CSV.close()

if option==4:
    while True:
        data1 = arduino.readline()
        if (data1):
            data2 = list(map(eval,str(data1)[2:-5].split("/")))
            print(data2)