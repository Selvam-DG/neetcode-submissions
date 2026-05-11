class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        if str is None:
            return result.append([''])

        hash_map = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in hash_map:
                hash_map[key].append(word)
            else:
                hash_map[key] = [word]
        
        for key,value in hash_map.items():
            result.append(value)
        return result
        