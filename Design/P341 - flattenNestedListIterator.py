# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        # get the top list
        nestedList, i = self.stack[-1]
        # increment the index of the top list
        self.stack[-1][1] += 1
        # return the integer
        return nestedList[i].getInteger()
        
    
    def hasNext(self) -> bool:
        s = self.stack
        while s:
            # get the top list
            nestedList, i = s[-1]
            # if we have traversed the top list
            # then remove and return false
            if i == len(nestedList):
                s.pop()
            else:
                # otherwise check for integer
                nl = nestedList[i]
                if nl.isInteger():
                    return True
                # increment the index of top nestedlist
                s[-1][1] += 1
                # add the new nested list to the stack
                s.append([nl.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())