def Sorte(T):
	return T[0]
def Mini(A,p):
	R=[]
	for i in range(len(A)):
		a=abs(p-A[i])
		t=[a,A[i]]
		R.append(t)
	R.sort(key=Sorte)
	return R[0][1]

Request=[98, 67, 78, 30, 10, 45, 180, 20, 150, 35]
position=60
movef=0
c=position
l=len(Request)
for i in range(l):
	movef=movef+abs(c-Request[i])
	c=Request[i]
print("First Come First Serve:")
print("No. of moves is",movef,"ns") 
print()
#SSTF
p=position
moves=0
for i in range(l):
	a=Mini(Request,p)
	moves=moves+abs(p-a)
	p=a
	Request.pop(Request.index(a))
print("Shortest Seek Time First:")
print("No. of moves is",moves,"ns")
print()
if(moves>movef):
	print("First Come First Serve is better")
elif(moves<movef):
	print("Shortest Seek Time First is better")
else:
	print("Both are equally better in this case")



