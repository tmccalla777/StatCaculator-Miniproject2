import unittest
from CsvReader.CsvReader import CsvReader
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_mean.csv').data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.statistics.mean(row['Value 1'], row['Value 2'], row['Value 3']), result)
            self.assertEqual(self.statistics.result, result)

    def test_median_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_median.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.statistics.median(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'], row['Value 9']), result)
            self.assertEqual(self.statistics.result, result)

    # def test_mode_statistics(self):
    #     test_data = CsvReader('Tests/Data/unit_test_statistics.csv').data
    #     result_data = CsvReader('Tests/Data/statistics_results.csv').data
    #     for row in test_data:
    #         result = result_data(row['Mode'])
    #         self.assertEqual(self.statistics.mode(row["TestData"], result))
    #         self.assertEqual(self.statistics.result, row["Mode"])
    #
    # def test_popSD_statistics(self):
    #     test_data = CsvReader('Tests/Data/unit_test_statistics.csv').data
    #     result_data = CsvReader('Tests/Data/statistics_results.csv').data
    #     for row in test_data:
    #         result = result_data(row['Population SD'])
    #         self.assertAlmostEqual(self.statistics.population_SD(row["TestData"], result))
    #         self.assertAlmostEqual(self.statistics.result, (row["Population SD"]))
    #
    # def test_variance_statistics(self):
    #     test_data = CsvReader('Tests/Data/unit_test_statistics.csv').data
    #     result_data = CsvReader('Tests/Data/statistics_results.csv').data
    #     for row in test_data:
    #         result = result_data(row['Variance'])
    #         self.assertAlmostEqual(self.statistics.population_variance(row["TestData"], result))
    #         self.assertAlmostEqual(self.statistics.result, row["Variance"])

if __name__ == '__main__':
    unittest.main()
