def floyd(matrix):
    n = len(matrix)
    res = [row[:] for row in matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                res[i][j] = min(res[i][j], res[i][k] + res[k][j])

    return res

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    n = int(input("Введіть кількість вершин у графі: "))
    matrix = []

    print("Введіть матрицю суміжності:")
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = floyd(matrix)

    print("\nМатриця Флойда:")
    print_matrix(result)

if __name__ == "__main__":
    main()
