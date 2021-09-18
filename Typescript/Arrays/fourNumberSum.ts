interface Pairs {
    [key: number]: [number, number][];
}

export function fourNumberSum(array: number[], targetSum: number) {
    const allPairSums: Pairs = {}
    let quadruplets: number[][] = []

    for (let idx = 1; idx < array.length - 1; idx++) {
        for (let jdx = idx + 1; jdx < array.length; jdx++) {
            const currentSum = array[idx] + array[jdx];
            const difference = targetSum - currentSum;

            if (difference in allPairSums) {
                for (const pair of allPairSums[difference]) {
                    quadruplets.push(pair.concat([array[idx], array[jdx]]));
                }
            }
        }

        for (let kdx = 0; kdx < idx; kdx++) {
            const currentSum = array[idx] + array[kdx];

            if (!(currentSum in allPairSums)) {
                allPairSums[currentSum] = [[array[idx], array[kdx]]]
            } else {
                allPairSums[currentSum].push([array[idx], array[kdx]])
            }
        }
    }
    return quadruplets;
}



// Call the function
const array = [7, 6, 4, -1, 1, 2]
const targetSum = 16
const output = fourNumberSum(array, targetSum)
console.log("👋 Output:", output)