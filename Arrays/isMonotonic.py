def isMonotonic(array):
    isIncreasing = True
    isDecreasing = True
    
    for idx in range(1, len(array)):
        if array[idx] > array[idx - 1]:
            isDecreasing = False
		
        if array[idx] < array[idx - 1]:
            isIncreasing = False
	
    return isIncreasing or isDecreasing


array = []
output = isMonotonic(array)
print("👋 Output", output)