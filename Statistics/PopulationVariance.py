
def varianceFunc(Value1, Value2, Value3):
    a = int(Value1)
    b = int(Value2)
    c = int(Value3)
    values = [a, b, c]
    n = len(values)
    meanValue = (a + b + c) / n
    variance = 0
    for item in values:
        variance = variance + float((meanValue - item) ** 2)
    varianceValue = float(variance/n)
    return varianceValue