import unittest

import magic_square_test

suite = unittest.TestSuite()
suite.addTests(magic_square_test.suite())
 
unittest.TextTestRunner(verbosity=2).run(suite)