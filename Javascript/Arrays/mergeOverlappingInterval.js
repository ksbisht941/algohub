function mergeOverlappingIntervals(interval) {
  var sortedInterval = interval.sort((a, b) => (a[0] - b[0]));
  var mergeIntervals = [];
  var currentInterval = sortedInterval[0];
  mergeIntervals.push(currentInterval);

  for (const nextInterval of sortedInterval) {
    const [_, currentIntervalEnd] = currentInterval;
    const [nextIntervalStart, nextIntervalEnd] = nextInterval;

    if (currentIntervalEnd >= nextIntervalStart) {
      currentInterval[1] = nextIntervalEnd;
    } else {
      currentInterval = nextInterval;
      mergeIntervals.push(currentInterval);
    }
  }
  return mergeIntervals;
}

// Call the function
var intervals = [
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10],
];
var output = mergeOverlappingIntervals(intervals);
console.log("👋 Output", output);
//  [[1, 2], [3, 8], [9, 10]]
