
n=int(input("Enter number of Processes:"))
class Process:
	def __init__(self,name):
		self.name=name
		self.alloc=None
		self.Max=None
		self.Need=None
P=[Process(input("name:")) for i in range(n)]
print("Enter Allocation:")
for i in range(n):
	arr=list(map(int,input().rstrip().split()))
	P[i].alloc=arr
print("Enter Max:")
for i in range(n):
	arr=list(map(int,input().rstrip().split()))
	P[i].Max=arr
#Need
for i in range(n):
	P[i].Need=[(P[i].Max[k]-P[i].alloc[k]) for k in range(len(P[i].Max))]

print("Enter Available(Work):")
work=list(map(int,input().rstrip().split()))
Q=[]
for i in P:
	Q.append(i)
T=[]
while Q:
	s=Q.pop(0)
	flag=0
	for i in range(len(s.Need)):
		if s.Need[i]>work[i]:
			flag=1
			Q.append(s)
			break
	if flag==0:
		T.append(s)
		for i in range(len(work)):
			work[i]+=s.alloc[i]

print("Safe Sequence is:",end="")
for j in T:
	print(j.name,end=" ")
print()
		
 








