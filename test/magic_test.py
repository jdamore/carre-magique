import unittest
import numpy

import magic

def suite():
	suite  = unittest.TestSuite()
	loader = unittest.TestLoader()
	suite.addTests(loader.loadTestsFromTestCase(MagicTest))
	suite.addTests(loader.loadTestsFromTestCase(MagicTest_odd))
	suite.addTests(loader.loadTestsFromTestCase(MagicTest_even))
	return suite

class MagicTest(unittest.TestCase):

	def setUp(self):
		self.dim = 5
		self.magic = magic.Magic(self.dim)

	def tearDown(self):
		self.magic = None

	def test_magic_sum_should_return_the_expected_value(self):
		self.assertEqual(self.magic.sum(), self.dim*((self.dim**2)+1)/2)

	def test_magic_square_should_return_a_matrix_of_the_correct_size(self):
		msquare = self.magic.square()
		self.assertEqual(msquare.size, self.dim*self.dim)

class MagicTest_odd(unittest.TestCase):

	def setUp(self):
		self.dim = 9
		self.magic = magic.Magic(self.dim)

	def tearDown(self):
		self.magic = None

	def test_magic_square_should_return_a_matrix_where_the_diagonal_is_magic(self):
		msquare = self.magic.square()
		print(self.magic.to_s())
		self.assertEqual(numpy.trace(msquare), self.magic.sum())

	def test_magic_square_should_return_a_matrix_where_the_other_diagonal_is_magic(self):
		msquare = self.magic.square()
		print(self.magic.to_s())
		self.assertEqual(numpy.sum(numpy.diagonal(msquare, 0, 1, 0)), self.magic.sum())


class MagicTest_even(unittest.TestCase):

	def setUp(self):
		self.dim = 10
		self.magic = magic.Magic(self.dim)

	def tearDown(self):
		self.magic = None

	def test_magic_square_should_return_a_matrix_where_the_diagonal_is_magic(self):
		msquare = self.magic.square()
		print(self.magic.to_s())
		self.assertEqual(numpy.trace(msquare), self.magic.sum())

	def test_magic_square_should_return_a_matrix_where_the_other_diagonal_is_magic(self):
		msquare = self.magic.square()
		print(self.magic.to_s())
		self.assertEqual(numpy.sum(numpy.diagonal(msquare, 0, 1, 0)), self.magic.sum())

if __name__ == "__main__":
	unittest.main()
