class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        for i in range(len(x)):
            x[i] = list(x[i])
            x[i].reverse()
            x[i] = "".join(x[i])
        x = " ".join((x))
        return x
        