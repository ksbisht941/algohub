# Merge Linked Lists
# Write a function that takes in the heads of two Singly Linked Lists that are in sorted order, respectively. The function should merge the lists in place (i.e., it shouldn't create a brand new list) and return the head of the merged list; the merged list should be in sorted order.

# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

# You can assume that the input linked lists will always have at least one node; in other words, the heads will never be None / null.

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p1Prev = None
    p2 = headTwo

    while p1 is not None and p2 is not None:
         if p1.value < p2.value:
             p1Prev = p1
             p1 = p1.next
        else:
            

# headOne = 2 -> 6 -> 7 -> 8 # the head node with value 2
# headTwo = 1 -> 3 -> 4 -> 5 -> 9 -> 10 # the head node with value 1

# output = mergeLinkedLists(headOne, headTwo)
# print('👋 Output', output)