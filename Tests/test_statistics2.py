try:
    

import unittest
from Csvreader.CsvReader import Csvreader
from Statistics.Statistics import Statisticss

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statisticss, Statistics)
        
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

         def test_samplemean(self):
        
             test_data = csvreader('Tests/csvdata/Array3.csv').data
             test_result = csvreader('Tests/csvdata/Array3_result2.csv').data
        
             for column in test_result:
                 result_test = float(column['samplemean'])
        
             listx = []
        
             for row in test_data:
                 result = float(row['Array'])
                listx.append(result)
       
       
            self.assertEqual(round(self.extendedstat.samplemean(listx)), round(result_test))
 def test_pvalue(self):

            test_data = csvreader('Tests/csvdata/UnitArgument.csv').data
            test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            for column in test_result:
                result_test = float(column['pvalue'])

            for column in test_data:
                a = float(column['a'])
                b = float(column['b'])
                c = float(column['c'])
                d = float(column['d'])

            self.assertAlmostEqual(self.extendedstat.pvalue_(a,b,c,d), result_test)
            
            
             # def test_samplestdev(self):
        
             test_data = csvreader('Tests/csvdata/Array3.csv').data
             test_result = csvreader('Tests/csvdata/Array3_result2.csv').data
        
             for column in test_result:
                 result_test = float(column['samplestdev'])
        
             listx = []
        
             for row in test_data:
                 result = float(row['Array'])
                 listx.append(result)
        
             self.assertAlmostEqual(self.extendedstat.samplestdev(listx),result_test)
        
        
         def test_Variance_of_sample_proportion(self):
        
             test_data = csvreader('Tests/csvdata/Array3.csv').data
             test_result = csvreader('Tests/csvdata/Array3_result2.csv').data
        
             for column in test_result:
                 result_test = float(column['Variance_of_sample_proportion'])
        
             listx = []
        
             for row in test_data:
                 result = float(row['Array'])
                 listx.append(result)
        
           self.assertAlmostEqual(self.extendedstat.Variance_of_sample_proportion(listx), result_test)

except IndentationError as e :
    print("Indentation Error in Extended Stat:", e)
except ImportError as e :
    print("Import Error in Extended Stat:", e)
except Exception as e :
    print("Any Other Kind of Exception:", e)
except AttributeError as e :
    print("Attribute Error", e)

        
