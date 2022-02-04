# Multi String Search
# Write a function that takes in a big string and an array of small strings, all of which are smaller in length than the big string. The function should return an array of booleans, where each boolean represents whether the small string at that index in the array of small strings is contained in the big string.

# Note that you can't use language-built-in string-matching methods.

# Solution 1
# O(bns) time | O(n) space
def multiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]

def isInBigString(bigString, smallString):
    for idx in range(len(bigString)):
        if idx + len(smallString) > len(bigString):
            break

        if isInBigStringHelper(bigString, smallString, idx):
            return True

    return False

def isInBigStringHelper(bigString, smallString, startIdx):
    leftBigIdx = startIdx
    rightBigIdx = startIdx + len(smallString) - 1
    leftSmallIdx = 0
    rightSmallIdx = len(smallString) - 1

    while (leftBigIdx < rightBigIdx):
        if (
            smallString[leftSmallIdx] != bigString[leftBigIdx] or
            smallString[rightSmallIdx] != bigString[rightBigIdx]
        ):
            return False

        leftBigIdx += 1
        rightBigIdx -= 1
        leftSmallIdx += 1
        rightSmallIdx -= 1
    
    return True



# Solution 2
# O(bns) time | O(n) space
# def multiStringSearch(bigString, smallStrings):
#     modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
#     return [modifiedSuffixTrie.contains(string) for string in smallStrings]

# class ModifiedSuffixTrie:
#     def __init__(self, string):
#         self.root = {}
#         self.populateModifiedSuffixTrieFrom(string)
    
#     def populateModifiedSuffixTrieFrom(self, string):
#         for idx in range(len(string)):
#             self.insertSubstringStartingAt(idx, string)

#     def insertSubstringStartingAt(self, idx, string):
#         node = self.root
#         for jdx in range(idx, len(string)):
#             letter = string[jdx]
#             if letter not in node:
#                 node[letter] = {}
#             node = node[letter]

#     def contains(self, string):
#         node = self.root
#         for letter in string:
#             if letter not in node:
#                 return False
#             node = node[letter]
#         return True



# Solution 3
# def multiStringSearch(bigString, smallStrings):
#     pass

bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]

output = multiStringSearch(bigString, smallStrings)
print('👋 Output', output)

# [true, false, true, true, false, true, false]