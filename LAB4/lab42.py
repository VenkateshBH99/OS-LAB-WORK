def completion(arr):
	comp=[]
	su=0
	for i in range(len(arr)):
		su+=arr[i][1]
		comp.append([arr[i][0],su])
	return comp

def waiting(comp,arr):
	brr=[]
	for i in range(len(comp)):
		brr.append([arr[i][0],comp[i][1]-arr[i][1]])
	return brr

def prin(name,arr,comp,warr,n):
	print("process  burst  turnaround  waiting")
	for i in range(len(arr)):
		print(arr[i][0],"     ",arr[i][1],"     ",comp[i][1],"       ",warr[i][1])
	Tavg=0
	for i in range(n):
		Tavg+=comp[i][1]
	Tavg=Tavg/n
	Wavg=0
	for i in range(n):
		Wavg+=warr[i][1]
	Wavg=Wavg/n
	print("avg turnaround:",Tavg)
	print("avg waiting time:",Wavg)
	print("-----------------------")
	
	return [name,Tavg,Wavg]

def main():
	n=int(input("Enter number of process:"))
	arr=[]
	print("Enter Burst time:")
	for i in range(n):
		print(i+1,":",end="")
		a=int(input())
		arr.append([i+1,a])
	print()
	#FCFS
	comp=completion(arr)
	warr=waiting(comp,arr)
	print("FCFS:")
	F=prin("FCFS",arr,comp,warr,n)


	#SJF
	crr=[]
	for i in range(n):
		crr.append([i+1,arr[i][1]])
	crr.sort(key=lambda k:k[1])
	comp=completion(crr)
	war=waiting(comp,crr)
	crr.sort(key=lambda k:k[0])
	comp.sort(key=lambda k:k[0])
	war.sort(key=lambda k:k[0])
	print("SJF:")
	SJ=prin("SJF",crr,comp,war,n)

	#RR
	t=float(input("Enter time quantum of RR:"))
	grr=[]
	frr=[]
	for i in range(n):
		grr.append([arr[i][0],arr[i][1]])
		frr.append([arr[i][0],arr[i][1]])
	trr=[]
	su=0
	con=0
	while grr:
		s=grr.pop(0)
		con+=1
		if s[1]<=t:
			su+=s[1]
			trr.append([s[0],su])
		elif s[1]>t:
			su+=t
			s[1]-=t
			grr.append(s)
	trr.sort(key=lambda k:k[0])
	war=waiting(trr,frr)
	print("RR:")
	R=prin("RR",frr,trr,war,n)
	print("No of context switch:",con-1)
	
	z=[F,SJ,R]
	z.sort(key=lambda k:k[1])
	print("Best Algorithm accord to Turnaround is:",end="")
	print(z[0][0])
	z.sort(key=lambda k:k[2])
	print("Best Algorithm accord to waiting time is:",end="")
	print(z[0][0])




if __name__ == '__main__':
	main()

