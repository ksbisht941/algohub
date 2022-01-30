# Shifted Binary Search
# Write a function that takes in a sorted array of distinct integers as well as a target integer. The caveat is that the integers in the array have been shifted by some amount; in other words, they've been moved to the left or to the right by one or more positions. For example, [1, 2, 3, 4] might have turned into [3, 4, 1, 2].

# The function should use a variation of the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.

# If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of the Binary Search question's video explanation before starting to code.

# def shiftedBinarySearch(array, target):
#     return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

# def shiftedBinarySearchHelper(array, target, leftIdx, rightIdx):
#     if leftIdx > rightIdx:
#         return -1

#     middleIdx = (leftIdx + rightIdx) // 2
#     potentialMatch = array[middleIdx]
#     leftNum = array[leftIdx]
#     rightNum = array[rightIdx]

#     if target == potentialMatch:
#         return middleIdx
#     elif leftNum <= potentialMatch:
#         if target < potentialMatch and target >= leftNum:
#             return shiftedBinarySearchHelper(array, target, leftIdx, middleIdx - 1)
#         else:
#             return shiftedBinarySearchHelper(array, target, middleIdx + 1, rightIdx)
#     else:
#         if target > potentialMatch and target <= rightNum:
#             return shiftedBinarySearchHelper(array, target, middleIdx + 1, rightIdx)
#         else:
#             return shiftedBinarySearchHelper(array, target, leftIdx, middleIdx - 1)

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, leftIdx, rightIdx):
    while leftIdx <= rightIdx:
        if leftIdx > rightIdx:
            return -1

        middleIdx = (leftIdx + rightIdx) // 2
        potentialMatch = array[middleIdx]
        leftNum = array[leftIdx]
        rightNum = array[rightIdx]

        if target == potentialMatch:
            return middleIdx
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >= leftNum:
                rightIdx = middleIdx - 1
            else:
                leftIdx = middleIdx + 1
        else:
            if target > potentialMatch and target <= rightNum:
                leftIdx = middleIdx + 1
            else:
                rightIdx = middleIdx - 1
    return -1


array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
output = shiftedBinarySearch(array, target)
print("👋 Output:", output)

# 8