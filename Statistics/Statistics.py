from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.PopulationStandardDeviation import population_SD

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.data = mean(data)
        return self.data

    def median(self, data):
        self.data = median(data)
        return self.data

    def mode(self, data):
        self.data = mode(data)
        return self.data

    def population_SD(self, data):
        self.data = population_SD(data)
        return self.data