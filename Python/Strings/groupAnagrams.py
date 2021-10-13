def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        print(sortedWord)
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
output = groupAnagrams(words)
print("👋 Output:", output)