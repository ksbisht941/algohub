# Min Number Of Coins For Change
# Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the smallest number of coins needed to make change for (to sum up to) that target amount using the given coin denominations.

# Note that you have access to an unlimited amount of coins. In other words, if the denominations are [1, 5, 10], you have access to an unlimited amount of 1s, 5s, and 10s.

# If it's impossible to make change for the target amount, return -1.

def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float('inf') for _ in range(n + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)

    return numOfCoins[n] if numOfCoins[n] != float('inf') else -1

n = 7
denoms = [1, 5, 10]

output = minNumberOfCoinsForChange(n, denoms)
print("👋 Output", output)