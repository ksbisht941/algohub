# Longest Balanced Substring
# Write a function that takes in a string made up of parentheses (( and )). The function should return an integer representing the length of the longest balanced substring with regards to parentheses.

# A string is said to be balanced if it has as many opening parentheses as it has closing parentheses and if no parenthesis is unmatched. Note that an opening parenthesis can't match a closing parenthesis that comes before it, and similarly, a closing parenthesis can't match an opening parenthesis that comes after it.

# Solution 1
# O(n) time | O(n) space - where n is the length of the input string
# def longestBalancedSubstring(string):
#     stack = []
#     stack.append(-1)
#     maxLength = 0
#     for idx in range(len(string)):
#         if string[idx] == '(':
#             stack.append(idx)
#         else:
#             stack.pop()
#             if len(stack) == 0:
#                 stack.append(idx)
#             else:
#                 balancedSubStringStartIdx = stack[-1]
#                 currentLength = idx - balancedSubStringStartIdx
#                 maxLength = max(maxLength, currentLength)
#     return maxLength


# Solution 2
# O(n^3) time | O(n) space - where n is the length of the input string
# def longestBalancedSubstring(string):
#     maxLength = 0
    
#     for idx in range(len(string)):
#         for jdx in range(idx + 2, len(string) + 1, 2):
#             if isBalanced(string[idx:jdx]):
#                 currentLength = jdx - 1
#                 maxLength = max(maxLength, currentLength)
				
#     return maxLength

# def isBalanced(string):
# 	openParenstack = []
	
# 	for char in string:
# 		if char == '(':
# 			openParenstack.append('(')
# 		elif len(openParenstack) > 0:
# 			openParenstack.pop()
# 		else:
# 			return False
		
# 	return len(openParenstack) == 0
			

# Solution 3
# O(n) time | O(1) space - where n is the length of the input string
# def longestBalancedSubstring(string):
#     maxLength = 0

#     openingCount = 0
#     closingCount = 0

#     for char in string:
#         if char == '(':
#             openingCount += 1
#         else:
#             closingCount += 1

#         if openingCount == closingCount:
#             maxLength = max(maxLength, closingCount * 2)
#         elif closingCount > openingCount:
#             openingCount = 0
#             closingCount = 0

#     for idx in reversed(range(len(string))):
#         char = string[idx]

#         if char == '(':
#             openingCount += 1
#         else:
#             closingCount += 1

#         if openingCount == closingCount:
#             maxLength = max(maxLength, closingCount * 2)
#         elif openingCount > closingCount:
#             openingCount = 0
#             closingCount = 0

#     return maxLength


# Solution 4
# O(n) time | O(n) space - where n is the length of the input string
def longestBalancedSubstring(string):
    return max(
       getLongestBalancedInDirection(string, True), 
       getLongestBalancedInDirection(string, False) 
    )

def getLongestBalancedInDirection(string, leftToRight):
    step = 1 if leftToRight else -1
    openingParen = '(' if leftToRight else ')'
    startIdx = 0 if leftToRight else len(string) - 1

    maxLength = 0

    openingCount = 0
    closingCount = 0
    idx = startIdx

    while idx >= 0 and idx < len(string):
        char = string[idx]

        if char == openingParen:
            openingCount += 1
        else:
            closingCount += 1

        if openingCount == closingCount:
            maxLength = max(maxLength, closingCount * 2)
        elif openingCount < closingCount:
            openingCount = 0
            closingCount = 0

        idx += step

    return maxLength
        
        

# Sample Input
string = "(()))("
output = longestBalancedSubstring(string)
print('👋 Output:', output)

# Sample Output
# 4 // The longest balanced substring is "(())".