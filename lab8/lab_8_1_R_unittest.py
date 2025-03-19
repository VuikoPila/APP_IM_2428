import unittest
from lab_8_1_R import contains_all_letters_recursive, replace_while_recursive


class TestStringProcessingRecursive(unittest.TestCase):
    def test_contains_all_letters_recursive(self):
        self.assertTrue(contains_all_letters_recursive("this is a while loop"))
        self.assertTrue(contains_all_letters_recursive("w h i l e"))
        self.assertFalse(contains_all_letters_recursive("this is a test"))
        self.assertFalse(contains_all_letters_recursive("whi"))
        self.assertFalse(contains_all_letters_recursive(""))

    def test_replace_while_recursive(self):
        self.assertEqual(replace_while_recursive("this is a while loop"), "this is a ** loop")
        self.assertEqual(replace_while_recursive("whilewhile"), "****")
        self.assertEqual(replace_while_recursive("while is important while"), "** is important **")
        self.assertEqual(replace_while_recursive("no matches here"), "no matches here")
        self.assertEqual(replace_while_recursive(""), "")


if __name__ == "__main__":
    unittest.main()