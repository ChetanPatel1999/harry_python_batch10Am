class students:
    def __init__(self):  # non - parameterized constructor
        self.name="raj"
        self.rno=101  
    def displayStudent(self):
        print("student info : ")
        print("student name : ",self.name)
        print("student rno : ",self.rno) 
        print("---------------------------")


s1=students()
s2=students()

s1.displayStudent()
s2.displayStudent()




