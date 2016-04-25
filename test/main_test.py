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
		self.dim = 10
		self.main = main.Main(self.dim)

	def tearDown(self):
		self.main = None

	def test_magic_sum_should_return_the_expected_value(self):
		self.assertEqual(self.main.magic_sum(), self.dim*((self.dim**2)+1)/2)

	def test_magic_square_should_return_a_matrix_of_the_correct_size(self):
		output = self.main.magic_square()
		self.assertEqual(output.size, self.dim*self.dim)

	def test_magic_vector_should_equal_to_magic_sum(self):
		magic_vector = self.main.magic_vector()
		self.assertEqual(numpy.sum(magic_vector), self.main.magic_sum())

if __name__ == "__main__":
	unittest.main()
