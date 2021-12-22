# Upper Bound: O((n*(2n)!/n!(n+1)!)) time | O(n) space
# def numberOfBinaryTreeTopologies(n):
#     if n == 0:
#         return 1

#     numberOfTrees = 0
#     for leftTreeSize in range(n):
#         rightTreeSize = n - 1 - leftTreeSize
#         numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
#         numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
#         numberOfTrees += numberOfLeftTrees * numberOfRightTrees
#     return numberOfTrees

# Upper Bound: O(n^2) time | O(n) space
# def numberOfBinaryTreeTopologies(n, cache = {0: 1}):
#     if n is cache:
#         return cache[n]

#     numberOfTrees = 0
#     for leftTreeSize in range(n):
#         rightTreeSize = n - 1 - leftTreeSize
#         numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize, cache)
#         numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize, cache)
#         numberOfTrees += numberOfLeftTrees * numberOfRightTrees
#     cache[n] = numberOfTrees
#     return numberOfTrees


# Upper Bound: O(n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    cache = [1]
    for m in range(1, n + 1):
        numberOfTrees = 0

        for leftTreeSize in range(n):
            rightTreeSize = m - 1 - leftTreeSize
            numberOfLeftTrees = cache[leftTreeSize]
            numberOfRightTrees = cache[rightTreeSize]
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        cache.append(numberOfTrees)
    return cache[n]


n = 3
output = numberOfBinaryTreeTopologies(n)
print("Output:", output)