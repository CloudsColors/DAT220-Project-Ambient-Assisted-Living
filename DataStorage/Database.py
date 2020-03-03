import traceback

def writeToFile(filename, flag, payload):
    try:
        f = open(filename, flag)
    except Exception:
        print(traceback.format_exc())
    f.write(payload)
    f.close()

def getFromFile(filename):
    try:
        f = open(filename, "r")
    except Exception:
        print(traceback.format_exc())
    data = f.read()
    return data


# Below is for testing cases
if __name__ == "__main__":
    writeToFile()