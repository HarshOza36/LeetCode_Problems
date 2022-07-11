class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for idx, t in enumerate(temperatures):
            while(stack and t > stack[-1][0]):
                    s_temp, s_idx = stack.pop()
                    ans[s_idx] = idx - s_idx
            stack.append((t, idx))
        return ans