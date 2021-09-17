function mergeOverlappingIntervals(interval) {
  var sortedInterval = interval.sort(function (a, b) {
    return a[0] - b[0];
  });
  var mergeIntervals = [];
  var currentInterval = sortedInterval[0];
  mergeIntervals.push(currentInterval);
  for (
    var _i = 0, sortedInterval_1 = sortedInterval;
    _i < sortedInterval_1.length;
    _i++
  ) {
    var nextInterval = sortedInterval_1[_i];
    var _ = currentInterval[0],
      currentIntervalEnd = currentInterval[1];
    var nextIntervalStart = nextInterval[0],
      nextIntervalEnd = nextInterval[1];
    if (currentIntervalEnd >= nextIntervalStart) {
      currentInterval[1] = Math.max(nextIntervalEnd, currentIntervalEnd);
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
