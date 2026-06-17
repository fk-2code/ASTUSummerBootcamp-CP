class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        sum = []
        while l < r:
            sum.append(nums[l]+nums[r])
            l += 1
            r -= 1
        return max(sum)

        