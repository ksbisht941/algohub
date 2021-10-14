def minRewards(scores):
    rewards = [1 for _ in scores]
    print(rewards)

    for idx in range(1, len(scores)):
        j = idx - 1
        if scores[idx] > scores[j]:
            rewards[idx] = rewards[j] + 1
        else:
            
         


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
minRewards(scores)