// Here is your solution
function subarraySort(array) {
  var maxOutOfOrder = -Infinity;
  var minOutOfOrder = Infinity;
  for (var idx = 0; idx < array.length; idx++) {
    var num = array[idx];
    if (isOutOfOrder(idx, num, array)) {
      maxOutOfOrder = Math.max(maxOutOfOrder, num);
      minOutOfOrder = Math.min(minOutOfOrder, num);
    }
  }
  if (minOutOfOrder === Infinity) {
    return [-1, -1];
  }
  var leftOutOfOrderIdx = 0;
  while (minOutOfOrder >= array[leftOutOfOrderIdx]) {
    leftOutOfOrderIdx++;
  }
  var rightOutOfOrder = array.length - 1;
  while (maxOutOfOrder < array[rightOutOfOrder]) {
    rightOutOfOrder--;
  }
  return [leftOutOfOrderIdx, rightOutOfOrder];
}

function isOutOfOrder(idx, num, array) {
  if (idx == 0) {
    return num > array[idx + 1];
  }
  if (idx == array.length - 1) {
    return num < array[array.length - 1];
  }
  return num < array[idx - 1] || num > array[idx + 1];
}
// Here is your Output
var array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19];
var output = subarraySort(array);
console.log("👋 Output:", output);
