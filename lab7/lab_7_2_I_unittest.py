import unittest
def create_matrix(rows, cols, min_val, max_val):
    import random
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))


def find_min_of_max_in_even_rows(matrix):
    max_elements = []
    for i in range(0, len(matrix), 2):  # Перебираємо парні рядки (індексація з 0)
        max_elements.append(max(matrix[i]))
    return min(max_elements)


def main():
    rows, cols = 5, 5
    min_val, max_val = 1, 100
    matrix = create_matrix(rows, cols, min_val, max_val)

    print("Початкова матриця:")
    print_matrix(matrix)

    result = find_min_of_max_in_even_rows(matrix)
    print(f"\nНайменший з максимальних елементів у парних рядках: {result}")

import unittest

class TestIterativeMethods(unittest.TestCase):
    def test_create_matrix(self):
        rows, cols = 3, 3
        min_val, max_val = 1, 10
        matrix = create_matrix(rows, cols, min_val, max_val)
        self.assertEqual(len(matrix), rows)
        self.assertEqual(len(matrix[0]), cols)
        for row in matrix:
            for elem in row:
                self.assertTrue(min_val <= elem <= max_val)

    def test_find_max_in_row(self):
        row = [1, 5, 3, 9, 2]
        self.assertEqual(max(row), 9)

    def test_find_min_of_max_in_even_rows(self):
        matrix = [
            [1, 2, 3],  # Парний рядок (індекс 0)
            [4, 5, 6],  # Непарний рядок
            [7, 8, 9],  # Парний рядок (індекс 2)
            [10, 11, 12]  # Непарний рядок
        ]
        result = find_min_of_max_in_even_rows(matrix)
        self.assertEqual(result, 3)  # Максимуми у парних рядках: 3 і 9. Найменший з них — 3.

if __name__ == "__main__":
    unittest.main()