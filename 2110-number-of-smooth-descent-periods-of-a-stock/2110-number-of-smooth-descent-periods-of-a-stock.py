class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        count = 0

        for i in range(len(prices)):

            if prices[i - 1] - prices[i] == 1:
                count += 1
            else:
                count = 1
            res += count
        
        return res
        