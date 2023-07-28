def area(l,b):
    return l*b
def perimeter(l,b):
    return 2*(l+b)
l,b=map(int,input().split())
print(area(l,b))
print(perimeter(l,b))
