# Powerset
# Write a function that takes in an array of unique integers and returns its powerset.

# The powerset P(X) of a set X is the set of all subsets of X. For example, the powerset of [1,2] is [[], [1], [2], [1,2]].

# Note that the sets in the powerset do not need to be in any particular order.

def powerset(array):
    subsets = [[]]
    for ele in array:
        for idx in range(len(subsets)):
            currentSubset = subsets[idx]
            subsets.append(currentSubset + [ele])
    return subsets

# def powerset(array, idx = None):
#     if idx is None:
#         idx = len(array) - 1
#     elif idx < 0:
#         return [[]]
#     ele = array[idx]
#     print(ele)
#     subsets = powerset(array, idx - 1)

#     for idx in range(len(subsets)):
#         currentSubset = subsets[idx]
#         subsets.append(currentSubset + [ele])

#     return subsets

array = [1, 2, 3]
output = powerset(array)
print("👋 Output:", output)
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]