import unittest
import pprint
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader




class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/unit_test_statistics.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data = CsvReader('Tests/Data/unit_test_statistics.csv')


if __name__ == '__main__':
    unittest.main()
