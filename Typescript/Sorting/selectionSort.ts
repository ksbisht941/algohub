export function selectionSort(array: number[]):number[] {
    let currentIdx = 0;

    while (currentIdx < array.length - 1) {
       let smallestIdx = currentIdx;

       for (let idx = currentIdx + 1; idx < array.length; idx++) {
           if (array[smallestIdx] > array[idx]) {
               smallestIdx = idx;
           }
        }

        swap(array, currentIdx, smallestIdx);
        currentIdx += 1;
    }
    return array;
}

function swap(array, idx, jdx) {
    const temp = array[idx];
    array[idx] = array[jdx];
    array[jdx] = temp;
}


const array = [8, 5, 2, 9, 5, 6, 3];
const output = selectionSort(array);
console.log("👋 Output", output);