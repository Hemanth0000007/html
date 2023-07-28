import csv
with open("data.csv","r")as f1:
    data=list(csv.reader(f1))
    dic={}

    for d in data [1:]:
        if d[-2] not in dic:
            dic[d[-2]]=[d]
        else:
            dic[d[-2]].append(d)
for coll,v in dic.items():
    print(coll)
    with open(coll+".csv","w",newline="")as f2:
                w2=csv.writer(f2)
                w2.writenow(["sno","roll.no","branch",'year","college","gender"])
                for r in v:
                    w2.writerow(r)
