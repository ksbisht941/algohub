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
    
    // O(1) time | O(1) space
    insertAtPosition(position: number, nodeToInsert: Node) {
        if (position === 1) {
            this.setHead(nodeToInsert);
            return;
        }

        let currentPosition = 1;
        let node = this.head;

        while (node !== null && currentPosition !== position) {
            node = node.next;
            currentPosition += 1
        }

        if (node !== null) {
            this.insertBefore(node, nodeToInsert);
        } else {
            this.setTail(nodeToInsert)
        }
    }

    // O(1) time | O(1) space
    removeNodesWithValue(value: number) {
        let node = this.head;

        while (node !== null) {
            if (node.value == value) {
                this.remove(node)
            }
            node = node.next
        }
    }

    remove(node: Node) {
        if (node === this.head) {
            this.head = this.head.next
        }
        if (node === this.tail) {
            this.tail = this.tail.prev
        }

        this.removeNodeBindings(node)
    }

    containsNodeWithValue(value: number) {
        let node = this.head;

        while (node !== null && node.value !== value) {
            node = node.next
        }

        return node !== null;
    }

    removeNodeBindings(node: Node) {
        if (node.prev !== null) {
            node.prev.next = node.next;
        }

        if (node.next !== null) {
            node.next.prev = node.prev
        }

        node.prev = null
        node.next = null
    }
}