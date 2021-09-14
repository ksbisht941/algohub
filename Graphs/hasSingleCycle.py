# Here is your solution
# SOLUTION 1
# O(n) time | O(1) space
def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0

    while numElementsVisited < len(array):
        if numElementsVisited > 0  and currentIdx == 0:
            return False

        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)

    return currentIdx == 0

def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    # print(nextIdx)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)


# Call the function
array = [2, 3, 1, -4, -4, 2]
output = hasSingleCycle(array)
print("👋 Output:", output)
# True