import unittest
from lab_8_1_I import contains_all_letters_iterative, replace_while_iterative


class TestStringProcessing(unittest.TestCase):
    def test_contains_all_letters_iterative(self):
        self.assertTrue(contains_all_letters_iterative("this is a while loop"))
        self.assertTrue(contains_all_letters_iterative("w h i l e"))
        self.assertFalse(contains_all_letters_iterative("this is a test"))
        self.assertFalse(contains_all_letters_iterative("whi"))
        self.assertFalse(contains_all_letters_iterative(""))

    def test_replace_while_iterative(self):
        self.assertEqual(replace_while_iterative("this is a while loop"), "this is a ** loop")
        self.assertEqual(replace_while_iterative("whilewhile"), "****")
        self.assertEqual(replace_while_iterative("while is important while"), "** is important **")
        self.assertEqual(replace_while_iterative("no matches here"), "no matches here")
        self.assertEqual(replace_while_iterative(""), "")


if __name__ == "__main__":
    unittest.main()
