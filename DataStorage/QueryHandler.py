import os,sys

import DataStorage.Database as db

from datetime import datetime

'''
This module is to mimic very roughly some database functionality for the project.
'''

def insert_heartbeat(path, heartbeat):
    db.writeToFile(path, "w+", heartbeat)

def insert_steps(path, steps):
    db.writeToFile(path, "w+", steps)

def insert_glucose(gluc):
    db.writeToFile(os.path.dirname(__file__)+"/data/glucose.txt", "a+", gluc + "," + datetime.now().strftime("%Y-%m-%d %H:%M") + "\n")
    
def insert_bloodpressure(blo):
    db.writeToFile(os.path.dirname(__file__)+"/data/bloodpressure.txt", "a+", blo + "," + datetime.now().strftime("%Y-%m-%d") + "\n")

def query_heartbeat():
    return db.getFromFile(os.path.dirname(__file__)+"/data/heartbeat.txt")

def query_stepcounter():
    return db.getFromFile(os.path.dirname(__file__)+"/data/stepcounter.txt")

def query_glucose():
    data = db.getFromFile(os.path.dirname(__file__)+"/data/glucose.txt").split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(",")
    return data

def query_bloodpressure():
    data = db.getFromFile(os.path.dirname(__file__)+"/data/bloodpressure.txt").split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(",")
    return data

'''
Below functions for testing
'''
def main():
    print(query_stepcounter())

if __name__ == "__main__":
    main()