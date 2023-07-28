def total(s1,s2,s3,s4,s5):
    return s1+s2+s3+s4+s5

def calper(s,m):
    return s*100//m

def calgrade (per):
    if per>90:
        return("A+")
    elif per>70:
        return("A")
    elif per>40:
        return("B")
    else:
        return("F")
    
bc=0
def printmarks(s,m):
    global bc
    per=calper(s,m)
    grade=calgrade(per)
    print(s,m,per,grade)
    if grade=="F":
        bc+=1
      

s1,m1=map(int,input().split())
s2,m2=map(int,input().split())
s3,m3=map(int,input().split())
s4,m4=map(int,input().split())
s5,m5=map(int,input().split())
if s1>=0 and s1<=m1 and s2>=0 and s2<=m2 and s3>=0 and s3<=m3 and s4>=0 and s4<=m4 and s5>=0 and s5<=m5:
    printmarks(s1,m1)
    printmarks(s2,m2)
    printmarks(s3,m3)
    printmarks(s4,m4)
    printmarks(s5,m5)
    ts=total(s1,s2,s3,s4,s5)
    ms=total(m1,m2,m3,m4,m5)
    per=ts*100//ms
    if bc==0:
        print(ts,ms,per)
    else:
        print(ts,ms,bc)
else:
    print("invalid marks")
