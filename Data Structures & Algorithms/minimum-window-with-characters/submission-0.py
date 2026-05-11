class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        if len(s) < len(t):
            return res
        
        # sliding window
        # left pointer and expand right pointer to find all char in t in sliding window
        # when char repeat mini the window to keep all char and store the result
        need = dict()
        for char in t:
            need[char] = 1 + need.get(char, 0)
        
        window = dict()
        have = 0
        need_count = len(need)
        res_len = float('inf')

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in need and window[char] == need[char]:
                have += 1
            while have == need_count:
                if r-l+1 < res_len:
                    res = s[l:r+1]
                    res_len = r - l +1
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1
        return res