export function insertionSort(array: number[]): number[] {
    for (let idx = 1; idx < array.length; idx++) {
        let jdx = idx;

        while (jdx > 0 && array[jdx] < array[jdx - 1]) {
            swap(array, jdx, jdx - 1);
            jdx -= 1;
        }
    }
    return array
}

function swap(array, idx, jdx) {
    const temp = array[idx];
    array[idx] = array[jdx];
    array[jdx] = temp;
}


const array = [8, 5, 2, 9, 5, 6, 3];
const output = insertionSort(array);
console.log("👋 Output", output);
