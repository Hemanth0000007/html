def total(s1,s2,s3,s4,s5):
    return s1+s2+s3+s4+s5
def calper(s,m):
    return sm*100//m
def grade (per):
    if per>90:
        return("A+")
    elif per>70:
        return("A")
    else:
        return("B")
    if per>40:
        return("F")
      

s1,m1=map(int,input().split())
s2,m2=map(int,input().split())
s3,m3=map(int,input().split())
s4,m4=map(int,input().split())
s5,m5=map(int,input().split())
if s1>=0 and s1<=m1 and s2>=0 and s2<=m2 and s3>=0 and s3<=m3 and s4>=0 and s4<=m4 and s5>=0 and s5<=m5:
            per1=calper(s1,s2)
            grade=calgrade(per)
            if grade=="F":
            bc+=1
            print(s1,m1,per1,grade)

            per1=calper(s1,s2)
            grade=calgrade(per)
            if grade=="F":
            bc+=1
            print(s1,m1,per1,grade)

            per1=calper(s1,s2)
            grade=calgrade(per)
            if grade=="F":
            bc+=1
            print(s1,m1,per1,grade)

            per1=calper(s1,s2)
            grade=calgrade(per)
            if grade=="F":
            bc+=1
            print(s1,m1,per1,grade)

            per1=calper(s1,s2)
            grade=calgrade(per)
            if grade=="F":
            bc+=1
            print(s1,m1,per1,grade)
else:
    print("invalid marks")

75 100 75 a
78 85 91 a+
45 75  60 b
56 75 74 b
78 100 78 a
