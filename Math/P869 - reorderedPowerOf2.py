class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Save all powers as a sorted string
        powers = set("".join(sorted(list(str(1<<i)))) for i in range(33))
        # we just just check our n as a sorted string is in powers or not
        target = "".join(sorted(list(str(n))))
        return target in powers