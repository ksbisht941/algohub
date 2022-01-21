# Number Of Ways To Traverse Graph
# You're given two positive integers representing the width and height of a grid-shaped, rectangular graph. Write a function that returns the number of ways to reach the bottom right corner of the graph when starting at the top left corner. Each move you take must either go down or right. In other words, you can never move up or left in the graph.

# For example, given the graph illustrated below, with width = 2 and height = 3, there are three ways to reach the bottom right corner when starting at the top left corner:

#  _ _
# |_|_|
# |_|_|
# |_|_|

# 1. Down, Down, Right
# 2. Right, Down, Down
# 3. Down, Right, Down
# Note: you may assume that width * height >= 2. In other words, the graph will never be a 1x1 grid.

# Solution 1
# def numberOfWaysToTraverseGraph(width, height):
#     if width == 1 or height == 1:
#         return 1

#     return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)

# def numberOfWaysToTraverseGraph(width, height):
#     numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

#     for idx in range(1, width + 1):
#         for jdx in range(1, height + 1):
#             if idx == 1 or jdx == 1:
#                 numberOfWays[jdx][idx] = 1
#             else:
#                 moveLeft = numberOfWays[jdx][idx - 1]
#                 moveUp = numberOfWays[jdx - 1][idx]
#                 numberOfWays[jdx][idx] = moveLeft + moveUp

#     return numberOfWays[height][width]

def numberOfWaysToTraverseGraph(width, height):
    xWidth = width - 1
    xHeight = height - 1

    num = factorial(xWidth + xHeight)
    den = factorial(xWidth) * factorial(xHeight)
    return num // den

def factorial(num):
    result = 1

    for n in range(2, num + 1):
        result *= n

    return result
            
width = 4
height = 3
output = numberOfWaysToTraverseGraph(width, height)
print('👋 Output:', output)

# [0, 0, 0, 0, 0], 
# [0, 1, 1, 1, 1], 
# [0, 1, 2, 3, 4], 
# [0, 1, 3, 6, 10]