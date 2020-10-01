import unittest2
from palindrome import Stack
from palindrome import list

class TestPalindrome(unittest2.TestCase):

    def test_is_palindrome_true(self):
        value = list.is_palindrome('madam')
        self.assertEquals(value, True)

    def test_is_palindrome_false(self):
        value = list.is_palindrome('man')
        self.assertEquals(value, False)

    def test_reverse_normal(self):
        value = list.reverse('man')
        self.assertEquals(value, 'nam')

    def test_reverse_error(self):
        list_of_bad_value = [
        100,
        None,
        ]
        for bad_value in list_of_bad_value:
            self.assertRaises(
                TypeError,
                list.reverse,
                bad_value
            )
def runTests(self):
        if self.testRunner is None:
            try:
                import xmlrunner
                self.testRunner = xmlrunner.XMLTestRunner(verbosity=self.verbosity)
            except ImportError:
                self.testRunner = unittest2.TextTestRunner(verbosity=self.verbosity)

        unittest2.TestProgram.runTests(self)