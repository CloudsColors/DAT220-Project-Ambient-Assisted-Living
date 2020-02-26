import paho.mqtt.client as mqttclient
import paho.mqtt.publish as mqttpub
import time, random

def main():
    steps = 0
    while(True):
        heartbeat = 75
        client = mqttclient.Client("WristbandReader")
        client.connect("localhost",188)
        steps+=1
        heartbeat += random.randint(-15, 15)
        client.publish("home/puc/stepcounter", f"{steps}")
        client.publish("home/puc/heartbeat", f"{heartbeat}")
        time.sleep(2)

if __name__ == "__main__":
    main()