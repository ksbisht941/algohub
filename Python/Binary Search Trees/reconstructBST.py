# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None

    currentValue = preOrderTraversalValues[0]
    rightSubTreeIdx = len(preOrderTraversalValues)

    for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx]
        if value >= currentValue:
            rightSubTreeIdx = idx
            break

    leftSubTree = reconstructBst(preOrderTraversalValues[1:rightSubTreeIdx])
    rightSubTree = reconstructBst(preOrderTraversalValues[rightSubTreeIdx:])

    return BST(currentValue, leftSubTree, rightSubTree)

preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
output = reconstructBst(preOrderTraversalValues)
print("👋 Output:", output)