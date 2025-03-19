import random


def generate_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))


def count_and_sum_elements(matrix, criterion):
    count = 0
    total_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if criterion(matrix[i][j]):
                count += 1
                total_sum += matrix[i][j]
                matrix[i][j] = 0
    return count, total_sum


def sort_matrix(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0]) - 1):
            if matrix[0][j] > matrix[0][j + 1]:
                for k in range(len(matrix)):
                    matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]
            elif matrix[0][j] == matrix[0][j + 1]:
                if matrix[1][j] > matrix[1][j + 1]:
                    for k in range(len(matrix)):
                        matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]
                elif matrix[1][j] == matrix[1][j + 1]:
                    if matrix[2][j] > matrix[2][j + 1]:
                        for k in range(len(matrix)):
                            matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]


def criterion(x):
    return x > 0 and x % 3 != 0


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


if __name__ == "__main__":
    main()