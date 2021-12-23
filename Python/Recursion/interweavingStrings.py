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