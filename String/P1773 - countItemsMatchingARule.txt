class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        found = 0
        key_list = {"type" : 0, "color" : 1, "name" : 2}
        index = key_list[ruleKey]
        for item in items:
            if(item[index] == ruleValue):
                found += 1
        return found