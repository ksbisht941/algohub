# Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers, and returns the root of the BST.

# The function should minimize the height of the BST.

# You've been provided with a BST class that you'll have to use to construct the BST.

# Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

# A BST is valid if and only if all of its nodes are valid BST nodes.

# Note that the BST class already has an insert method which you can use if you want.

# Solution 1
# O(nlog(n)) time | O(n) space - where n is the length of the array
# def minHeightBst(array):
#     return contructMinHeightBST(array, None, 0, len(array) - 1)

# def contructMinHeightBST(array, bst, startIdx, endIdx):
#     if endIdx < startIdx:
#         return 

#     midIdx = (startIdx + endIdx) // 2;

#     valueToAdd = array[midIdx]
#     if bst is None:
#         bst = BST(valueToAdd)
#     else:
#         bst.insert(valueToAdd)
    
#     contructMinHeightBST(array, bst, startIdx, midIdx - 1)
#     contructMinHeightBST(array, bst, midIdx + 1, endIdx)

#     return bst


# Solution 2
# O(n) time | O(n) space - where n is the length of the array
# def minHeightBst(array):
#     return contructMinHeightBST(array, None, 0, len(array) - 1)

# def contructMinHeightBST(array, bst, startIdx, endIdx):
#     if endIdx < startIdx:
#         return 

#     midIdx = (startIdx + endIdx) // 2;
#     newBstNode = BST(array[midIdx])

#     if bst is None:
#         bst = newBstNode
#     else:
#         if array[midIdx] < bst.value:
#             bst.left = newBstNode
#         else:
#             bst.right = newBstNode
    
#     contructMinHeightBST(array, bst, startIdx, midIdx - 1)
#     contructMinHeightBST(array, bst, midIdx + 1, endIdx)

#     return bst

# Solution 3
# O(n) time | O(n) space - where n is the length of the array
def minHeightBst(array):
    return contructMinHeightBST(array, 0, len(array) - 1)

def contructMinHeightBST(array, startIdx, endIdx):
    if endIdx < startIdx:
        return 

    midIdx = (startIdx + endIdx) // 2;
    bst = BST(array[midIdx])
    bst.left = contructMinHeightBST(array, startIdx, midIdx - 1)
    bst.right = contructMinHeightBST(array, midIdx + 1, endIdx)
    return bst;


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
output = minHeightBst(array)
print(output)