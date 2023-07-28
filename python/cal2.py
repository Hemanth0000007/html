def digitcount(num):
    c=0
    while num:
        d=num%10
        num=num//10
        c+=1
    return c
num=int(input())
dc=digitcount(num)
print(dc)
