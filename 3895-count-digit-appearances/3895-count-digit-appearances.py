class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        x = []
        for num in nums:
            for y in str(num):
                x.append(int(y))
        return x.count(digit)
        