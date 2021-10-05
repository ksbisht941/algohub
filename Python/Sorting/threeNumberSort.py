# def threeNumberSort(array, order):
#     valueCounts = [0, 0, 0]

#     for element in array:
#         orderIdx = order.index(element)
#         valueCounts[orderIdx] += 1

#     print(valueCounts)

#     for idx in range(3):
#         value = order[idx]
#         count = valueCounts[idx]

#         numElementsBefore = sum(valueCounts[:idx])
#         print(numElementsBefore)

#         for nth in range(count):
#             currentIdx = numElementsBefore + nth
#             array[currentIdx] = value

#     return array


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

output = threeNumberSort(array, order)
print("👋 Output:", output)