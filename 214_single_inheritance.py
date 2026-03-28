#single inheritance 
class student:
    def setStudent(self, name, rno):
        self.name= name
        self.rno= rno
    def dispStudent(self):
        print("student info : ")
        print("name : ",self.name)    
        print("rno : ",self.rno)    


class Btech(student):
    def setBranch(self , branch):
        self.branch=branch        
    def dispBranch(self):
        # super().dispStudent()
        student.dispStudent(self)
        print("Branch : ",self.branch)

s1= Btech()
s1.setStudent("rydham",101)
s1.setBranch("CSE")
s1.dispBranch()
