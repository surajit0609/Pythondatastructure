class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
class person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class employ(person,person2):
    def __init__(self, name, idnumber):
        super().__init__(name, idnumber)
        
  
        

        