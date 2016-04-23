import unittest
import main
import numpy

def suite():
	suite  = unittest.TestSuite()
	loader = unittest.TestLoader()
	suite.addTests(loader.loadTestsFromTestCase(MainTest))
	return suite

class MainTest(unittest.TestCase):

	def setUp(self):
		self.size = 10
		self.main = main.Main(self.size)

	def tearDown(self):
		self.main = None

	def test_magic_sum_should_return_the_expected_value(self):
		self.assertEqual(self.main.magic_sum(), self.size*((self.size**2)+1)/2)

	def test_magic_square_should_return_a_matrix_of_the_correct_size(self):
		output = self.main.magic_square()
		self.assertEqual(output.size, self.size*self.size)

	def test_sum_of_first_row_should_equal_to_magic_sum(self):
		magic_row = self.main.magic_row()
		self.assertEqual(numpy.sum(magic_row), self.main.magic_sum())

if __name__ == "__main__":
	unittest.main()
