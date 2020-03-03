#!/bin/bash

echo "Starting the MQTT subscribers in python!"
pipenv run python WristbandReader.py & disown
pipenv run python HomeSensorHandler/SensorDataCollector.py & disown
echo "Started subscribers, now starting the publishers"
./start-all-publishers.sh