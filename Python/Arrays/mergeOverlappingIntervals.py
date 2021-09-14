# Here is your solution
# O(nLog(n)) time | O(n) space
def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    # print(sortedIntervals)

    mergeIntervals = []
    currentInterval = sortedIntervals[0]
    mergeIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            print(currentInterval)
            mergeIntervals.append(currentInterval)

    return mergeIntervals

# Call the function
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
output = mergeOverlappingIntervals(intervals)
print("👋 Output", output)
# [[1, 2], [3, 8], [9, 10]]