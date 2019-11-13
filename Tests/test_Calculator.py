import unittest
import math
from decimal import Decimal
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_zscore(self):
        test_data = CsvReader('/Tests/Data/unit_test_zscore.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.zscore(row['Value 1'],row['Value 2'],row['Value 3']), Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_standardized_score(self):
        test_data = CsvReader('/Tests/Data/unit_test_standardized_score.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.standardized_score(row['Value 1'],row['Value 2'],row['Value 3']), Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))
 
    def test_population_correlation_coefficient(self):
        test_data = CsvReader('/Tests/Data/unit_test_population_correlation_coefficient.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.population_correlation_coefficient(row['Value 1'],row['Value 2'],row['Value 3']), Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_confidence_interval(self):
        test_data = CsvReader('/Tests/Data/unit_test_confidence_interval.csv').data
        for row in test_data:
            self.assertEqual(
                self.calculator.confidence_interval(row['Value 1'], row['Value 2'], row['Value 3']),
                Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))



if __name__ == '__main__':
    unittest.main()