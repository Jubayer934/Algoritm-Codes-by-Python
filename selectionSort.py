def swap(arr,i,j):
    t=arr[i]
    arr[i]=arr[j]
    arr[j]=t
    return arr

def smallestindex(arr,low,high):
    indexMin=low
    for i in range(low+1,high):
        if arr[i]<arr[indexMin]:
            indexMin=i
    return indexMin

def selectionsort(arr):
    for i in range(0,len(arr)):
        j=smallestindex(arr,i,len(arr))
        swap(arr,i,j)
    return arr

arr=[3,5,1,4,8,4,0]
print(selectionsort(arr))