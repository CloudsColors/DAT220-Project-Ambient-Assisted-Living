import paho.mqtt.client as mqttclient

import random, time

'''
Mimics all the sensors in the house.
'''
def createAndRunPublishers():
    while(True):
        client = mqttclient.Client("HomeSensors")
        client.connect("localhost")
        smokeAlarm = 0
        #Doors
        client.publish("home/door/maindoor", f"{random.randint(0,1)}")
        client.publish("home/door/backdoor", f"{random.randint(0,1)}")
        #Windows
        client.publish("home/window/bedroom", f"{random.randint(0,1)}")
        client.publish("home/window/livingroom", f"{random.randint(0,1)}")
        client.publish("home/window/kitchen", f"{random.randint(0,1)}")
        #Sensors (smoke)
        if(random.randint(1,100) > 80):
            smokeAlaram = 1
        else:
            smokeAlarm = 0
        client.publish("home/sensors/smoke", f"{smokeAlarm}")
        time.sleep(1)

if __name__ == "__main__":
    createAndRunPublishers()