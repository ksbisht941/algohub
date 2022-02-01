# Two Number Sum
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

# Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

# You can assume that there will be at most one pair of numbers summing up to the target sum.

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