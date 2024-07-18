"""
Given string S representing a postfix expression, the task is to evaluate the expression and find the final
value. Operators will only include the basic arithmetic operators like *, /, + and -.

Input: S = "231*+9-"
Output: -4
Explanation:
After solving the given expression, 
we have -4 as result. 
"""

#Optimal solution using stack
def Postfix(s):
    stack = []

    for i in s:

        if i.isdigit():
            stack.append(int(i))
        else:
            x = stack.pop()
            y = stack.pop()

            if i == "+":
                stack.append(y+x)
            elif i == "-":
                stack.append(y-x)
            elif i == "*":
                stack.append(y*x)
            elif i == "/":
                stack.append(y//x)
    
    return stack[-1]

s = "231*+9-"
print(Postfix(s))