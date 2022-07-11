class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        stack = []
        lvl = 0
        # We set all the parentheses at odd-numbered levels for partition A and the remaining ones for B. (Because It's up to us answers can be different). The maximum depth is always minimal.
        
        n = len(seq)
        ans = [-1] * n
        for i in range(n):
            if(seq[i] == '('):
                stack.append(i)
                lvl += 1
            elif(seq[i] == ')'):
                s = stack.pop()
                depth = 0
                if((lvl & 1) == 0): 
                    depth = 1
                ans[s] = depth
                ans[i] = depth
                lvl -= 1
        return ans