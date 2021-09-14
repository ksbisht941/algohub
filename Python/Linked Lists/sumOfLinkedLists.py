# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Here is your solution
# Solution 1 
def sumOfLinkedLists(linkedListOne, linkedListTwo):
  
  newLinkedListHeaderPointer = LinkedList(0)
  currentNode = newLinkedListHeaderPointer
  carry = 0

  nodeOne = linkedListOne
  nodeTwo = linkedListTwo

  print(nodeOne)

  while nodeOne is not None or nodeTwo is not None or carry != 0:
    valueOne = nodeOne.value if nodeOne is not None else 0
    valueTwo = nodeTwo.value if nodeTwo is not None else 0
    sumOfValue = valueOne + valueTwo + carry

    newValue = sumOfValue % 10
    newNode = LinkedList(newValue)
    currentNode.next = newNode
    currentNode = newNode

    carry = sumOfValue // 10
    nodeOne = nodeOne.next if nodeOne is not None else None
    nodeTwo = nodeTwo.next if nodeTwo is not None else None

  return newLinkedListHeaderPointer.next




# Call the function
linkedListOne = {
    "head": "2",
    "nodes": [
      {"id": "2", "next": "4", "value": 2},
      {"id": "4", "next": "7", "value": 4},
      {"id": "7", "next": "1", "value": 7},
      {"id": "1", "next": None, "value": 1}
    ]
  }

linkedListTwo = {
    "head": "9",
    "nodes": [
      {"id": "9", "next": "4", "value": 9},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": None, "value": 5}
    ]
  }

output = sumOfLinkedLists(linkedListOne, linkedListTwo)
print('👋 Output:', output)

# {
#   "head": "1",
#   "nodes": [
#     {"id": "1", "next": "9", "value": 1},
#     {"id": "9", "next": "2", "value": 9},
#     {"id": "2", "next": "2-2", "value": 2},
#     {"id": "2-2", "next": null, "value": 2}
#   ]
# }