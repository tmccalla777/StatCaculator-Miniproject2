from Statistics.PopulationVariance import variance

def SD(Value1, Value2, Value3):
    a = int(Value1)
    b = int(Value2)
    c = int(Value3)
    varianceValue = variance(a,b,c)
    SDvalue = varianceValue**0.5
    return SDvalue