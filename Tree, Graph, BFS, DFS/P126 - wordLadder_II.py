# This gave alot of TLE
# Finally used this reference https://leetcode.com/problems/word-ladder-ii/discuss/2367587/Python-BFS-%2B-DFS-With-Explanation-Why-Optimization-Is-Needed-to-Not-TLE

class Solution:

    WILDCARD = "."
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Given a wordlist, we perform BFS traversal to generate a word tree where
        every node points to its parent node.Then we perform a DFS traversal on this tree starting at the endWord.
        """
        if endWord not in wordList:
            return []

        word_tree = self.getWordTree(beginWord, endWord, wordList)
        # print(word_tree)
        return self.getLadders(beginWord, endWord, word_tree)
    
    
    def getWordTree(self, beginWord: str, endWord: str, wordList: List[str]) -> Dict[str, List[str]]:
        """
        BFS traversal from begin word until end word is encountered.
        This functions constructs a tree in reverse, starting at the endWord.
        """
        
        adjacency_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + Solution.WILDCARD + word[i+1:]
                adjacency_list[pattern].append(word)
        
        # Holds the tree of words in reverse order
        # For example, {a: [b,c]} means we got to "a" from "b" and "c"
        visited_tree = {beginWord: []}
        found = False
        q = deque([beginWord])
        
        while q and not found:
            n = len(q)
            
            # keep track of words visited at this level of BFS
            visited_this_level = {}

            for i in range(n):
                word = q.popleft()
                
                for i in range(len(word)):
                    pattern = word[:i] + Solution.WILDCARD + word[i+1:]

                    for next_word in adjacency_list[pattern]:
                        if next_word == endWord:
                            # we don't return immediately because other
                            # sequences might reach the endWord in the same
                            # BFS level
                            found = True
                        if next_word not in visited_tree:
                            if next_word not in visited_this_level:
                                visited_this_level[next_word] = [word]
                                # queue up next word iff we haven't visited it yet
                                # or already are planning to visit it
                                q.append(next_word)
                            else:
                                visited_this_level[next_word].append(word)
            
            # add all seen words at this level to the global visited tree
            visited_tree.update(visited_this_level)    
        return visited_tree
    
    
    def getLadders(self, beginWord: str, endWord: str, wordTree: Dict[str, List[str]]) -> List[List[str]]:
        
        """
        DFS traversal from endWord to beginWord in a given tree.
        """
        def dfs(node: str) -> List[List[str]]:
            if node == beginWord:
                return [[beginWord]]
            if node not in wordTree:
                return []

            res = []
            parents = wordTree[node]
            for parent in parents:
                res += dfs(parent)
            # print(res)
            for r in res:
                r.append(node)
            return res

        return dfs(endWord)
