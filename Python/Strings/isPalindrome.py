# Palindrome Check
# Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

# A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

def isPalindrome(string):
	leftIdx = 0
	rightIdx = len(string) - 1
	
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]: return False

		leftIdx += 1
		rightIdx -= 1
			
    
	return True