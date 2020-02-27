import paho.mqtt.client as mqttclient

import time, random

'''
This module mimics the sensor for a fitbit in a very barebones manner and publishes the data to another module with MQTT
'''
def start_sensor_fitbit():
    steps = 0
    while(True):
        # General data variation
        heartbeat = 70
        steps += random.randint(0,1)
        heartbeat += random.randint(-1, 1)
        # Networking with MQTT (publish)
        client = mqttclient.Client("WristbandReader")
        client.connect("localhost")
        client.publish("home/puc/stepcounter", f"{steps}")
        client.publish("home/puc/heartbeat", f"{heartbeat}")
        # Sleep one second for data-sanity
        time.sleep(1)

if __name__ == "__main__":
    start_sensor_fitbit()