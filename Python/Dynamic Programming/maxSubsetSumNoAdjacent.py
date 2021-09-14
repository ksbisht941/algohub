# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]

    second = array[0]
    first = max(array[0], array[1])
    
    for idx in range(2, len(array)):
        current = max(first, second + array[idx])
        second = first
        first = current
        
    return first 

# O(n) time | O(n) space
# def maxSubsetSumNoAdjacent(array):
#     if not len(array):
#         return 0
#     elif len(array) == 1:
#         return array[0]

#     maxSum = array[:]
#     maxSum[1] = max(array[0], array[1])

#     for idx in range(2, len(array)):
#         maxSum[idx] = max(maxSum[idx - 1], maxSum[idx - 2] + array[idx])

#     return maxSum[-1]


array = [30, 25, 50, 55, 100, 120]
output = maxSubsetSumNoAdjacent(array)
print("👋 Output", output)

# 7, 10, 12, 7, 9, 14
# 7, 10, 19, 19, 

""" 
FORMULA 
maxSum[i] = max(maxSum[i - 1], maxSum[i - 2] + array[i])
"""