class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for character in s:
            if character == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif character == "]":
                if not stack or stack.pop() != "[":
                    return False
            elif character == ")":
                if not stack or stack.pop() != "(":
                    return False
            else:
                stack.append(character)
        
        if not stack:
            return True
        else:
            return False