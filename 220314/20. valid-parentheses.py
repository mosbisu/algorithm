class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        opener = "({["
        stack = []

        for char in s:
            if char in opener:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pair[char] != top:
                    return False

        return not stack