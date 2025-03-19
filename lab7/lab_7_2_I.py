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


if __name__ == "__main__":
    main()
# create_matrix(rows, cols, min_val, max_val):
#
# rows: кількість рядків у матриці.
#
# cols: кількість стовпців у матриці.
#
# min_val: мінімальне значення елемента матриці.
#
# max_val: максимальне значення елемента матриці.
#
# Функція повертає матрицю заданого розміру з випадковими цілими числами в заданому діапазоні.
#
# print_matrix(matrix):
#
# matrix: матриця, яку потрібно вивести на екран.
#
# Функція виводить матрицю у вигляді таблиці з вирівнюванням.
#
# find_min_of_max_in_even_rows(matrix):
#
# matrix: матриця, в якій потрібно знайти найменший з максимальних елементів у парних рядках.
#
# Функція повертає найменший з максимальних елементів у парних рядках.