class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Runs O(m*n) with O(n) stack space
        def isSubseq(s,t):
            stack = []
            for i in t:
                stack.append(i)
            
            n = len(s)
            for i in range(n-1,-1,-1):
                if not stack:
                    return True
                if stack[-1] == s[i]:
                    stack.pop()
            return stack == []
        
        
        seen = {}
        cnt = 0
        for w in words:
            if w not in seen:
                if isSubseq(s,w):
                    cnt += 1
                    seen[w] = True
                else:
                    seen[w] = False
            else:
                if seen[w]:
                    cnt += 1
        return cnt