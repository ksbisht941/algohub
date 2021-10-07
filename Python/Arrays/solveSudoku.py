def solveSudoku(board):
    solvePartialSodoku(0, 0, board)
    return board

def solvePartialSodoku(row, col, board):
    currentRow = row
    currentCol = col

    if currentCol == len(board[row]):
        currentRow += 1
        currentCol = 0

        if currentRow == len(board):
            return True

    if board[currentRow][currentRow] == 0:
        return tryDigitsAtPosition(currentRow, currentCol, board)

    return solvePartialSodoku(currentRow, currentCol, board)


def tryDigitsAtPosition(row, col, board):
    for digit in range(1, 10):
        if isValidAtPosition(digit, row, col, board):
            board[row][col] = digit

            if solvePartialSodoku(row, col + 1, board):
                return True

    board[row][col] = 0
    return False

def isValidAtPosition(value, row, col, board):
    rowIsValid = value not in board[row]
    colIsValid = value not in map(lambda r: r[col], board)

    if not rowIsValid and not colIsValid:
        return False

    subgridRowStart = row // 3
    subgridColStart = col // 3

    for rowIdx in range(3):
        for colIdx in range(3):
            rowToCheck = subgridRowStart * 3 + rowIdx
            colToCheck = subgridColStart * 3 + colIdx
            existingValue = board[rowToCheck][colToCheck]

            if existingValue == value:
                return False

    return True

            


# 0 * 3 + 1 = 1
# 1 * 3 + 1 = 4
# 2 * 3 + 1 = 7


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
  ]

output = solveSudoku(board)
print("👋 Output:", output)