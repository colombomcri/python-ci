import unittest
from src.math import Math

class MathTest(unittest.TestCase):
	def test_addition(self):
		''' 
		Make Test fail 
		'''
		xx = Math()
		yy = xx.addition(2,4)
		self.assertEqual(yy, 6)
