graph = [[1,9],
         [0,8],
         [3],
         [2,4,5],
         [3],
         [3,6],
         [5,7],
         [3,6,8,10,11],
         [1,7,9],
         [0,8],
         [7,11],
         [7,10],
         []]
n = len(graph)
prev = [-1]*n
q = []
visited = [False]*n
path = []

def shortestPath(graph,u,v):

    q.append(u)


    visited[u] = True

    while len(q)!=0:
        node = q.pop(0)

        for neighbor in graph[node]:
            
            if visited[neighbor] == False:
                q.append(neighbor)
                prev[neighbor] = node

                visited[neighbor] = True

    while v != -1:
        path.append(v)
        v = prev[v]

    path.reverse()
    print(path)
shortestPath(graph,0,4)