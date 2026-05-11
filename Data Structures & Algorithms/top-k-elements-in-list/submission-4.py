class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        bucket = [[] for _ in range(len(nums)+1)]

        for num, cnt in count.items():
            bucket[cnt].append(num)
        result = []
        for cnt in range(len(bucket)-1, 0, -1):
            for num in bucket[cnt]:
                result.append(num)
                if len(result) == k:
                    return result