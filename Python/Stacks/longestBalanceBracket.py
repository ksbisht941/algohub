
# Solution 1
# O(n^3) time | O(n) space
# def longestBalancedSubstring(string):
#     maxLength = 0

#     for i in range(len(string)):
#         for j in range(i + 2, len(string) + 1, 2):
#             if isBalanced(string[i:j]):
#                 currentLength = j - i
#                 maxLength = max(maxLength, currentLength)

#     return maxLength

# def isBalanced(string):
#     openParensStack = []

#     for char in string:
#         if char == "(":
#             openParensStack.append("(")
#         elif len(openParensStack) > 0:
#             openParensStack.pop()
#         else:
#             return False

#     return len(openParensStack) == 0


# Solution 2
# O()

def longestBalancedSubstring(string):
    maxLength = 0
    idxStack = []
    idxStack.append(-1)

    for i in range(len(string)):
        if string[i] == "(":
            idxStack.append(i)
        else:
            idxStack.pop()

            if len(idxStack) == 0:
                idxStack.append(i)
            else:
                balancedSubstringStartIdx = idxStack[len(idxStack) - 1]
                currentLength = i - balancedSubstringStartIdx
                maxLength = max(currentLength, maxLength)

    return maxLength

string = "(())(("
output = longestBalancedSubstring(string)
print("👋 Output: ", output)