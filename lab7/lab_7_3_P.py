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


if __name__ == "__main__":
    main()