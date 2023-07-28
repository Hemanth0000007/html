def reverse(num):
    rev=0
    temp=num
    while num:
        d=num%10
        num=num//10
        rev=rev*10+d
    return rev==temp
num=int(input())
res=reverse(num)
print(res)

