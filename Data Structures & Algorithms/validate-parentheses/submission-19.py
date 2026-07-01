class Solution:
    def isValid(self, s: str) -> bool:
        validMatches = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in validMatches:
                if stack and validMatches[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        return False