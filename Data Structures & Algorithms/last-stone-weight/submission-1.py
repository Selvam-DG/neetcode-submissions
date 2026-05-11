class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)

        while n > 1:
            heavy_stones_diff = stones.pop() - stones.pop()
            n -= 2
            if heavy_stones_diff:
                l,r = 0, n-1
                while l <= r:
                    mid = l + (r-l)//2
                    if stones[mid] < heavy_stones_diff:
                        l = mid + 1
                    else:
                        r = mid - 1
                pos = l
                n += 1
                stones.append(0)
                for i in range(n-1,pos, -1):
                    stones[i] = stones[i-1]
                stones[pos] = heavy_stones_diff
        return stones[0] if stones else 0
        