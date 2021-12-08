import unittest
from Operations import *

class TestOperationsMethods(unittest.TestCase):
    def setUp(self):
        self.operations = Operations()

    def test_operations(self):
        self.assertEqual("Running app 'app1' in namespace 'dev' nice", self.operations.runningInfo("app1","dev"))
 
if __name__ == '__main__':
    unittest.main()