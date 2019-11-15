from Statistics.PopulationVariance import varianceFunc

def SD(Value1, Value2, Value3):
    a = int(Value1)
    b = int(Value2)
    c = int(Value3)
    varianceValue = varianceFunc(a,b,c)
    SDvalue = varianceValue**0.5
    return SDvalue