def mode(Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8):
    val1 = int(Value1)
    val2 = int(Value2)
    val3 = int(Value3)
    val4 = int(Value4)
    val5 = int(Value5)
    val6 = int(Value6)
    val7 = int(Value7)
    val8 = int(Value8)
    values = [val1, val2, val3, val4, val5, val6, val7, val8]
    modeValue = max(set(values), key=values.count)
    return modeValue