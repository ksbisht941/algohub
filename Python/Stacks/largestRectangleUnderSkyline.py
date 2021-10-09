# Solution 1
# O(n) time | O(1) space
# def largestRectangleUnderSkyline(buildings):
#     maxArea = 0

#     for pillarIdx in range(len(buildings)):
#         currentPillar = buildings[pillarIdx]

#         furthestLeft = pillarIdx
#         while furthestLeft > 0 and buildings[furthestLeft - 1] >= currentPillar:
#             furthestLeft -= 1

#         furthestRight = pillarIdx
#         while furthestRight < len(buildings) - 1 and buildings[furthestRight + 1] >= currentPillar:
#             furthestRight += 1

#         areaWithCurrentBuilding = (furthestRight - furthestLeft + 1) * currentPillar
#         maxArea = max(areaWithCurrentBuilding, maxArea)

#     return maxArea


# Solution 2
def largestRectangleUnderSkyline(buildings):
    maxArea = 0
    pillarIndices = []



    return maxArea


buildings = []
output = largestRectangleUnderSkyline(buildings)
print("👋 Output:", output)