def create_matrix(height, width, default=None):
    return [[default] * width for _ in range(height)]

def lcs_length(x, y):
    n = len(x)
    m = len(y)

    length = create_matrix(n + 1, m + 1, default=0)
    arrows = create_matrix(n + 1, m + 1, default='top')

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                length[i][j] = length[i - 1][j - 1] + 1
                arrows[i][j] = 'diag'
            elif length[i - 1][j] >= length[i][j - 1]:
                length[i][j] = length[i - 1][j]
                arrows[i][j] = 'top'
            else:
                length[i][j] = length[i][j - 1]
                arrows[i][j] = 'left'

    return length[n][m], arrows

def print_lcs(arrows, x, i, j):
    if i == 0 or j == 0:
        return ''
    if arrows[i][j] == 'diag':
        return print_lcs(arrows, x, i - 1, j - 1) + x[i - 1]
    elif arrows[i][j] == 'top':
        return print_lcs(arrows, x, i - 1, j)
    else:
        return print_lcs(arrows, x, i, j - 1)

def main():
    x = input("Введіть першу строку: ")
    y = input("Введіть другу строку: ")

    lcs_len, arrows = lcs_length(x, y)

    print(f"Довжина найбільшої спільної підпослідовності: {lcs_len}")
    
    if lcs_len > 0:
        lcs_str = print_lcs(arrows, x, len(x), len(y))
        print(f"Найбільша спільна підпослідовність: {lcs_str}")

if __name__ == "__main__":
    main()
