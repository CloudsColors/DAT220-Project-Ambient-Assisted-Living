import csv, os

def get_alarm_detection():
    f = csv.reader(open(os.path.dirname(__file__)+"/../DataStorage/data/compositedata.csv", "r"))
    compData = list(f)
    return [[compData[1][0], compData[1][1]]]