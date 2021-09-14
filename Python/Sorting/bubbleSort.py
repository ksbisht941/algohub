def bubbleSort(array):
    isSorted = False

    while not isSorted:
        isSorted = True

        for idx in range(len(array) - 1):
            if array[idx] > array[idx + 1]:
                swap(idx, idx + 1, array)
                print(array)
                isSorted = False

    return array

def swap(idx, jdx, array):
    array[idx], array[jdx] = array[jdx], array[idx]


array = [8, 5, 2, 9, 5, 6, 3]
output = bubbleSort(array)
print("👋 Output", output)

# [5, 8, 2, 9, 5, 6, 3]
# [5, 2, 8, 9, 5, 6, 3]
# [5, 2, 8, 5, 9, 6, 3]
# [5, 2, 8, 5, 6, 9, 3]
# [5, 2, 8, 5, 6, 3, 9]
# [2, 5, 8, 5, 6, 3, 9]
# [2, 5, 5, 8, 6, 3, 9]
# [2, 5, 5, 6, 8, 3, 9]
# [2, 5, 5, 6, 3, 8, 9]
# [2, 5, 5, 3, 6, 8, 9]
# [2, 5, 3, 5, 6, 8, 9]
# [2, 3, 5, 5, 6, 8, 9]