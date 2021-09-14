def selectionSort(array):
    currentIdx = 0
    
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx

        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
            
        array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
        # print(array)
        currentIdx += 1

    return array

array = [8, 5, 2, 9, 5, 6, 3]
output = selectionSort(array)
print("👋 Output", output)

# [8, 5, 2, 9, 5, 6, 3]
# [2, 5, 8, 9, 5, 6, 3]
# [2, 3, 8, 9, 5, 6, 5]
# [2, 3, 5, 9, 8, 6, 5]
# [2, 3, 5, 5, 8, 6, 9]
# [2, 3, 5, 5, 6, 8, 9]
# [2, 3, 5, 5, 6, 8, 9]