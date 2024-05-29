
#Brute force 
def LinerSearch(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return True
    return False

def LongestSequence(arr):
    if len(arr) == 0:
        return 0
    largest = 1
    for i in range(len(arr)):
        x = arr[i]
        count = 1
        while(LinerSearch(arr,x+1) == True):
            x += 1
            count += 1
        if largest < count:
            largest = count

    return largest

nums = []
print(LongestSequence(nums))
#Time complexity is O(N*N)


#Better Solution
import sys
def Longest(arr):

    if len(arr) == 0:
        return 0
    
    arr.sort()
    current = 0
    lastsmaller = -sys.maxsize - 1
    largest = 1
    for i in range(len(arr)):
        if (arr[i]-1) == lastsmaller:
            current += 1
            lastsmaller = arr[i]
        elif (arr[i]-1) != lastsmaller:
            current = 1
            lastsmaller = arr[i]
        largest = max(largest,current)
    return largest

nums = [101,103,102,1,4,100,5]
print(LongestSequence(nums))
#Time complexity is O(NlogN) + O(N)


#optimal solution
def longestSuccessiveElements(a):
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set()
    # put all the array elements into set
    for i in range(n):
        st.add(a[i])

    # Find the longest sequence
    for it in st:
        # if 'it' is a starting number
        if it - 1 not in st:
            # find consecutive numbers
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
print(longestSuccessiveElements(nums))
#Time complexity is O(N)