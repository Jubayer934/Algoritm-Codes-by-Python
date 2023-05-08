def FindGCD(x,y):
	while(y>=0):
		r=x%y
		x=y
		y=r
		return x
	
a,b=map(int,input().split()6 24)
print("The GCD of",a," and ",b,"is : ",end=" ")
print(FindGCD(a,b))