# Memory Limit exceeded Bruteforce 69/72
# class SnapshotArray(object):

#     def __init__(self, length):
#         """
#         :type length: int
#         """
#         self.arr = [0] * length
#         self.snap_d = {}
#         self.snapId = 1

#     def set(self, index, val):
#         """
#         :type index: int
#         :type val: int
#         :rtype: None
#         """
#         self.arr[index] = val

#     def snap(self):
#         """
#         :rtype: int
#         """
#         snap_id = self.snapId - 1
#         self.snap_d[snap_id] = self.arr[:]
#         self.snapId += 1
#         return snap_id

#     def get(self, index, snap_id):
#         """
#         :type index: int
#         :type snap_id: int
#         :rtype: int
#         """
#         if snap_id in self.snap_d:
#             return self.snap_d[snap_id][index]
#         return -1
class SnapshotArray(object):
    def __init__(self, length):
        self.snap_d = defaultdict(list)
        self.snapId = 0

    def set(self, index, val):
        if self.snap_d[index] and self.snap_d[index][-1][0] == self.snapId:
            # basically replacing the index if already existing
            self.snap_d[index][-1][1] = val
            return
        self.snap_d[index].append([self.snapId, val])

    def snap(self):
        self.snapId += 1
        return self.snapId - 1

    def get(self, index, snap_id):
        # now we will have to search this snap_id and then return the index
        arr = self.snap_d[index]
        l, r, ans = 0, len(arr) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= snap_id:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        if ans == -1: return 0
        return arr[ans][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)