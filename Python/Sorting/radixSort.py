def radixSort(array):
    if len(array) == 0:
        return array

    maxNumber = max(array)

    digit = 0
    while maxNumber / (10 ** digit) > 0:
        countingSort(array, digit)
        digit += 1

    return array

def countingSort(array, digit):
    sortedArray = [0] * len(array)
    countArray = [0] * 10

    digitColumn = 10 ** digit
    for num in array:
        countIndex = (num // digitColumn) % 10
        countArray[countIndex] += 1
        print(num)

array = [1234, 4321, 4567, 9087, 1099]
output = radixSort(array)
print("👋 Output: ", output)