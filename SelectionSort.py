def SelectionSort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i] , arr[minimum] = arr[minimum] , arr[i]

arr = [5,4,3,2,1]

SelectionSort(arr)

print(arr)