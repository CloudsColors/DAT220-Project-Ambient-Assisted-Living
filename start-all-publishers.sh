#!/bin/bash

step=0

while true;
do
    $step+=1
    mosquitto_pub -h localhost -t home/door/maindoor -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/door/backdoor -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/window/bedroom -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/window/livingroom -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/window/kitchen -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/sensors/smoke -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/puc/stepcounter -m $step
    mosquitto_pub -h localhost -t home/puc/stepcounter -m $(($RANDOM%10+70))
    sleep 1
done