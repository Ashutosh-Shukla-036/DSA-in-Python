def partitionFunction(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    
    while(i < j):
        while(arr[i] <= pivot and i < high):
            i += 1
        while(arr[j] > pivot and j > low):
            j -= 1
        if(i < j):
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[low] , arr[j] = arr[j] , arr[low]
    return j

def QuickSort(arr,low,high):
    if(low < high):
        partitionIndex = partitionFunction(arr,low,high)
        QuickSort(arr,low,partitionIndex-1)
        QuickSort(arr,partitionIndex+1,high)

arr = [3,8,2,5,9,1,6]

QuickSort(arr,0,len(arr)-1)

print(arr)
