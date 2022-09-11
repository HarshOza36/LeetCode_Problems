class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # stack = []
        # weak = 0
        # # sort in ascending order of attack and if tie decreasing defense
        # properties.sort(key = lambda x: (x[0], -x[1]))
        # for atk, defe in properties:
        #     while stack and atk > stack[-1][0] and defe > stack[-1][1]:
        #         stack.pop()
        #         weak += 1
        #     stack.append([atk, defe])
        # return weak
        
        weak = 0
        maxDef = 0
        properties.sort(key = lambda x: (-x[0], x[1]))
        # we can improve the the time, by just checking the defense
        # with the max defense seen when sorted in descending by attack
        for _, defe in properties:
            if defe < maxDef:
                   weak += 1
            else:
                maxDef = defe
        return weak