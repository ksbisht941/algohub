# Here is your solution
# SOLUTION 1
# O(nLog(n) + mLog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idx = 0
    jdx = 0
    smallestPair = []
    smallest = float('inf')
    current = float('inf')

    while idx < len(arrayOne) and jdx < len(arrayTwo):
        valueOne = arrayOne[idx]
        valueTwo = arrayTwo[jdx]
        # current = abs(valueOne - valueTwo)

        if valueOne < valueTwo:
            current = valueTwo - valueOne
            idx += 1
        elif valueOne > valueTwo:
            current = valueOne - valueTwo
            jdx += 1
        else:
            return [valueOne, valueTwo]

        if current < smallest:
            smallest = current
            smallestPair = [valueOne, valueTwo]

    return smallestPair

# Call the function
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
output = smallestDifference(arrayOne, arrayTwo)
print('👋 Output:', output)
# [28, 26]