def insertionsort(arr):
    for i in range(1,len(arr)):
        if (arr[i]<arr[i-1]):
            toinsert=arr[i]
            j=i
            while True:
                arr[j]=arr[j-1]
                j=j-1
                if toinsert>=arr[j-1] or j<=0:
                    break
            arr[j]=toinsert

n=int(input())
l=list(map(int,input().split()))[:n]
insertionsort(l)
print('sorted= ',l)