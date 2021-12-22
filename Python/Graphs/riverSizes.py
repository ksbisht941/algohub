def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(matrix):
        for j in range(matrix[i]):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)

    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    


matrix =  [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]

output = riverSizes(matrix)
print('👋 Output', output)