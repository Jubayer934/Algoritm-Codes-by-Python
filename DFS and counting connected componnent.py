n=9
graph= [[2,8],[2],[0,1,3],[2,8],[5,6,7],[4,6],[4,5],[4],[0,3]]

visited= [False]*n

def dfs(a):
    print('Visiting node: ',a)
    visited[a] = True
    for u in graph[a]:
        if not visited[u]:
            dfs(u)
    print('Backing node: ',a)
    
def find_components():
    count= 0
    for i in range(n):
        if visited[i]==False:
            count += 1
            dfs(i)
    return count
print('The number of connected components are: ',find_components())