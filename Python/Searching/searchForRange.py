# Search For Range
# Write a function that takes in a sorted array of integers as well as a target integer. The function should use a variation of the Binary Search algorithm to find a range of indices in between which the target number is contained in the array and should return this range in the form of an array.

# The first number in the output array should represent the first index at which the target number is located, while the second number should represent the last index at which the target number is located. The function should return [-1, -1] if the integer isn't contained in the array.

# If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of the Binary Search question's video explanation before starting to code.

def searchForRange(array, target):
    finalResult = [-1, -1]
    searchForRangeHelper(array, target, 0, len(array) - 1, finalResult, True)
    searchForRangeHelper(array, target, 0, len(array) - 1, finalResult, False)
    return finalResult

def searchForRangeHelper(array, target, left, right, finalResult, goLeft):
    if left > right:
        return

    mid = (left + right) // 2
    if array[mid] < target:
        searchForRangeHelper(array, target, mid + 1, right, finalResult, goLeft)
    elif array[mid] > target:
        searchForRangeHelper(array, target, left, mid - 1, finalResult, goLeft)
    else:
        if goLeft:
            if mid == 0 or array[mid - 1] != target:
                finalResult[0] = mid
            else:
                searchForRangeHelper(array, target, left, mid - 1, finalResult, goLeft)
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                finalResult[1] = mid
            else:
                searchForRangeHelper(array, target, mid + 1, right, finalResult, goLeft)



# Sample Input
array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45

output = searchForRange(array, target)
print('👋 Output', output)

# Sample Output
[4, 9]