class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store the unique numbers
        # sort the numbers
        # start from index1 such that index-1 =1 , increment the consequent , store the result if consequent
        # greater than result
        # time complext is 0(nlogn), space is unique element space
        
    
        unique = set(nums)
        sort = sorted(unique)
        result = 0
        cons = 1
        if len(sort) == 1:
            return 1

        for i in range(1, len(sort)):
            if sort[i] - sort[i-1] != 1:
                cons = 1
            if sort[i]-sort[i-1] == 1:
                cons += 1
            result = max(result, cons)
        return result