class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charcount = [0] * 26

        for char in s:
            idx = ord(char) - ord('a')
            charcount[idx] += 1
        
        for char in t:
            idx = ord(char) - ord('a')
            charcount[idx] -= 1

            if charcount[idx] < 0:
                return False
        return sum(charcount) == 0
        