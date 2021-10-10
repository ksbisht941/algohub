# Here is your solution
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reversePositionInPlace(redShirtSpeeds)
    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
        totalSpeed += max(rider1, rider2)
    return totalSpeed

def reversePositionInPlace(array):
    start = 0
    end = len(array) - 1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array

# Call the function
redShirtSpeeds =  [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True

output = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
print('👋 Output:', output)