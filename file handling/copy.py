f = open ("F:\\THUB\\input.txt",'r')
k=f.read()
f.close()

w= open ('output.txt', 'w')
print(w.write(k))
w.close()
