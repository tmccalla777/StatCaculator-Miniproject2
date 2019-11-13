from Statistics.Mean import mean
from Calculator.Squareroot import squarerooting

def population_standard_deviation(data):
    n = len(data)
    variance = 0
    meanData = mean(data)
    for i in data:
        variance += (i-meanData)**2
    variance /= n
    return squarerooting(variance)