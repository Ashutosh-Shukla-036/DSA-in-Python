"""A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], 
[2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
 More formally, if all the permutations of the array are sorted in one container according to their lexicographical 
 order, then the next permutation of that array is the permutation that follows it in the sorted container. 
 If such arrangement is not possible, the array must be rearranged as the lowest possible order 
 (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory."""

def reverse(arr,start,end):
    left = start
    right = end
    while(left<right):
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1

def NextPermutation(arr):
    index = -1
    for i in range(len(arr)-2,-1,-1):
        if(arr[i] < arr[i+1]):
            index = i
            break
    
    if (index == -1):
        reverse(arr,0,len(arr)-1)
    else:
        for i in range(len(arr)-1,index,-1):
            if (arr[i] > arr[index]):
                arr[i] , arr[index] = arr[index] , arr[i]
                break

        reverse(arr,index+1,len(arr)-1)
    
    return arr

nums = [2,5,5,5,5,0,0]
print(NextPermutation(nums))