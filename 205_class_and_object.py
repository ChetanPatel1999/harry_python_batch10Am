class student:
    def setStudent(self,name,rno,fees):
        self.name=name
        self.rno=rno
        self.fees=fees
    def displayStudent(self):
        print("student info : ")
        print("student name : ",self.name)
        print("student rno : ",self.rno)
        print("student fees : ",self.fees)
        print("-------------------------------\n")
    def maxFess(ob1,ob2,ob3):  # like static method of java and c++
        if ob1.fees>ob2.fees and ob1.fees>ob3.fees:
            print("max fess of :",ob1.fees)
            print("studant name :",ob1.name)
        elif ob2.fees>ob3.fees:
            print("max fess of :",ob2.fees)
            print("studant name :",ob2.name)    
        else:
            print("max fess of :",ob3.fees)
            print("studant name :",ob3.name)   
    def fun():   # like static method of java and c++
        print("hello i am fun")



student.fun()

s1=student()
s1.setStudent("rydham",101,55000)
s1.displayStudent()


s2=student()
s2.setStudent("sahaj",102,8000)
s2.displayStudent()
        
s3 = student()  
s3.setStudent("ranveer",103,10000)
s3.displayStudent()     

student.maxFess(s1,s2,s3)
