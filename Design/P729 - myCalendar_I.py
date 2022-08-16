# class MyCalendar:

#     def __init__(self):
#         self.calendar = []        

#     def book(self, start: int, end: int) -> bool:
#         for old_s, old_e in self.calendar:
#             if old_s < end and start < old_e:
#                 return False
#         self.calendar.append((start, end))
#         return True

# # Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(start,end)


# The above approach is O(n^2)

# Now we will optimize it to O(nlogn)
import bisect
class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        
        # the leftmost position where (start,end) has to be inserted
        # will be returned
        pos = bisect.bisect_left(self.booked, (start, end))

        if (pos == 0 or start >= self.booked[pos - 1][1]) and \
            (pos >= len(self.booked) or end <= self.booked[pos][0]):
            self.booked.insert(pos, (start, end))
            return True
        
        return False
