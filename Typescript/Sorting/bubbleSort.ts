export function bubbleSort(array: number[]): number[] {
    let isSorted: boolean = false;

    while (!isSorted) {
        isSorted = true;

        for (let idx = 1; idx < array.length; idx++) {
            if (array[idx] < array[idx - 1]) {
                swap(array, idx, idx - 1);
                isSorted = false
            }
        }
    }
    return array;
}

function swap(array: number[], idx: number, jdx: number): void {
    const temp = array[idx];
    array[idx] = array[jdx];
    array[jdx] = temp
}

let array = [3, 5, 1, 9, 10];
const output = bubbleSort(array);
console.log("👋 Output:", output);
