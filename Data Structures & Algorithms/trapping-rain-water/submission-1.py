class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]* len(height)
        maxR = [0]* len(height)
        res = 0
        maxL[0] = height[0]
        for i in range(1,len(height)):
            maxL[i] = max((maxL[i-1]), height[i])
        maxR[-1] = height[-1]
        for j in range(len(height)-2, -1, -1):
            maxR[j] = max((maxR[j+1]), height[j])
        for i in range(len(height)):
            if min(maxL[i], maxR[i])-height[i] >0:
                res += min(maxL[i], maxR[i])-height[i]
        return res