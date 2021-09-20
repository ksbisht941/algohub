"use strict";

exports.__esModule = true;
exports.reverseLinkedList = exports.LinkedList = void 0; // This is an input class. Do not edit.

var LinkedList =
/** @class */
function () {
  function LinkedList(value) {
    this.value = value;
    this.next = null;
  }

  return LinkedList;
}();

exports.LinkedList = LinkedList;

function reverseLinkedList(head) {
  var previousNode = null;
  var currentNode = head;

  while (currentNode !== null) {
    var nextNode = currentNode.next;
    currentNode.next = previousNode;
    previousNode = currentNode;
    currentNode = nextNode;
  }

  return previousNode;
}

exports.reverseLinkedList = reverseLinkedList;