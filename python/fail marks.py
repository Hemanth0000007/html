def total(s1,s2,s3,s4,s5):
    return s1+s2+s3+s4+s5


s1,m1=map(int,input().split())
s2,m2=map(int,input().split())
s3,m3=map(int,input().split())
s4,m4=map(int,input().split())
s5,m5=map(int,input().split())
if s1>=0 and s1<=m1 and s2>=0 and s2<=m2 and s3>=0 and s3<=m3 and s4>=0 and s4<=m4 and s5>=0 and s5<=m5:
    if s1*100//m1>=40 and s2*100//m2>=40 and s3*100//m3>=40 and s4*100//m4>=40 and s5*100//m5>=40:
        ts=total(s1,s2,s3,s4,s5)
        ms=total(m1,m2,m3,m4,m5)
        print(ts,ms)
        print(ts*100//ms)

    else:
        print("fail")
else:
    print("invalid marks")
