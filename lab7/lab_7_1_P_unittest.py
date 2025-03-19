import random
import unittest


# Функція для генерації матриці
def generate_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


# Функція для виведення матриці
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))


# Функція для підрахунку та суми елементів, що задовольняють критерію (рекурсивно)
def count_and_sum_elements(matrix, criterion, i=0, j=0, count=0, total_sum=0):
    if i == len(matrix):
        return count, total_sum
    if j == len(matrix[i]):
        return count_and_sum_elements(matrix, criterion, i + 1, 0, count, total_sum)
    if criterion(matrix[i][j]):
        count += 1
        total_sum += matrix[i][j]
        matrix[i][j] = 0
    return count_and_sum_elements(matrix, criterion, i, j + 1, count, total_sum)


# Функція для сортування матриці (рекурсивно)
def sort_matrix(matrix, col=0):
    if col == len(matrix[0]) - 1:
        return
    for i in range(len(matrix[0]) - col - 1):
        if matrix[0][i] > matrix[0][i + 1]:
            for k in range(len(matrix)):
                matrix[k][i], matrix[k][i + 1] = matrix[k][i + 1], matrix[k][i]
        elif matrix[0][i] == matrix[0][i + 1]:
            if matrix[1][i] > matrix[1][i + 1]:
                for k in range(len(matrix)):
                    matrix[k][i], matrix[k][i + 1] = matrix[k][i + 1], matrix[k][i]
            elif matrix[1][i] == matrix[1][i + 1]:
                if matrix[2][i] > matrix[2][i + 1]:
                    for k in range(len(matrix)):
                        matrix[k][i], matrix[k][i + 1] = matrix[k][i + 1], matrix[k][i]
    sort_matrix(matrix, col + 1)


# Критерій для вибору елементів
def criterion(x):
    return x > 0 and x % 3 != 0


# Основна функція
def main():
    rows, cols = 7, 9
    min_val, max_val = -12, 37
    matrix = generate_matrix(rows, cols, min_val, max_val)

    print("Original Matrix:")
    print_matrix(matrix)

    count, total_sum = count_and_sum_elements(matrix, criterion)
    print(f"\nCount of elements satisfying the criterion: {count}")
    print(f"Sum of elements satisfying the criterion: {total_sum}")

    print("\nMatrix after replacing elements with zeros:")
    print_matrix(matrix)

    sort_matrix(matrix)
    print("\nMatrix after sorting:")
    print_matrix(matrix)


# Unit Test
class TestMatrixOperationsRecursive(unittest.TestCase):
    def test_generate_matrix(self):
        matrix = generate_matrix(7, 9, -12, 37)
        self.assertEqual(len(matrix), 7)
        self.assertEqual(len(matrix[0]), 9)
        for row in matrix:
            for elem in row:
                self.assertTrue(-12 <= elem <= 37)

    def test_count_and_sum_elements(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        count, total_sum = count_and_sum_elements(matrix, lambda x: x % 2 == 0)
        self.assertEqual(count, 4)
        self.assertEqual(total_sum, 20)
        self.assertEqual(matrix, [[1, 0, 3], [0, 5, 0], [7, 0, 9]])

    def test_sort_matrix(self):
        matrix = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        sort_matrix(matrix)
        self.assertEqual(matrix, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


if __name__ == "__main__":
    # Запуск основної програми
    main()

    # Запуск тестів
    unittest.main()