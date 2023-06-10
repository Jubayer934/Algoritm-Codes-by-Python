n=int(input())
graph=[]
elemants=[]
for i in range(n):
    elemants=list(map(int,input().split()))
    graph.append(elemants)
print(graph)
visited = [False]*n
topsort = []

def dfs(u):
    visited[u] = True
    print('Visiting ',u)

    for v in graph[u]:
        if not visited[v]:
            dfs(v) 
    print('Backtracking ',u)
    topsort.append(u)


for i in range (n):
    if visited[i]==False:
        dfs(i)
topsort.reverse()
print(topsort)