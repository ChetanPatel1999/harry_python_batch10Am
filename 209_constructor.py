class students:
    def __init__(self,name, rno):
        self.name=name
        self.rno=rno  
    def displayStudent(self):
        print("student info : ")
        print("student name : ",self.name)
        print("student rno : ",self.rno) 


s1=students("ram",101)
s1.displayStudent()
print(s1.name)
