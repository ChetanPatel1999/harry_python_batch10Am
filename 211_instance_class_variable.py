class Student:
    institueName="hello world institute" # class variable
    totalStd=0  # class variable
    totalPass=0  # class variable
    totalFail=0  # class variable
    def __init__(self,name,rno, per):
        self.name=name      # self.name is instance variable
        self.rno=rno
        self.per=per
        Student.totalStd+=1  # 2
        if self.per>33:
            Student.totalPass+=1
        else:
             Student.totalFail+=1    

    def ReultCard(self):
        print("student ResultCard : ")
        print("institute name : ",Student.institueName)    
        print("student name : ",self.name)    
        print("student rno : ",self.rno)    
        print("student per : ",self.per)  
        if self.per>33:
            print("student Pass")
        else:
            print("student Fail")
        print("--------------------------------\n")    
    
    def totalStudent():
        print("total student : ",Student.totalStd)
        print("--------------------------------\n")    

    def totalResult():
        print("Total Result of student : ")
        print("total pass :",Student.totalPass)
        print("total Fail :",Student.totalFail)
        print("--------------------------------\n")    





s1=Student("rydham",101, 23.4)
s2=Student("sahaj",102, 80.4)
s3=Student("ranweer",103, 56.4)
s4=Student("yuvraj",104, 70.4)

s1.ReultCard()
s2.ReultCard()
s3.ReultCard()
s4.ReultCard()

Student.totalStudent()
Student.totalResult()

