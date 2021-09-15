""" 
  👉 Write a function that takes in a positive integer numberOfTags and returns a list of all the valid strings that you can generate with that number of matched <div></div> tags.
  👉
"""

def generateDivTags(numberOfTags):
    generatedTags = []
    generateDivTagsHelper(numberOfTags, numberOfTags, "", generatedTags)
    return generatedTags

def generateDivTagsHelper(openingTagsNeeded, closingTagsNeeded, prefix, generatedTags):
    if openingTagsNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsHelper(openingTagsNeeded - 1, closingTagsNeeded, newPrefix, generatedTags)

    if openingTagsNeeded < closingTagsNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsHelper(openingTagsNeeded, closingTagsNeeded - 1, newPrefix, generatedTags)

    if closingTagsNeeded == 0:
        generatedTags.append(prefix)

numberOfTags = 3
output = generateDivTags(numberOfTags)
print("👋 Output:", output)