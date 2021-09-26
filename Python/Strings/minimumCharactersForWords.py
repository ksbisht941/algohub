# O(n * l) time | O(c) space - where n is the number of words,
# l is the length of the longest word, and c is the number of
# unique characters across all words
def minimumCharactersForWords(words):
    maximumCharacterFrequencies = {}

    for word in words:
        characterFrequencies = countCharacterFrequency(word)
        updateMaximumFrequency(characterFrequencies, maximumCharacterFrequencies)

    return makeArrayFromMaximumFrequency(maximumCharacterFrequencies)

def countCharacterFrequency(word):
    characterFreqency = {}
    for character in word:
        if character not in characterFreqency:
            characterFreqency[character] = 0
        
        characterFreqency[character] += 1

    return characterFreqency

def updateMaximumFrequency(frequencies, maximumFrequencies):
    for character in frequencies:
        frequency = frequencies[character]

        if character in maximumFrequencies:
            maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
        else:
            maximumFrequencies[character] = frequency

def makeArrayFromMaximumFrequency(maximumCharacterFrequencies):
    characters = []

    for character in maximumCharacterFrequencies:
        frequency = maximumCharacterFrequencies[character]

        for _ in range(frequency):
            characters.append(character)

    return characters

words = ["this", "that", "did", "deed", "them!", "a"]
output = minimumCharactersForWords(words)
print("👋 Output", output)
# 👋 Output ['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']