def create_matrix(height, width, default=None):
    return [[default] * width for _ in range(height)]

def levenstein(s1, s2, insert_cost, delete_cost, replace_cost):
    m, n = len(s1), len(s2)
    d = create_matrix(2, n + 1, default=0)

    for j in range(1, n + 1):
        d[0][j] = d[0][j - 1] + insert_cost

    prev_row, curr_row = 0, 1
    d[1][0] = delete_cost

    for i in range(1, m + 1):
        curr_row = 1 - prev_row
        d[curr_row][0] = d[prev_row][0] + delete_cost

        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                d[curr_row][j] = d[prev_row][j - 1]
            else:
                d[curr_row][j] = min(
                    d[prev_row][j] + delete_cost,
                    d[curr_row][j - 1] + insert_cost,
                    d[prev_row][j - 1] + replace_cost,
                )

        prev_row = curr_row

    return d[curr_row][n]

def main():
    s1 = input("Введіть перший рядок: ")
    s2 = input("Введіть другий рядок: ")
    
    insert_cost = int(input("Введіть вартість вставки: "))
    delete_cost = int(input("Введіть вартість видалення: "))
    replace_cost = int(input("Введіть вартість заміни: "))

    result = levenstein(s1, s2, insert_cost, delete_cost, replace_cost)
    print(f"Відстань Левенштейна: {result}")

if __name__ == "__main__":
    main()
