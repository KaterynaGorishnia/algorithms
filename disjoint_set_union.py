class Item:
    def __init__(self, id: int):
        self.id = id
        self.head = self
        self.tail = self 
        self.next = None
        self.count = 1  

def find_set(item: Item) -> Item:
    return item.head

def union(a: Item, b: Item):
    a, b = find_set(a), find_set(b)
    if a == b:
        return

    if b.count > a.count:  
        a, b = b, a

    (a.tail.next, a.tail) = (b, b.tail)  

    a.count += b.count

    while b:
        b.head = a  
        b = b.next

def print_sets(items: list):
    sets = {}
    for item in items:
        representative = find_set(item)
        if representative not in sets:
            sets[representative] = []
        sets[representative].append(item.id)

    print("Непересічні множини:")
    for representative, elements in sets.items():
        print(f"{representative.id}: {elements}")

def main():
    n = int(input("Введіть кількість елементів: "))
    items = [Item(i) for i in range(n)]

    print("Введіть пари елементів для об'єднання множин:")
    while True:
        try:
            a_id, b_id = map(int, input().split())
            union(items[a_id], items[b_id])
        except ValueError:
            break

    print_sets(items)

if __name__ == "__main__":
    main()
