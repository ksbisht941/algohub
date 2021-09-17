export function maxSubsetSumNoAdjacent(array: number[]): number {
    if (!array.length) {
        return 0
    } else if (array.length == 1) {
        return array[0]
    }

    let second = array[0]
    let first = Math.max(array[0], array[1]);

    for (let idx = 2; idx < array.length; idx++) {
        const current = Math.max(first, second + array[idx])
        second = first;
        first = current
    }

    return first
}

const array = [30, 25, 50, 55, 100, 120]
const output = maxSubsetSumNoAdjacent(array)
console.log("👋 Output", output)

// 7, 10, 12, 7, 9, 14
// 7, 10, 19, 19, 

 
// FORMULA 
// maxSum[i] = max(maxSum[i - 1], maxSum[i - 2] + array[i])
