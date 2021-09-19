# Here is your solution
def largestRange(array):
    nums = {}
    bestRange = []
    longestLength = 0

    for num in array:
        nums[num] = True

    for num in array:
        if not nums[num]:
            continue

        nums[num] = False

        left = num - 1
        right = num + 1
        currentLength = 0

        while left in nums:
            nums[left] = False
            left -= 1
            currentLength += 1

        while right in nums:
            nums[right] = False
            right += 1
            currentLength += 1

        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]

    return bestRange


# Here is output
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
output = largestRange(array)
print("👋 Output:", output)
# 👋 Output: [0, 7]