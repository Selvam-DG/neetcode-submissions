class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map_s1 = {}
        for char in s1:
            if char in hash_map_s1:
                hash_map_s1[char] += 1
            else:
                hash_map_s1[char] = 1
        count =  len(hash_map_s1)
        for i in range(len(s2)):
            hp_s2 = {}
            count2 = 0
            for j in range(i, len(s2)):
                if s2[j] not in hp_s2:
                    hp_s2[s2[j]] = 1
                elif s2[j] in hp_s2:
                    hp_s2[s2[j]] += 1
                if hash_map_s1.get(s2[j] , 0) < hp_s2[s2[j]]:
                    break
                if hash_map_s1.get(s2[j], 0) == hp_s2[s2[j]]:
                    count2 += 1
                if count == count2:
                    return True
        return False
                


                

            