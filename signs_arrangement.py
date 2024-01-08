def get_max_value(a):
    n = len(a)
    
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = a[i]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            for k in range(i, j):
                d[i][j] = max(
                    d[i][j], 
                    d[i][k] + d[k + 1][j],
                    d[i][k] * d[k + 1][j],
                )

    return d[0][n - 1]

def main():
    a = list(map(int, input("Введіть послідовність чисел: ").split()))
    
    result = get_max_value(a)
    print("Максимальне можливе значення:", result)

if __name__ == "__main__":
    main()
