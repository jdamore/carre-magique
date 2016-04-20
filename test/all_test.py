import unittest

import main_test

suite = unittest.TestSuite()
suite.addTests(main_test.suite())
 
unittest.TextTestRunner(verbosity=2).run(suite)