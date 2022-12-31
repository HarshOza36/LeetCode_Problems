class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # Simulation
#         distTravelled = 1
#         for i in range(1, len(rounds)):
#             if rounds[i - 1] < rounds[i]:
#                 distTravelled += rounds[i] - rounds[i - 1]
#             else:
#                 distTravelled += n - (rounds[i - 1] - rounds[i])
#         freq = collections.defaultdict(int)
#         for i in range(rounds[0], rounds[0] + distTravelled):
#             if i % n != 0:  freq[i % n] += 1
#             else: freq[n] += 1

#         maxFreq = max(freq.values())

#         res = []
#         for key in freq:
#             if freq[key] == maxFreq:
#                 res.append(key)
#         return sorted(res)

        # Mathematical solution
        start = rounds[0]
        end = rounds[-1]
        # we have two options
        # if our start is <= end then we will just have to go from start to end
        # otherwise, we will go from start to n and then 1 to end

        if start <= end:
            freq = list(range(start, end + 1))
        else:
            freq = list(range(1, end + 1)) + list(range(start, n + 1))

        return freq