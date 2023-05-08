import math


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

l=[3,5,1,4,8,4,0]
insertionsort(l)
print('sorted= ',l)