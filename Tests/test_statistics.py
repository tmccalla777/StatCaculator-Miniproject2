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

    def test_mode_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_mode.csv').data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.statistics.mode(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6'], row['Value 7'], row['Value 8']), result)
            self.assertEqual(self.statistics.result, result)

    def test_popSD_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_SD.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.statistics.SD(row['Value 1'], row['Value 2'], row['Value 3']), result)
            self.assertAlmostEqual(self.statistics.result, result)

    def test_variance_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_variance.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.statistics.varianceFunc(row['Value 1'], row['Value 2'], row['Value 3']), result)
            self.assertAlmostEqual(self.statistics.result, result)

if __name__ == '__main__':
    unittest.main()
    
    def test_proportion(self):

            test_data = csvreader('Tests/csvdata/Array3.csv').data
            test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            for column in test_result:
                result_test = float(column['proportion'])

            listx = []

            for row in test_data:
                result = float(row['Array'])
                listx.append(result)


            self.assertEqual(round(self.extendedstat.proportion_(listx)), round(result_test))
