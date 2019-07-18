from django.test import TestCase


class FirstTest(TestCase):

    def divide_by_zero(self):
        return 7 / 0

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.divide_by_zero)
