def count_words_starting_with_b_recursive(words: list, index: int = 0) -> int:
    if index >= len(words):
        return 0
    count = 1 if words[index].lower().startswith('b') else 0
    return count + count_words_starting_with_b_recursive(words, index + 1)

def count_words_starting_with_b(text: str) -> int:
    words = text.split()
    return count_words_starting_with_b_recursive(words)

text = "big apple banana boat bus black cat"
result = count_words_starting_with_b(text)
print("Кількість слів, що починаються з 'b':", result)
