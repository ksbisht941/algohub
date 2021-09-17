class Program {
  class MinHeap {
    var heap = [Int]()

    init(array: [Int]) {
      var array = array
      heap = buildHeap(array: &array)
    }

    func buildHeap(array: inout [Int]) -> [Int] {
      // Write your code here.
      return []
    }

    func siftDown(currentIndex: inout Int, endIndex: inout Int, heap: inout [Int]) {
      // Write your code here.
    }

    func siftUp(currentIndex: inout Int, heap: inout [Int]) {
      // Write your code here.
    }

    func peek() -> Int {
      // Write your code here.
      return -1
    }

    func remove() -> Int {
      // Write your code here.
      return -1
    }

    func insert(value: Int) {
      // Write your code here.
    }
  }
}
