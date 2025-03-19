import random


def generate_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))


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