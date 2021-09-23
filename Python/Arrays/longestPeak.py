def longestPeak(array):
    longestRange = 0
    idx = 1

    while idx < len(array) - 1:
        isPeak = array[idx - 1] < array[idx] and array[idx] > array[idx + 1];
        if not isPeak:
            idx += 1
            continue

        leftIdx = idx - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = idx + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeak = rightIdx - leftIdx - 1
        longestRange = max(currentPeak, longestRange)
        idx = rightIdx

    return longestRange

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
output = longestPeak(array)
print("👋 Output:", output)