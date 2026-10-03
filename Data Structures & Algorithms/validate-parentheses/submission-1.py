class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching.values():  # opening bracket
                stack.append(char)
            elif char in matching:  # closing bracket
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                return False  # ký tự không hợp lệ
        
        return len(stack) == 0