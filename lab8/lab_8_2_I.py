def count_words_starting_with_b(text: str) -> int:
    words = text.split()  # Розбиваємо рядок на слова за пробілами
    count = sum(1 for word in words if word.lower().startswith('b'))
    return count


# Приклад використання
text = "big apple banana boat bus black cat"
result = count_words_starting_with_b(text)
print("Кількість слів, що починаються з 'b':", result)
