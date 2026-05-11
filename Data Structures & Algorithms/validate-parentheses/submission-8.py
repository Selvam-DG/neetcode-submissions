class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {']':'[', ')':'(', '}':'{'}

        stack = []

        for char in s:
            
            # closed parenthesis
            if char in parenthesis:
                if not stack or stack.pop() != parenthesis[char]:
                    return False

            # open parenthesis
            else:
                stack.append(char)
        
        return len(stack) == 0
        