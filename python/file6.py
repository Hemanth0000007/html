impot csv
with open("sk.csv")as f1:
    data=list(csv.reader(f1))
    roll=[]
    for d in data[1:]:
        roll.append(d[1])

with open("att.csv")as f1:
    data=list(csv.reader(f1))
    proll=[]
    for d in data[1:]:
        proll.append(d[1])

aroll=[]
for r in roll:
    if r not in proll:
        aroll.append(r)

with open("absent.csv","w",newline="")as f3:
    
