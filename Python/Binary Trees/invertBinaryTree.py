def invertBinaryTree(tree):
    if tree is None:
        return

    swapBinaryTree(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

    return tree

def swapBinaryTree(tree):
    tree.left, tree.right = tree.right, tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
