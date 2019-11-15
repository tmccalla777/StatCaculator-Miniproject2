import unittest
from CsvReader.CsvReader import CsvReader
from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_statistics.csv').data
        result_data = CsvReader('Tests/Data/statistics_results.csv').data
        for row in test_data:
            result = result_data(row['Mean'])
            self.assertEqual(self.statistics.mean(row['TestData'], result))
            self.assertEqual(self.statistics.result, row['Mean'])

    def test_median_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_statistics.csv').data
        result_data = CsvReader('Tests/Data/statistics_results.csv').data
        for row in test_data:
            result = result_data(row['Median'])
            self.assertEqual(self.statistics.median(row['TestData'], result))
            self.assertEqual(self.statistics.result, row['Median'])

    def test_mode_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_statistics.csv').data
        result_data = CsvReader('Tests/Data/statistics_results.csv').data
        for row in test_data:
            result = result_data(row['Mode'])
            self.assertEqual(self.statistics.mode(row['TestData'], result))
            self.assertEqual(self.statistics.result, row['Mode'])

    def test_popSD_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_statistics.csv').data
        result_data = CsvReader('Tests/Data/statistics_results.csv').data
        for row in test_data:
            result = result_data(row['Population SD'])
            self.assertAlmostEqual(self.statistics.population_SD(row['TestData'], result))
            self.assertAlmostEqual(self.statistics.result, (row['Population SD']))

    def test_variance_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_statistics.csv').data
        result_data = CsvReader('Tests/Data/statistics_results.csv').data
        for row in test_data:
            result = result_data(row['Variance'])
            self.assertAlmostEqual(self.statistics.population_variance(row['TestData'], result))
            self.assertAlmostEqual(self.statistics.result, row['Variance'])

if __name__ == '__main__':
    unittest.main()
