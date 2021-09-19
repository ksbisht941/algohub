export function largestRange(array: number[]): [number, number] {
  const nums: {[key: number]: boolean} = {}
  let bestRange: [number, number] = [-1, -1];
  let longestRange: number = 0;

  for (const num of array) {
    nums[num] = true
  }

  for (const num of array) {
    if (!nums[num]) {
      continue;
    }

    nums[num] = false;

    let leftIdx = num - 1
    let rightIdx = num + 1
    let currentLength = 1

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
      bestRange = [leftIdx + 1, rightIdx - 1]
    }
  }

  return bestRange;
}

// Here is output
const array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
const output = largestRange(array)
console.log("👋 Output:", output)
// 👋 Output: [0, 7]