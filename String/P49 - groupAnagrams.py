class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = {}
        
        for word in strs:
            sort_word = "".join(sorted(word))
            if(sort_word in seen):
                seen[sort_word].append(word)
            else:
                seen[sort_word] = [word]
        
        return list(seen.values())
                