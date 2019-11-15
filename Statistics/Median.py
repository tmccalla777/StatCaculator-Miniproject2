from Calculator.Addition import addition
from Calculator.Division import division

def median(Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8, Value9):
    val1 = int(Value1)
    val2 = int(Value2)
    val3 = int(Value3)
    val4 = int(Value4)
    val5 = int(Value5)
    val6 = int(Value6)
    val7 = int(Value7)
    val8 = int(Value8)
    val9 = int(Value9)
    values = [val1, val2, val3, val4, val5, val6, val7, val8, val9]
    sortedData = sorted(values)
    middleIndex = (len(sortedData)-1) // 2
    return sortedData[middleIndex]