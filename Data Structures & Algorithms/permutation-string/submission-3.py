class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap = {}
        for char in s1:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1
        for i in range(len(s2)-len(s1)+1):
            s=''
            s2_hash_map={}
            for j in range(i, len(s1)+i):
                if s2[j] in s2_hash_map:
                    s2_hash_map[s2[j]] += 1
                else:
                    s2_hash_map[s2[j]] = 1
            if hashMap == s2_hash_map:
                return True
        return False

                

            