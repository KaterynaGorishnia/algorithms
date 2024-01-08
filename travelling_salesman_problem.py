import math

def create_matrix(height, width, default=None):
    return [[default] * width for _ in range(height)]

def solve():
    d = create_matrix(n, 1 << n, default=math.inf)
    d[0][0] = 0
    return get_cheapest(0, (1 << n) - 1, d)

def get_cheapest(i: int, mask: int, d: list) -> int:
    if d[i][mask] != math.inf:
        return d[i][mask]
    for j in range(n):
        if w[i][j] and mask & (1 << j):  
            new_mask = mask - (1 << j)
            new_value = get_cheapest(j, new_mask, d) + w[i][j]
            d[i][mask] = min(d[i][mask], new_value)
    return d[i][mask]

def find_way(d: list) -> list:
    solve()
    i, path, mask = 0, [0], (1 << n) - 1
    while mask != 0:
        for j in range(n):
            has_bit = mask & (1 << j)
            new_mask = mask - (1 << j)
            if w[i][j] and has_bit and \
                    d[i][mask] == d[j][new_mask] + w[i][j]:
                path.append(j)
                mask = new_mask
                i = j  
                break
    return path

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    global n, w
    n = int(input("Введіть кількість вершин в графі: "))
    w = []
    print("Введіть матрицю суміжності графа:")
    for _ in range(n):
        row = list(map(int, input().split()))
        w.append(row)

    path = find_way([])
    print("\nМатриця суміжності графа:")
    print_matrix(w)
    print("\nНайкоротший шлях у графі:", path)

if __name__ == "__main__":
    main()
