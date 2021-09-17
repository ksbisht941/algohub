// Here is your solution
// O(nLog(n))| O(1)
export function twoNumberSum(array: number[], targetSum: number) {
    array.sort((a, b) => (a - b));
    let left = 0;
    let right = array.length - 1;

    while (left < right) {
        const potentialSum = array[left] + array[right]

        if (potentialSum > targetSum) {
            right--;
        } else if (potentialSum < targetSum) {
            left++;
        } else {
            return [array[left], array[right]]
        }
    }

    return [-1, -1];
}


// Call the function
const array: number[] = [3, 5, -4, 8, 11, 1, -1, 6]
const targetSum: number = 10
const output = twoNumberSum(array, targetSum)
console.log("👋 Output:", output)