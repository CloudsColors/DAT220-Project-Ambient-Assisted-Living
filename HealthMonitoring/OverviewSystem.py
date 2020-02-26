import DataStorage.QueryHandler as qh 

def heartBeatandStep():
    hb = qh.query_heartbeat()
    sc = qh.query_stepcounter()
    
    return hb,sc

#if __name__ == "__main__":
 #   main()