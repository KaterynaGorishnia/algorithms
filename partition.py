import math

def create_matrix(height, width, default=None):
    return [[default] * width for _ in range(height)]

def find_partition(s, k):
    n = len(s)
    values = create_matrix(n + 1, k + 1, default=0)  
    delims = create_matrix(n + 1, k + 1, default=0) 
    p = [0] * (n + 1) 
    for i in range(1, n + 1):
        p[i] = p[i - 1] + s[i - 1]
        values[i][1] = p[i]
    for j in range(1, k + 1):
        values[1][j] = s[0]
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            values[i][j] = math.inf
            for x in range(1, i):
                new_value = max(values[x][j - 1], p[i] - p[x])
                if new_value < values[i][j]:
                    values[i][j] = new_value
                    delims[i][j] = x
    return delims

def reconstruct_partition(delims, s, n, k):
    if k == 1:
        print(', '.join(map(str, s[:n])))
    else:
        delim = delims[n][k]
        reconstruct_partition(delims, s, delim, k - 1)
        print(', '.join(map(str, s[delim:n])))

def main():
    s = [int(x) for x in input("Введіть список цілих чисел: ").split()]
    k = int(input("Введіть кількість частин, на які розділити список: "))

    delims = find_partition(s, k)
    
    print("Результат розділення:")
    reconstruct_partition(delims, s, len(s), k)

if __name__ == "__main__":
    main()
