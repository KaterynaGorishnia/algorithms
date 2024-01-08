n = int(input("Введіть кількість елементів: "))

parents = [i for i in range(n)] 
ranks = [0 for i in range(n)]   

def find(a: int) -> int:
    root = a
    while parents[root] != root: 
        root = parents[root]

    node = a
    while parents[node] != node: 
        node, parents[node] = parents[node], root

    return root 

def union(a: int, b: int):
    a, b = find(a), find(b)
    if a == b:
        return
    if ranks[a] == ranks[b]:
        ranks[a] += 1
    if ranks[a] < ranks[b]:
        parents[a] = b
    else:
        parents[b] = a

def print_sets():
    sets = {}
    for i in range(n):
        representative = find(i)
        if representative not in sets:
            sets[representative] = []
        sets[representative].append(i)

    print("Система непересічних множин: ")
    for representative, elements in sets.items():
        print(f"{representative}: {elements}")

def main():
    print_sets()

    print("Введіть пари елементів для об'єднання множин: ")
    while True:
        try:
            a, b = map(int, input().split())
            union(a, b)
            print_sets()
        except ValueError:
            break

if __name__ == "__main__":
    main()
