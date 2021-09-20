"use strict";
exports.__esModule = true;
exports.findSuccessor = exports.BinaryTree = void 0;
// This is an input class. Do not edit.
var BinaryTree = /** @class */ (function () {
    function BinaryTree(value) {
        this.value = value;
        this.left = null;
        this.right = null;
        this.parent = null;
    }
    return BinaryTree;
}());
exports.BinaryTree = BinaryTree;
function findSuccessor(tree, node) {
    var inOrderTraversal = getInOrderTraversal(tree);
    for (var idx = 0; idx < inOrderTraversal.length; idx++) {
        var currentNode = inOrderTraversal[idx];
        if (currentNode !== node)
            continue;
        if (idx === inOrderTraversal.length - 1)
            return null;
        return inOrderTraversal[idx + 1];
    }
}
exports.findSuccessor = findSuccessor;
function getInOrderTraversal(tree, order) {
    if (order === void 0) { order = []; }
    if (!tree) {
        return order;
    }
    getInOrderTraversal(tree.left, order);
    order.push(tree);
    getInOrderTraversal(tree.right, order);
    return order;
}
