import paho.mqtt.client as mqttclient

def on_connect(client, userdata, flags, rc):
    client.subscribe([("home/puc/heartbeat", 0),("home/puc/stepcounter", 1)])

def on_message(client, userdata, msg):
    if(msg.topic == "home/puc/heartbeat"):
        writeToFile("heartbeat.txt", msg.payload.decode())
    elif(msg.topic == "home/puc/stepcounter"):
        writeToFile("stepcounter.txt", msg.payload.decode())

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