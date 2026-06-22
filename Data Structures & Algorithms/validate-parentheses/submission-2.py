class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validAppends = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in validAppends:
                if stack and stack[-1] == validAppends[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        return True