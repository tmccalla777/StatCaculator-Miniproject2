from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.PopulationStandardDeviation import population_SD

class Statistics(Calculator):
    result = 0

    def __init__(self):
        super().__init__()

    def mean(self, Value1, Value2, Value3):
        self.result = mean(Value1, Value2, Value3)
        return self.result

    def median(self, Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8, Value9):
        self.result = median(Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8, Value9)
        return self.result

    def mode(self, Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8):
        self.result = mode(Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8)
        return self.result

    def population_SD(self, data):
        self.data = population_SD(data)
        return self.result