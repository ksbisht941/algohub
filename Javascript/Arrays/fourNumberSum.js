function fourNumberSum(array, targetSum) {
  var allPairSums = {};
  var quadruplets = [];
  for (var idx = 1; idx < array.length - 1; idx++) {
    for (var jdx = idx + 1; jdx < array.length; jdx++) {
      var currentSum = array[idx] + array[jdx];
      var difference = targetSum - currentSum;
      if (difference in allPairSums) {
        for (const pair of allPairSums[difference]) {
          quadruplets.push(pair.concat([array[idx], array[jdx]]));
        }
      }
    }
    for (var kdx = 0; kdx < idx; kdx++) {
      var currentSum = array[idx] + array[kdx];
      if (!(currentSum in allPairSums)) {
        allPairSums[currentSum] = [[array[idx], array[kdx]]];
      } else {
        allPairSums[currentSum].push([array[idx], array[kdx]]);
      }
    }
  }
  return quadruplets;
}


// Call the function
var array = [7, 6, 4, -1, 1, 2];
var targetSum = 16;
var output = fourNumberSum(array, targetSum);
console.log("👋 Output:", output);
