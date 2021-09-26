# Here is your solution
def minimumAreaRectangle(points):
    columns = initializeColumns(points)
    minimumAreaFound = float('inf')
    edgesParallerToYAxis = {}

    sortedColumns = sorted(columns.keys())
    for x in sortedColumns:
        yValuesInCurrentColumn = columns[x]
        yValuesInCurrentColumn.sort()

        for currentIdx, y2 in enumerate(yValuesInCurrentColumn):
            for previousIdx in range(currentIdx):
                y1 = yValuesInCurrentColumn[previousIdx]
                pointString = str(y1) + ':' + str(y2)

                if pointString in edgesParallerToYAxis:
                    currentArea = (x - edgesParallerToYAxis[pointString]) * (y2 - y1)
                    minimumAreaFound = min(minimumAreaFound, currentArea)

                edgesParallerToYAxis[pointString] = x

    return minimumAreaFound if minimumAreaFound != float("inf") else 0

def initializeColumns(points):
    columns = {}
    for point in points:
        x, y = point
        if x not in columns:
            columns[x] = []

        columns[x].append(y)

    return columns


# Call the function
points = [
    [1, 5],
    [5, 1],
    [4, 2],
    [2, 4],
    [2, 2],
    [1, 2],
    [4, 5],
    [2, 5],
    [-1, -2]
  ]
output = minimumAreaRectangle(points)
print("👋 Output:", output)