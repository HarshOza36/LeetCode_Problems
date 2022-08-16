class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
#         seen = {}
        
#         for word in strs:
#             sort_word = "".join(sorted(word))
#             if(sort_word in seen):
#                 seen[sort_word].append(word)
#             else:
#                 seen[sort_word] = [word]
        
#         return list(seen.values())
        
        # Using Hashkey instead of sorting
        seen = {}
        
        for word in strs:
            sum = 0
            prod = 1
            for ch in word:
                sum += ord(ch) 
                prod *= ord(ch)
            
            key = (sum, prod, len(word))
            if key not in seen:
                seen[key] = []
            seen[key].append(word)
        return list(seen.values())
