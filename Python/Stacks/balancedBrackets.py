def balancedBrackets(string):
    openingBracket = "({["
    cloasingBracket = ")}]"
    matchingBracket = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    stack = []

    for char in string:
        if char in openingBracket:
            stack.append(char)
        elif char in cloasingBracket:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBracket[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0
 

string = "([])(){}(())()()"
output = balancedBrackets(string)
print("👋 Output:", output)