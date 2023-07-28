import csv
with open("data.csv","r")as f1:
    data=list(csv.reader(f1))
    dic=()

    for d in data [1:]:
        if d[-2] not in dic:
            dic[d[-2]]=1
        else:
            dic[d[-2]]+=1
for k,v in dic.items():
    print(k,v)
