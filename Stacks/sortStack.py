# Here is your solution
def sortStack(stack):

    if len(stack) == 0:
        return stack

    top = stack.pop()

    print(top)

    sortStack(stack)

    insertInSortedOrder(stack, top)

    return stack

def insertInSortedOrder(stack, value):

    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return

    top = stack.pop()

    insertInSortedOrder(stack, value)

    stack.append(top)


# Call the function
input = [-5, 2, -2, 4, 3, 1]
output = sortStack(input)
print('👋 Output:', output)
# [-5, -2, 1, 2, 3, 4]