# Here is your solution
# Solution 1
# O(v + e) time | O(v) space
# def cycleInGraph(edges):
#     numberOfEdges = len(edges)
#     visited = [False for _ in range(numberOfEdges)]
#     currentlyInstack = [False for _ in range(numberOfEdges)]

#     for node in range(numberOfEdges):
#         if visited[node]:
#             continue

#         containsCycle = isNodeInCycle(edges, node, visited, currentlyInstack)
#         if containsCycle:
#             return True

#     return False

# def isNodeInCycle(edges, node, visited, currentlyInStack):
#     visited[node] = True
#     currentlyInStack[node] = True

#     neighbors = edges[node]

#     for neighbor in neighbors:
#         if not visited[neighbor]:
#             containsCycle = isNodeInCycle(edges, neighbor, visited, currentlyInStack)

#             if containsCycle:
#                 return True

#         elif currentlyInStack[neighbor]:
#             return True

#     currentlyInStack[node] = False
#     return False

# Solution 2
# O(v + e) time | O(v) space
WHITE, GREY, BLACK = 0, 1, 2
def cycleInGraph(edges):
    
    return False

edges = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
output = cycleInGraph(edges)
print("👋 Output:", output)