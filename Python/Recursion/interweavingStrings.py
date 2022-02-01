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
    
    cache = [[None for jdx in range(len(two) + 1)] for idx in range(len(one) + 1)]
    return areInterwoven(one, two, three, 0, 0, cache)

def areInterwoven(one, two, three, idx, jdx, cache):
    kdx = idx + jdx

    if kdx == len(three):
        cache[idx][jdx] = True
        return True
    
    if idx < len(one) and one[idx] == three[kdx]:
        cache[idx][jdx] = areInterwoven(one, two, three, idx + 1, jdx, cache)
        if cache[idx][jdx]:
            return True

    if jdx < len(two) and two[jdx] == three[kdx]:
        cache[idx][jdx] = areInterwoven(one, two, three, idx, jdx + 1, cache)
        return cache[idx][jdx]

    cache[idx][jdx] = False
    return False
    



one = "algohub"
two = "your-dream-job"
three = "your-algodream-expertjob"
output = interweavingStrings(one, two, three)
print("👋 Output:", output)