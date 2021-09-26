# Here is your solution
# SOLUTION 1
# O(n) time | O(n) space - where n is the length of the input array
# def sunsetViews(buildings, direction):
#     buildingsWithSunsetViews = []

#     startIdx = 0 if direction == 'WEST' else len(buildings) - 1
#     step = 1 if direction == 'WEST' else -1

#     idx = startIdx
#     runningMaxHeight = 0

#     while idx >= 0 and idx < len(buildings):
#         buildingHeight = buildings[idx]

#         if buildingHeight > runningMaxHeight:
#             buildingsWithSunsetViews.append(idx)

#         runningMaxHeight = max(runningMaxHeight, buildingHeight)

#         idx += step

#     if direction == 'EAST':
#         return buildingsWithSunsetViews[::-1]
    
#     return buildingsWithSunsetViews



# SOLUTION 2
# O(n) time | O(n) space - where n is the length of the input array
def sunsetViews(buildings, direction):
    candidateBuildings = []

    startIdx = 0 if direction == 'EAST' else len(buildings) - 1
    step = 1 if direction == 'EAST' else -1
    idx = startIdx
    # runningMaxHeightBuilding = 0
 
    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]

        while len(candidateBuildings) > 0 and buildings[candidateBuildings[-1]] <= buildingHeight:
            print(candidateBuildings[-1])
            candidateBuildings.pop()
        
        candidateBuildings.append(idx)

        idx += step

    if direction == 'WEST':
        return candidateBuildings[::-1]
    
    return candidateBuildings


# Call the function
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = 'WEST'

output = sunsetViews(buildings, direction)
print('👋 Output', output)


#     _
#    | |_ _
#   _| | | |_   _
#  | | | | | | | |_
#  | | | | | |_| | |
# _|_|_|_|_|_|_|_|_|_
