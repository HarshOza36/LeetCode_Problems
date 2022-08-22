class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
#         # We will create word for each character place, 
#         # so we will run BFS in O(n^2 . m . 26)
#         wordSet = set(wordList)
#         q = deque([beginWord])
#         visited = set([beginWord])
#         ans = 1

#         while q:
#             for i in range(len(q)):
#                 word = q.popleft()

#                 if word == endWord:
#                     return ans
                
#                 # we will form word by replacing each letter 26 times
#                 # for say hot, we will O(1) check if, aot,bot,cot,dot...
#                 # are in wordSet, if yes add to next layer of bfs
#                 for j in range(len(word)):
#                     for k in range(26):
#                         newWord = word[:j] + chr(ord('a') + k) + word[j+1:]
#                         if newWord in wordSet and newWord not in visited:
#                             q.append(newWord)
#                             visited.add(newWord)
#             ans += 1
#         return 0
    
        # Faster approach is, we pre calculate the connections
        if endWord not in wordList:
            return 0
        neig = {}
        wordList.append(beginWord)
        
        
        # Forming the adjacency list in O(n x m^2)
        # a word say hot can replace one character in 3 ways
        # *ot, h*t or ho*
        # we will use this as pattern so say if lot comes
        # it also matches *ot and hence it will be connect to other
        # words with same pattern *ot.
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in neig:
                    neig[pattern] = []
                neig[pattern].append(word)
        
        
        # BFS runs O(n^2) and we need to compare m words
        # Total O(n^2 x m)
        visited = set([beginWord])
        q = deque([beginWord])
        ans = 1
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ans
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    
                    for neiWord in neig[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            ans += 1
        return 0
        
