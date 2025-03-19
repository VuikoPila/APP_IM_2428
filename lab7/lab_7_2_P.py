def create_matrix(rows, cols, min_val, max_val):
    import random
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))


def find_max_in_row(row, index=0, current_max=None):
    if index >= len(row):
        return current_max
    if current_max is None or row[index] > current_max:
        current_max = row[index]
    return find_max_in_row(row, index + 1, current_max)


def find_min_of_max_in_even_rows(matrix, row_index=0, max_elements=None):
    if max_elements is None:
        max_elements = []
    if row_index >= len(matrix):
        return min(max_elements)
    if row_index % 2 == 0:
        max_elements.append(find_max_in_row(matrix[row_index]))
    return find_min_of_max_in_even_rows(matrix, row_index + 1, max_elements)


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
# find_max_in_row(row, index, current_max):
#
# row: рядок матриці, в якому потрібно знайти максимальний елемент.
#
# index: поточний індекс у рядку.
#
# current_max: поточний максимальний елемент у рядку.
#
# Функція повертає максимальний елемент у рядку.
#
# find_min_of_max_in_even_rows(matrix, row_index, max_elements):
#
# matrix: матриця, в якій потрібно знайти найменший з максимальних елементів у парних рядках.
#
# row_index: поточний індекс рядка.
#
# max_elements: список максимальних елементів у парних рядках.
#
# Функція повертає найменший з максимальних елементів у парних рядках.