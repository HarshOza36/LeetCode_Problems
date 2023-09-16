# class Solution(object):
#     def minDeletions(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         freq = {}
#         for ch in s:
#             if ch in freq:
#                 freq[ch] += 1
#             else:
#                 freq[ch] = 1
#         ans = 0
        
#         v = freq.values()
#         v.sort(reverse = True)

#         for i in range(1, len(v)):
#             if(v[i-1] == 0):
#                 ans += v[i]
#                 v[i] = 0
#             elif(v[i-1] == v[i]):
#                 v[i] = v[i] - 1  
#                 ans += 1
#             elif(v[i] > v[i-1]):
#                 prev = v[i] - v[i-1]
#                 # prev stores value difference at this moment say we have 
#                 # 3 5 , so prev will be 2. 
#                 v[i] = v[i] - prev - 1
#                 ans += prev + 1
#         return ans
                
            
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = 1 + freq.get(ch, 0)
        
        delete = 0
        used = set()

        for ch, cnt in freq.items():
            while cnt > 0 and cnt in used:
                cnt -= 1
                delete += 1
            used.add(cnt)
        return delete