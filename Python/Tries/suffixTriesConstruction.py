# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        for idx in range(len(string)):
            self.insertSubstringStartingAt(idx, string)

    def insertSubstringStartingAt(self, idx, string):
        node = self.root
        for jdx in range(idx, len(string)):
            letter = string[jdx]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

        node[self.endSymbol] = True

    # O(m) time | O(1) space - m is length of input string
    def contains(self, string):
        node = self.root

        for letter in string:
            if letter not in node:
                return False

            node = node[letter]

        return self.endSymbol in node

output = SuffixTrie("babc").populateSuffixTrieFrom
print(output)