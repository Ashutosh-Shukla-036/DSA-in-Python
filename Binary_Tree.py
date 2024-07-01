class BinaryTree:
    class Node:
        def __init__(self,value: int) -> None:
            self.left = None
            self.right = None
            self.value = value

    def __init__(self,RootValue) -> None:
        self.root = self.Node(RootValue)

if __name__ == "__main__":
    BT = BinaryTree(10)
    BT.root.left = BT.Node(6)
    BT.root.right = BT.Node(9)
    BT.root.left.right = BT.Node(8)
    BT.root.right.left = BT.Node(7)

    print("Root value:", BT.root.value)  
    print("Left child of root:", BT.root.left.value)  
    print("Right child of root:", BT.root.right.value)