# Node Swap
# Write a function that takes in the head of a Singly Linked List, swaps every pair of adjacent nodes in place (i.e., doesn't create a brand new list), and returns its new head.

# If the input Linked List has an odd number of nodes, its final node should remain the same.

# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

# You can assume that the input Linked List will always have at least one node; in other words, the head will never be None / null.

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    if head is None or head.next is None:
        return head

    nextNode = head.next
    head.next = nodeSwap(head.next.next)
    nextNode.next = head

    return nextNode

# 0 -> 1 -> 2 -> 3 -> 4 -> 5
# 1 -> 0 -> 3 -> 2 -> 5 -> 4