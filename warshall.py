def warshall(graph):
    n = len(graph)
    res = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                res[i][j] = res[i][j] or (res[i][k] and res[k][j])

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

    result = warshall(matrix)

    print("\nМатриця досяжності:")
    print_matrix(result)

if __name__ == "__main__":
    main()
