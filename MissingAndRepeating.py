"""
🧠 Finding the Missing and Duplicate Number using XOR
Problem Statement: 
You're given an array of n elements. The numbers range from 1 to n, but:
        1)One number is missing
        2)One number is repeated (duplicate)

You must find both numbers in O(n) time and O(1) extra space.

-------------------------------------------------------------------

Intuition Behind Using XOR

🔑 Key XOR Properties:

a ^ a = 0 (same numbers cancel out)

a ^ 0 = a

XOR is commutative and associative:
→ a ^ b ^ c = c ^ a ^ b

---------------------------------------------------------------------

🧠 Why XOR Helps Here?

If there were no errors, XOR of all numbers from 1 to n and the array would be 0 (since all pairs would cancel).

But due to:
        One missing number
        One duplicate number


Final XOR result becomes:
xor1 = missing ^ duplicate

This gives us the combined effect of these two numbers.

------------------------------------------------------------------------

🚩 Problem:

We now have: xor1 = missing ^ duplicate

But we don't know which number is which. We need to separate them.

------------------------------------------------------------------------

Step: Find the Rightmost Set Bit

💭 Why?

We know that missing ≠ duplicate, so their XOR is not zero.
That means at least one bit in xor1 is set (is 1).

A set bit means that the two numbers differ at that specific bit.

⚙ How to Find It?

We want to isolate the rightmost bit that is set: rightmost_set_bit = xor1 & -xor1

🧠 Why This Works?

Let's say:

xor1 = 010100 (binary)
      -xor1 = 101100 (two's complement)
xor1 & -xor1 = 000100  ← this gives rightmost set bit

This bit is different between missing and duplicate.
It gives us a basis to split numbers into two groups.

----------------------------------------------------------------------------

✂ Step: Partition All Numbers

Now, we divide:
        Numbers from the array
        Numbers from 1 to n

Into 2 buckets:

Group	Condition	Meaning

A	(num & rightmost_set_bit) ≠ 0 (bit set)	Bit is 1 in that pos
B	(num & rightmost_set_bit) == 0 (not set)	Bit is 0 in that pos


> The idea: Missing and Duplicate must fall into different buckets (since they differ at that bit).

-----------------------------------------------------------------------------

🧪 Step: XOR Each Group Separately

Each group will contain:
        Some numbers that cancel out
        One of the special numbers (missing or duplicate)

So:
x = XOR of all nums with the bit set
y = XOR of all nums with the bit not set

At the end:
    x and y will be:
        One is the missing number
        One is the duplicate number

-------------------------------------------------------------------------------

🧾 Final Step: Identify Which is Which

We now know the two numbers, say x and y.

We still don't know which one is missing and which one is duplicate.

So we check the original array:

if arr.count(x) == 2:
    duplicate = x
    missing = y
else:
    duplicate = y
    missing = x

Simple and fast.

-------------------------------------------------------------------------------

🧠 Important Notes to Remember

XOR helps cancel all matching values and isolate mismatched ones.

xor1 = duplicate ^ missing gives the net imbalance.

rightmost_set_bit isolates a position where they differ.

This bit is used to separate numbers and isolate duplicate and missing.

Use arr.count() to finalize who's who.
"""

def MissingAndRepeat(nums):
    xor = 0
    for i in nums:
        xor ^= i
    for i in range(1,len(nums)+1):
        xor ^= i

    RightMostSetBit = xor & -xor

    x , y = 0 , 0

    for i in nums:
        if i & RightMostSetBit:
            x ^= i
        else:
            y ^= i
    for i in range(1,len(nums)+1):
        if i & RightMostSetBit:
            x ^= i
        else:
            y ^= i
    
    if nums.count(x) == 2:
        print(f"Duplicate: {x}")
        print(f"Missing: {y}")
    else:
        print(f"Duplicate: {y}")
        print(f"Missing: {x}")

MissingAndRepeat([1,2,3,3,5,6,7,8])