# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]
        
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(number, lastMinMax["min"])
            newMinMax["max"] = max(number, lastMinMax["max"])

        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

        return self.stack

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]

MinMaxStack().push(2)
MinMaxStack().push(4)
output = MinMaxStack().push(6)
print("👋 Output:", output)