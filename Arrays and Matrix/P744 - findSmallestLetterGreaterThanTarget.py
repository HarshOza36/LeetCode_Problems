class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        l, r = 0, n - 1
        while (l <= r):
            mid = (l + r) / 2
            if(letters[mid] <= target):
                l = mid + 1
            else:
                r = mid - 1
        if(l == n): return letters[0]
        return letters[l]