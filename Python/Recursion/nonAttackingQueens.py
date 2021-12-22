

# def nonAttackingQueens(n):
#     columnsPlacements = [0] * n
#     return getNumberOfNonAttackingQueenPlacements(0, columnsPlacements, n)

# def getNumberOfNonAttackingQueenPlacements(row, columnsPlacements, boardSize):
#     print(row)
#     print(columnsPlacements)
#     print(boardSize)

#     if row == boardSize:
#         return 1

#     validPlacements = 0
#     for col in range(boardSize):
#         if isNonAttackingPlacement(row, col, columnsPlacements):
#             columnsPlacements[row] = col
#             validPlacements += getNumberOfNonAttackingQueenPlacements(row + 1, columnsPlacements, boardSize)

#     return validPlacements

# def isNonAttackingPlacement(row, col, columnsPlacements):
#     for previousRow in range(row):
#         columnToCheck = columnsPlacements[previousRow]
#         sameColumn = columnToCheck == col
#         onDiagonal = abs(columnToCheck - col) == row - previousRow

#         if sameColumn or onDiagonal:
#             return False

#     return True

def nonAttackingQueens(n):
    blockedColumns = set()
    blockedUpDiagonals = set()
    blockedDownDiagonals = set()

    return getNumberOfNonAttackingQueenPlacements(0, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, n)

def getNumberOfNonAttackingQueenPlacements(row, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize):
    if row == boardSize:
        return 1

    validPlacements = 0
    for col in range(boardSize):
        if isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
            placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
            validPlacements += getNumberOfNonAttackingQueenPlacements(row + 1, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize)
            removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
    return validPlacements

def isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    if col in blockedColumns:
        return False

    if row + col in blockedUpDiagonals:
        return False

    if row - col in blockedDownDiagonals:
        return False

    return True

def placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.add(col)
    blockedUpDiagonals.add(row + col)
    blockedDownDiagonals.add(row - col)

def removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
    blockedColumns.remove(col)
    blockedUpDiagonals.remove(row + col)
    blockedDownDiagonals.remove(row - col)


n = 5
output = nonAttackingQueens(n)
print(output)