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
    previous_level = 1               # Keep track of level of last printed node
    current = (root, previous_level)
    cq.insertFront(current)
    while not cq.isEmpty():
        current = cq.getFront()
        if current[0] != None:
            if previous_level < current[1]:
                print()
            print(current[0].val, end = " ")
            cq.insertRear((current[0].left, current[1] + 1))
            cq.insertRear((current[0].right, current[1]+ 1))
            previous_level = current[1]
        cq.deleteFront()
    print("\n")

myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert(root, num)
printLevelOrder(root)
myTree.delete(root, 13)
printLevelOrder(root)
