import paho.mqtt.client as mqttclient
import DataStorage.QueryHandler as qh

import os

'''
Module for mimicing how the "database" stores the sensor information that is sent over MQTT.
'''
def on_connect(client, userdata, flags, rc):
    client.subscribe([("home/puc/heartbeat", 0),("home/puc/stepcounter", 0)])

def on_message(client, userdata, msg):
    if(msg.topic == "home/puc/heartbeat"):
        qh.insert_heartbeat(os.path.dirname(__file__)+"DataStorage/data/heartbeat.txt", msg.payload.decode())
    elif(msg.topic == "home/puc/stepcounter"):
        qh.insert_steps(os.path.dirname(__file__)+"DataStorage/data/stepcounter.txt", msg.payload.decode())

def main():
    client = mqttclient.Client("Collector")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost")
    client.loop_forever()

if __name__ == "__main__":
    main()