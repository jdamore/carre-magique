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
		self.msum = self.magic.sum()
		self.msquare = self.magic.square()

	def tearDown(self):
		self.magic = None
		self.msum = 0
		self.msquare = None

	def test_magic_sum_should_return_the_expected_value(self):
		self.assertEqual(self.msum, self.dim*((self.dim**2)+1)/2)

	def test_magic_square_should_return_a_matrix_of_the_correct_size(self):
		self.assertEqual(self.msquare.size, self.dim*self.dim)



class MagicTest_even(unittest.TestCase):

	def setUp(self):
		self.dim = 10
		self.magic = magic.Magic(self.dim)
		self.msum = self.magic.sum()
		self.msquare = self.magic.square()

	def tearDown(self):
		self.magic = None
		self.msum = 0
		self.msquare = None

	def test_magic_square_should_return_a_matrix_where_the_diagonal_is_magic(self):
		print(self.magic.to_s())
		self.assertEqual(numpy.trace(self.msquare), self.magic.sum())

	def test_magic_square_should_return_a_matrix_where_the_other_diagonal_is_magic(self):
		print(self.magic.to_s())
		self.assertEqual(numpy.sum(numpy.diagonal(self.msquare, 0, 1, 0)), self.msum)



class MagicTest_odd(unittest.TestCase):

	def setUp(self):
		self.dim = 9
		self.magic = magic.Magic(self.dim)
		self.msum = self.magic.sum()
		self.msquare = self.magic.square()

	def tearDown(self):
		self.magic = None
		self.msum = 0
		self.msquare = None

	def test_magic_square_should_return_a_matrix_where_the_diagonal_is_magic(self):
		print(self.magic.to_s())
		self.assertEqual(numpy.trace(self.msquare), self.msum)

	def test_magic_square_should_return_a_matrix_where_the_other_diagonal_is_magic(self):
		print(self.magic.to_s())
		self.assertEqual(numpy.sum(numpy.diagonal(self.msquare, 0, 1, 0)), self.msum)

	def test_magic_square_should_return_a_matrix_where_the_middle_row_is_magic(self):
		print(self.magic.to_s())
		self.assertEqual(numpy.sum(self.msquare[int(self.dim/2)]), self.msum)

	def test_magic_square_should_return_a_matrix_where_the_middle_column_is_magic(self):
		print(self.magic.to_s())
		self.assertEqual(numpy.sum(list(zip(*self.msquare))[int(self.dim/2)]), self.msum)


if __name__ == "__main__":
	unittest.main()
