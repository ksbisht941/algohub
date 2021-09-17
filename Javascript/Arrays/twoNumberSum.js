// Here is your solution
// O(nLog(n))| O(1)
function twoNumberSum(array, targetSum) {
    array.sort(function (a, b) { return (a - b); });
    var left = 0;
    var right = array.length - 1;
    while (left < right) {
        var potentialSum = array[left] + array[right];
        if (potentialSum > targetSum) {
            right--;
        }
        else if (potentialSum < targetSum) {
            left++;
        }
        else {
            return [array[left], array[right]];
        }
    }
    return [-1, -1];
}

// Call the function
var array = [3, 5, -4, 8, 11, 1, -1, 6];
var targetSum = 10;
var output = twoNumberSum(array, targetSum);
console.log("👋 Output:", output);
