class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        ints = set()
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                ints.add(nums2[i])
        return list(ints)
        