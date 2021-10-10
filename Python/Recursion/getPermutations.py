# def getPermutations(array):
#     permutations = []
#     permutationsHelper(array, [], permutations)
#     return permutations

# def  permutationsHelper(array, currentPermutation, permutations):
#     if not len(array) and len(currentPermutation):
#         permutations.append(currentPermutation)
#     else:
#         for idx in range(len(array)):
#             newArray = array[:idx] + array[idx + 1 :]
#             newPermutation = currentPermutation + [array[idx]]
#             permutationsHelper(newArray, newPermutation, permutations)

def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations

def permutationsHelper(idx, array, permutations):
    if idx == len(array) - 1:
        permutations.append(array[:])
    else:
        for jdx in range(idx, len(array)):
            swap(idx, jdx, array)
            permutationsHelper(idx + 1, array, permutations)
            swap(idx, jdx, array)

def swap(idx, jdx, array):
    array[idx], array[jdx] = array[jdx], array[idx]

    
array = [1, 2, 3]
output = getPermutations(array)
print("👋 Output:", output)
