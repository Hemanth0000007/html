n=input()
dec=0
p=0
for i in n[::-1]:
    print(i)
    if ord(i)>=65 and ord(i)<=90:
        dec=dec+(ord(i)-65+10)*(36**p)
    else:
        dec=dec+(ord(i)-48)*(36**p)
    p+=1
print(dec)


c=1
ot=0
while dec:
    d=dec%8
    dec=dec//8
    ot=ot+c*d
    c=c*10
print(ot)
