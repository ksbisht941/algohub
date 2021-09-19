# O(n) time | O(1) space
def subarraySort(array):
    maxOutOfOrder = float("-inf")
    minOutOfOrder = float("inf")
    for idx in range(len(array)):
        num = array[idx]
        if isOutOfOrder(idx, num, array):
            maxOutOfOrder = max(maxOutOfOrder, num)
            minOutOfOrder = min(minOutOfOrder, num)

    if minOutOfOrder == float("inf"):
        return [-1, -1]

    leftOutOfOrderIdx = 0
    rightOutOfOrder = len(array) - 1

    while (minOutOfOrder >= array[leftOutOfOrderIdx]):
        leftOutOfOrderIdx += 1

    while (maxOutOfOrder <= array[rightOutOfOrder]):
        rightOutOfOrder -= 1

    return [leftOutOfOrderIdx, rightOutOfOrder]

    print(maxOutOfOrder)
    print(minOutOfOrder)

    return array

def isOutOfOrder(idx, num, array):
    if idx == 0:
        return num > array[idx + 1]
    if idx == len(array) - 1:
        return num < array[idx - 1]
    return num > array[idx + 1] or num < array[idx - 1] 

# Here is your Output
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
output = subarraySort(array)
print("👋 Output:", output);

# [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
#  1  2  3  4   5   6  7   8  9  10 11  12  13
#  1  2  4  6   7   7  7  10  11 12 16  18  19
#  