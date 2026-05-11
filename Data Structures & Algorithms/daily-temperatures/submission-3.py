class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        l = 0
        r = 1
        while l < r and r < len(temperatures):
            if temperatures[l] < temperatures[r]:
                res[l] = r-l
                l += 1
                r = l + 1
            elif r == len(temperatures)-1:
                res[l] = 0
                l += 1
                r = l + 1
            else:
                r += 1
        return res
        