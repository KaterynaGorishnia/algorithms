def binomial_coefficient(n: int, m: int) -> int:
    bc = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        bc[i][0] = 1
    for j in range(n + 1):
        bc[j][j] = 1
    for i in range(1, n + 1):
        for j in range(1, i):
            bc[i][j] = bc[i - 1][j - 1] + bc[i - 1][j]

    return bc[n][m]


n = int(input("Enter value n: "))
m = int(input("Enter value m: "))
result = binomial_coefficient(n, m)
print(f"The binomial coefficient C({n}, {m}) is equal to: {result}")
