def create_matrix(height, width, default=None):
    return [[default] * width for _ in range(height)]

def matrix_multiply(a, b):
    if not a or not b:
        print("Помилка: одна з матриць пуста")
        return

    a_height, a_width = len(a), len(a[0])
    b_height, b_width = len(b), len(b[0])

    if a_width != b_height:
        print("Помилка: несумісні розміри матриць")
        return

    result = create_matrix(a_height, b_width, default=0)

    for i in range(a_height):
        for j in range(b_width):
            for k in range(a_width):
                result[i][j] += a[i][k] * b[k][j]

    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    a_height = int(input("Введіть висоту матриці A: "))
    a_width = int(input("Введіть ширину матриці A: "))
    
    print("Введіть матрицю A:")
    a = [list(map(int, input().split())) for _ in range(a_height)]

    b_height = int(input("Введіть висоту матриці B: "))
    b_width = int(input("Введіть ширину матриці B: "))
    
    print("Введіть матрицю B:")
    b = [list(map(int, input().split())) for _ in range(b_height)]

    result = matrix_multiply(a, b)

    print("\nРезультат множення матриць:")
    print_matrix(result)

if __name__ == "__main__":
    main()
