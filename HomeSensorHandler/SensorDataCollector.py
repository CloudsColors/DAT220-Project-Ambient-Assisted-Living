import paho.mqtt.client as mqttclient

import os
import csv

'''
Module for mimicing how the "database" stores the sensor information that is sent over MQTT.
'''
def on_connect(client, userdata, flags, rc):
    client.subscribe([("home/door/maindoor", 0),
                      ("home/door/backdoor", 1),
                      ("home/window/bedroom", 2),
                      ("home/window/livingroom", 3),
                      ("home/window/kitchen", 4)
                      ])

def on_message(client, userdata, msg):
    if(msg.topic == "home/door/maindoor"):
        writeToCsv(0,0, msg.payload.decode())

    if(msg.topic == "home/door/backdoor"):
        writeToCsv(1,1, msg.payload.decode())

    if(msg.topic == "home/window/bedroom"):
        writeToCsv(2,2, msg.payload.decode())

    if(msg.topic == "home/window/livingroom"):
        writeToCsv(3,3, msg.payload.decode())

    if(msg.topic == "home/window/kitchen"):
        writeToCsv(4,4, msg.payload.decode())


def writeToCsv(x,y, payload):
    r = csv.reader(open(os.path.dirname(__file__)+"/data/doorwindowdata.csv"))
    lines = list(r)
    lines[x][y] = payload
    writer = csv.writer(open(os.path.dirname(__file__)+"/data/doorwindowdata.csv", 'w'))
    writer.writerows(lines)

def main():
    client = mqttclient.Client("Collector")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost")
    client.loop_forever()

if __name__ == "__main__":
    main()