class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        result = 0
        for t in tokens:
            if t == '+':
                one = int(stack.pop())
                two = int(stack.pop())
                result = one + two
                str(stack.append(result))
            elif t == '-':
                one = int(stack.pop())
                two = int(stack.pop())
                result = two - one
                str(stack.append(result))
            elif t == '*':
                one = int(stack.pop())
                two = int(stack.pop())
                result = one * two
                str(stack.append(result))
            elif t == '/':
                one = float(stack.pop())
                two = float(stack.pop())
                result = two / one
                str(stack.append(result))
            else:
                stack.append(t)

        return int(result)