class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxarea = 0
        area = 0
        l = 0
        r = n-1

        while l < r:
            height = min(heights[l], heights[r])
            area = height * (r-l)
            maxarea = max(area, maxarea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxarea


