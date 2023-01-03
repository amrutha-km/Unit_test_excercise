import unittest
from src.general_example import GeneralExample

GeneralExamle_instane=GeneralExample()

class test_general(unittest.TestCase):
    def test_flatten_dictionary(self):
        d={'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]}
        excepted=[0, 1, 2, 3, 10, 22, 42, 55]
        self.assertEqual(excepted,GeneralExamle_instane.flatten_dictionary(d))

    def load_employee_rec_from_database(self):
        excepted=['emp001', 'Sam', '100000']
        self.assertEqual(excepted,GeneralExamle_instane.load_employee_rec_from_database())

    def test_fetch_emp_details(self):
        expected= {'emp_id':'emp001',
                    'empName':'Sam',
                    'empSalary':'100000'}
        self.assertEqual(expected,GeneralExamle_instane.fetch_emp_details())

if __name__==" __main__":
    unittest.main()