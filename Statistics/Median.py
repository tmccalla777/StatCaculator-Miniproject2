from Calculator.Addition import addition
from Calculator.Division import division

def median(data):
    sortedData = sorted(data)
    middleIndex = len(sortedData)-1 // 2

    if(len(sortedData)) % 2:
        sumMiddle = addition(sortedData[middleIndex],sortedData[middleIndex+1])
        return (division(sumMiddle,2.0))
    else:
        return sortedData[middleIndex]
