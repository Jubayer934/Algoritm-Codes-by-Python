def insertionSort1(n, arr):
    key = arr[n-1]
    i = n-2

    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]
        print(' '.join(map(str, arr))) #print arr without box
        i =i-1

    arr[i+1] = key
    print(' '.join(map(str, arr)))

n = int(input())
arr = list(map(int, input().split()))
insertionSort1(n, arr)