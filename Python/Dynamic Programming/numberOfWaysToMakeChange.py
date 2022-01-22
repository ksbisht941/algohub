# Number Of Ways To Make Change
# Given an array of distinct positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the number of ways to make change for that target amount using the given coin denominations.

# Note that an unlimited amount of coins is at your disposal.

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for _ in range(n + 1)]
    print(ways)
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]

n = 10
denoms = [1, 5, 10, 25]
output = numberOfWaysToMakeChange(n, denoms)
print('👋 Output:', output)