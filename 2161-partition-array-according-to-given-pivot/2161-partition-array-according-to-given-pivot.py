class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        p = []
        gr = []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                gr.append(n)
            else:
                p.append(n)
        return less + p + gr
        