import unittest

def count_words_starting_with_b(text: str) -> int:
    words = text.split()
    count = sum(1 for word in words if word.lower().startswith('b'))
    return count


class TestCountWordsStartingWithB(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_words_starting_with_b(""), 0)

    def test_no_b_words(self):
        self.assertEqual(count_words_starting_with_b("apple orange pear"), 0)

    def test_some_b_words(self):
        self.assertEqual(count_words_starting_with_b("big apple banana boat bus black cat"), 5)

    def test_all_b_words(self):
        self.assertEqual(count_words_starting_with_b("banana boat bus black"), 4)

    def test_mixed_case_b_words(self):
        self.assertEqual(count_words_starting_with_b("Banana boat Bus BLACK"), 4)


if __name__ == "__main__":
    unittest.main()