import HomeAccess.HomeStatus as hh

def get_smoke_status():
    data = hh.get_smoke()
    for i in range(len(data)):
        if(data[i][1] == "0"):
            data[i][1] = "no smoke :("
        else:
            data[i][1] = "FIRE 8===D"
    return data

if __name__ == "__main__":
    get_smoke_status()