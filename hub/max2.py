#arbitrary number of arguments to funtion
def mymax(*lst):
    mx = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > mx:
            mx = lst[i]
    print(mx)
mymax(10,20)
mymax(10,20,30)
mymax(10,20,30,40)
mymax(10,20,30,40,50)
