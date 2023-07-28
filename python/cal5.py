def digitcount(num):
    ec=0
    oc=0
    c=0
    while num:
        d=num%10 
        num=num//10
        c+=1
        if d%2==1:
            oc+=1
        else:
            ec+=1
    if c==ec:
        return "even"
    elif c==oc:
        return "odd"
    else:
        return "mixed"
num=int(input())
res=digitcount(num)
print(res)
