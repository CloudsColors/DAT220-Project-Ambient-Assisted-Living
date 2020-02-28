import DataStorage.QueryHandler as qh 

def glucose_data(glu):
    qh.insert_glucose(glu)

def blood_data(blo):
    qh.insert_bloodpressure(blo) 
    