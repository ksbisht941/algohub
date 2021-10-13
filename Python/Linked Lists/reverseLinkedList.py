# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Here is your solution
def reverseLinkedList(head):
   p1, p2 = None, head

   while p2 is not None:
     nextNode = p2.next
     p2.next = p1
     p1 = p2
     p2 = nextNode

   return p1

# Call the function
head = {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": None, "value": 5}
    ]
  }
  
output = reverseLinkedList(head)
print('👋 Output:', output)
# 0 -> 1 -> 2 -> 3 -> 4 -> 5
# 5 -> 4 -> 3 -> 2 -> 1 -> 0