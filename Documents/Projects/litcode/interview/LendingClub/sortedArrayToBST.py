# binary tree node 
class Node: 
    def __init__(self, d): 
        self.data = d 
        self.left = None
        self.right = None

def preOrder(node):
    if not node:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


def inOrder(node):
    if not node:
        return
    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)


def postOrder(node):
    if not node:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data, end=" ")

def sortedArrayToBST(arr):
    if not arr:
        return None

    mid = int(len(arr)/2)
    root = Node(arr[mid])

    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])

    return root


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    root = sortedArrayToBST(arr)
    
    preOrder(root)
    print("\n")
    inOrder(root)
    print("\n")
    postOrder(root)
    print("\n")
