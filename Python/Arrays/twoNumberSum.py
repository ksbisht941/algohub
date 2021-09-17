# Here is your solution
# O(nLog(n))| O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        potentialSum = array[left] + array[right]

        if potentialSum > targetSum:
            right -= 1
        elif potentialSum < targetSum:
            left += 1
        else:
            return [array[left], array[right]]
            
    return []


# Call the function
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
output = twoNumberSum(array, targetSum)
print("👋 Output:", output)