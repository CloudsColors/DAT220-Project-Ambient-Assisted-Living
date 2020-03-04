import HomeAccess.HomeStatus as hh

def get_movement_status():
    data = hh.get_movement_filter()
    lastSeen = data[1][0]
    if(lastSeen == "0"):
        data[1][0] = "Livingroom"
    elif(lastSeen == "1"):
        data[1][0] = "Kitchen"
    elif(lastSeen == "2"):
        data[1][0] = "Bedroom"
    else:
        data[1][0] = "The loo"
    return data