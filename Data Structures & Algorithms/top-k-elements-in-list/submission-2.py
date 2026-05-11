class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        result = defaultdict()
        for num in nums:
            result[num] = 1 + result.get(num,0)
        arr = []
        for num, count in result.items():
            arr.append([count, num])
        arr.sort()
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
        '''
        count = {}
        freq = [ [] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, count in count.items():
            freq[count].append(num)
        res  =[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        


        