#hierarchical inheritance
class person:
    def setName(self, name):
        self.name=name
    def getName(self):
        print("person info : ")
        print("name : ",self.name)    

class teacher(person):
    def setSubject(self, subject):
       self.subject=subject
    def getSubject(self):
        print("subject : ",self.subject) 

class doctor(person):
    def setSpeci(self, speci):
        self.speci=speci
    def getSpeci(self):
        print("speci : ",self.speci) 

t1=teacher()
t1.setName("sahaj chabra")
t1.setSubject("maths")
t1.getName()
t1.getSubject()


d1=doctor()
d1.setName("rydham patel")
d1.setSpeci("dental")
d1.getName()
d1.getSpeci()
