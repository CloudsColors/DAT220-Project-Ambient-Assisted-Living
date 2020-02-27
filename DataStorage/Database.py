import paho.mqtt.client as mqttclient

import os,sys

'''
Module for mimicing how the "database" stores the sensor information that is sent over MQTT.
'''
def on_connect(client, userdata, flags, rc):
    client.subscribe([("home/puc/heartbeat", 0),("home/puc/stepcounter", 1)])

def on_message(client, userdata, msg):
    if(msg.topic == "home/puc/heartbeat"):
        writeToFile(os.path.dirname(__file__)+"/data/heartbeat.txt", msg.payload.decode())
    elif(msg.topic == "home/puc/stepcounter"):
        writeToFile(os.path.dirname(__file__)+"/data/stepcounter.txt", msg.payload.decode())

def writeToFile(filename, payload):
    f = open(filename, "w+")
    f.write(payload)
    f.close()

def main():
    client = mqttclient.Client("Collector")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost")
    client.loop_forever()

if __name__ == "__main__":
    main()