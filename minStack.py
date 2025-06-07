class MinStack:

    class Node:

        def __init__(self, value, minSoFar, Next = None):
            self.value = value
            self.minSoFar = minSoFar
            self.Next = Next

    def __init__(self):
        self.Top = None

    def push(self, val: int) -> None:
        if not self.Top:
            newNode = self.Node(val, val)
        else:
            newMin = min(val, self.Top.minSoFar)
            newNode = self.Node(val, newMin, self.Top)
        self.Top = newNode

    def pop(self) -> None:
        if self.Top:
            self.Top = self.Top.Next

    def top(self) -> int:
        if self.Top:
            return self.Top.value

    def getMin(self) -> int:
        if self.Top:
            return self.Top.minSoFar


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()