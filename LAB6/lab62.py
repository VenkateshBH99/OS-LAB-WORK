import math
st=list(map(int,input("Enter Request Queue:").rstrip().split()))
pos=60
fc=[]
S=[]
for i in st:
	fc.append(i)
	S.append(i)
#First-Come First-Serve (FCFS)
pre=pos
t1=0
while fc:
	q=fc.pop(0)
	t1+=abs(q-pre)
	pre=q
print("------------------------------")
print("First-Come First-Serve (FCFS)")
print("the total number of track movements:",t1)
print("the total time taken for the R/W head movement:",t1,"ns")


#Shortest Seek Time First (SSTF)

t2=0
last=pos

while S:
	j=0
	ma=float("inf")
	for i in range(len(S)):
		if abs(last-S[i])<ma:
			ma=abs(last-S[i])
			j=i

	t2+=abs(last-S[j])
	last=S.pop(j)
print("------------------------------")
print("Shortest Seek Time First (SSTF)")
print("the total number of track movements:",t2)
print("the total time taken for the R/W head movement:",t2,"ns")
print("------------------------------")
if(t1>t2):
	print("Shortest Seek Time First (SSTF) algorithm performs better")
elif t2>t1:
	print("First-Come First-Serve (FCFS) algorithm performs better")
else:
	print("Both the algorithm performs better")