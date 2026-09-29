class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operands = "+-*/"

        for token in tokens:
            if token not in operands:
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))
        
        a = stack[-1]
        return a