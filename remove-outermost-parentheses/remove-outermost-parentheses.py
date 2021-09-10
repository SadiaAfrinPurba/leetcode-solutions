class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ''
        for char in s:
            if char == '(':
                if stack:
                    ans += char
                stack.append(char)
                     
            else:
                stack.pop()
                if stack:
                    ans+= char
                    
        return ans
