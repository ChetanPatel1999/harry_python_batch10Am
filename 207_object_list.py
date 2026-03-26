class student:
    def setStudent(self):
        self.name=input("enter your name : ")
        self.rno=int(input("enter your rno : "))
        self.fees=int(input("enter your fess : "))
        self.per=eval(input("enter your percentage : "))
        print()
    def displayStudent(self):
        print("student info : ")
        print("student name : ",self.name)
        print("student rno : ",self.rno)
        print("student fees : ",self.fees)
        print("student per : ",self.per)
        print("-------------------------------\n")

    def maxFess(students):  
        max= float("-inf")
        for obj in students:
            if max<obj.fees:
                max=obj.fees
                s=obj
        print("student details which pay maximum fess : ")        
        s.displayStudent()   

    def marks_above_70(students):
        print("students which have above then 70 marks : ")
        for obj in students:
            if obj.per>70:
                obj.displayStudent()



students=[]
num=int(input("enter total number of student : "))#5
for i in range(num):
    s=student()
    s.setStudent()
    students.append(s)
    # students.append(student())
    # students[i].setStudent()


# for obj in students:
#     obj.setStudent()


for obj in students:
    obj.displayStudent()   

student.maxFess(students)

student.marks_above_70(students)

# max= float("-inf")
# for obj in students:
#     if max<obj.fees:
#         max=obj.fees
#         s=obj


# s.displayStudent()

    







