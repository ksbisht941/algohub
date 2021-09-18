"use strict";
exports.__esModule = true;
exports.DoublyLinkedList = exports.Node = void 0;
// This is an input class. Do not edit.
var Node = /** @class */ (function () {
    function Node(value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
    return Node;
}());
exports.Node = Node;
// Feel free to add new properties and methods to the class.
var DoublyLinkedList = /** @class */ (function () {
    function DoublyLinkedList() {
        this.head = null;
        this.tail = null;
    }
    DoublyLinkedList.prototype.setHead = function (node) {
        // Write your code here.
    };
    DoublyLinkedList.prototype.setTail = function (node) {
        // Write your code here.
    };
    DoublyLinkedList.prototype.insertBefore = function (node, nodeToInsert) {
        // Write your code here.
    };
    DoublyLinkedList.prototype.insertAfter = function (node, nodeToInsert) {
        // Write your code here.
    };
    DoublyLinkedList.prototype.insertAtPosition = function (position, nodeToInsert) {
        // Write your code here.
    };
    DoublyLinkedList.prototype.removeNodesWithValue = function (value) {
        // Write your code here.
    };
    DoublyLinkedList.prototype.remove = function (node) {
        // Write your code here.
    };
    DoublyLinkedList.prototype.containsNodeWithValue = function (value) {
        // Write your code here.
        return false;
    };
    return DoublyLinkedList;
}());
exports.DoublyLinkedList = DoublyLinkedList;
