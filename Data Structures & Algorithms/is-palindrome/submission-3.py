class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''s = s.replace(" ", '')
        w = ''
        for l  in s:
            if l.isalnum():
                w += l.lower()
        if w == w[::-1]:
            return True
        return False
        '''
        


        l = 0
        r = len(s)-1
        while l<r:
            if l<r and  not self.isalphanum(s[l]):
                l += 1
                continue
            if r>l and not self.isalphanum(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -=1
        return True

    def isalphanum(self,c):
        if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9') :
            return True
        return False