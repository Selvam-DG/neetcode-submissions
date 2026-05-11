class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        # brute force method
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []
        '''
        # Two pointers
        l = 0
        r = len(numbers)-1
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            

        return []