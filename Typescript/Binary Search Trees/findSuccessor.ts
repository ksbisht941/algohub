// This is an input class. Do not edit.
export class BinaryTree {
    value: number;
    left: BinaryTree | null;
    right: BinaryTree | null;
    parent: BinaryTree | null;

    constructor(value: number) {
        this.value = value;
        this.left = null;
        this.right = null;
        this.parent = null;
    }
}

export function findSuccessor(tree: BinaryTree, node: BinaryTree) {
    const inOrderTraversal = getInOrderTraversal(tree);

    for (let idx = 0; idx < inOrderTraversal.length; idx++) {
        const currentNode = inOrderTraversal[idx];

        if (currentNode !== node) continue;
        if (idx === inOrderTraversal.length - 1) return null;
        return inOrderTraversal[idx + 1]
    }
}

function getInOrderTraversal(tree: BinaryTree | null, order: BinaryTree[] = []) {
    if (!tree) {
        return order;
    }

    getInOrderTraversal(tree.left, order);
    order.push(tree);
    getInOrderTraversal(tree.right, order);

    return order;
}