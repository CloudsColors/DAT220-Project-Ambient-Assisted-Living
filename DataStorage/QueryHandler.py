import os,sys
from datetime import datetime

'''
This module is to mimic very roughly some database functionality for the project.
'''
def query_heartbeat():
    f = open(os.path.dirname(__file__)+"/data/heartbeat.txt", "r")
    data = f.read()
    f.close()
    return data

def query_stepcounter():
    f = open(os.path.dirname(__file__)+"/data/stepcounter.txt", "r")
    data = f.read()
    f.close()
    return data

def insert_glucose(gluc):
    f = open(os.path.dirname(__file__)+"/data/glucose.txt", "a+")
    f.write(gluc + "," + datetime.now().strftime("%Y-%m-%d %H:%M") + "\n")
    f.close()
    

def insert_bloodpressure(blo):
    f = open(os.path.dirname(__file__)+"/data/bloodpressure.txt", "a+")
    f.write(blo + "," + datetime.now().strftime("%Y-%m-%d") + "\n")
    f.close()

def query_glucose():
    f = open(os.path.dirname(__file__)+"/data/glucose.txt", "r")
    data = f.read().split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(",")
    f.close()
    return data

def query_bloodpressure():
    f = open(os.path.dirname(__file__)+"/data/bloodpressure.txt", "r")
    data = f.read().split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(",")
    f.close()
    return data
    
'''
Below functions for testing
'''
def main():
    print(query_stepcounter())

if __name__ == "__main__":
    main()