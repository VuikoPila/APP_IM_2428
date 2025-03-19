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


if __name__ == "__main__":
    main()