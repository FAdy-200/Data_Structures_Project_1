from AVL_Tree import AVLTree
from Circular_Queue import CircularDeque

def printLevelOrder(root):
    """
    Given root node, print the root tree level by level
    """
    if root == None:                 # Empty Tree
        print("Tree is empty")
        return
    last_level = 2 ** root.height    # Maximum number of Nodes in last level + 1
    cq = CircularDeque(last_level)
    current = root
    cq.insertFront(current)
    while not cq.isEmpty():
        current = cq.getFront()
        if current != None:
            print(current.val, end = " ")
            cq.insertRear(current.left)
            cq.insertRear(current.right)
        cq.deleteFront()
    print()

# myTree = AVLTree()
# root = None
# nums = [33, 13, 52, 9, 21, 61, 8, 11]
# for num in nums:
#     root = myTree.insert(root, num)
# printLevelOrder(root)
# myTree.delete(root, 13)
# printLevelOrder(root)
