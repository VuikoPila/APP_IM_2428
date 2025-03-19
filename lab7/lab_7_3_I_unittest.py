import unittest
from io import StringIO
import sys


def input_matrix(rows: int, cols: int) -> list:
    """Зчитує матрицю з клавіатури"""
    matrix = []
    for i in range(rows):
        matrix.append(list(map(int, input(f"Введіть {cols} елементів для рядка {i + 1}: ").split())))
    return matrix


def column_characteristic(matrix: list, col: int) -> int:
    """Обчислює характеристику стовпця (суму модулів від’ємних непарних елементів)"""
    return sum(abs(matrix[i][col]) for i in range(len(matrix)) if matrix[i][col] < 0 and matrix[i][col] % 2 != 0)


def sort_columns_by_characteristic(matrix: list) -> None:
    """Сортує стовпці за характеристикою"""
    cols = len(matrix[0])
    characteristics = [column_characteristic(matrix, col) for col in range(cols)]
    sorted_indices = sorted(range(cols), key=lambda x: characteristics[x])

    # Перетворення матриці відповідно до нового порядку стовпців
    for i in range(len(matrix)):
        matrix[i] = [matrix[i][j] for j in sorted_indices]


def sum_of_columns_with_negatives(matrix: list) -> int:
    """Обчислює суму елементів у стовпцях, які містять хоча б один від’ємний елемент"""
    cols = len(matrix[0])
    total_sum = 0
    for col in range(cols):
        if any(matrix[row][col] < 0 for row in range(len(matrix))):
            total_sum += sum(matrix[row][col] for row in range(len(matrix)))
    return total_sum


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

    sort_columns_by_characteristic(matrix)
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

    def test_sort_columns_by_characteristic(self):
        # Тестування функції sort_columns_by_characteristic
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        expected_matrix = [[3, 1, -2], [-6, -4, 5], [9, 7, -8]]

        sort_columns_by_characteristic(matrix)
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