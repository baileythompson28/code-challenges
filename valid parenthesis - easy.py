# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type

def valid_parentheses(s):
    stack = []
    bracket = {')': '(', '}': '{', ']': '['}
    open_bracket = set(bracket.values())

    for char in s:
        if char in open_bracket:
            stack.append(char)
        elif char in bracket:
            if not stack or stack[-1] != bracket[char]:
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    string = input("Enter string of parentheses: ")
    if valid_parentheses(string):
        print(f"'{string}' is valid.")
    else:
        print(f"'{string}' is invalid.")