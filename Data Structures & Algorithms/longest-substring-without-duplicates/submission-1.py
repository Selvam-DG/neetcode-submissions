class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        
        for i in range(len(s)):
            char_set = set()
            for j in range(i, len(s)):
                if s[j] in char_set:
                   
                    break
                char_set.add(s[j])
                
                result = max(result, len(char_set))
        return result