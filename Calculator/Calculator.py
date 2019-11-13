import math
from decimal import Decimal
import statistics


def mean(a, b):
    a = int(a)
    b = int(b)
    c = ( a + b ) / 2
    return c


def median(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.median([a, b, c])
    return d


def mode(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.mode([a, b, c])
    return d


def stdev(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.stdev([a, b, c])
    return Decimal(d).quantize(Decimal('.001'))


def variance(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.variance([a, b, c])
    return Decimal(d).quantize(Decimal('.001'))


def zscore(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.stdev([a, b, c])
    e = ( a + b + c) / 3
    f = (a - e)/ d
    return Decimal(f).quantize(Decimal('.001'))


def standardized_score(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.stdev([a, b, c])
    e = ( a + b + c) / 3
    f = (a - e)/ d
    return Decimal(f).quantize(Decimal('.001'))


def population_correlation_coefficient(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = statistics.stdev([a, b, c])
    e = ( a + b + c) / 3
    f = ((a - e)/ d +(b - e)/ d +(c - e)/ d)/ 3
    return Decimal(f).quantize(Decimal('.001'))


def confidence_interval(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = zscore(a, b, c)
    e = stdev(a, b, c)
    f = d * e / Decimal(math.sqrt(3)).quantize(Decimal('.001'))
    return Decimal(f).quantize(Decimal('.001'))


def population_variance(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = stdev(a, b, c)
    e = d * d
    return Decimal(e).quantize(Decimal('.001'))


def p_value(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = stdev(a, b, c)
    e = 2 * abs(d)
    return Decimal(e).quantize(Decimal('.001'))


def proportion(a, b, c, d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = (a * b + c * d )/ (b + d)
    return Decimal(e).quantize(Decimal('.001'))


def sample_mean(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = (a + b + c)/ 3
    return Decimal(d).quantize(Decimal('.001'))


def sample_standard_deviation(a, b, c):
    a = Decimal(a).quantize(Decimal('.001'))
    b = Decimal(b).quantize(Decimal('.001'))
    c = Decimal(c).quantize(Decimal('.001'))
    d = (a + b + c)/ 3
    e = math.sqrt(Decimal(((a - d)*(a - d) + (b - d)*(b - d) + (c - d)*(c - d)) / 2).quantize(Decimal('.001')))
    return Decimal(e).quantize(Decimal('.001'))


def variance_of_sample_proportion(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = (a * b) / (c - 1)
    return Decimal(d).quantize(Decimal('.001'))


class Calculator:
    result = 0

    def __init__(self):
        pass

    def mean(self, a, b):
        self.result = mean(a, b)
        return self.result

    def median(self, a, b, c):
        self.result = median(a, b, c)
        return self.result

    def mode(self, a, b, c):
        self.result = mode(a, b, c)
        return self.result

    def stdev(self, a, b, c):
        self.result = stdev(a, b, c)
        return self.result

    def variance(self, a, b, c):
        self.result = variance(a, b, c)
        return self.result

    def zscore(self, a, b, c):
        self.result = zscore(a, b, c)
        return self.result

    def standardized_score(self, a, b, c):
        self.result = standardized_score(a, b, c)
        return self.result

    def population_correlation_coefficient(self, a, b, c):
        self.result = population_correlation_coefficient(a, b, c)
        return self.result

    def confidence_interval(self, a, b, c):
        self.result = confidence_interval(a, b, c)
        return self.result

    def population_variance(self, a, b, c):
        self.result = population_variance(a, b, c)
        return self.result

    def p_value(self, a, b, c):
        self.result = p_value(a, b, c)
        return self.result

    def proportion(self, a, b, c, d):
        self.result = proportion(a, b, c, d)
        return self.result

    def sample_mean(self, a, b, c):
        self.result = sample_mean(a, b, c)
        return self.result

    def sample_standard_deviation(self, a, b, c):
        self.result = sample_standard_deviation(a, b, c)
        return self.result

    def variance_of_sample_proportion(self, a, b, c):
        self.result = variance_of_sample_proportion(a, b, c)
        return self.result