# Validate Subsequence
# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

# A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

# def isValidSubsequence(array, sequence):
#     idx = 0
# 	jdx = 0
	
# 	while idx < len(array) and jdx < len(sequence):
# 		if array[idx] == sequence[jdx]:
# 			jdx += 1
			
# 		idx += 1
	
# 	return jdx == len(sequence)


def isValidSubsequence(array, sequence):
	seqIdx = 0
	
	for value in array:
		if seqIdx == len(sequence):
			break;
		
		if sequence[seqIdx] == value:
			seqIdx += 1
			
	return seqIdx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
output = isValidSubsequence(array, sequence)
print('👋 Output', output)