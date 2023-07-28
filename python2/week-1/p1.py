n=int(input())
res=0
c=1
while n:
    d=n%2
    n=n//2
    res=res+c*d
    c=c*10
    
    print(res)
