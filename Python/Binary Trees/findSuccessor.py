# Find Successor
# Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent node) as well as a node contained in that tree and returns the given node's successor.

# A node's successor is the next node to be visited (immediately after the given node) when traversing its tree using the in-order tree-traversal technique. A node has no successor if it's the last node to be visited in the in-order traversal.

# If a node has no successor, your function should return None / null.

# Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

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

    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent

    return currentNode

