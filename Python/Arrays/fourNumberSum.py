def fourNumberSum(array, targetSum):
    allPairsSums = {}
    quadruplets = []

    for idx in range(1, len(array) - 1):
        for jdx in range(idx + 1, len(array)):
            currentSum = array[idx] + array[jdx]
            difference = targetSum - currentSum
            
            if difference in allPairsSums:
                for pair in allPairsSums[difference]:
                    quadruplets.append(pair + [array[idx], array[jdx]])

        for kdx in range(0, idx):
            currentSum = array[idx] + array[kdx]
            if currentSum not in allPairsSums:
                allPairsSums[currentSum] = [[array[kdx], array[idx]]]
            else:
                allPairsSums[currentSum].append([array[kdx], array[idx]])

    return quadruplets


# Call the function
array = [7, 6, 4, -1, 1, 2]
targetSum = 16
output = fourNumberSum(array, targetSum)
print("👋 Output:", output)