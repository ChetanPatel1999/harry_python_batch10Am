class student:
    def __init__(self, name, rno):
        self.name= name
        self.rno= rno
    def dispStudent(self):
        print("student info : ")
        print("name : ",self.name)    
        print("rno : ",self.rno)    


class Btech(student):
    def __init__(self ,name,rno, branch):
        # super().__init__(name,rno)
        student.__init__(self,name,rno)
        self.branch=branch        
    def dispBranch(self):
        print("Branch : ",self.branch)

s1= Btech("sahaj",101,"CSE")
s1.dispStudent()
s1.dispBranch()



