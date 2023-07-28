# l = [1,2,7,3,2,10,2]
# sum = 12
l = list(map(int,input().split()))
sum_ = int(input())
prefix = []
x =0
for i in range(len(l)):
    x = x + l[i]
    prefix.append(x)
d = {}
for i in range(len(prefix)):
    if prefix[i] == sum_:
        print(l[0:i+1])
    elif prefix[i]-sum_ in d:
       print(l[d[prefix[i]-sum_]+1:i+1])
    d[prefix[i]] = i








        
    











