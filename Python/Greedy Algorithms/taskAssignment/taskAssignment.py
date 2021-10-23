def taskAssignment(k, tasks):
    pairedTasks = []
    taskDurationToIndices = getTaskDurationToIndices(tasks)

    sortedTasks = sorted(tasks)

    for k in range(k):
        task1Duration = sortedTasks[k]
        task1DurationIndices = taskDurationToIndices[task1Duration]
        task1 = task1DurationIndices.pop()

        task2Idx = len(tasks) - 1 - k
        task2Duration = sortedTasks[task2Idx]
        task2DurationIndices = taskDurationToIndices[task2Duration]
        task2 = task2DurationIndices.pop()

        pairedTasks.append([task1, task2])

    return pairedTasks

def getTaskDurationToIndices(tasks):
    taskDurationToIndices = {}
     
    for idx, taskDuration in enumerate(tasks):
        if taskDuration in taskDurationToIndices:
            taskDurationToIndices[taskDuration].append(idx)
        else:
            taskDurationToIndices[taskDuration] = [idx]

    return taskDurationToIndices


k = 3
tasks = [1, 3, 5, 3, 1, 4]

output = taskAssignment(k, tasks)
print("👋 Output:", output)