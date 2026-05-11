class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        product = 1
        zero_count = 0
        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return res
        for i in range(len(nums)):
            if zero_count:
                if nums[i]:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product // nums[i]

        return res

        
        