class Frames:
	def __init__(self,n):
		self.frame=[None for i in range(n)]
		self.hit=0
		self.miss=0
		self.total=0
		self.p=0

	def hitratio(self):
		return (self.hit/self.total)*100

	def missratio(self):
		return (self.miss/self.total)*100

n=int(input("Enter the number of Frames:"))
st=list(map(int,input("Enter Reference String:").rstrip().split()))
fc=[]
Op=[]
L=[]
for i in st:
	Op.append(i)
	L.append(i)
	fc.append(i)

#First-Come First-Serve (FIFO)
f=Frames(n)
while fc:
	q=fc.pop(0)
	if q in f.frame:
		f.hit+=1
	else:
		f.frame[f.p]=q
		f.miss+=1
		f.p=(f.p+1)%n
	f.total+=1

#Optimal Page Replacement
f1=Frames(n)
while Op:
	q=Op.pop(0)
	if q in f1.frame:
		f1.hit+=1
	elif None in f1.frame:
		f1.frame[f1.p]=q
		f1.miss+=1
		f1.p=(f1.p+1)%n
	else:
		arr=[]
		for i in Op:
			if i not in arr and i in f1.frame:
				arr.append(i)
		if arr==[]:
			f1.frame[0]=q
		elif len(arr)<n:
			for h in range(len(f1.frame)):
			    if f1.frame[h] not in arr:
			    	f1.frame[h]=q
			    	break
		else:
			j=f1.frame.index(arr.pop())
			f1.frame[j]=q
		f1.miss+=1
	f1.total+=1

#Least Recently Used (LRU)
f2=Frames(n)
brr=[]

while L:
	q=L.pop(0)
	brr.append(q)
	if q in f2.frame:
		f2.hit+=1
	elif None in f2.frame:
		f2.frame[f2.p]=q
		f2.miss+=1
		f2.p=(f2.p+1)%n
	else:
		arr=[]
		for i in range(len(brr)-2,-1,-1):
			if brr[i] not in arr and brr[i] in f2.frame:
				arr.append(brr[i])
		
		if arr==[]:
			f2.frame[0]=q
		elif len(arr)<n:
			for h in range(len(f2.frame)):
			    if f2.frame[h] not in arr:
			    	f2.frame[h]=q
			    	break
		else:
			j=f2.frame.index(arr.pop())
			f2.frame[j]=q
		f2.miss+=1
	f2.total+=1

print("-----------------------------")
print("First-Come First-Serve (FIFO)")
print("No of page hit:",f.hit,"\nNo of page Miss:",f.miss,"\nNo of References:",f.total)
print("Hit ratio:",f.hitratio())
print("Miss ratio:",f.missratio())
print("-----------------------------")
print("Optimal Page Replacement")
print("No of page hit:",f1.hit,"\nNo of page Miss:",f1.miss,"\nNo of References:",f1.total)
print("Hit ratio:",f1.hitratio())
print("Miss ratio:",f1.missratio())
print("-----------------------------")
print("Least Recently Used (LRU)")
print("No of page hit:",f2.hit,"\nNo of page Miss:",f2.miss,"\nNo of References:",f2.total)
print("Hit ratio:",f2.hitratio())
print("Miss ratio:",f2.missratio())
print("-----------------------------")
m=[["First-Come First-Serve (FIFO)",f.hitratio()],["Optimal Page Replacement",f1.hitratio()],["Least Recently Used (LRU)",f2.hitratio()]]

m.sort(key=lambda k:k[1])
q=m.pop()
print("Algorithm best suites for the given reference string is:",q[0])









