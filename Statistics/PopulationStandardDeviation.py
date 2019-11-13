from Statistics.Mean import mean
from Calculator.Squareroot import squareroot

def population_SD(data):
    n = len(data)
    variance = 0
    meanData = mean(data)
    for i in data:
        variance += (i-meanData)**2
    variance /= n
    return squareroot(variance)