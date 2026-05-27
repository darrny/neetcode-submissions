class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            
            if c == ')':
                if len(stack) == 0:
                    return False
                if stack.pop() != '(':
                    return False

            elif c == ']':
                if len(stack) == 0:
                    return False
                if stack.pop() != '[':
                    return False

            elif c == '}':
                if len(stack) == 0:
                    return False
                if stack.pop() != '{':
                    return False

            else:
                stack.append(c)

        if len(stack) != 0:
            return False

        return True