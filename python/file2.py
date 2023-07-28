import csv
with open("data.csv","r")as f1:
    data=list(csv.reader(f1))
    mc=0
    fc=0
    for d in data [1:]:
        if d[-1]=="male":
            mc+=1
        else:
            fc+=1
    print(mc,fc)
