def cal_total(s1,s2,s3,s4,s5):
	return s1+s2+s3+s4+s5
def cal_per(total,n):
	return total/n


s1,s2,s3,s4,s5=map(int,input().split())
total=cal_total(s1,s2,s3,s4,s5)
per=cal_per(total,5)
print(total,per)
