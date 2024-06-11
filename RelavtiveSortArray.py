#Relative Sort Array
"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements
 that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""

#Better Solution
#time complexity O(n*n)
def relativeSortArray(arr1, arr2):
    count = 0
    n = len(arr1)
    for i in range(len(arr2)):
        j = 0
        while (j<n):
            if arr1[j] == arr2[i]:
                arr1[j] , arr1[count] = arr1[count] , arr1[j]
                count += 1
            j += 1
    arr1[count:] = sorted(arr1[count:])

    print(arr1)

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
relativeSortArray(arr1,arr2)