#!/bin/bash

step=0

while true;
do
    let "step+=1"
    mosquitto_pub -h localhost -t home/door/maindoor -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/door/backdoor -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/window/bedroom -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/window/livingroom -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/window/kitchen -m $(($RANDOM%2))
    mosquitto_pub -h localhost -t home/puc/movement -m $(($RANDOM%4))
    if [ $(($step % 5)) -eq 0 ]
    then
        if [ $(($RANDOM % 100)) -gt 66 ]
        then
            mosquitto_pub -h localhost -t home/sensors/smoke -m 1
        else
            mosquitto_pub -h localhost -t home/sensors/smoke -m 0
        fi
    fi
    mosquitto_pub -h localhost -t home/puc/stepcounter -m $step
    mosquitto_pub -h localhost -t home/puc/heartbeat -m $(($RANDOM%10+70))
    sleep 1
done