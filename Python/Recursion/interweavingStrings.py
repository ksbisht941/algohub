# Interweaving Strings
# Write a function that takes in three strings and returns a boolean representing whether the third string can be formed by interweaving the first two strings.

# To interweave strings means to merge them by alternating their letters without any specific pattern. For instance, the strings "abc" and "123" can be interwoven as "a1b2c3", as "abc123", and as "ab1c23" (this list is nonexhaustive).

# Letters within a string must maintain their relative ordering in the interwoven string.

# O(2^(n + m)) time | O(n + m) space 
# def interweavingStrings(one, two, three):
#     if len(three) != len(one) + len(two):
#         return False
#     return areInterwoven(one, two, three, 0, 0)

# def areInterwoven(one, two, three, i, j):
#     k = i + j
#     if k == len(three):
#         return True
    
#     if i < len(one) and one[i] == three[k]:
#         if areInterwoven(one, two, three, i + 1, j):
#             return True

#     if j < len(two) and two[j] == three[k]:
#          return areInterwoven(one, two, three, i, j + 1)

#     return False
    
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    
    
    return areInterwoven(one, two, three, 0, 0)

def areInterwoven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]
        
    k = i + j
    if k == len(three):
        return True
    
    if i < len(one) and one[i] == three[k]:
        if areInterwoven(one, two, three, i + 1, j):
            return True

    if j < len(two) and two[j] == three[k]:
         return areInterwoven(one, two, three, i, j + 1)

    return False
    



one = "algohub"
two = "your-dream-job"
three = "your-algodream-expertjob"
output = interweavingStrings(one, two, three)
print("👋 Output:", output)