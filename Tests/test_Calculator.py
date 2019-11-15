import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)


    def test_addition(self):
         test_data = CsvReader('/Tests/Data/Addition.csv').data
         for row in test_data:
                    self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
                    self.assertEqual(self.calculator.result, int(row['Result']))


    def test_division(self):
                test_data = CsvReader('/Tests/Data/Division.csv').data
                for row in test_data:
                 self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
                 self.assertEqual(self.calculator.result, int(row['Result']))


    def test_multiplication(self):
                test_data = CsvReader('/Tests/Data/Multiplication.csv').data
                for row in test_data:
                    self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
                    self.assertEqual(self.calculator.result, int(row['Result']))

     def test_sqaure(self):
                test_data = CsvReader('/Tests/Data/Square.csv').data
                for row in test_data:
                    self.assertEqual(self.calculator.squares(row['Value 1']), int(row['Result']))
                    self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
                test_data = CsvReader('/Tests/Data/Square Root.csv').data
                for row in test_data:
                    self.assertEqual(self.calculator.squares(row['Value 1']), int(row['Result']))
                    self.assertEqual(self.calculator.result, int(row['Result']))


    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()