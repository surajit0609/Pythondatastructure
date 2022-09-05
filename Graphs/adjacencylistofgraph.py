class Graph:
    def __init__(self,n_vertices,edges):
        self.data=[[] for _ in range(n_vertices)]
        for v1,v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)

n=5
ed=[(0,1),(0,4),(1,4),(1,3),(1,2),(2,3),(4,3)]
g1=Graph(n,ed)
print(g1.data)
        