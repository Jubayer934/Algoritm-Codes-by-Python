graph = [[(1,-1),(2,2),(5,1)],
         [(7,6)],
         [],
         [(4,3)],
         [(1,4)],
         [],
         [(5,2)],
         []]

for u in range(len(graph)):
    for v in graph[u]:
        print(u,' --> ',v[0],' cost: ',v[1])