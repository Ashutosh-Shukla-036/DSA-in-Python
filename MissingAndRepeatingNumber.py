#Finding the missing and repeating in the array

#Brute force solution
def MissingAndRepeating(arr):
    n = len(arr)
    missing , repeating = -1 , -1

    for i in range(1,n):
        counter = 0
        for j in range(n):
            if arr[j] == i:
                counter += 1
        if counter == 2:
            repeating = i
        elif counter == 0:
            missing = i
        if(missing != -1 and repeating != -1):
            break
    return [missing,repeating]

num = [4,2,1,3,1,7,5]
print(MissingAndRepeating(num))

#Optimal solution 1:using maths
def MAR(arr):
    n = len(arr)
    Sn = (n*(n+1))//2
    S2n = (n*(n+1)*(2*n+1))//6
    S , S2 = 0 , 0

    for i in range(n):
        S += arr[i]
        S2 += (arr[i]*arr[i])

    val1 = S - Sn
    val2 = (S2 - S2n)//val1

    x = (val1 + val2) // 2
    y = val2 - x

    return [x,y]
nums = [4,3,1,2,1,6]
print(MAR(nums))    

#Optimal solution 2:using XOR and Bit manipulation
def MissingRepeating(nums):
    n = len(nums)
    xor = 0
    for i in range(n):
        xor = xor ^ nums[i]
        xor = xor ^ (i+1)

    bitNo = 0
    while(1):
        if (xor & (1<<bitNo)) != 0:
            break
        bitNo += 1

    zero = 0
    one = 0
    for i in range(n):
        if (nums[i] & (1<<bitNo)) !=0 :
            one  = one ^ nums[i]
        else:
            zero = zero ^ nums[i]

    for i in range(1,n+1):
        if (i & (1<<bitNo)) != 0:
            one = one ^ i
        else:
            zero = zero ^ i

    counter = 0
    for i in range(n):
        if nums[i] == zero :
            counter += 1

    if counter == 2:
        return [zero,one]
    return [one,zero]
nums = [4,3,1,2,1,6]
print(MissingRepeating(nums))