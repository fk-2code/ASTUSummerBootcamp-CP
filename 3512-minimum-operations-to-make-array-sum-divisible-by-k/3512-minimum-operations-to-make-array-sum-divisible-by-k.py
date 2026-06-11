class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = sum(nums) % k
        return operations

        