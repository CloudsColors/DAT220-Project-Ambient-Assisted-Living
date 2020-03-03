import csv, os

def get_doors():
    f = csv.reader(open(os.path.dirname(__file__)+"/../DataStorage/data/doorwindowdata.csv", "r"))
    doorData = list(f)
    return [[doorData[0][0], doorData[1][0]], [doorData[0][1],doorData[1][1]]]

def get_windows():
    f = csv.reader(open(os.path.dirname(__file__)+"/../DataStorage/data/doorwindowdata.csv", "r"))
    windowData = list(f)
    return [[windowData[0][2], windowData[1][2]], [windowData[0][3], windowData[1][3]], [windowData[0][4], windowData[1][4]]]

if __name__ == "__main__":
    print(get_windows())