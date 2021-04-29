import unittest
from src.app import review, default, present

class TestApp(unittest.TestCase):

    def test_review_should_return_default(self):
        self.assertIn(review(1), default)
        self.assertIn(review(-10), default)
        self.assertIn(review(2021), default)

    def test_review_should_not_return_default(self):
        with self.subTest(msg="year = 0"):
            self.assertEqual(review(0), "Jesus Christ what a year!")
        with self.subTest(msg="year = 42"):
            self.assertEqual(review(42), "A year worth living for")
        with self.subTest(msg="year = 1337"):
            self.assertEqual(review(1337), ":sunglasses:")
        with self.subTest(msg="year = 1984"):
            self.assertEqual(review(1984), "You never felt alone")
        with self.subTest(msg="year = 1987"):
            self.assertEqual(review(1987), "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        with self.subTest(msg="year = 2020"):
            self.assertEqual(review(2020), "Sad year :(")
        
    def test_review_invalid_type_raise(self):
        self.assertRaises(TypeError, review, "42")
        self.assertRaises(TypeError, review, 42.3)

    def test_review_future_year_raise(self):
        self.assertRaises(ValueError, review, present + 1)
    

from TestRunner import HTMLTestRunner
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestApp("test_review_should_return_default"))
    suit.addTest(TestApp("test_review_should_not_return_default"))
    suit.addTest(TestApp("test_review_invalid_type_raise"))
    suit.addTest(TestApp("test_review_future_year_raise"))

    with(open('result.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<project name>test report',
            description='describe: ... '
        )
        runner.run(suit)
