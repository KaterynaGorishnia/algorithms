import math

def create_matrix(height, width, default=None):
    return [[default] * width for _ in range(height)]

def optimal_expected_value(p, q):
    n = len(p)
    
    e = create_matrix(n + 2, n + 1, default=0.0)
    w = create_matrix(n + 2, n + 1, default=0.0)
    root = create_matrix(n + 1, n + 1, default=0.0)

    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = math.inf
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j - 1]
            for r in range(i, j + 1):
                e_new = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if e_new < e[i][j]:
                    e[i][j] = e_new
                    root[i][j] = r
                    
    return e[1][n]

def main():
    p = [float(x) for x in input("Введіть ймовірності p через пробіл: ").split()]
    q = [float(x) for x in input("Введіть ймовірності q через пробіл: ").split()]

    result = optimal_expected_value(p, q)
    print(f"Оптимальне математичне сподівання: {result}")

if __name__ == "__main__":
    main()
