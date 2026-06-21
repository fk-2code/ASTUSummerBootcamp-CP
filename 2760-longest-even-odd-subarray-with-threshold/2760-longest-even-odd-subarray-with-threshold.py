class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        l = 0
        ans = 0
        x = len(nums) - 1

        for r in range(x + 1):
            if nums[l] % 2 != 0 or nums[l] > threshold:
                l += 1
                continue
            if nums[r] > threshold :
                if r - l < x - r:
                    l = r + 1
                    continue
                else:
                    r -= 1
                    break

            if  nums[r] % 2 == nums[r-1] % 2:
                l = r
            ans = max(ans, r - l + 1)
        return ans
            
        