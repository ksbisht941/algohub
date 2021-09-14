# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# SOLUTION 1
# O(n) time | O(n) space
# def findSuccessor(tree, node):
#     inOrderTraversalOrder = getInOrderTraversalOrder(tree)

#     for idx, currentNode in enumerate(inOrderTraversalOrder):
#         if currentNode != node:
#             continue

#         if idx > len(inOrderTraversalOrder) - 1:
#             continue

#         return currentNode

# def getInOrderTraversalOrder(node, inOrder = []):
#     if node is None:
#         return inOrder

#     getInOrderTraversalOrder(node.left)
#     inOrder.append(node.value)
#     getInOrderTraversalOrder(node.right)

#     return inOrder

# SOLUTION 2
# O(n) time | O(1) space
def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftMostChild(node.right)

    return getRightMostParent(node)

def getLeftMostChild(node):
    currentNode = node

    while currentNode.left is not None:
        currentNode = currentNode.left

    return currentNode
    
def getRightMostParent(node):
    currentNode = node

    while currentNode.parent is not None and currentNode.parenet.right == currentNode:
        currentNode = currentNode.parent

    return currentNode

