# Min Rewards
# Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the final exam in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules:

# All students must receive at least one reward.
# Any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score.
# Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students to satisfy the two rules.

# You can assume that all students have different scores; in other words, the scores are all unique.

# Sample Input
# scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]


def minRewards(scores):
    rewards = [1 for _ in scores]
    
    for idx in range(1, len(scores) - 1):
        jdx = idx - 1
        if scores[idx] > scores[jdx]:
            rewards[idx] = rewards[jdx] + 1
        else:
            while jdx >= 0 and scores[jdx] > scores[jdx + 1]:
                rewards[jdx] = max(rewards[jdx], rewards[jdx + 1] + 1)
                jdx -= 1

    return sum(rewards)

         

scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
output = minRewards(scores)
print('👋 Output', output)

# Sample Output
# 25 // you would give out the following rewards: [4, 3, 2, 1, 2, 3, 4, 5, 1]

# 8 4 2 1 3 6 7 9 5
# 4 3 2 1 2 3 4 5 1
