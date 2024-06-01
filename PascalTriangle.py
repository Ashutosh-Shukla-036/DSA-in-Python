#Pascal Triangle

"""
1)Given row and column , print element at that row and column from Pascal Triangle.
Formula is (row-1)C(column-1) . Combination formula nCr = n!/r!(n-r)!. 
"""
def NcR(n,r):
    ans = 1
    for i in range(r):
        ans = ans * (n-i)
        ans = ans // (i+1)
    return ans
print(NcR(5-1,4-1))

"""
2)Given Nth row , print Pascal Triangle.
"""
def PascalTriangle(row):
    ans = 1
    ansRow = [1]
    for col in range(1,row):
        ans = ans * (row - col)
        ans = ans // col
        ansRow.append(ans)
    return ansRow
rows = 5
ansRow = []
for row in range(1,rows+1):
    ansRow.append(PascalTriangle(row))
    print(ansRow)