
def variance(Value1, Value2, Value3):
    a = int(Value1)
    b = int(Value2)
    c = int(Value3)
    values = [a, b, c]
    meanValue = (a + b + c) / len(values)
    n = len(values)
    variance = 0
    for i in values:
        variance = variance + float((meanValue - i) ** 2)
    varianceValue = float(variance/n)
    return varianceValue
