# Square of Zeroes
# Write a function that takes in a square-shaped n x n two-dimensional array of only 1s and 0s and returns a boolean representing whether the input matrix contains a square whose borders are made up of only 0s.

# Note that a 1 x 1 square doesn't count as a valid square for the purpose of this question. In other words, a singular 0 in the input matrix doesn't constitute a square whose borders are made up of only 0s; a square of zeroes has to be at least 2 x 2.

# Solution 1
def squareOfZeroes(matrix):
    lastMatrix = len(matrix) - 1
    return hasSquareOfZeroes(matrix, 0, 0, lastMatrix, lastMatrix, {})

def hasSquareOfZeroes(matrix, r1, c1, r2, c2, cache):
    if r1 >= r2 or c1 >= c2:
        return False

    key = str(r1) + '-' + str(c1) + '-' + str(r2) + '-' + str(c2)
    if key in cache:
        return cache[key]

    cache[key] = 

matrix = [
  [1, 1, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 1],
  [0, 1, 1, 1, 0, 1],
  [0, 0, 0, 1, 0, 1],
  [0, 1, 1, 1, 0, 1],
  [0, 0, 0, 0, 0, 1],
]

output = squareOfZeroes(matrix)
print('👋 Output', output)

# true
# [
#   [ ,  ,  ,  ,  ,  ],
#   [0, 0, 0, 0, 0,  ],
#   [0,  ,  ,  , 0,  ],
#   [0,  ,  ,  , 0,  ],
#   [0,  ,  ,  , 0,  ],
#   [0, 0, 0, 0, 0,  ],
# ]