class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        ones = [i for i in range(len(boxes)) if boxes[i] == '1']
        out = []
        for i in range(len(boxes)):
            out.append(sum([abs(i-j) for j in ones]))
        return out