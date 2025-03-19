import unittest
from io import StringIO
import sys


def input_matrix(rows: int, cols: int) -> list:
    """Зчитує матрицю з клавіатури"""
    matrix = []
    for i in range(rows):
        while True:
            row = list(map(int, input(f"Введіть {cols} елементів для рядка {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Помилка! Введіть рівно {cols} чисел.")
    return matrix


def column_characteristic(matrix: list, col: int) -> int:
    """Обчислює характеристику стовпця (суму модулів від’ємних непарних елементів)"""
    return sum(abs(matrix[i][col]) for i in range(len(matrix)) if
               0 <= col < len(matrix[i]) and matrix[i][col] < 0 and matrix[i][col] % 2 != 0)


def recursive_sort(matrix: list, characteristics: list, indices: list, n: int) -> None:
    """Рекурсивне сортування стовпців за характеристикою"""
    if n <= 1:
        return

    for i in range(n - 1):
        if characteristics[indices[i]] > characteristics[indices[i + 1]]:
            indices[i], indices[i + 1] = indices[i + 1], indices[i]

    recursive_sort(matrix, characteristics, indices, n - 1)


def apply_sorted_columns(matrix: list, sorted_indices: list) -> None:
    """Переставляє стовпці відповідно до відсортованих індексів"""
    for i in range(len(matrix)):
        matrix[i] = [matrix[i][j] for j in sorted_indices]


def sum_of_columns_with_negatives(matrix: list, col: int = 0, total: int = 0) -> int:
    """Рекурсивно обчислює суму елементів у стовпцях, які містять хоча б один від’ємний елемент"""
    if col >= len(matrix[0]):
        return total

    if any(matrix[row][col] < 0 for row in range(len(matrix)) if 0 <= col < len(matrix[row])):
        total += sum(matrix[row][col] for row in range(len(matrix)))

    return sum_of_columns_with_negatives(matrix, col + 1, total)


def print_matrix(matrix: list) -> None:
    """Виводить матрицю на екран"""
    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    rows = int(input("Введіть кількість рядків: "))
    cols = int(input("Введіть кількість стовпців: "))

    matrix = input_matrix(rows, cols)
    print("Початкова матриця:")
    print_matrix(matrix)

    characteristics = [column_characteristic(matrix, col) for col in range(cols)]
    sorted_indices = list(range(cols))
    recursive_sort(matrix, characteristics, sorted_indices, cols)
    apply_sorted_columns(matrix, sorted_indices)

    print("Матриця після сортування стовпців за характеристикою:")
    print_matrix(matrix)

    total_sum = sum_of_columns_with_negatives(matrix)
    print(f"Сума елементів у стовпцях, що містять хоча б один від’ємний елемент: {total_sum}")


class TestMatrixFunctions(unittest.TestCase):

    def test_input_matrix(self):
        # Тестування функції input_matrix
        input_data = "1 2 3\n4 5 6\n7 8 9"
        expected_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # Перенаправлення вводу
        sys.stdin = StringIO(input_data)
        matrix = input_matrix(3, 3)

        self.assertEqual(matrix, expected_matrix)

    def test_column_characteristic(self):
        # Тестування функції column_characteristic
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]

        # Характеристика для стовпця 1 (індекс 0)
        self.assertEqual(column_characteristic(matrix, 0), 4)

        # Характеристика для стовпця 2 (індекс 1)
        self.assertEqual(column_characteristic(matrix, 1), 10)

        # Характеристика для стовпця 3 (індекс 2)
        self.assertEqual(column_characteristic(matrix, 2), 6)

    def test_recursive_sort(self):
        # Тестування функції recursive_sort
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        characteristics = [column_characteristic(matrix, col) for col in range(3)]
        sorted_indices = list(range(3))

        recursive_sort(matrix, characteristics, sorted_indices, 3)

        # Очікуваний порядок індексів після сортування
        expected_indices = [2, 0, 1]
        self.assertEqual(sorted_indices, expected_indices)

    def test_apply_sorted_columns(self):
        # Тестування функції apply_sorted_columns
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        sorted_indices = [2, 0, 1]
        expected_matrix = [[3, 1, -2], [-6, -4, 5], [9, 7, -8]]

        apply_sorted_columns(matrix, sorted_indices)
        self.assertEqual(matrix, expected_matrix)

    def test_sum_of_columns_with_negatives(self):
        # Тестування функції sum_of_columns_with_negatives
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]

        # Сума елементів у стовпцях, що містять хоча б один від’ємний елемент
        self.assertEqual(sum_of_columns_with_negatives(matrix), -2)

    def test_print_matrix(self):
        # Тестування функції print_matrix
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = "1 2 3\n4 5 6\n7 8 9\n"

        # Перенаправлення виводу
        captured_output = StringIO()
        sys.stdout = captured_output
        print_matrix(matrix)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()