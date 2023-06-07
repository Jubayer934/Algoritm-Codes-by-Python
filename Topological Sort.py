graph = [[1,4],
         [2,4],
         [3,5],
         [],
         [5],
         [3]]

n = len(graph)
visited = [False]*n
topsort = []

def dfs(u):
    visited[u] = True
    print('Visiting ',u)

    for v in graph[u]:
        if v==False:
            dfs(v) 
    print('Backtracking ',u)
    topsort.append(u)

dfs(0)
topsort.reverse()
print(topsort)