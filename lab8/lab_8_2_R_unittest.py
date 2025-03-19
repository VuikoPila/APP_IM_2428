import unittest


def count_words_starting_with_b_recursive(words: list, index: int = 0) -> int:
    if index >= len(words):
        return 0
    count = 1 if words[index].lower().startswith('b') else 0
    return count + count_words_starting_with_b_recursive(words, index + 1)


def count_words_starting_with_b_wrapper(text: str) -> int:
    words = text.split()
    return count_words_starting_with_b_recursive(words)


class TestCountWordsStartingWithBRecursive(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_words_starting_with_b_wrapper(""), 0)

    def test_no_b_words(self):
        self.assertEqual(count_words_starting_with_b_wrapper("apple orange pear"), 0)

    def test_some_b_words(self):
        self.assertEqual(count_words_starting_with_b_wrapper("big apple banana boat bus black cat"), 5)

    def test_all_b_words(self):
        self.assertEqual(count_words_starting_with_b_wrapper("banana boat bus black"), 4)

    def test_mixed_case_b_words(self):
        self.assertEqual(count_words_starting_with_b_wrapper("Banana boat Bus BLACK"), 4)


if __name__ == "__main__":
    unittest.main()
