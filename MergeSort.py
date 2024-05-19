def Merge(arr,low,mid,high):
    new_arr = []
    left = low
    right = mid + 1

    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            new_arr.append(arr[left])
            left += 1
        else:
            new_arr.append(arr[right])
            right += 1

    while (left <= mid):
        new_arr.append(arr[left])
        left += 1

    while (right <= high):
        new_arr.append(arr[right])
        right += 1

    for i in range(len(new_arr)):
        arr[low + i] = new_arr[i] 

def MergeSort(arr,low,high):
    if (low >= high):
        return
    mid = (low + high) // 2
    MergeSort(arr,low,mid)
    MergeSort(arr,mid+1,high)
    Merge(arr,low,mid,high)

arr = [5, 4, 3, 2, 1]
MergeSort(arr, 0, len(arr) - 1)
print(arr)