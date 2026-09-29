class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        string = "+-*/"
        stack = []

        for token in tokens:
            if token in string:

                if token == '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a+b)
                
                elif token == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a-b)
                
                elif token == "*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a*b)

                elif token == '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a/b))
                
                else:
                    print("Invalid")
            
            else:
                stack.append(int(token))
        
        return stack[-1]
