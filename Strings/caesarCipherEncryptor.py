# Here is your solution
# SOLUTION 1 
# O(n) time | O(n) space
# def caesarCipherEncryptor(string, key):
#     newLetters = []
#     newKey = key % 26
#     for letter in string:
#         newLetters.append(getNewLetters(letter, newKey))
#     return "".join(newLetters)

# def getNewLetters(letter, newKey):
#     newLetterCode = ord(letter) + key
#     return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

# SOLUTION 2
# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetters(letter, newKey, alphabet))
    return "".join(newLetters)

def getNewLetters(letter, newKey, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode % 26]

# Call the function
string = 'xyz'
key = 2
output = caesarCipherEncryptor(string, key)
print('👋 Output:', output)
# [zab]