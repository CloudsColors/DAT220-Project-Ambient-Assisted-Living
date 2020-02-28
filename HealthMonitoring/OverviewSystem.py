import DataStorage.QueryHandler as qh 

def heartbeat_data():
    hb = qh.query_heartbeat()
    return hb

def stepcounter_data():
    sc = qh.query_stepcounter()
    return sc

def bloodpressure_data():
    bp = qh.query_bloodpressure()
    return bp

def glucose_data():
    gc = qh.query_glucose()
    return gc

#if __name__ == "__main__":
 #   main()