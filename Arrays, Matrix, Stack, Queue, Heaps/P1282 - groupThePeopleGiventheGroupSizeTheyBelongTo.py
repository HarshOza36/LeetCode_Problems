class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groups = {}
        for ids,grp in enumerate(groupSizes):
            if(grp in groups):
                groups[grp].append(ids)
            else:
                groups[grp] = [ids]

        answer = []
        for k,v in groups.items():

                temp = 0
                temp_ans = []
                while(True):
                    if(len(temp_ans) == k):
                        answer.append(temp_ans)
                        temp_ans = []
                    if(temp > len(v)-1):
                        break
                    temp_ans.append(v[temp])
                    temp += 1
        return answer
                