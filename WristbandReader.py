import paho.mqtt.client as mqttclient
import DataStorage.QueryHandler as qh

import os, platform

'''
Module for mimicing how the "database" stores the sensor information that is sent over MQTT.
'''
def on_connect(client, userdata, flags, rc):
    client.subscribe([("home/puc/heartbeat", 0),("home/puc/stepcounter", 0)])

def on_message(client, userdata, msg):
    path = ""
    if(platform.system() == "Windows"):
        path = os.path.dirname(__file__)+"/DataStorage/data/stepcounter.txt"
    else:
        path = os.path.dirname(__file__)+"DataStorage/data/stepcounter.txt"
    if(msg.topic == "home/puc/heartbeat"):
        qh.insert_heartbeat("./DataStorage/data/heartbeat.txt", msg.payload.decode())
    elif(msg.topic == "home/puc/stepcounter"):
        qh.insert_steps("./DataStorage/data/stepcounter.txt", msg.payload.decode())

def main():
    client = mqttclient.Client("Collector")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost")
    client.loop_forever()

if __name__ == "__main__":
    main()