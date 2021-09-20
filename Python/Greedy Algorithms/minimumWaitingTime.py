def minimumWaitingTime(queries):
	queries.sort()
	
	totalWaitingTime = 0
	
	for idx, duration in enumerate(queries):
		remainQueriesLeft = len(queries) - (idx + 1)
		totalWaitingTime += remainQueriesLeft * duration

	return totalWaitingTime

queries = [3, 2, 1, 2, 6]
output = minimumWaitingTime(queries)
print("👋 Output:", output)
# 👋 Output: 17