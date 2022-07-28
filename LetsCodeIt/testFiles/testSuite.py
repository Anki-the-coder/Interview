import unittest
from testFiles.courses.testRC import buyCourseTest
from testFiles.practice.practiceTest import practiceTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(buyCourseTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(practiceTest)

testSuite = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(testSuite)

