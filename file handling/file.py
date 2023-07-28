#opening a file
#f = open ('filepath' , 'modepath')
f = open ('input.txt', 'r')#file object
#print(f)
#reading operations can be performed
#using file object
# ome general methods on file object
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
f.close()
print(f.closed)
