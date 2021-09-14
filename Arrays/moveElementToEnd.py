# Here is your solution
# SOLUTION 1
# O(n) time | O(1) space - where n is the length of the input array
def moveElementToEnd(array, toMove):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx < rightIdx:
        while leftIdx < rightIdx and array[rightIdx] == toMove:
            rightIdx -= 1

        if array[leftIdx] == toMove:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]

        leftIdx += 1

    return array

# Call the function
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

output = moveElementToEnd(array, toMove)
print("👋 Output:", output)
# [4, 1, 3, 2, 2, 2, 2, 2]