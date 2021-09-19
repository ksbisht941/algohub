// Here is your solution
export function subarraySort(array: number[]): number[] {
    let maxOutOfOrder = -Infinity;
    let minOutOfOrder = Infinity;

    for (let idx = 0; idx < array.length; idx++) {
        const num = array[idx];
        if (isOutOfOrder(idx, num, array)) {
            maxOutOfOrder = Math.max(maxOutOfOrder, num);
            minOutOfOrder = Math.min(minOutOfOrder, num);
        }
    }

    if (minOutOfOrder === Infinity) {
        return [-1, -1];
    }

    let leftOutOfOrderIdx = 0;
    while (minOutOfOrder >= array[leftOutOfOrderIdx]) {
        leftOutOfOrderIdx++;
    }

    let rightOutOfOrder = array.length - 1;
    while (maxOutOfOrder < array[rightOutOfOrder]) {
        rightOutOfOrder--;
    }

    return [leftOutOfOrderIdx, rightOutOfOrder]
}

function isOutOfOrder(idx: number, num: number, array: number[]): boolean {
    if (idx == 0) {
        return num > array[idx + 1];
    }

    if (idx == array.length - 1) {
        return num < array[array.length - 1];
    }

    return num < array[idx - 1] || num > array[idx + 1]
}

// Here is your Output
const array: number[] = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
const output = subarraySort(array)
console.log("👋 Output:", output);