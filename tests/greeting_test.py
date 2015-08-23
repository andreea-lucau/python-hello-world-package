import unittest

import hello.greeting

class TestGreeting(unittest.TestCase):
    def test_get_greeting(self):
        expected_greeting = "Hello, Andreea!"
        greeting = hello.greeting.get_greeting("Andreea")

        self.assertEquals(greeting, expected_greeting)

    def test_get_greeting_name_not_valid(self):
        with self.assertRaises(hello.greeting.Error):
            hello.greeting.get_greeting("")

    def test_is_valid_name_no_digits(self):
        valid = hello.greeting.is_valid_name("1234456")
        self.assertFalse(valid)

    def test_is_valid_name_no_whitespaces(self):
        valid = hello.greeting.is_valid_name("andreea lucau")
        self.assertFalse(valid)

    def test_is_valid_name_no_lowercase_start(self):
        valid = hello.greeting.is_valid_name("andreea")
        self.assertFalse(valid)

    def test_is_valid_name(self):
        valid = hello.greeting.is_valid_name("Andreea")
        self.assertTrue(valid)

if __name__ == '__main__':
    unittest.main()
