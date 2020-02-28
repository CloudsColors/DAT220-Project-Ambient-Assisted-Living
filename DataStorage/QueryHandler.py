import os,sys

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
    f.write(gluc + "\n")
    f.close()
    

def insert_bloodpressure(blo):
    f = open(os.path.dirname(__file__)+"/data/bloodpressure.txt", "a+")
    f.write(blo + "\n")
    f.close()
    
'''
Below functions for testing
'''
def main():
    print(query_stepcounter())

if __name__ == "__main__":
    main()