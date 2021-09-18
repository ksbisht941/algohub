// This is an input class. Do not edit.
export class Node {
    value: number;
    prev: Node | null;
    next: Node | null;

    constructor(value: number) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

// Feel free to add new properties and methods to the class.
export class DoublyLinkedList {
    head: Node | null;
    tail: Node | null;

    constructor() {
        this.head = null;
        this.tail = null;
    }

    // O(1) time | O(1) space
    setHead(node: Node) {
        if (this.head === null) {
            this.head = node;
            this.tail = node;
            return
        }

        this.insertBefore(this.head, node)
    }

    // O(1) time | O(1) space
    setTail(node: Node) {
        if (this.tail === null) {
            this.setHead(node)
        }

        this.insertAfter(this.tail, node);
    }

    // O(1) time | O(1) space
    insertBefore(node: Node, nodeToInsert: Node) {
        // 10 -> 30 -> 40 -> 50 -> 70
        // node -> 50
        // nodeToInsert -> 40
        // node.next -> 70 and node.prev -> 30
        // nodeToInsert.next -> 50 and nodeToInsert.prev -> 30

        if (nodeToInsert == this.head && nodeToInsert == this.tail) {
            return
        }

        this.remove(nodeToInsert);

        nodeToInsert.prev = node.prev;
        nodeToInsert.next = node;

        if (node.prev === null) {
            this.head = nodeToInsert
        } else {
            node.prev.next = nodeToInsert
        }

        node.prev = nodeToInsert
    }

    // O(1) time | O(1) space
    insertAfter(node: Node, nodeToInsert: Node) {
        // 10 -> 30 -> 40 -> 50 -> 70

        // node -> 40
        // nodeToInsert -> 50

        // node.next -> 70 and node.prev = 30
        // nodeToInsert.next -> 70 and nodeToInsert.prev -> 40

        if (nodeToInsert == this.head && nodeToInsert == this.tail) {
            return;
        }

        this.remove(nodeToInsert);

        nodeToInsert.prev = node;
        nodeToInsert.next = node.next;

        if (node.next === null) {
            this.tail = nodeToInsert
        } else {
            node.next.prev = nodeToInsert
        }

        node.next = nodeToInsert;



    }

    insertAtPosition(position: number, nodeToInsert: Node) {
        // Write your code here.
    }

    removeNodesWithValue(value: number) {
        // Write your code here.
    }

    remove(node: Node) {
        // Write your code here.
    }

    containsNodeWithValue(value: number) {
        // Write your code here.
        return false;
    }
}