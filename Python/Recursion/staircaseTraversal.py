def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps)

def numberOfWaysToTop(height, maxSteps):
    if height <= 1:
        return 1

    numberOfWays = 0

    for step in range(1, min(maxSteps, height) + 1):
        numberOfWays += numberOfWaysToTop(height - step, maxSteps)

    return numberOfWays

height = 4
maxSteps = 2
output = staircaseTraversal(height, maxSteps)
print("👋 Output:", output)