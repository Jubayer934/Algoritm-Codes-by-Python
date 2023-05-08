def bubbleSort(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range (0,i):
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)
    return arr

def swap(arr,i,j):
    t=arr[i]
    arr[i]=arr[j]
    arr[j]=t
    return arr

arr=[3,5,1,4,8,4,0]
print(bubbleSort(arr))