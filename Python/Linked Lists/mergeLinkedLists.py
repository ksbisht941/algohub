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
            