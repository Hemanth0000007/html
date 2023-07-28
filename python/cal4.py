def digitcount(num):
    ec=0
    oc=0
    while num:
        d=num%2 
        num=num//10
        if d%2==1:
            oc+=1
        else:
            ec+=1
    return ec,oc
num=int(input())
res=digitcount(num)
print(*res)
