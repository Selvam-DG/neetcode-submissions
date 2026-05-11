class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            char_count = {}
            maxf = 0
            for j in range(i, len(s)):
                
                if s[j] in char_count:
                    char_count[s[j]] = 1 + char_count[s[j]]
                else:
                    char_count[s[j]] = 1
                maxf = max(maxf, char_count[s[j]])
                if (j-i+1) - maxf <= k:
                    res = max(res, j-i+1)
        return res
                  

        