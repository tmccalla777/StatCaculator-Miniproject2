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

    def test_z_score(self):
        test_data = CsvReader("Tests/Data/unit_test_zscore.csv").data

        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.statistics.zscore(row['Value 1'], row['Value 2'], row['Value 3']), result)
            self.assertEqual(self.statistics.result, result)

    def test_standardized_score(self):
        test_data = CsvReader("Tests/Data/unit_test_standardized_score.csv").data

        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.statistics.standardized(row['Value 1'], row['Value 2'], row['Value 3']), result)
            self.assertEqual(self.statistics.result, result)

    def test_correlation_coefficient(self):
        test_data = CsvReader("Tests/Data/unit_test_population_correlation_coefficient.csv").data

        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.statistics.corr_coef(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                       row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                       row['Value 9'], row['Value 10']), float(row['Result']))
            self.assertEqual(self.statistics.result, result)

    def test_confidence_interval(self):
        test_data = CsvReader("Tests/Data/unit_test_confidence_interval.csv").data

        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.statistics.confidence(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                        row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                        row['Value 9'], row['Value 10']), float(row['Result']))
            self.assertEqual(self.statistics.result, result)

    def test_population_variance(self):
        test_data = CsvReader("Tests/Data/unit_test_population_variance.csv").data

        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.statistics.pop_var(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'],
                                                     row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8'],
                                                     row['Value 9'], row['Value 10']), float(row['Result']))
            self.assertEqual(self.statistics.result, result)

if __name__ == '__main__':
    unittest.main()
