import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Cody', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.email, 'Cody.Schafer@gmail.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@gmail.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'John.Schafer@gmail.com')
        self.assertEqual(emp_1.email, 'Jane.Smith@gmail.com')

    def test_fullname(self):
        emp_1 = Employee('Cody', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.fullname, 'Cody Schafer')
        self.assertEqual(emp_1.fullname, 'Sue Smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_1.fullname, 'Jane Smith')

    def test_apply_raise(self):
        emp_1 = Employee('Cody', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)