class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)
        
        
        for num in nums:
            
            streak = 0
            current = num
            while current in nums_set:
                streak += 1
                current +=1
            result = max(result, streak)
            
        return result