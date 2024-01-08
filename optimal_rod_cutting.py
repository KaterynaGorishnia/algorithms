prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
results = [None] * 11
splits = [None] * 11 

def cut(n: int) -> int:
    results[0] = 0
    for j in range(1, n + 1):
        result = -1
        for i in range(1, j + 1):
            candidate = prices[i - 1] + results[j - i]
            if candidate > result:
                result = candidate
                splits[j] = i
        results[j] = result
    return results[n]

def print_solution(n: int, splits: list):
    size = n
    while size > 0:
        cut_size = splits[size]
        print(f"Optimal cut: {cut_size}")
        size -= cut_size

rod_length = int(input("Enter the rod length: "))
optimal_price = cut(rod_length)
print(f"The optimal cost for a rod of length {rod_length} is: {optimal_price}")

print_solution(rod_length, splits)    


