"use strict";

function largestRange(array) {
  var nums = {};
  var bestRange = [-1, -1];
  var longestRange = 0;

  for (var _i = 0, array_1 = array; _i < array_1.length; _i++) {
    var num = array_1[_i];
    nums[num] = true;
  }

  for (var _a = 0, array_2 = array; _a < array_2.length; _a++) {
    var num = array_2[_a];

    if (!nums[num]) {
      continue;
    }

    nums[num] = false;
    var leftIdx = num - 1;
    var rightIdx = num + 1;
    var currentLength = 1;

    while (leftIdx in nums) {
      nums[leftIdx] = false;
      leftIdx--;
      currentLength++;
    }

    while (rightIdx in nums) {
      nums[rightIdx] = false;
      rightIdx++;
      currentLength++;
    }

    if (currentLength > longestRange) {
      longestRange = currentLength;
      bestRange = [leftIdx + 1, rightIdx - 1];
    }
  }

  return bestRange;
} // Here is output


var array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6];
var output = largestRange(array);
console.log("👋 Output:", output); // 👋 Output: [0, 7]