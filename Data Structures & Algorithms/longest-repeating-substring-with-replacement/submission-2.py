class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        hmap = dict()
        max_freq = 0
        longest = 0
        l = 0

        for r in range(n):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)
            max_freq = max(max_freq, hmap[s[r]])

            while (r-l+1) - max_freq > k:
                hmap[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        
        return longest

