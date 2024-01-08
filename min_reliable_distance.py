import math

def get_min_reliable_distance(s, t, k, graph):
    n = len(graph)
    
    d = [[math.inf] * (k + 1) for _ in range(n)]
    d[s][0] = 0

    for m in range(k):
        for v1 in range(n):
            for v2, w in graph[v1]:
                d[v2][m + 1] = min(d[v2][m + 1], d[v1][m] + w)

    return min(d[t])

def main():
    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n):
        edge = list(map(int, input().split()))
        v1, v2, w = edge
        graph[v1].append((v2, w))

    s, t, k = map(int, input().split())
    
    result = get_min_reliable_distance(s, t, k, graph)
    print(result)

if __name__ == "__main__":
    main()
