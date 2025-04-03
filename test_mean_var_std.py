'''
freecodecamp Mean-Variance-Standard Deviation Calculator
Test Module for mean_var_std.py
John Pierre

Test cases: Normal case and Negative numbers 
'''

import unittest
import mean_var_std

# Test Case
class TestCalcFunc(unittest.TestCase):
    def test_calc(self):
        actual = mean_var_std.calculate([1,2,3,4,5,6,7,8,9])
        expected = {
            'mean': [[4.0, 5.0, 6.0], [2.0, 5.0, 8.0], 5.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[7, 8, 9], [3, 6, 9], 9],
            'min': [[1, 2, 3], [1, 4, 7], 1], 
            'sum': [[12, 15, 18], [6, 15, 24], 45]
            }
        self.assertAlmostEqual(actual, expected)
    
    def test_calc_neg_num(self):
        actual = mean_var_std.calculate([-2,-8,-9,-4,-2,-7,-3,-1,-1])
        expected = {
            'mean': [[-3.0, -3.6666666666666665, -5.666666666666667], [-6.333333333333333, -4.333333333333333, -1.6666666666666667], -4.111111111111111],
            'variance': [[0.6666666666666666, 9.555555555555557, 11.555555555555557], [9.555555555555555, 4.222222222222222, 0.888888888888889], 8.543209876543209],
            'standard deviation': [[0.816496580927726, 3.091206165165235, 3.39934634239519], [3.0912061651652345, 2.0548046676563256, 0.9428090415820634], 2.9228769862146455],
            'max': [[-2, -1, -1], [-2, -2, -1], -1],
            'min': [[-4, -8, -9], [-9, -7, -3], -9],
            'sum': [[-9, -11, -17], [-19, -13, -5], -37]
            }
        self.assertAlmostEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()