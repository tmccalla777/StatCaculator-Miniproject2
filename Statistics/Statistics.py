from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.PopulationStandardDeviation import SD
from Statistics.z_score import z_score
from Statistics.standardized_score import score
from Statistics.correlation_coefficient import correlation_coefficient
from Statistics.confidence_interval import confidence_interval
from Statistics.population_variance import population_variance

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

    def SD(self, Value1, Value2, Value3):
        self.result = SD(Value1, Value2, Value3)
        return self.result

    def zscore(self, a, b, c):
        self.result = z_score(a, b, c)
        return self.result

    def standardized(self, a, b, c):
        self.result = score(a, b, c)
        return self.result

    def corr_coef(self, a, b, c, d, e, f, g, h, j, k):
        self.result = correlation_coefficient(a, b, c, d, e, f, g, h, j, k)
        return self.result

    def confidence(self, a, b, c, d, e, f, g, h, j, k):
        self.result = confidence_interval(a, b, c, d, e, f, g, h, j, k)
        return self.result

    def pop_var(self, a, b, c, d, e, f, g, h, j, k):
        self.result = population_variance(a, b, c, d, e, f, g, h, j, k)
        return self.result