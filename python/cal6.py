def evenodd(num):
    en=0
    on=0
    a=1
    b=1
    while num:
        d=num%10 
        num=num//10
        if d%2:
            on=d*a+on
            a=a*10
        else:
            en=d*b+en
            b=b*10
    return en,on
num=int(input())
res=evenodd(num)
print(*res)
