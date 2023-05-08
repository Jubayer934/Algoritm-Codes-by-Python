def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print("Move ",a,"to ",c)
        hanoi(n-1,b,a,c)

a=int(input())   
print(hanoi(a,"A","B","C"))