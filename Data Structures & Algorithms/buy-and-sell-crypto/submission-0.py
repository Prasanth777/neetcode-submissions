class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        max_p = 0
        while r < len(prices):
            max_p = max(max_p, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
        return max_p
