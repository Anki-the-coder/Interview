import unittest
from SeleniumProject.basicWeb.myPractice import testingThis
from Se
# import

test1 = unittest.TestLoader().loadTestsFromTestCase(testingThis)

smoking = unittest.TestSuite([test1])

unittest.TextTestRunner(verbosity=2).run(smoking)
