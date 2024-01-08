import math
import bisect

def find_lis(a):
    n = len(a) 
    d = [math.inf] * (n + 1)
    d[0] = -math.inf
    pos = [0] * (n + 1)
    pos[0] = -1
    prev = [0] * n
    length = 0

    for i in range(n):
        j = bisect.bisect_left(d, a[i]) 
        if d[j - 1] < a[i] < d[j]:
            d[j] = a[i]
            pos[j] = i
            prev[i] = pos[j - 1]
            length = max(length, j)

    answer = []
    p = pos[length]
    while p != -1:  
        answer.append(a[p])
        p = prev[p]
    answer.reverse()

    return answer

def main():
    a = [int(x) for x in input("Введіть список цілих чисел: ").split()]

    lis = find_lis(a)
    
    print("Найбільша зростаюча підпослідовність:")
    print(" ".join(map(str, lis)))

if __name__ == "__main__":
    main()
