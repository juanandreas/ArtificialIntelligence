class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def equalTrees(root1, root2): 
      
    if root1 is None and root2 is None: 
        return True
        
    if root1 is not None and root2 is None:
        return False
  
    if root1 is not None and root2 is not None: 
        return ((root1.val == root2.val) and 
                equalTrees(root1.left, root2.left)and
                equalTrees(root1.right, root2.right)) 
      
    return False
    
def isSubtreeUtil(root1, root2):
    if root1 != None:
        if root1.val == root2.val:
            if equalTrees(root1, root2):
                return True
        else:
            if root1.left != None or root1.right != None:
                return isSubtreeUtil(root1.left, root2) or isSubtreeUtil(root1.right, root2)
        
    return False

def isSubtree(root1, root2): 
    # WRITE YOUR CODE HERE

    if isSubtreeUtil(root1, root2):
        return 1 
    else:
        return -1


if __name__ == '__main__':

    root1 = Node(55)
    r1_11 = Node(35)
    r1_12 = Node(76)
    root1.left = r1_11
    root1.left = r1_12
    r1_21 = Node(10)
    r1_22 = Node(43)
    r1_23 = Node(59)
    r1_24 = Node(82)
    r1_11.left = r1_21
    r1_11.right = r1_22
    r1_12.left = r1_23
    r1_12.right = r1_24
    r2_31 = Node(7)
    r2_32 = Node(22)
    r1_21.left = r2_31
    r1_21.right = r2_32

    root2 = Node(35)
    root2.left = Node(10)
    root2.right = Node(43)

    print(isSubtree(root1, root2))

