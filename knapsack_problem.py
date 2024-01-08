def create_matrix(height, width, default=None):
    return [[default] * width for _ in range(height)]

def print_things(n, w, weights, prices, answers):
    i, j = n, w
    selected_items = []

    while i > 0 and j > 0:
        if answers[i][j] != answers[i - 1][j]:
            selected_items.append(i)
            j -= weights[i - 1]
        i -= 1

    print("Вибрані предмети:")
    for item in reversed(selected_items):
        print(f"Предмет {item}: вага {weights[item - 1]}, ціна {prices[item - 1]}")

def knapsack():
    n = int(input("Введіть кількість предметів: "))
    w = int(input("Введіть вмістимість рюкзака: "))
    
    weights = [int(x) for x in input("Введіть ваги предметів: ").split()]
    prices = [int(x) for x in input("Введіть ціни предметів: ").split()]
    answers = create_matrix(n + 1, w + 1, default=0)

    for i in range(1, n + 1):  
        for j in range(1, w + 1):  
            if weights[i - 1] <= j: 
                new_weight = j - weights[i - 1]
                answers[i][j] = max(
                    answers[i - 1][j],
                    answers[i - 1][new_weight] + prices[i - 1]
                )
            else:  
                answers[i][j] = answers[i - 1][j]

    print_things(n, w, weights, prices, answers)

if __name__ == "__main__":
    knapsack()
