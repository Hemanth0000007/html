def digitcount(num):
    c=0
    while num:
        d=num%2 
        num=num//10
        if d%2==1:
            oc+=1
        else:
            ec+=1
        print(ec,oc)
num=int(input())
dc=digitcount(num)
