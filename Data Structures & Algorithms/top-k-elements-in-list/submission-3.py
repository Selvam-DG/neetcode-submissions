class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use hashmap to count the number
        # sort the hmap with values in descending order
        # loop till k reduces to 0 and store the key in result

        hmap = dict()

        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        
        sorted_hmap = sorted(hmap.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_hmap[i][0])
        
        return result

