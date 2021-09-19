def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1 

    print(len(matrix))

    while row < len(matrix) and col >= 0:
        print(matrix[row][col])

        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]

    return [-1, -1]

matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]
target = 44

output = searchInSortedMatrix(matrix, target)
print("👋 Output:", output)