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

'''
Below functions for testing
'''
def main():
    print(query_stepcounter())

if __name__ == "__main__":
    main()