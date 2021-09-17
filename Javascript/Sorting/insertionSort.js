function insertionSort(array) {
    for (var idx = 1; idx < array.length; idx++) {
        var jdx = idx;
        while (jdx > 0 && array[jdx] < array[jdx - 1]) {
            swap(array, jdx, jdx - 1);
            jdx -= 1;
        }
    }
    return array;
}

function swap(array, idx, jdx) {
    var temp = array[idx];
    array[idx] = array[jdx];
    array[jdx] = temp;
}
var array = [8, 5, 2, 9, 5, 6, 3];
var output = insertionSort(array);
console.log("👋 Output", output);
