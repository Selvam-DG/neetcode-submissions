class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        count = 0
        unique_nums = set()
        for num in nums:
            unique_nums.add(num)
        unique_nums = list(unique_nums)
        unique_nums.sort()
        for i in range(1, len(unique_nums)):
            
            if unique_nums[i]  == 1 + unique_nums[i-1]:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res+1
        