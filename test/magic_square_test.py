import unittest
import magic_square

def suite():
	suite  = unittest.TestSuite()
	loader = unittest.TestLoader()
	suite.addTests(loader.loadTestsFromTestCase(MagicSquareTest))
	return suite

class MagicSquareTest(unittest.TestCase):
	
	def setUp(self):
		self.magic_square = magic_square.MagicSquare()
	
	def tearDown(self):
		self.magic_square = None
	
	def test_with_valid_input_should_return_a_magic_square(self):
		str('Hello Test')
	
if __name__ == "__main__":
	unittest.main()