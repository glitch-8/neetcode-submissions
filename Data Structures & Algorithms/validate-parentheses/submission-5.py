class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False

        hashmap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = list()
        for i in range(len(s)):
            if s[i] in ['}', ']', ')']:
                # pop the element from the stack
                if not stack or hashmap[s[i]] != stack.pop():
                    return False

            else:
                stack.append(s[i])
        
        if stack:
            return False
        
        return True
