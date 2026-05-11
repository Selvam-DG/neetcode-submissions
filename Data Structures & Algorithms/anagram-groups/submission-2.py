class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        hmap = dict()

        for i in range(n):
            substr = strs[i]
            key = self.str2list(substr)
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(substr)
        
        result = []
        for key, value in hmap.items():
            result.append(value)
        
        return result
        
    def str2list(self, s:str):
        hcount = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            hcount[idx] += 1
        return tuple(hcount)
        