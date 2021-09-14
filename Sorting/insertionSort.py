def insertionSort(array):
    for idx in range(1, len(array)):
        jdx = idx
        
        while (jdx > 0 and array[jdx] < array[jdx - 1]):
            array[jdx], array[jdx - 1] = array[jdx - 1], array[jdx]
            # print(array)
            jdx -= 1
            
    return array

array = [8, 5, 2, 9, 5, 6, 3]
output = insertionSort(array)
print("👋 Output", output)

# [5, 8, 2, 9, 5, 6, 3]
# [5, 2, 8, 9, 5, 6, 3]
# [2, 5, 8, 9, 5, 6, 3]
# [2, 5, 8, 5, 9, 6, 3]
# [2, 5, 5, 8, 9, 6, 3]
# [2, 5, 5, 8, 6, 9, 3]
# [2, 5, 5, 6, 8, 9, 3]
# [2, 5, 5, 6, 8, 3, 9]
# [2, 5, 5, 6, 3, 8, 9]
# [2, 5, 5, 3, 6, 8, 9]
# [2, 5, 3, 5, 6, 8, 9]
# [2, 3, 5, 5, 6, 8, 9]