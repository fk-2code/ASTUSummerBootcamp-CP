class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        window_ave = sum(nums[ :k])/k
        max_ave = window_ave

        for i in range(k, len(nums)):
            window_ave += (nums[i]/k) - (nums[i - k]/k)
            if window_ave > max_ave:
                max_ave = window_ave
        return max_ave
        