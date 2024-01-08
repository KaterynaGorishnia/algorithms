import math

graph = {
    0: [(1, 3), (2, 2)],
    1: [(3, 1)],
    2: [(3, 7)],
}

n = len(graph) 
visited = [False] * n  

def dfs(v: int, ts: list):
    visited[v] = True
    for u, w in graph[v]:
        if not visited[u]:
            dfs(u, ts)
    ts.append(v)

def topologic_sort():
    ts = []
    for v in range(n):
        if not visited[v]:
            dfs(v, ts)
    ts.reverse()
    return ts

def min_distance(u: int, v: int) -> int:
    d = [math.inf] * n
    d[u] = 0
    ts = topologic_sort()

    for v1 in ts: 
        for v2, w in graph[v1]:
            d[v2] = min(d[v2], d[v1] + w)

    return d[v]

start_vertex = int(input("Enter the starting vertex: "))
end_vertex = int(input("Enter end vertex: "))
distance = min_distance(start_vertex, end_vertex)
print(f"Minimum distance from vertex {start_vertex} to {end_vertex}: {distance}")
