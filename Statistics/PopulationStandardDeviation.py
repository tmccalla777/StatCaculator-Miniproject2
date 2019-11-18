from Statistics.Mean import mean
from Calculator.Squareroot import squareroot
from Statistics.PopulationVariance import variance

def population_SD(data):
    SDvalue = squareroot(variance(data))
    return SDvalue