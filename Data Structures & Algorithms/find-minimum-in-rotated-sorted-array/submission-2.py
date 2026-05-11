class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        res = float('inf')

        while l < r:
            mid = l + (r-l)//2
            # left half is sorted
            if nums[mid] < nums[r]:
                r = mid
            else:
                
                l = mid + 1
            
        return nums[l]
