class Graph:
    def __init__(self,edge):
        self.edge=edge
        self.graph={}
        for  start, end in self.edge:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
        print(self.graph)
        pass
    def get_path(self,start,end,path=[]):
        path = path +[start]
        if start==end:
            return [path]
        if start not in self.graph:
            return []
            

if __name__== '__main__':
    routs=[("mumbai","paris"),("mumbai","dubai"),
    ("paris","dubai"),("paris","new york"),
    ("dubai","new york"),('new york','toronto')]
    rout_garph=Graph(routs)