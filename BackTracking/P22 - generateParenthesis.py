class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # So a backtracking approach.
        # We have 2 choices to place ( or )
        # when forming parenthesis we cannot close until we open
        # number of open brackets = n
        # and we need to place total 2n characters of ( and )
        
        # say n = 3
        # We have 3, 3 (ie. 3 open, 3 close)
        #                       3,3
        #                "("/         \ cannot Close without open
        #                   2,3       X
        #             "((" /        \"()"
        #                1,3        2,2
        #        "((("/   \"(()"  /"()("   \ cannot close without open
        #          0,3     1,2    1,2       X
        #     "((()"|      and so one we get it.
        #          0,2
        #    "((())"|
        #          0,1
        #        "((()))"
        ans = []
        # so we will have open, close, parenthesis and n
        def helper(o, c, parenthesis, n):
            if(o == 0 and c == 0 and len(parenthesis) ==  2*n):
                ans.append(parenthesis)
                return
            if(o == c):
                # we cannot use a close bracket here
                helper(o-1, c, parenthesis + "(", n)
            elif(o == 0):
                # we cannot open now
                helper(o, c-1, parenthesis + ")", n)
            else:
                helper(o-1, c, parenthesis + "(", n)
                helper(o, c-1, parenthesis + ")", n)
        helper(n, n, "", n)
        return ans
                
                
                