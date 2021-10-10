# def powerset(array):
#     subsets = [[]]
#     for ele in array:
#         for idx in range(len(subsets)):
#             currentSubset = subsets[idx]
#             subsets.append(currentSubset + [ele])
#     return subsets

def powerset(array, idx = None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    print(ele)
    subsets = powerset(array, idx - 1)

    for idx in range(len(subsets)):
        currentSubset = subsets[idx]
        subsets.append(currentSubset + [ele])

    return subsets

array = [1, 2, 3]
output = powerset(array)
print("👋 Output:", output)