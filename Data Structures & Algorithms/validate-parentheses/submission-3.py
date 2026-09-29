class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == "(" or i=="[" or i=="{":
                stack.append(i)

            else:
                if not stack:
                    return False
                top = stack.pop()
                if top is None or top == "(" and i != ")" or top == "[" and i != "]" or top == "{" and i != "}":
                    return False
        
        return len(stack) == 0