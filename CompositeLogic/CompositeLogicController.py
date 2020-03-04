import csv, os

def get_alarm_detection():
    f = csv.reader(open(os.path.dirname(__file__)+"/../DataStorage/data/compositedata.csv"))
    compData = list(f)
    return [[compData[1][0], compData[1][1]]]


def detect_smoke():
    r = csv.reader(open(os.path.dirname(__file__)+"/../DataStorage/data/compositedata.csv"))
    lines = list(r)
    lines[1][0] = 'smoke detected'
    lines[1][1] = 'alert all'
    writer = csv.writer(open(os.path.dirname(__file__)+"/../DataStorage/data/compositedata.csv", 'w+', newline=""))
    writer.writerows(lines)

def reset():
    r = csv.reader(open(os.path.dirname(__file__)+"/../DataStorage/data/compositedata.csv"))
    lines = list(r)
    lines[1][0] = '0'
    lines[1][1] = '0'
    writer = csv.writer(open(os.path.dirname(__file__)+"/../DataStorage/data/compositedata.csv", 'w+', newline=""))
    writer.writerows(lines)
