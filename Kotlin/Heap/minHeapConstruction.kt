
// Do not edit the class below except for the buildHeap,
// siftDown, siftUp, peek, remove, and insert methods.
// Feel free to add new properties and methods to the class.
open class MinHeap(array: MutableList<Int>) {
    val heap = this.buildHeap(array)

    fun buildHeap(array: MutableList<Int>): MutableList<Int> {
        // Write your code here.
        return array
    }

    fun siftDown(currentIdx: Int, endIdx: Int, heap: MutableList<Int>) {
        // Write your code here.
    }

    fun siftUp(currentIdx: Int, heap: MutableList<Int>) {
        // Write your code here.
    }

    fun peek(): Int? {
        // Write your code here.
        return -1
    }

    fun remove(): Int? {
        // Write your code here.
        return -1
    }

    fun insert(value: Int) {
        // Write your code here.
    }
}
