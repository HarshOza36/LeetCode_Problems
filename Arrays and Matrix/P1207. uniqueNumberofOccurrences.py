class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        distinct = set(arr)
        count_arr = []
        for i in distinct:
            count = arr.count(i)
            if(count in count_arr):
                return False
            count_arr.append(count)
        return True
