class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", '')
        w = ''
        for l  in s:
            if l.isalnum():
                w += l.lower()
        if w == w[::-1]:
            return True
        return False