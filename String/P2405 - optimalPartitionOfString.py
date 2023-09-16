class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()

        partitions = 0
        for ch in s:
            if ch in seen:
                seen = set()
                partitions += 1
            seen.add(ch)
        partitions += 1
        return partitions