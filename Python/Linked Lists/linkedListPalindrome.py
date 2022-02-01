# Linked List Palindrome
# Write a function that takes in the head of a Singly Linked List and returns a boolean representing whether the linked list's nodes form a palindrome. Your function shouldn't make use of any auxiliary data structure.

# A palindrome is usually defined as a string that's written the same forward and backward. For a linked list's nodes to form a palindrome, their values must be the same when read from left to right and from right to left. Note that single-character strings are palindromes, which means that single-node linked lists form palindromes.

# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

# You can assume that the input linked list will always have at least one node; in other words, the head will never be None / null.

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    slowLinkedList = head
    fastLinkedList = head
    while fastLinkedList is not None and fastLinkedList.next is not None:
        slowLinkedList = slowLinkedList.next
        fastLinkedList = fastLinkedList.next.next

    firstHalfHead = head
    reversedSecondHalfHead = reversedLinkedList(slowLinkedList)

    while reversedSecondHalfHead is not None:
        if firstHalfHead.value != reversedSecondHalfHead.value:
            return False
        		
        reversedSecondHalfHead = reversedSecondHalfHead.next
        firstHalfHead = firstHalfHead.next

    return True

def reversedLinkedList(linkedList):
    previousNode, currentNode = None, linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode

# Sample Input
# head = 0 -> 1 -> 2 -> 2 -> 1 -> 0 // the head node with value 0

# Sample Output
# true