import csv, os

def get_doors():
    doorData = get_file_contents()
    return [[doorData[0][0], doorData[1][0]], [doorData[0][1],doorData[1][1]]]

def get_windows():
    windowData = get_file_contents()
    return [[windowData[0][2], windowData[1][2]], [windowData[0][3], windowData[1][3]], [windowData[0][4], windowData[1][4]]]

def get_smoke():
    smokeData = get_file_contents()
    return [[smokeData[0][5], smokeData[1][5]]]

def get_movement_filter():
    movementData = get_file_contents()
    return [[movementData[0][6]], [movementData[1][6]]]
    
def get_file_contents():
    f = csv.reader(open(os.path.dirname(__file__)+"/../DataStorage/data/doorwindowdata.csv", "r"))
    return list(f)

if __name__ == "__main__":
    print(get_windows())