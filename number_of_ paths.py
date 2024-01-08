n = 6  

graph_reversed = [
    [1, 2],   
    [3, 4],   
    [4],       
    [2],      
    [5],        
    [3]        
]

def count_paths(s: int, t: int) -> int:
    d = [None] * n 
    d[s] = 1
    return count_rec(d, t)

def count_rec(d: list, v: int) -> int:
    if d[v] is not None:
        return d[v]

    result = 0
    for u in graph_reversed[v]:
        result += count_rec(d, u)

    d[v] = result
    return result


start_vertex = int(input("Enter the starting vertex: "))
end_vertex = int(input("Enter end vertex: "))

paths_count = count_paths(start_vertex, end_vertex)
print(f"Number of paths from vertex {start_vertex} to {end_vertex}: {paths_count}")