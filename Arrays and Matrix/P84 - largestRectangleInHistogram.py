class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        ans = 0
        stack = []
        for i in range(n+1):
            while stack and ((i==n) or (heights[stack[-1]] >= heights[i])):
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans,w*h)
            stack.append(i)
        return ans