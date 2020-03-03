import HomeAccess.HomeStatus as hh

def get_door_status():
    data = hh.get_doors()
    for i in range(len(data)):
        if(data[i][1] == "0"):
            data[i][1] = "closed"
        else:
            data[i][1] = "opened"
    return data

if __name__ == "__main__":
    get_door_status()