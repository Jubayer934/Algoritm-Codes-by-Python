graph = {
    'S': ['A'],
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['G'],
    'D': ['F'],
    'E': ['G'],
    'F': [],
    'G': []
}
Q = []
def bfs(graph, start):
    visited = []
    Q = [start]

    while len(Q) != 0:
        node = Q.pop(0)
        for _ in graph[node]:
            if node not in visited:
                Q += graph[node]
                visited.append(node)
    print(visited)
    print(' '.join(visited))
        
bfs(graph, 'S')