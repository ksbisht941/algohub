export function mergeOverlappingIntervals(interval: number[][]) {
    const sortedInterval: number[][] = interval.sort((a, b) => a[0] - b[0]);
    const mergeIntervals: number[][] = []
    let currentInterval: number[] = sortedInterval[0];
    mergeIntervals.push(currentInterval);

    for (const nextInterval of sortedInterval) {
        const [_, currentIntervalEnd] = currentInterval;
        const [nextIntervalStart, nextIntervalEnd] = nextInterval;

        if (currentIntervalEnd >= nextIntervalStart) {
            currentInterval[1] = Math.max(nextIntervalEnd, currentIntervalEnd)
        } else {
            currentInterval = nextInterval;
            mergeIntervals.push(currentInterval);
        }
    }

    return mergeIntervals;
}

// Call the function
let intervals: number[][] = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
const output: number[][] = mergeOverlappingIntervals(intervals)
console.log("👋 Output", output);
//  [[1, 2], [3, 8], [9, 10]]