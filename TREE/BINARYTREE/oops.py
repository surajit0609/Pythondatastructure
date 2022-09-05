class parent:
    def __init__(self):
        self.__a=10
        pass   
    def fun(self,a,b):
        print(" i am in parent")

class child(parent):
    def get_a(self):
        print(self.__a)
    #def fun(self,a,b,c):
        #print(" i am in child")
    pass
c= child()
c.get_a()
        
        

