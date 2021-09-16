# Here is your solution
# Solution 1 

# Time:
# Worst: O(n^2)
# Best: O(n Log(n))
# Avg: O(n Log(n))

# Space: O(Log(n))

def quickSort(array):
    quickSortHelper(array, 0, len(array) -1)
    return array

def quickSortHelper(array, startIdx, endIdx, ):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx

    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(array, rightIdx, leftIdx)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(array, pivotIdx, rightIdx)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)        

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    print(array)
    

# Call the function
array = [8, 5, 2, 9, 5, 6, 3]
output = quickSort(array)
print("👋 Output:", output)

# Start 8 is pivot, 5 is left and 3 is right
# We can swap in these following condition:
# - if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]

# We can step up the left idx in case of
# - if array[leftIdx] <= array[pivotIdx]

# We can step down the right idx in case of
# - if array[rightIdx] >= array[pivotIdx]

# [8, 5, 2, 3, 5, 6, 9]
# [6, 5, 2, 3, 5, 8, 9]
# [5, 5, 2, 3, 6, 8, 9]
# [3, 5, 2, 5, 6, 8, 9]
# [3, 2, 5, 5, 6, 8, 9]
# [2, 3, 5, 5, 6, 8, 9]

# p -> Pivot
# l -> Left
# r -> Right