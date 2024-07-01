from Binary_Tree import BinaryTree

class Traversal:

    def InOrder(self,Node,result = None):
        if result is None:
            result = []
        if Node:
            self.InOrder(Node.left,result)
            result.append(Node.value)
            self.InOrder(Node.right,result)
        return result

    def PreOrder(self,Node,result = None):
        if result is None:
            result = []
        if Node:
            result.append(Node.value)
            self.PreOrder(Node.left,result)
            self.PreOrder(Node.right,result)
        return result
    
    def PostOrder(self,Node,result = None):
        if result is None:
            result = []
        if Node:
            self.PostOrder(Node.left,result)
            self.PostOrder(Node.right,result)
            result.append(Node.value)
        return result
    

if __name__ == "__main__":
    BT = BinaryTree(10)
    BT.root.left = BT.Node(6)
    BT.root.right = BT.Node(9)
    BT.root.left.right = BT.Node(8)
    BT.root.right.left = BT.Node(7)

    traversal = Traversal()

    Inorder = traversal.InOrder(BT.root)
    PreOrder = traversal.PreOrder(BT.root)
    PostOrder = traversal.PostOrder(BT.root)

    print("Inorder:",Inorder)
    print("PreOrder:",PreOrder)
    print("PostOrder:",PostOrder)        