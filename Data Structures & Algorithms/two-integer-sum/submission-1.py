class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = dict()

        for i in range(n):
            need = target - nums[i]
            if need in hashmap:
                return sorted([i, hashmap[need]])
            
            hashmap[nums[i]] = i
        