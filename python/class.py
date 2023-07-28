class Student:
    college="ADITYA"
    def __init__(self,n,r,p):
            self.name=n
            self.rollno=r
            self.per=p
            self.college="aditya"

            
    def display(self):
        print(self.name,self.rollno,self.per)
        print(Student.college)

s1=Student("hemanth",457,99.99)
s1.display
