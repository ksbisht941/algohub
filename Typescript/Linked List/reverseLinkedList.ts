// This is an input class. Do not edit.
export class LinkedList {
    value: number;
    next: LinkedList | null;

    constructor(value: number) {
        this.value = value;
        this.next = null;
    }
}

export function reverseLinkedList(head: LinkedList) {
    let previousNode: LinkedList | null = null;
    let currentNode: LinkedList | null = head;

    while (currentNode !== null) {
        const nextNode: LinkedList | null = currentNode.next;
        currentNode.next = previousNode;
        previousNode = currentNode;
        currentNode = nextNode;
    }
    return previousNode;
}
