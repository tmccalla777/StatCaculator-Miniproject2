import unittest
from CsvReader.CsvReader import CsvReader as ReadCSV
from CsvReader.ClassFactory import class_factory




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('/Tests/CSVTests/Data/unit_test_zscore.csv')

    def test_return_data_as_objects(self):
        values = self.csv_reader.return_data_as_objects('a_value')
        self.assertIsInstance(values, list)
        test_class = class_factory('a_value', self.csv_reader.data[0])
        for a_value in values:
            self.assertEqual(a_value[0], test_class[0])


if __name__ == '__main__':
    unittest.main()



