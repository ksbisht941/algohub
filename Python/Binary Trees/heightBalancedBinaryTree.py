# Height Balanced Binary Tree
# You're given the root node of a Binary Tree. Write a function that returns true if this Binary Tree is height balanced and false if it isn't.

# A Binary Tree is height balanced if for each node in the tree, the difference between the height of its left subtree and the height of its right subtree is at most 1.

# Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / None.

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(True, -1)

    leftSubTree = getTreeInfo(tree.left)
    rightSubTree = getTreeInfo(tree.right)

    isBalanced = leftSubTree.isBalanced and rightSubTree.isBalanced and abs(leftSubTree.height - rightSubTree.height) <= 1
    height = max(leftSubTree.height, rightSubTree.height) + 1
    return TreeInfo(isBalanced, height)

nodes = [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": None, "right": "6", "value": 3},
    {"id": "4", "left": None, "right": None, "value": 4},
    {"id": "5", "left": "7", "right": "8", "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8}
],
root =  "1"