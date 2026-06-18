class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        for y in range(len(nums)):
            if nums[y] != nums[x]:
                x += 1
                nums[x] = nums[y]
        return x+1
        
        