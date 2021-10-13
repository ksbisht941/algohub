# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for idx in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, idx - 1, idx + 1)
        even = getLongestPalindromeFrom(string, idx - 1, idx)
        longest = max(odd, even, key = lambda x:x[1] - x[0])
        currentLongest = max(currentLongest, longest, key = lambda x:x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1

    return [leftIdx + 1, rightIdx]

string = "abaxyzzyxf"
output = longestPalindromicSubstring(string)
print("👋 Output:", output)