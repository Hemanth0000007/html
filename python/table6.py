n,r1,r2=map(int,input().split())
d=1
if r1>r2:
    d=-1
    
    

for i in range(r1,r2+d,d):
    print(n,'X',i,'=',n*i)
    
