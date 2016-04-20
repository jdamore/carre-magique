import unittest
import main
import space

def suite():
	suite  = unittest.TestSuite()
	loader = unittest.TestLoader()
	suite.addTests(loader.loadTestsFromTestCase(MainTest))
	return suite

class MainTest(unittest.TestCase):
	
	def setUp(self):
		self.main = main.Main(10)
	
	def tearDown(self):
		self.magic_square = None
	
	def test_magic_square_with_valid_input_should_return_a_matrix_of_the_correct_size(self):
		output = main.magic_square()
		self.assertEquals(output.size(), 10)


if __name__ == "__main__":
	unittest.main()