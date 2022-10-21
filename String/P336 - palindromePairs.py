class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        seen = {}
        
        # given unique words, we will store their indices
        for idx, w in enumerate(words):
            seen[w] = idx
        
        ans = []
        
        # we have 3 cases
        # 1st case - If we have a palindrome string with empty string
        # it is a pair example a, "" we have 2 palidromes
        # ""a and a""
        
        # 2nd case reflection palindromes
        # say we have abc and cba in the given words
        # we can form abccba and cbaabc as 2 palindromes
        
        # 3rd case when palindromes are formed with different lengths
        # for example, lls and s we get slls 
        # in this case we will keep splitting the first word
        # until we find a case where first half of that word is a palindrome
        # and remaining part is reverse of the pair string in the words array
        # in this case ll is palidrome and s is reverse of s
        # same way we can check if remaining part is palindrome and first half
        # is reverse of the pair string in words array or not
        
        # Time complexity : O(n.k^2) where n is length of words array
        # and k is length of combined formed palindrome pair
                
        # Case 1
        if "" in seen:
            pairIdx = seen[""]
            for idx,w in enumerate(words):
                if idx != pairIdx and w == w[::-1]:
                    ans.append([idx, pairIdx])
                    ans.append([pairIdx, idx])
        
        # Case 2
        for idx, w in enumerate(words):
            reverse = w[::-1]
            if reverse in seen and seen[reverse] != idx:
                ans.append([idx, seen[reverse]])
        
        # Case 3
        for idx, w in enumerate(words):
            for cut in range(1, len(w)):
                left = w[0 : cut]
                right = w[cut : ]
                
                revLeft = left[::-1]
                revRight = right[::-1]
                
                if left == revLeft:
                    if revRight in seen:
                        ans.append([seen[revRight], idx])
                
                if right == revRight:
                    if revLeft in seen:
                        ans.append([idx, seen[revLeft]])
        return ans
                    
        