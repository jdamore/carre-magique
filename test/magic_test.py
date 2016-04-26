import unittest
import numpy

import magic

def suite():
	suite  = unittest.TestSuite()
	loader = unittest.TestLoader()
	suite.addTests(loader.loadTestsFromTestCase(MagicTest))
	return suite

class MagicTest(unittest.TestCase):

	def setUp(self):
		self.dim = 7
		self.magic = magic.Magic(self.dim)

	def tearDown(self):
		self.magic = None

	def test_magic_sum_should_return_the_expected_value(self):
		self.assertEqual(self.magic.sum(), self.dim*((self.dim**2)+1)/2)

	def test_magic_square_should_return_a_matrix_of_the_correct_size(self):
		output = self.magic.square()
		print(self.magic.to_s())
		self.assertEqual(output.size, self.dim*self.dim)

if __name__ == "__main__":
	unittest.main()
