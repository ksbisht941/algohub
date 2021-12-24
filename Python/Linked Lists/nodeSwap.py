# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    if head is None or head.next is None:
        return head

    nextNode = head.next # 1 -> 3 -> 5
    head.next = nodeSwap(head.next.next) # None -> 5 -> 3 -> 1 
    nextNode.next = head # 4 -> 2 -> 0
    return nextNode
