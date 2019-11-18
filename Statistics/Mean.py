from Calculator.Addition import addition
from Calculator.Division import division

def mean(Value1, Value2, Value3):
    a = int(Value1)
    b = int(Value2)
    c = int(Value3)
    values = [a,b,c]
    meanValue = (a+b+c)/len(values)
    return meanValue