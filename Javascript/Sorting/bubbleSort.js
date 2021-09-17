"use strict";

function bubbleSort(array) {
    var isSorted = false;
    while (!isSorted) {
        isSorted = true;
        for (var idx = 1; idx < array.length; idx++) {
            if (array[idx] < array[idx - 1]) {
                swap(array, idx, idx - 1);
                isSorted = false;
            }
        }
    }
    return array9;
}

function swap(array, idx, jdx) {
    var temp = array[idx];
    array[idx] = array[jdx];
    array[jdx] = temp;
}

var array = [3, 5, 1, 9, 10];
var output = bubbleSort(array);
console.log("👋 Output:", output);
