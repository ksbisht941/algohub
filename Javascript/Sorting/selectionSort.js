"use strict";
exports.__esModule = true;
exports.selectionSort = void 0;
function selectionSort(array) {
    var currentIdx = 0;
    while (currentIdx < array.length - 1) {
        var smallestIdx = currentIdx;
        for (var idx = currentIdx + 1; idx < array.length; idx++) {
            if (array[smallestIdx] > array[idx]) {
                smallestIdx = idx;
            }
        }
        swap(array, currentIdx, smallestIdx);
        currentIdx += 1;
    }
    return array;
}
exports.selectionSort = selectionSort;
function swap(array, idx, jdx) {
    var temp = array[idx];
    array[idx] = array[jdx];
    array[jdx] = temp;
}
var array = [8, 5, 2, 9, 5, 6, 3];
var output = selectionSort(array);
console.log("👋 Output", output);
