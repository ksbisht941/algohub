# Zip Linked List
# You're given the head of a Singly Linked List of arbitrary length k. Write a function that zips the Linked List in place (i.e., doesn't create a brand new list) and returns its head.

# A Linked List is zipped if its nodes are in the following order, where k is the length of the Linked List:

# 1st node -> kth node -> 2nd node -> (k - 1)th node -> 3rd node -> (k - 2)th node -> ...
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

# You can assume that the input Linked List will always have at least one node; in other words, the head will never be None / null.

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList):
    if linkedList.next is None or linkedList.next.next is None:
        return linkedList

    firstHalfHead = linkedList
    secondHalfHead = splitLinkedList(linkedList)

    reverseSecondHalfHead = reverseLinkedList(secondHalfHead)

    return interweaveLinkedList(firstHalfHead, reverseSecondHalfHead)

def splitLinkedList(linkedList):
    pass

def reverseLinkedList(linkedList):
    pass

def interweaveLinkedList(linkedList1, linkedList2):
    pass

# Sample Input
# linkedList = 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 1 

# Sample Output
# 1 -> 6 -> 2 -> 5 -> 3 -> 4 // the head node with value 1